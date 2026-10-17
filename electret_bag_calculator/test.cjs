// node electret_bag_calculator/test.cjs
// Checks every layout the search returns against a direct geometric test of where the hole lands.
const S = require("./solver.js");
const assert = require("assert");

// Sample the hole disc, map each point into folded-stack coordinates, and report which
// panels have hole inside their active area (more than MARGIN + TOL from every edge).
function holeHits(piece, hx, hy) {
  const hits = new Set();
  const lim = S.MARGIN + S.TOL + 1e-6;
  for (let i = -40; i <= 40; i++) for (let j = -40; j <= 40; j++) {
    const dx = i / 40 * S.HOLE_R, dy = j / 40 * S.HOLE_R;
    if (dx * dx + dy * dy > S.HOLE_R * S.HOLE_R) continue;
    const x = hx + dx - piece.ux, y = hy + dy - piece.uy;
    if (x < 0 || y < 0 || x > piece.p * piece.su || y > piece.q * piece.sv) continue;
    const pi = Math.min(piece.p - 1, Math.floor(x / piece.su)), pj = Math.min(piece.q - 1, Math.floor(y / piece.sv));
    const u = x - pi * piece.su, v = y - pj * piece.sv;
    if (Math.min(u, piece.su - u) > lim && Math.min(v, piece.sv - v) > lim) hits.add(pi + "," + pj);
  }
  return [...hits];
}

function checkLayout(c, inp, label) {
  let outsideLayers = 0;
  for (const pc of c.pieces) {
    // Inside its region, inside the sheet.
    assert(pc.ux >= pc.reg.x0 - 1e-6 && pc.ux + pc.p * pc.su <= pc.reg.x1 + 1e-6, label + ": x overflow");
    assert(pc.uy >= pc.reg.y0 - 1e-6 && pc.uy + pc.q * pc.sv <= pc.reg.y1 + 1e-6, label + ": y overflow");
    assert(S.MARGIN * 2 < Math.min(pc.su, pc.sv), label + ": panel smaller than margins");
    const hits = holeHits(pc, inp.hx, inp.hy);
    if (pc.rank >= 2) assert.strictEqual(hits.length, 0, `${label}: ${pc.hole} but hole in active area ${hits}`);
    if (pc.rank === 1) {
      assert.strictEqual(hits.length, 1, `${label}: top-layer hole hits ${hits.length} panels`);
      const [i, j] = hits[0].split(",").map(Number);
      assert((i === 0 || i === pc.p - 1) && (j === 0 || j === pc.q - 1), `${label}: holed panel ${hits[0]} is not a corner panel`);
      outsideLayers++;
    }
  }
  assert(outsideLayers <= 1, label + ": two holed outside layers");
  // Panels fit the face, flow and PF are consistent.
  for (const pc of c.pieces)
    assert((pc.su <= inp.FW + 1e-6 && pc.sv <= inp.FH + 1e-6) || (pc.su <= inp.FH + 1e-6 && pc.sv <= inp.FW + 1e-6), label + ": panel too big for face");
  const n = c.pieces.reduce((s, pc) => s + pc.p * pc.q, 0);
  assert.strictEqual(n, c.n, label + ": layer count");
  const fan = 0.765 * inp.V ** 2 - 0.000383 * c.Q ** 2;
  assert(Math.abs(fan - c.dp) < 1e-6 * Math.max(1, fan), label + ": fan and filter Δp disagree");
}

const cases = [
  { W: 62, H: 69, hx: 31, hy: 12, FW: 30, FH: 40 },
  { W: 62, H: 69, hx: 31, hy: 34.5, FW: 30, FH: 40 },
  { W: 62, H: 69, hx: 10, hy: 60, FW: 25, FH: 25 },
  { W: 40, H: 100, hx: 20, hy: 50, FW: 35, FH: 35 },
  { W: 30, H: 30, hx: 15, hy: 15, FW: 30, FH: 30 },
  { W: 55, H: 48, hx: 3, hy: 3, FW: 20, FH: 50 },
  { W: 80, H: 25, hx: 40, hy: 12, FW: 40, FH: 25 },
];
let n = 0;
for (const base of cases) for (const mat of ["arome", "kenmore"]) for (const V of [8, 12, 15, 20]) for (const Qt of [150, 200]) {
  const inp = Object.assign({ mat, slope: "comp", V, Qt }, base);
  const t0 = Date.now();
  const r = S.solve(inp);
  const ms = Date.now() - t0;
  const label = JSON.stringify(inp);
  assert(ms < 3000, label + ": slow " + ms + " ms");
  for (const c of S.singleCandidates(inp).concat(S.doubleCandidates(inp))) { checkLayout(c, inp, label); n++; }
  if (r.best) checkLayout(r.best.c, inp, label);
}
console.log(`ok: ${n} layouts checked`);

// One worked example, for eyeballing.
const ex = S.solve({ mat: "arome", slope: "comp", V: 15, Qt: 200, W: 62, H: 69, hx: 31, hy: 12, FW: 30, FH: 40 });
const b = ex.best.c;
console.log("example:", { cls: b.cls, hole: b.hole, n: b.n, panel: [b.sx.toFixed(1), b.sy.toFixed(1)], Q: b.Q.toFixed(0), dp: b.dp.toFixed(0), logPF: b.logPF.toFixed(2),
  pieces: b.pieces.map(p => ({ p: p.p, q: p.q, su: +p.su.toFixed(2), sv: +p.sv.toFixed(2), ux: +p.ux.toFixed(2), uy: +p.uy.toFixed(2) })), candidates: ex.count });
