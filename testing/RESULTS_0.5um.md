# 0.5 µm material fits

`coefficients_0.5um.json` contains eight fits to count-based 0.5 µm PF.
The 0.3 µm catalogue and planner are unchanged. Reproduction commands are in
[FITTING.md](FITTING.md); [fit plots](plots/fits_0.5um.png) show the measured responses.

Sources are the saved September 5 prototype export and the separate IIR mask CSV,
from [DIY PAPR Testing](https://docs.google.com/spreadsheets/d/1vNnPBNcy6AXGmybD3XqS8CLbzuCFn33SeNJbljD8o0Y/edit).
Input hashes, row selections, geometry, residual errors and velocity ranges are
stored with the coefficients. These are fits to those measurements, not independent
validation. The fit form and bounds match the 0.3 µm procedure, with the impaction
endpoint rule applied anew to the 0.5 µm observations.

Both particle channels now use only current grey-fuzzy rows 5–9 and share the
same pressure coefficient, 5.783331 Pa/(cm/s) per layer. The previous 0.3 µm
grey-fuzzy fit included superseded data and was corrected on 2026-09-08.

IIR has a small highest-velocity upturn (PF 22.9 versus a minimum of 22.8), which
triggers the existing impaction rule. That is weak evidence for the extra term.
Its 0.5 and 1 cm/s predictions are extrapolations below the measured 5.1 cm/s floor,
with the diffusion exponent at its 2/3 cap.

For rolls, `midpoint_v_lo/hi` is the range of mid-wall velocities of the tests;
`v_lo/hi` spans the local velocities across all measured annuli. The summary uses
mid-wall ranges for consistency with the existing table; they are not flat-coupon
measurements at every velocity in that interval.
