// node FnF_testing_blanket_filter_design/test.cjs
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {load: loadPlanner, cases} = require('../planner/test-solver.cjs');

const page = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8');
const planner = fs.readFileSync(path.join(__dirname, '../planner/src.html'), 'utf8');
const coreOf = html => html.match(/<script id="solvercore">([\s\S]*?)<\/script>/)[1];
const lf = s => s.split('\r\n').join('\n');
const fromFold = core => lf(core).slice(lf(core).indexOf('/* ---- folding ---- *'));

// 1. Folding and search are the planner's, character for character.
assert.equal(fromFold(coreOf(page)).trimEnd(), fromFold(coreOf(planner)).trimEnd(),
  'optimiser differs from planner/src.html - re-copy it');

const mats = page.match(/(const FITS=[\s\S]*?)\/\* ---- solver worker/)[1];
const S = new Function(`${coreOf(page)}\n${mats}\nreturn {FITS, TYPES, termsOf, logsOf, dpOf,
  solve(sel,p=202,r=15,h=50,ri=null,q=3000,seed=null){Q=q;LAST=seed;return optimise(sel,p,r,h,ri,false);}, seed:()=>LAST};`)();
const P = loadPlanner(planner);

// 2. Fits match the published coefficients and the planner.
const coeffs = JSON.parse(fs.readFileSync(path.join(__dirname, '../testing/coefficients.json'), 'utf8'));
for (const [id, f] of Object.entries(S.FITS)) {
  const c = coeffs[id].fits['0.3'], m = P.mats.find(m => m.id === id);
  for (const [a, b] of [['D','D'],['C','C'],['alpha','alpha'],['k','k_layer'],['vlo','v_lo'],['vhi','v_hi']])
    assert.equal(f[a], c[b], `${id} ${a} vs coefficients.json`);
  assert.equal(f.t, coeffs[id].t_layer, `${id} t`);
  assert.equal(f.B || 0, c.B || 0, `${id} B`);
  for (const k of ['D','C','alpha','k','t']) assert.equal(f[k], m[k === 'D' ? 'A' : k], `${id} ${k} vs planner`);
}

// 3. Term form reproduces the planner's closed form.
for (const id of Object.keys(S.FITS)) {
  const m = P.mats.find(m => m.id === id), g = {...m, terms: S.termsOf(S.FITS[id])};
  for (const [r0, r1, K] of [[2, 3, 50], [4, 15, 9.5], [0.6, 1.1, 120]]) {
    const a = P.logsOf(m, r0, r1, K), b = S.logsOf(g, r0, r1, K);
    assert(Math.abs(a - b) < 1e-12 * Math.max(1, a), `${id} logs ${a} vs ${b}`);
    assert(Math.abs(P.dpOf(m, r0, r1, K) - S.dpOf(g, r0, r1, K)) < 1e-9);
  }
}

// 4. Generic blanket = geometric mean per layer of the four tested blankets.
const B = ['blue holey', 'grey fuzzy', 'pink', 'grey holey'], bl = S.TYPES.blanket;
const perLayer = (terms, v) => terms.reduce((s, [c, p]) => s + c * v ** p, 0);
for (const v of [0.64, 1.2, 2.4, 6]) {
  const mean = B.reduce((s, id) => s + perLayer(S.termsOf(S.FITS[id]), v), 0) / 4;
  assert(Math.abs(perLayer(bl.terms, v) - mean) < 1e-12);
}
const gm = k => Math.exp(B.reduce((s, id) => s + Math.log(S.FITS[id][k]), 0) / 4);
assert(Math.abs(bl.k - gm('k')) < 1e-12 && Math.abs(bl.t - gm('t')) < 1e-12);
assert.equal(bl.vlo, 1.16); assert.equal(bl.vhi, 4.63);
assert.equal(S.TYPES.duvet.t, S.FITS.duvet.t); assert.equal(S.TYPES.linen.k, S.FITS['soft linen'].k);
console.log(`blanket: t ${bl.t.toFixed(4)} cm, k ${bl.k.toFixed(3)} Pa/(cm/s), ` +
  `QF@1.2 ${(Math.LN10 * perLayer(bl.terms, 1.2) / (bl.k * 1.2 / 1000)).toFixed(1)} kPa^-1`);

// 5. Same materials in, same plan out as the planner.
for (const [name, sel, ...args] of cases) {
  const a = P.solve(sel, ...args), b = S.solve(sel.map(m => ({...m, terms: S.termsOf({...m, D: m.A})})), ...args);
  assert(Math.abs(a.logs - b.logs) < 1e-9, `${name}: planner ${a.logs} vs page ${b.logs}`);
}

// 6. Generic multi-item builds are feasible and fast enough.
function check(t, sel, p = 202, r = 15, h = 50, ri = null, q = 3000) {
  assert(t && t.bands.length, 'expected a feasible plan');
  assert(t.H > 0 && t.H <= h + 1e-8 && t.ro <= r + 1e-8);
  if (ri) assert.equal(t.ri, ri);
  let logs = 0, dp = 0, radius = t.ri;
  const K = q / (2 * Math.PI * t.H), ids = new Set();
  for (const b of t.bands) {
    assert(sel.some(m => m.id === b.m.id) && !ids.has(b.m.id)); ids.add(b.m.id);
    assert(Math.abs(b.r0 - radius) < 1e-8 && b.n >= 1 - 1e-8);
    const f = t.folds[b.m.id];
    if (f.f * b.m.t >= 1) assert(Math.abs(b.turns - Math.round(b.turns)) < 1e-7);
    assert(f.axial >= t.H + t.ro - 1e-7);
    assert(Math.PI * (b.r1 ** 2 - b.r0 ** 2) / b.m.t <= f.stock + 1e-6);
    logs += S.logsOf(b.m, b.r0, b.r1, K); dp += S.dpOf(b.m, b.r0, b.r1, K);
    radius = b.r1;
  }
  assert(dp <= p + 1e-6 && Math.abs(dp - t.dp) < 1e-7 && Math.abs(logs - t.logs) < 1e-7);
}
const item = (type, L, W, n) => ({...S.TYPES[type], id: 'i' + n, type, L, W});
const builds = [
  ['one blanket', [item('blanket', 200, 150, 1)]],
  ['two blankets + duvet', [item('blanket', 200, 150, 1), item('blanket', 130, 170, 2), item('duvet', 200, 200, 3)]],
  ['mixed five', [item('blanket', 180, 130, 1), item('duvet', 220, 200, 2), item('linen', 230, 220, 3),
                  item('blanket', 150, 125, 4), item('linen', 200, 135, 5)]],
  ['eight pieces', [1,2,3,4,5,6,7,8].map(n => item(['blanket','duvet','linen'][n % 3], 120 + 10 * n, 140 + 7 * n, n))],
  ['tight limits', [item('blanket', 200, 150, 1), item('duvet', 200, 200, 2)], 80, 10, 30],
];
let worst = 0;
for (const [name, sel, ...args] of builds) {
  const t0 = performance.now(), t = S.solve(sel, ...args), ms = performance.now() - t0;
  worst = Math.max(worst, ms);
  check(t, sel, ...args);
  console.log(`${name}: PF ${(10 ** t.logs).toFixed(0)}, ${t.dp.toFixed(0)} Pa, ${t.bands.length} bands, ${ms.toFixed(0)} ms`);
}
// Two identical blankets can never do worse than one.
const one = S.solve([item('blanket', 200, 150, 1)]), two = S.solve([item('blanket', 200, 150, 1), item('blanket', 200, 150, 2)]);
assert(two.logs >= one.logs - 1e-9);
assert(worst < 5000, `slowest solve ${worst.toFixed(0)} ms`);
console.log('All checks passed.');
