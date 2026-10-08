# Blanket filter designer (friends-and-family testing)

A simpler front end to the [planner](../planner/README.md) for people who don't own the
tested products. Each piece is entered as a generic **blanket**, **duvet** or **linen** with
its length and width; the page returns a rolled-filter build within an airflow, pressure,
outer-diameter and length budget.

Published at https://mattnewell-cam.github.io/papr-filter/FnF_testing_blanket_filter_design/.

## Materials

All fits are the 0.3 µm per-layer fits in `../testing/coefficients.json`.

| type | model | t_layer (cm) | k_layer (Pa/(cm/s)) | measured v (cm/s) | QF @1.2 cm/s (kPa⁻¹) |
|---|---|---|---|---|---|
| blanket | geometric mean of blue holey, grey fuzzy, pink, grey holey | 0.2968 | 3.184 | 1.16–4.63 | 61.8 |
| duvet | duvet (13.5 tog, polyester fill) | 1.9516 | 3.083 | 0.66–4.76 | 74.9 |
| linen | soft linen (polyester soft-touch duvet cover) | 0.0514 | 6.293 | 0.42–3.52 | 14.7 |

The blanket average is taken per layer: its log10PF curve is the arithmetic mean of the
four blankets' curves (the geometric mean of their PFs), and k_layer and t_layer are
geometric means. The mean curve is kept as a sum of the four fits' terms rather than
refitted. Its measured range is the overlap of the four ranges, so more layers are
flagged as extrapolated than for any single blanket.

## Solver

The folding rules and optimiser are copied character for character from
`../planner/src.html`. The only change is `logsOf`, which takes a list of power-law terms
so the averaged blanket can be represented. Each entered piece is its own material, so it
gets at most one band. `node FnF_testing_blanket_filter_design/test.cjs` (run from the
repository root) checks that the copied code still matches the planner, that the
coefficients match `coefficients.json`, that the planner's own test cases give identical
scores, and that multi-piece builds are feasible. Re-copy the optimiser after changing
the planner's.

`index.html` is the source; there is no build step. Entries are saved in the browser's
local storage. Push to `main` to redeploy.
