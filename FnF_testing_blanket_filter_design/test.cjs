// node FnF_testing_blanket_filter_design/test.cjs
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {load: loadPlanner} = require('../planner/test-solver.cjs');

const page = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8');
const planner = fs.readFileSync(path.join(__dirname, '../planner/src.html'), 'utf8');
const core = page.match(/<script id="solvercore">([\s\S]*?)<\/script>/)[1];
const mats = page.match(/(const FITS=[\s\S]*?)\/\* ---- solver worker/)[1];
const S = new Function(`${core}\n${mats}\nreturn {FITS, TYPES, termsOf, logsOf, dpOf, foldAll, RI, OVERHANG, H_MIN, PLY_OPTS,
  solve(sel,p=202,r=15,h=50,q=3000){Q=q;return optimise(sel,p,r,h);}};`)();
const P = loadPlanner(planner);

// 1. Fits match the published coefficients and the planner.
const coeffs = JSON.parse(fs.readFileSync(path.join(__dirname, '../testing/coefficients.json'), 'utf8'));
for (const [id, f] of Object.entries(S.FITS)) {
  const c = coeffs[id].fits['0.3'], m = P.mats.find(m => m.id === id);
  for (const [a, b] of [['D','D'],['C','C'],['alpha','alpha'],['k','k_layer']])
    assert.equal(f[a], c[b], `${id} ${a} vs coefficients.json`);
  assert.equal(f.t, coeffs[id].t_layer, `${id} t`);
  assert.equal(f.B || 0, c.B || 0, `${id} B`);
  for (const k of ['D','C','alpha','k','t']) assert.equal(f[k], m[k === 'D' ? 'A' : k], `${id} ${k} vs planner`);
}

// 2. Term form reproduces the planner's closed form (impaction cap off), and the cap only
// ever lowers logs, by nothing when every speed is within the measured range.
for (const id of Object.keys(S.FITS)) {
  const m = P.mats.find(m => m.id === id), g = {...m, terms: S.termsOf(S.FITS[id]).map(([c, p]) => [c, p])};
  const capped = {...g, terms: S.termsOf(S.FITS[id])};
  for (const [r0, r1, K] of [[3.25, 8, 30], [3.25, 15, 9.5], [10, 15, 300]]) {
    const a = S.logsOf(g, r0, r1, K), b = S.logsOf(capped, r0, r1, K);
    assert(b <= a + 1e-12);
    if (!(K / r0 > (S.FITS[id].vhi || Infinity))) assert(Math.abs(a - b) < 1e-12, `${id} cap applied in range`);
  }
  for (const [r0, r1, K] of [[2, 3, 50], [4, 15, 9.5], [0.6, 1.1, 120]]) {
    const a = P.logsOf(m, r0, r1, K), b = S.logsOf(g, r0, r1, K);
    assert(Math.abs(a - b) < 1e-12 * Math.max(1, a), `${id} logs ${a} vs ${b}`);
    assert(Math.abs(P.dpOf(m, r0, r1, K) - S.dpOf(g, r0, r1, K)) < 1e-9);
  }
}

// 3. Generic blanket = geometric mean per layer of the four tested blankets.
const B = ['blue holey', 'grey fuzzy', 'pink', 'grey holey'], bl = S.TYPES.blanket;
const perLayer = (terms, v) => terms.reduce((s, [c, p]) => s + c * v ** p, 0);
for (const v of [0.64, 1.2, 2.4, 6]) {
  const mean = B.reduce((s, id) => s + perLayer(S.termsOf(S.FITS[id]), v), 0) / 4;
  assert(bl.terms.every(([c, p, vmax]) => p <= 0 || vmax === 11.24), 'blanket impaction cap');
  assert(Math.abs(perLayer(bl.terms, v) - mean) < 1e-12);
}
const gm = k => Math.exp(B.reduce((s, id) => s + Math.log(S.FITS[id][k]), 0) / 4);
assert(Math.abs(bl.k - gm('k')) < 1e-12 && Math.abs(bl.t - gm('t')) < 1e-12);
assert.equal(S.TYPES.duvet.t, S.FITS.duvet.t); assert.equal(S.TYPES.linen.k, S.FITS['soft linen'].k);

// 4. Plans obey the build rules: 65 mm core, whole pieces that go round at least once,
// >= 8 cm past the far end, folds people can do.
function check(t, sel, p = 202, r = 15, h = 50, q = 3000) {
  assert(t && t.bands.length, 'expected a feasible plan');
  assert(t.H >= S.H_MIN - 1e-9 && t.H <= h + 1e-8 && t.ro <= r + 1e-8 && t.ri === S.RI);
  let logs = 0, dp = 0, radius = S.RI;
  const K = q / (2 * Math.PI * t.H), ids = new Set();
  for (const b of t.bands) {
    assert(sel.some(m => m.id === b.m.id) && !ids.has(b.m.id)); ids.add(b.m.id);
    assert(Math.abs(b.r0 - radius) < 1e-9);
    const f = b.fold, side = f.roll === 'L' ? b.m.W : b.m.L, circ = f.roll === 'L' ? b.m.L : b.m.W;
    assert(Math.abs(f.axial * f.f - side) < 1e-9 && f.circ === circ && [1,2,3,4,6,8].includes(f.f));
    assert(b.r1 - b.r0 >= f.f * b.m.t - 1e-9, 'piece does not go round once');
    assert(f.axial - t.H >= S.OVERHANG - 1e-9, 'overhang under 8 cm');
    assert(Math.abs(Math.PI * (b.r1 ** 2 - b.r0 ** 2) - f.f * circ * b.m.t) < 1e-7, 'piece not used whole');
    logs += S.logsOf(b.m, b.r0, b.r1, K); dp += S.dpOf(b.m, b.r0, b.r1, K);
    radius = b.r1;
  }
  assert(dp <= p + 1e-6 && Math.abs(dp - t.dp) < 1e-7 && Math.abs(logs - t.logs) < 1e-7);
}

// Exhaustive reference: every length on a fine grid plus every fold threshold, every
// subset, fold and order.
function brute(sel, p = 202, r = 15, h = 50, q = 3000) {
  const all = sel.map(S.foldAll);
  const Hs = new Set([h]);
  for (let x = S.H_MIN; x <= h; x += 0.25) Hs.add(x);
  for (const o of all.flat()) if (o.axial - S.OVERHANG >= S.H_MIN && o.axial - S.OVERHANG <= h) Hs.add(o.axial - S.OVERHANG);
  const perms = a => a.length ? a.flatMap((v, i) => perms(a.filter((_, j) => j !== i)).map(x => [v, ...x])) : [[]];
  // Adjacent pieces of one material form one band whatever their order: try one order per run.
  const distinct = order => order.every(([m, f, j], k) => k === 0 || order[k - 1][0].type !== m.type || order[k - 1][2] < j);
  let best = 0;
  for (const H of Hs) {
    const K = q / (2 * Math.PI * H);
    const choices = all.map(opts => [null, ...opts.filter(o => o.axial >= H + S.OVERHANG - 1e-9)]);
    const room = Math.PI * (r * r - S.RI * S.RI);   // total cross-section the diameter allows
    const pick = (i, acc, area) => {
      if (i === sel.length) {
        const used = acc.map((f, j) => f && [sel[j], f, j]).filter(Boolean);
        for (const order of perms(used)) {
          if (!distinct(order)) continue;
          let rr = S.RI, dp = 0, logs = 0, ok = true;
          for (const [m, f] of order) {
            const r1 = Math.sqrt(rr * rr + f.area / Math.PI);
            if (r1 - rr < f.f * m.t - 1e-9) { ok = false; break; }
            dp += S.dpOf(m, rr, r1, K); logs += S.logsOf(m, rr, r1, K); rr = r1;
            if (rr > r + 1e-9 || dp > p + 1e-9) { ok = false; break; }
          }
          if (ok && logs > best) best = logs;
        }
        return;
      }
      for (const c of choices[i]) if (area + (c ? c.area : 0) <= room + 1e-7) pick(i + 1, [...acc, c], area + (c ? c.area : 0));
    };
    pick(0, [], 0);
  }
  return best;
}

const item = (type, L, W, n) => ({...S.TYPES[type], id: 'i' + n, type, L, W});
const small = [
  ['one blanket', [item('blanket', 200, 150, 1)]],
  ['one duvet', [item('duvet', 200, 200, 1)]],
  ['two blankets + duvet', [item('blanket', 200, 150, 1), item('blanket', 130, 170, 2), item('duvet', 200, 200, 3)]],
  ['blanket, duvet, sheet, blanket', [item('blanket', 180, 130, 1), item('duvet', 220, 200, 2),
                                       item('linen', 230, 220, 3), item('blanket', 150, 125, 4)]],
  ['tight', [item('blanket', 200, 150, 1), item('duvet', 200, 200, 2), item('linen', 200, 135, 3)], 80, 10, 30],
  ['short pieces', [item('blanket', 60, 90, 1), item('linen', 55, 200, 2), item('duvet', 140, 200, 3)], 202, 15, 50],
  ['high flow', [item('blanket', 200, 150, 1), item('blanket', 200, 150, 2), item('duvet', 200, 200, 3)], 300, 15, 50, 5000],
];
// The reviewer's case: PF depended on entry order before pieces were sorted canonically.
small.push(['reviewer five', [item('blanket', 200, 150, 1), item('blanket', 130, 170, 2), item('duvet', 200, 200, 3),
                              item('linen', 230, 220, 4), item('blanket', 60, 90, 5)]]);
small.push(['tiny sheet', [item('linen', 14, 14, 1), item('blanket', 120, 100, 2)]]);
// Random instances, fixed seed.
let seed = 7;
const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
for (let c = 0; c < 6; c++) {
  const n = 2 + Math.floor(rnd() * 3), types = ['blanket', 'duvet', 'linen'];
  small.push([`random ${c}`, Array.from({length: n}, (_, i) => item(types[Math.floor(rnd() * 3)],
    Math.round(60 + rnd() * 180), Math.round(60 + rnd() * 180), i + 1)),
    Math.round(80 + rnd() * 220), Math.round(10 + rnd() * 10), Math.round(25 + rnd() * 35)]);
}
const big = [
  ['eight pieces', [1,2,3,4,5,6,7,8].map(n => item(['blanket','duvet','linen'][n % 3], 120 + 10 * n, 140 + 7 * n, n))],
  ['ten blankets', Array.from({length: 10}, (_, n) => item('blanket', 150 + 5 * n, 130, n + 1)), 202, 20, 50],
];
let worst = 0;
for (const [name, sel, ...args] of [...small, ...big]) {
  const t0 = performance.now(), t = S.solve(sel, ...args), ms = performance.now() - t0;
  worst = Math.max(worst, ms);
  check(t, sel, ...args);
  let ref = '';
  if (small.some(c => c[0] === name)) {
    const b = brute(sel, ...args);
    assert(t.logs >= b - 1e-9, `${name}: solver ${t.logs} < exhaustive ${b}`);
    ref = `, exhaustive ${(10 ** b).toFixed(1)}`;
  }
  console.log(`${name}: PF ${(10 ** t.logs).toFixed(1)}, ${t.dp.toFixed(0)} Pa, ${t.bands.length}/${sel.length} pieces, ` +
    `H ${t.H.toFixed(1)} cm, OD ${(t.ro * 20).toFixed(0)} mm, ${ms.toFixed(0)} ms${ref}`);
}
// Entry order and ids must not matter.
const five = small.find(c => c[0] === 'reviewer five')[1];
const shuffled = [five[3], five[0], five[4], five[2], five[1]].map((m, i) => ({...m, id: 'z' + (9 - i)}));
assert.equal(S.solve(shuffled).logs, S.solve(five).logs, 'entry order changed the plan');
assert.equal(S.solve([item('blanket', 10, 10, 1)]), null);
assert(worst < 5000, `slowest solve ${worst.toFixed(0)} ms`);
console.log('All checks passed.');
