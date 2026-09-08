# Reproduce the Google Doc figures

These scripts load `../coefficients.json`; no material coefficients are copied into them.
The geometry examples deliberately use alpha = 0.5, 200 Pa, 180 L/min and 20 L,
matching THEORY.md section 7. They are illustrations, not separate fitted catalogues.
The percentage labels on `annulus_trio.png` are losses in log10 PF, not PF.

From the repository root:

```
python testing/theory_figures/branches.py
python testing/theory_figures/combined.py
python testing/theory_figures/capped.py
python testing/theory_figures/trio.py
python testing/roll_surface.py testing/plots/roll_ridge.png
python testing/roll_surface.py testing/plots/roll_ro15.png --ro 15 --h 50
python testing/roll_surface.py testing/plots/roll_ro12.png --ro 12 --h 50
python testing/plot_material_comparison.py
```

The Google Doc embeds these as static images, so replace them there after regeneration.
