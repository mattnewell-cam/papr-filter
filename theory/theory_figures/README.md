# Reproduce the Google Doc figures

These scripts load `../../testing/coefficients.json` (the 0.3 µm fits); no material coefficients are copied into them.
The geometry examples deliberately use alpha = 0.5, 200 Pa, 180 L/min and 20 L,
matching THEORY.md section 7. They are illustrations, not separate fitted catalogues.
The percentage labels on `annulus_trio.png` are losses in log10 PF, not PF.

Outputs go to `theory/plots/`. From the repository root:

```
python theory/theory_figures/branches.py
python theory/theory_figures/combined.py
python theory/theory_figures/capped.py
python theory/theory_figures/trio.py
python theory/roll_surface.py theory/plots/roll_ridge.png
python theory/roll_surface.py theory/plots/roll_ro15.png --ro 15 --h 50
python theory/roll_surface.py theory/plots/roll_ro12.png --ro 12 --h 50
python testing/plot_material_comparison.py   # -> testing/plots/material_comparison.png
```

The Google Doc embeds these as static images, so replace them there after regeneration.
