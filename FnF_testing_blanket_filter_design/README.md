# Blanket filter designer (friends-and-family testing)

A user-facing front end to the rolled-filter model for people who don't own the tested
products. Each piece is entered as a generic **blanket**, **duvet** or **sheet** with its
length and width; the page returns a build within an airflow, pressure, diameter and
length budget. The page itself carries no model or testing detail; it lives here.

Published at https://mattnewell-cam.github.io/papr-filter/FnF_testing_blanket_filter_design/.

## Build rules

These differ from the [planner](../planner/README.md):

- Core inside diameter is fixed at **65 mm**.
- Every piece starts level with the fan end and must run **at least 8 cm past the far
  end**, where the overhang is gathered and tied. (The planner requires an overhang of
  at least the outer radius.)
- **Every piece used is used whole.** Its cross-section is plies × rolled length × t, so
  turns are fractional and are not reported. Each must go round at least once (radial
  depth ≥ plies × t), so no piece leaves an open slot. A piece that would break the
  pressure or diameter limit is left out, never trimmed.
- Folds are 1, 2, 3, 4, 6 or 8 equal plies: halving and thirding only. Roll length is
  searched from 5 cm up to the length limit, which excludes the overhang.
- There is no cap on overhang, so an unfolded duvet on a short roll can leave a very long
  tail.

## Materials

All fits are the 0.3 µm per-layer fits in `../testing/coefficients.json`.

| type | model | t_layer (cm) | k_layer (Pa/(cm/s)) | QF @1.2 cm/s (kPa⁻¹) |
|---|---|---|---|---|
| blanket | geometric mean of blue holey, grey fuzzy, pink, grey holey | 0.2968 | 3.184 | 61.8 |
| duvet | duvet (13.5 tog, polyester fill) | 1.9516 | 3.083 | 74.9 |
| sheet | soft linen (polyester soft-touch duvet cover) | 0.0514 | 6.293 | 14.7 |

The blanket average is taken per layer: its log10PF curve is the arithmetic mean of the
four blankets' curves (the geometric mean of their PFs), kept as the sum of their terms
rather than refitted; k_layer and t_layer are geometric means.

**Impaction cap.** Rising (impaction) terms are held at their value at the fastest
measured speed of their source fit (duvet 4.76 cm/s, blue holey 11.24 cm/s) wherever the
local speed is higher. Without it, the duvet's B·v term extrapolated to ~30 cm/s made a
5 cm long, 232 mm wide duvet roll the best single-duvet build (PF 7.9 against 3.2 for a
50 cm roll). Diffusion and interception terms are extrapolated as fitted. The planner does
not apply this cap.

## Solver

Seeded differential evolution over roll length, and per piece an order key, fold and use
flag, followed by a local search over length (including every length at which a fold just
fits), folds, use, pairwise order swaps and two-piece moves. The fold gene is the most
cloth a piece may contribute; if that breaks a limit the next wider fold is tried. Pieces
are sorted by type and size first, so entry order cannot change the plan. Runs in a Web
Worker.

`node FnF_testing_blanket_filter_design/test.cjs` (from the repository root) checks the
coefficients against `coefficients.json`, the term form against the planner's closed form,
the blanket average, the build rules on every plan, entry-order independence, and the
solver against an exhaustive search (0.25 cm length grid plus fold thresholds, every
subset, fold and order) on 15 cases of up to five pieces, six of them random. It takes
about a minute, almost all of it in the exhaustive search.

`index.html` is the source; there is no build step. Entries are saved in the browser's
local storage. Push to `main` to redeploy.
