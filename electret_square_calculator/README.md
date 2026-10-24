# Electret square calculator

Sizes a square stack of vacuum-bag electret for a fan that pressurises a room.
[Live page](https://mattnewell-cam.github.io/papr-filter/electret_square_calculator/).

**Inputs:** room pressure, orifice area (the room's total leak), fan shut-off pressure, and
either a PF target (100, 1,000 or 10,000 at 0.3 µm) or the electret on hand (m²).

**Outputs:** square side, number of layers and total electret area. PF target mode adds a
cost estimate; electret-on-hand mode gives the PF.

## Model

- **Airflow:** what leaks out through the orifice at the room pressure,
  Q = 0.61·A·√(2ΔP/ρ) with ρ = 1.2 kg/m³ (sharp-edged orifice).
- **Fan:** p(Q) = p_shut-off − 0.000383·Q², Q in L/min. The Q² term is the bag calculator's
  fan fit. The "Motor characterisation" tab's closed-end and open-end readings give
  0.00035–0.00039 at 8–15 V.
- **Filter pressure:** fan pressure at Q, minus the room pressure.
- **Per layer:** Arome Livii electret from [the bag calculator](../electret_bag_calculator/README.md),
  Δp = 2.58·v and log10 PF = 1.5863·v^−0.307 at 0.3 µm, v in cm/s. It was measured only at
  4.9–5.9 cm/s (inferred), and most designs run faster, so PF is usually extrapolated.
- **Seal:** every layer loses 2 cm on each side, as in the bag calculator.
- **PF target mode:** for each layer count, the fastest face speed that meets both the
  target and the pressure, with the square rounded up to 0.5 cm. The page picks the layer
  count that uses the least electret.
- **Electret on hand:** for each layer count, the biggest square the stock allows, rounded
  down to 0.5 cm. The page picks the highest PF within the pressure.
- **Cost:** 20 g/m² at US$2/kg. See the bag calculator's "Basis weight and price" notes.
