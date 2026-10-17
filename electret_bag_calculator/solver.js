// Electret layer calculator: flow/PF model and the fold/cut layout search.
// Browser: defines window.ElectretSolver. Node: module.exports.
(function (root) {
  "use strict";

  // Fan: the "Vacuum bags & filters" tab's p–V–Q fit, Q in L/min.
  const FAN_K = 0.765, FAN_C = 0.000383;

  // Per layer: Δp = R·v, log10PF(0.3 µm) = D·v^-α, v in cm/s.
  // R: Arome from a 6 cm outlet run at 15 V (54.5 s / 100 L); Kenmore inferred from the
  // fan model on its two PF runs (2.88, 3.29). D for "comp" is fitted to the electret-only
  // points with α fixed to the brand's whole-bag fit.
  const MATS = {
    arome:   { name: "Arome Livii", R: 2.58, vRange: [4.94, 5.93],
               comp: { D: 1.5863, a: 0.3070 }, own: { D: 2.3479, a: 0.5350 } },
    kenmore: { name: "Kenmore", R: 3.09, vRange: [8.69, 14.40],
               comp: { D: 1.5854, a: 0.3500 }, own: { D: 1.1458, a: 0.2207 } },
  };

  const LOG_ENOUGH = 4;   // past 4 logs, spend spare pressure on airflow instead
  const HOLE_R = 2.25;    // 45 mm hole
  const MARGIN = 2;       // lost on every side of every layer
  const TOL = 0.3;        // how far the hole may reach past the margin (a fold through its centre gives 0.25)
  const MIN_PANEL = 8;    // smallest panel side worth folding, cm
  const TRIM_MIN = 0.5;   // narrower offcuts are left as folding slack, not cut
  const EPS = 1e-6;

  function flowFor(n, area, R, V) {
    // N·R·v = fan pressure, v = Q/(0.06·A)  ->  a·Q + c·Q² = k·V²
    const a = n * R / (0.06 * area), kv = FAN_K * V * V;
    return 2 * kv / (a + Math.sqrt(a * a + 4 * FAN_C * kv));
  }

  function perf(n, sx, sy, inp) {
    const m = MATS[inp.mat], fit = m[inp.slope];
    const area = (sx - 2 * MARGIN) * (sy - 2 * MARGIN);
    const Q = flowFor(n, area, m.R, inp.V), v = Q / (0.06 * area);
    return { n, area, Q, v, dp: n * m.R * v, logPF: n * fit.D * Math.pow(v, -fit.a) };
  }

  // Hole at u along an axis, measured from the start of n panels of size s.
  function classify1D(u, n, s) {
    const span = n * s;
    if (u + HOLE_R <= EPS || u - HOLE_R >= span - EPS) return { st: "out" };
    // How far the hole reaches past the margin, taking each panel boundary in turn.
    let reach = Math.min(HOLE_R + u, HOLE_R + span - u) - MARGIN;
    for (let k = 1; k < n; k++) reach = Math.min(reach, HOLE_R + Math.abs(u - k * s) - MARGIN);
    if (reach <= TOL + EPS) return { st: "edge" };
    const clamp = i => Math.min(n - 1, Math.max(0, i));
    return { st: "in", i0: clamp(Math.floor((u - HOLE_R) / s)), i1: clamp(Math.floor((u + HOLE_R - EPS) / s)) };
  }

  // Start positions for n panels of size s along an axis of length L, hole at h.
  function place1D(L, h, n, s) {
    const span = n * s, slack = L - span;
    if (slack < -EPS) return [];
    const xs = [0, Math.max(0, slack)];
    const add = x => { if (x > EPS && x < slack - EPS) xs.push(x); };
    for (let k = 1; k < n; k++) add(h - k * s);           // fold through the hole
    add(h + HOLE_R - MARGIN); add(h - HOLE_R + MARGIN - span); // hole a notch in the margin
    add(h + HOLE_R); add(h - HOLE_R - span);              // hole cut off
    return xs.map(x0 => Object.assign({ x0 }, classify1D(h - x0, n, s)));
  }

  // Panel sizes worth trying for n panels: as big as fits, or shrunk so a fold or edge meets the hole.
  function sizes1D(L, h, n, fmax) {
    const base = Math.min(L / n, fmax), out = [base];
    const lim = v => { if (v >= MIN_PANEL && v < base - 0.05) out.push(v); };
    for (let k = 1; k < n; k++) lim(Math.min(h / k, (L - h) / (n - k)));
    lim((L - h - HOLE_R + MARGIN) / n); lim((h - HOLE_R + MARGIN) / n);
    lim((L - h - HOLE_R) / n); lim((h - HOLE_R) / n);
    return out;
  }

  function combine(X, Y, p, q) {
    if (X.st === "out" || Y.st === "out") return { rank: 3, hole: "removed" };
    if (X.st === "edge" && Y.st === "edge") return { rank: 3, hole: "corner" };
    if (X.st === "edge" || Y.st === "edge") return { rank: 2, hole: "edge" };
    const end = (i0, i1, n) => i0 === i1 && (i0 === 0 || i0 === n - 1);
    if (end(X.i0, X.i1, p) && end(Y.i0, Y.i1, q)) return { rank: 1, hole: "top", panel: [X.i0, Y.i0] };
    return null;
  }

  // Best placement of p×q panels (su along x, sv along y) inside a region of the sheet.
  // Returns one option per cut flag: [no trims, trimmed].
  function placeRegion(reg, p, q, su, sv, hx, hy) {
    const W = reg.x1 - reg.x0, H = reg.y1 - reg.y0;
    const Xo = place1D(W, hx - reg.x0, p, su), Yo = place1D(H, hy - reg.y0, q, sv);
    const best = [null, null];
    for (const X of Xo) for (const Y of Yo) {
      const h = combine(X, Y, p, q);
      if (!h) continue;
      const trims = { left: X.x0, right: W - X.x0 - p * su, top: Y.x0, bottom: H - Y.x0 - q * sv };
      const nTrim = Object.values(trims).filter(t => t > TRIM_MIN).length;
      const k = nTrim ? 1 : 0, b = best[k];
      if (!b || h.rank > b.rank || (h.rank === b.rank && nTrim < b.nTrim))
        best[k] = Object.assign({ reg, p, q, su, sv, ux: reg.x0 + X.x0, uy: reg.y0 + Y.x0, trims, nTrim }, h);
    }
    return best;
  }

  function faceOrients(inp) {
    return inp.FW === inp.FH ? [[inp.FW, inp.FH]] : [[inp.FW, inp.FH], [inp.FH, inp.FW]];
  }

  function fitsFace(a, b, inp) {
    return (a <= inp.FW + EPS && b <= inp.FH + EPS) || (a <= inp.FH + EPS && b <= inp.FW + EPS);
  }

  // One piece: trim (optional) then zig-zag fold into p×q panels.
  function singleCandidates(inp) {
    const out = [], sheet = { x0: 0, y0: 0, x1: inp.W, y1: inp.H };
    for (const [fx, fy] of faceOrients(inp))
      for (let p = 1; inp.W / p >= MIN_PANEL - EPS; p++)
        for (const sx of sizes1D(inp.W, inp.hx, p, fx))
          for (let q = 1; inp.H / q >= MIN_PANEL - EPS; q++)
            for (const sy of sizes1D(inp.H, inp.hy, q, fy)) {
              if (sx < MIN_PANEL - EPS || sy < MIN_PANEL - EPS) continue;
              const pf = perf(p * q, sx, sy, inp);
              for (const pc of placeRegion(sheet, p, q, sx, sy, inp.hx, inp.hy))
                if (pc) out.push(Object.assign({ cls: pc.nTrim ? 1 : 0, rank: pc.rank, hole: pc.hole,
                  sx, sy, pieces: [pc] }, pf));
            }
    return out;
  }

  // Two pieces from one straight cut, each trimmed and folded to the same panel size.
  function doubleCandidates(inp) {
    const out = [];
    const dims = f => {
      const s = new Set([f]);
      for (let p = 1; p <= 12; p++) for (const L of [inp.W, inp.H]) if (L / p <= f && L / p >= MIN_PANEL) s.add(L / p);
      return [...s];
    };
    const pairs = [];
    for (const a of dims(inp.FW)) for (const b of dims(inp.FH)) pairs.push([a, b]);
    for (const [a, b] of pairs) {
      const pf = {};
      for (const vert of [true, false]) {
        const L = vert ? inp.W : inp.H;
        const along = [a, b].filter((d, i, arr) => arr.indexOf(d) === i);
        const cuts = new Set();
        for (const d of along) for (let k = 1; k * d < L - MIN_PANEL; k++) { cuts.add(k * d); cuts.add(L - k * d); }
        for (const c of cuts) {
          const regs = vert
            ? [{ x0: 0, y0: 0, x1: c, y1: inp.H }, { x0: c, y0: 0, x1: inp.W, y1: inp.H }]
            : [{ x0: 0, y0: 0, x1: inp.W, y1: c }, { x0: 0, y0: c, x1: inp.W, y1: inp.H }];
          const opts = regs.map(r => [[a, b], [b, a]].map(([su, sv]) => {
            const p = Math.floor((r.x1 - r.x0 + EPS) / su), q = Math.floor((r.y1 - r.y0 + EPS) / sv);
            if (p < 1 || q < 1) return null;
            const [o0, o1] = placeRegion(r, p, q, su, sv, inp.hx, inp.hy);
            if (!o0) return o1;
            if (!o1) return o0;
            return o1.rank > o0.rank ? o1 : o0;
          }).filter(Boolean));
          for (const A of opts[0]) for (const B of opts[1]) {
            if (A.rank === 1 && B.rank === 1) continue;   // only one layer can go outside
            const n = A.p * A.q + B.p * B.q;
            pf[n] = pf[n] || perf(n, a, b, inp);
            const worst = A.rank <= B.rank ? A : B;
            out.push(Object.assign({ cls: 2, rank: worst.rank, hole: worst.hole, sx: a, sy: b, pieces: [A, B], cut: { vert, at: c } }, pf[n]));
          }
        }
      }
    }
    return out;
  }

  function pickBest(list, Qt) {
    if (!list.length) return null;
    const goal = list.filter(c => c.Q >= Qt && c.logPF >= LOG_ENOUGH);
    if (goal.length) return { c: goal.reduce((x, y) => (y.rank > x.rank || (y.rank === x.rank && y.Q > x.Q) ? y : x)), goal: true };
    const flow = list.filter(c => c.Q >= Qt);
    if (flow.length) {
      const top = Math.max(...flow.map(c => c.logPF));
      const near = flow.filter(c => c.logPF >= top - 0.05);
      return { c: near.reduce((x, y) => (y.cls < x.cls || (y.cls === x.cls && (y.rank > x.rank || (y.rank === x.rank && y.logPF > x.logPF))) ? y : x)), goal: false };
    }
    return { c: list.reduce((x, y) => (y.Q > x.Q ? y : x)), goal: false, short: true };
  }

  function solve(inp) {
    const single = singleCandidates(inp);
    const double = doubleCandidates(inp);
    const byCls = [0, 1, 2].map(k => pickBest((k < 2 ? single : double).filter(c => c.cls === k), inp.Qt));
    // Fold only if it reaches the goal, else trim, else two pieces; if nothing does, best PF overall.
    let best = byCls.find(b => b && b.goal);
    if (!best) best = pickBest(single.concat(double), inp.Qt);
    return { best, byCls, count: single.length + double.length };
  }

  const api = { MATS, LOG_ENOUGH, HOLE_R, MARGIN, TOL, MIN_PANEL, TRIM_MIN,
                flowFor, perf, classify1D, place1D, combine, solve, singleCandidates, doubleCandidates };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.ElectretSolver = api;
})(this);
