# Patents pool - loading / ageing of electret filter media

Conventions. "Deposited" = mass captured on the media. Patents that report DOP "exposure" or "challenge" give mass incident on the sample, not mass captured; captured = incident x (1 - P) integrated, and I bound it by using the start and end penetration of each interval (bounds shown). g/m2 is per m2 of media area (exposed sample area). Retained = ln P_loaded / ln P_initial (fraction of -ln P kept). Lost-electrostatic = (ln P_loaded - ln P_initial)/(ln P_discharged - ln P_initial). QF converted with 1 mmH2O = 9.807 Pa, so QF[kPa^-1] = QF[1/mmH2O] x 102.0.
3M "DOP" tests: TSI 212 sprayer or TSI AFT 8110/8130, nominally 0.3 um mass-median DOP, upstream ~100 mg/m3, light-scattering (photometric, mass-weighted) penetration. Not count-based.

---

## US5496507 (3M, Angadjivand et al., filed 1993, granted 1996) - hydrocharging
Link: https://patents.google.com/patent/US5496507A/en (PDF pages read: 6, 9, 10, 11). Same examples reprinted in US6119691 (3M, "Electret filter media").

CORRECTION to the brief: the Table 10 and Table 11 media are poly(4-methyl-1-pentene) (PMP, Mitsui TPX), not polypropylene. Ex 42/44 are "prepared as in Example 31", and Ex 31 is "a web of the poly(4-methyl-1-pentene) ... prepared as in Example 28, except only one extruder" (col. 10-11; Ex 28 used TPX MX-007 in the second extruder). Ex 43 is TPX MX-002. All corona-charged then water-jet (hydro) charged.

### Series 1 - Table 10 (p.10, col. 14): cigarette smoke, flat sample
- Media: Ex 42 PMP (TPX MX-007), EFD 14 um, 50 g/m2, corona + hydrocharge, dP 2.8 mmH2O at 26.7 cm/s. Ex 43 PMP (TPX MX-002), same process, dP 3.4 mmH2O at 26.7 cm/s.
- Loading: 1 m3 chamber, Norelco CAM 770 room air cleaner fitted with a 14 x 14 cm flat sample (0.0196 m2 face); smoker burns 1-10 cigarettes over 4-5 min; fan mixing. No mass, no flow through the sample, no RH stated.
- Efficiency test: TSI AFT-8110, NaCl, photometer (mass-weighted), 26.7 cm/s.
- E (%) uncharged / initial / after 1 / after 5 / after 10 cigarettes:
  - Ex 42: 16.5 / 80.5 / - / 48.8 / 17.9
  - Ex 43: 18.6 / 67.1 / 60.3 / 53.9 / 34.4
- Retained -lnP (Ex 42): 5 cig 0.41; 10 cig 0.12. Lost-electrostatic (uncharged 16.5%): 5 cig 0.66; 10 cig 0.99 (fully discharged by 10 cigarettes).
- Retained (Ex 43): 1 cig 0.83, 5 cig 0.70, 10 cig 0.38. Lost-electrostatic (uncharged 18.6%): 0.21 / 0.37 / 0.76.
- Deposited mass: NOT STATED. Cannot convert to g/m2 without the smoke mass and the air cleaner's flow.

### Series 2 - Table 11 (p.11, col. 15-16): ambient air, pleated element
- Media: Ex 44 PMP (TPX MX-007), EFD 14 um, 40 g/m2, 1.2 mm, corona + hydrocharge; pleated with an 80 g/m2 Colback scrim; element 29 cm x 10 cm, 52 pleats of 28 mm height. Media area 52 x 2 x 0.028 x 0.10 = 0.29 m2 if "pleats" means folds (the text doesn't say).
- Loading: "ambient air at a flow rate of 149 ft3/min (250 m3/hr)" through samples 300 mm x 116 mm (col. 5, verified on p.6 image). Face velocity 250/3600/0.0348 = 2.0 m/s; media velocity ~24 cm/s if 0.29 m2. Location, concentration, RH and mass gained NOT STATED.
- Efficiency at 0.3 / 1.0 um: "measured as described in the cigarette smoke adsorption test" (which used a PMS LAS-X counter in the chamber and an AFT-8110 photometer - which instrument gave the size-resolved number is ambiguous).
- Ex 44a 0.3 um: E 70.5 -> 53.8 (133 h) -> 47 (290 h). dP 10.8 -> 13.8 -> 15.5 mmH2O.
- Ex 44b 1.0 um: E 86.8 -> 79.0 (133 h) -> 75 (290 h). dP same column (10.8 / 13.8 / 15.5).
- Retained -lnP: 0.3 um 0.63 (133 h), 0.52 (290 h); 1.0 um 0.77, 0.68. No uncharged value for this web.
- dP rose 43% in 290 h, so a cake/deposit was forming; mass not reported.

### Series 3 - Table 9 (p.10): respirator filter elements, "Loaded penetration"
- Multi-layer elements (2-6 layers per wall, 10.16 cm discs, Brostrom-type element). Initial and "loaded" DOP penetration and dP. The loading amount and protocol for "loaded" are not defined anywhere in the text (searched). Example: Ex 41e (2 layers PP 55 g/m2, corona+hydro) 0.177% -> 3.37%; C11 (6 layers PP corona only) 0.015% -> 0.127%. Unusable for g/m2.

---

## US4874399 (3M, Reed et al., filed 1988, granted 1989; = EP0325854B1) - PP vs poly(4-methyl-1-pentene) blends; DOP mass COLLECTED at 75% and 50% of initial Q
Link: https://patents.google.com/patent/US4874399A/en ; text read from EP0325854B1 (data.epo.org); Tables I-III verified on USPTO image (cols. 5-6, PDF p.9).
- Media (Ex 1): melt-blown, Fina 12 MFI PP and/or TPX MX-007 PMP, EFD 6.5-7.5 um, solidity 5-6%. Single-layer 13.3 cm sample mass 0.71 g (PP) -> 0.71 g / 138.9 cm2 = 51 g/m2; 0.66 g (PMP) = 47.5 g/m2. Charged by corona / pulsed high voltage (generic; Kubik/Wadsworth/Nakao methods cited).
- Loading Test: ATI Q127, DOP 0.3 um, 0.15-0.2 g/m3, 46.7 L/min through a 11.4 cm (4.5 in) circle = 102.6 cm2 -> 7.6 cm/s; 30 min; samples weighed before/after and the integrated (1-Pen) mass forced to agree with the weighed gain within 5%. So the masses below are COLLECTED DOP. Q = -ln(Pen)/dP [1/mmH2O]; the Q drop includes the (small) dP rise.
- Table II (single layer): initial Q 0.55-0.57 /mmH2O (56-58 kPa^-1 at 7.6 cm/s).
  - 100% PP: Q -> 0.75 Q0 at 8.7 / 8.6 mg (0.85 / 0.84 g/m2); -> 0.5 Q0 at 24.9 / 27.9 mg (2.4 / 2.7 g/m2).
  - 0.2% PMP: 7.7 / 9.3 mg (0.75 / 0.91 g/m2); 23.9 / 24.8 mg (2.3 / 2.4 g/m2).
  - 1% PMP: 17.2 mg (1.7 g/m2); 55.8 mg (5.4 g/m2).
  - 10% PMP: 17.9 / 17.7 mg (1.7 g/m2); 72.2 / 90.0 mg (7.0 / 8.8 g/m2).
  - 30% / 50% / 100% PMP: 16.0 / 14.4-16.0 / 18.2 mg (1.4-1.8 g/m2); 62.7 / 58.0-66.0 / 74.2 mg (5.7-7.2 g/m2).
- Table III (4 layers of the same webs, 204 g/m2 total): PP 42.5 mg (4.1 g/m2 of face) at 0.75 Q0, 132.9 mg (13.0 g/m2) at 0.5 Q0; 1-100% PMP 88.6-152.1 mg (8.6-14.8 g/m2) at 0.75 Q0 and > 220 mg (> 21 g/m2) at 0.5 Q0.
- Table V (Ex 3, fibrillated split-film fibres ~10 x 40 um, initial Q 1.5-2.3): single layer PP (129-205 g/m2) 12.9-13.8 mg (1.3 g/m2) at 0.75 Q0, 28.5-34.2 mg (2.8-3.3 g/m2) at 0.5 Q0; 15% PMP 20.0 / 50.1 mg (1.9 / 4.9 g/m2); 100% PMP 15.8 / 38.0 mg. Multi-layer (~640 g/m2): PP 48.7-64.7 mg (4.7-6.3 g/m2) / 112.5-136.5 mg (11-13 g/m2); 15% PMP 81.3 / 192.5 mg (7.9 / 18.8 g/m2).
- Table I (Aging Test, no load; 70 C oven, then 20 s DOP at 32 L/min = 5.2 cm/s): PP Q 1.23 -> 0.79 (8 h) -> 0.74 (24 h) -> 0.64 (72 h); 100% PMP 1.71 -> 1.37 -> 1.21 -> 1.05.
- Table VI (cup respirators, 1 layer, extrapolated to 100 mg DOP; respirator area not stated): PP pen 15.9% -> 53%; 10% PMP 8.9 -> 21%; 100% PMP 8.5 -> 19%.
- Normalised by fibre surface area (S = 4 BW / (rho d), rho 0.90, d 7 um -> 32 m2 per m2 for one PP layer): 0.5 Q0 at 0.075-0.085 g DOP per m2 of fibre surface (single layer) and 0.10 (4 layers, 130 m2/m2). Toyobo's plain corona PP (US10940415 Comp 2-1, tobacco smoke) halves -lnP at ln2/9.17 = 0.076 g per m2 of fibre surface - the same number from a different aerosol, lab and decade.

---

## US5411576 (3M, Jones et al., filed 1993, granted 1995) and US5472481 (division, identical examples) - fluorochemical melt additive
Link: https://patents.google.com/patent/US5411576A/en ; page images read: USPTO PDF pp. 5-6 (Tables II-VI all verified).
- Media: Exxon Escorene PP-3505 melt-blown, corona charged (0.01 mA/cm), annealed 140 C 10 min (except C6). 50-57 g/m2, 0.69-1.45 mm (Table II). Additives A-J at 1 wt% (A-G fluorochemical oxazolidinones / piperazine / perfluorinated alkane). C4 and C7: no additive. C5: additive A, uncharged.
- DOP Loading Test: 4.5 in (11.43 cm) disc, 42.5 L/min, 6.9 cm/s (exposed area 102.6 cm2 = 0.01026 m2; consistent with 42.5 L/min / 6.9 cm/s). DOP "0.3 um", 70-110 mg/m3, TSI 212 sprayer; Air Techniques TPA-8F light-scattering photometer. Exposure 45 min (130-200 mg). Results interpolated to 50 and 100 mg EXPOSURE (incident, not captured). 50 mg = 4.87 g/m2 incident; 100 mg = 9.75 g/m2 incident. RH not stated. Tested ~3 days after charging.
- Penetration (%) initial / 50 mg / 100 mg, dP (mmH2O) initial / 50 / 100 (Table III, Table V, Table VI):

| Ex | additive | P0 | P50 | P100 | dP0/50/100 | deposited at 50 mg (g/m2, bounds) | at 100 mg | retained -lnP 50/100 | lost-electrostatic 50/100 (P_d = C5 84%) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | A 1% | 29 | 35 | 38 | 1.8/2.0/2.1 | 3.2-3.5 | 6.2-6.6 | 0.85/0.78 | 0.18/0.25 |
| 2 | B | 29 | 33 | 35 | 1.8/2.0/2.1 | 3.3-3.5 | 6.4-6.7 | 0.90/0.85 | 0.12/0.18 |
| 3 | C | 21 | 24 | 26 | 2.3/2.6/2.8 | 3.7-3.8 | 7.3-7.6 | 0.91/0.86 | 0.10/0.15 |
| 4 | D | 15 | 23 | 33 | 2.2/2.3/2.4 | 3.8-4.1 | 7.0-7.9 | 0.77/0.58 | 0.25/0.46 |
| 5 | E | 32 | 36 | 41 | 1.7/1.9/2.0 | 3.1-3.3 | 6.0-6.4 | 0.90/0.78 | 0.12/0.26 |
| 6 | F | 11 | 22 | 40 | 4.1/4.3/4.3 | 3.8-4.3 | 6.7-8.1 | 0.69/0.42 | 0.34/0.64 |
| 7 | G | 37 | 55 | 64 | 1.7/1.8/1.8 | 2.2-3.1 | 3.9-5.3 | 0.60/0.45 | 0.48/0.67 |
| C2 | I (low m.p.) | 40 | 38 | 48 | 2.2/2.4/2.5 | 2.9-3.0 | 5.5-6.0 | 1.06/0.80 | -0.07/0.25 |
| C3 | J | 34 | 78 | 81 | 2.5/2.5/2.6 | 1.1-3.2 | 2.0-4.3 | 0.23/0.20 | 0.92/0.96 |
| C4 = C7 | none | 41 | 77 | 81 | 1.9/1.9/1.9 | 1.1-2.9 | 2.0-4.0 | 0.29/0.24 | 0.88/0.95 |
| C5 | A, uncharged | 84 | 81 | 79 | 1.9/2.0/2.0 | - | - | - | - |
| C6 | A, not annealed | 30 | 69 | 81 | 2.1/2.1/2.1 | 1.5-3.4 | 2.4-4.9 | 0.31/0.18 | 0.81/0.96 |
| C8 (aged 70 C 72 h) | none | 44 | 70 | 83 | 2.2/2.1/2.3 | 1.5-2.7 | 2.3-4.2 | 0.43/0.23 | 0.72/0.98 |
| 8 (aged) | A 0.5% | 30 | 32 | 38 | 2.3/2.5/2.6 | 3.3-3.4 | 6.3-6.7 | 0.95/0.80 | 0.06/0.23 |
| 9 (aged) | A 1% | 31 | 28 | 27 | 2.1/2.4/2.6 | 3.4-3.5 | 6.9-7.1 | 1.09/1.12 | <0 |
| 10 (aged) | A 2% | 39 | 39 | 37 | 1.7/1.9/2.1 | 3.0 | 5.9-6.0 | 1.00/1.06 | <0 |

- Initial QF (Table III): Ex 1 0.70 /mmH2O = 71 kPa^-1 at 6.9 cm/s; C4 0.47 /mmH2O = 48 kPa^-1. Ex 1 QF at 100 mg after 60 C/72 h ageing 0.52 /mmH2O (53 kPa^-1); C4 0.14 (14 kPa^-1) (Table IV).
- Table IV (aged 47-73 h at 60-70 C, then loaded): Ex 1 30/32/32; Ex 2 27/29/30; C4 35/66/76; C3 50/77/79; C2 83/81/83 (charge lost in ageing).
- Reading: plain corona PP (no additive) loses ~90% of its electrostatic -lnP by ~2-4 g/m2 of captured DOP; the best fluorochemical webs lose 10-25% by ~6-7 g/m2. Additive identity matters (Ex 6, 7 lose 64-67% by 100 mg). Annealing is required (C6).

---

## US6398847 (3M, Jones et al., filed 1998/2000, granted 2002) - surface-fluorinated electret
Link: https://patents.google.com/patent/US6398847B1/en ; FIG. 1-3 on PDF pp. 3-5 (read from rendered images; values below read off the plots, +/-0.3 percentage points at low P).
- Media (Ex 36-39): Exxon 3505G PP BMF, EFD 7.5 um, 62 g/m2 (Example 1), AC-corona fluorinated in 0.1% hexafluoropropylene (HFP; Ex 36, 38) or 0.1% C5F12 (Ex 37, 39); then hydrocharged (36, 37) or DC corona charged (38, 39). Ex 40: PP BMF 61 g/m2, fluorinated with 5-10% F2 gas (62 at% F), DC corona.
- DOP Loading Test: 4.5 in sample (102.6 cm2), 42.5 L/min, 6.9 cm/s, DOP 70-140 mg/m3, TPA-8F photometer, >=45 min. x-axis is "DOP Load (grams)" = mass COLLECTED on the web (col. 6). g/m2 = grams / 0.01026.
- Uncharged and initial references (Table II, same fluorination recipes): HFP uncharged 59.0%, corona 16.2%, hydro 0.276%; C5F12 0.1% uncharged 52.5%, corona 14.0%, hydro 0.250%.
- FIG. 1 (hydrocharged): Ex 37 (C5F12) ~1.0% at 0.05 g (4.9 g/m2), ~1.3% at 0.10 g (9.7 g/m2), ~1.8% at 0.15 g, ~2.4% at 0.20 g, ~3.3% at 0.25 g (24 g/m2). Ex 36 (HFP) ~1.6% at 0.10 g, ~2.9% at 0.20 g, ~3.8% at 0.25 g, ~4.0% at 0.26 g.
  - Retained -lnP (P0 from Table II): Ex 37 0.77 (4.9 g/m2), 0.72 (9.7), 0.57 (24); Ex 36 0.70 (9.7), 0.56 (24).
  - Lost-electrostatic: Ex 37 0.26 / 0.31 / 0.48; Ex 36 0.33 (9.7) / 0.49 (24).
- FIG. 2 (DC corona): Ex 38 (HFP) ~17% -> ~25% at 0.195 g (19 g/m2): retained 0.78, lost 0.31. Ex 39 (C5F12) ~14.5% -> min ~13% near 0.05 g -> ~15.5% at 0.22 g (21 g/m2): retained 0.97, lost 0.05.
- FIG. 3 (Ex 40, F2-gas fluorinated, corona): 7.5% at 0 -> 8.7% at 0.006 g -> ~9.2% at 0.04 g -> ~10% at 0.08 g -> ~11% at 0.11 g -> ~12% at 0.135 g (13.2 g/m2): retained 0.82 at 13 g/m2.
- Initial QF (Table II): hydro-charged fluorinated PP 1.89-2.03 /mmH2O (193-207 kPa^-1) at 6.9 cm/s; corona-charged 0.58-0.65 /mmH2O (59-66 kPa^-1).

---

## US6068799 (3M, Rousseau et al., filed 1997, granted 2000) + divisions US6214094, US6238466 (identical examples) - quench/anneal, fluorochemical additive; "Min@Chl"
Link: https://patents.google.com/patent/US6068799A/en (Tables 9A/9B verified on PDF p.25, col. 21)
- Media: Escorene 3505G or Fina 3860 PP + ~1.1 wt% fluorochemical melt additive, BMF 69-74 g/m2, 1.3-1.4 mm, dP 6.2-7.0 mmH2O at 13.8 cm/s (one layer), annealed ~150 C 4.5 min, corona charged. Quenched (water spray at die) vs not.
- DOP Loading Test: TSI AFT 8110/8130, DOP 0.3 um MMD, 100 mg/m3, 85 L/min, ionizer OFF, light-scattering. TWO layers stacked. Procedure 1: 15.2 cm exposed (182.4 cm2), 7.77 cm/s. Procedure 2: 11.4 cm exposed (102.6 cm2), 13.8 cm/s. Samples weighed after loading as a cross-check.
- Metric: Min@Chl = DOP mass INCIDENT on the sample when penetration reaches its minimum, i.e. the challenge before any degradation starts. The patent states a preferred initial DOP penetration < 5% (example values are not printed); if so, incident ~ captured within 5%.
- Table 1 (Ex 1, Procedure 2, 102.6 cm2): Min@Chl 78-340 mg by position = 7.6-33 g/m2.
- Table 4A/4B (Ex 4, Proc. 2): unquenched 67-200 mg (6.5-19 g/m2); quenched 106-344 mg (10-34 g/m2).
- Table 9A/9B (averages, Ex 4-8): unquenched averages 93-198 mg; quenched 248-647 mg (individual up to 899 mg). Ex 4 = Proc. 2 (102.6 cm2); Ex 5-8 = Proc. 1 (182.4 cm2): quenched averages 375-647 mg = 21-35 g/m2; unquenched 93-198 mg = 5-11 g/m2.
- Preferred claims: Min@Chl > 500 mg, ideally 800-1000 mg on 182 cm2 (27-55 g/m2); respirator of 180 cm2 > 400-600 mg DOP under NIOSH APRS-STP-0051-00 (22-33 g/m2).
- Min@Chl says when degradation STARTS, not how fast it proceeds afterwards; no penetration-after-Min values printed.

## US6213122 (3M, Rousseau et al., filed 1997, granted 2001) + US6237595, US6319452 (same examples) - extractable hydrocarbons
Link: https://patents.google.com/patent/US6213122B1/en
- Same DOP loading test as US6068799 Procedure 2 (two layers, 102.6 cm2 exposed, 13.8 cm/s, 85 L/min, ionizer off).
- Min@Chl vs chloroform-extractable hydrocarbon (Table 3, col. 10, verified on image): 1.1-1.5% extractables -> 71-270 mg (6.9-26 g/m2 incident; the patent quotes only the best, 183-270); 2.1-2.5% -> 62-163 mg; 3.4-4.0% (Fina HMF 3860) -> 23-57 mg (2.2-5.6 g/m2). Weak correlation, 3-sample averages.

---

## US6627563 (3M, Huberty et al., filed 1999, granted 2003) - two-layer P-series respirator filter; full DOP curves to 600 mg
Link: https://patents.google.com/patent/US6627563B1/en ; FIG. 4-9 on PDF pp. 3-5 (read off rendered plots; +/- ~0.3 points at P > 5%, +/- 0.03 points at P < 1%).
- Test: TSI AFT 8110/8130, DOP 0.3 um MMD, ~100 mg/m3, ionizer ON (charge-neutralised aerosol), 85 L/min, 2 stacked discs, 15.2 cm exposed (182.4 cm2 = 0.01824 m2), 7.77 cm/s; x-axis = DOP CHALLENGE (incident). 200 mg = 11.0 g/m2 incident; 600 mg = 32.9 g/m2.
- Layer A (Comp. Ex A): PP + fluorochemical additive, water-spray quenched, annealed, corona charged (as WO 99/16532 Ex 7); 100 g/m2, 1.5 mm, ~5.5 mmH2O per layer, initial QF 0.45 /mmH2O (46 kPa^-1) per layer.
- Layer B (Comp. Ex B): Fina 3960 PP, made "according to" layer A but not quenched and hydrocharged; 33 g/m2, 0.58 mm, ~1.7 mmH2O, initial QF 1.6 /mmH2O (163 kPa^-1). The text says the second layer "preferably include[s]" an oily-mist additive; whether B has it is not stated explicitly. Comp. Ex D = B layers aged 95 C for 15 h (QF 0.8).
- FIG. 4, A+A (200 g/m2, F778 dP 10.9 mmH2O): P 0.76% -> max 0.92% at ~60-100 mg -> 0.67% (200 mg) -> 0.46% (300) -> 0.30% (400) -> 0.25% (500) -> 0.23% (600). Worst retained -lnP 0.96 (at the maximum, ~3-5 g/m2). Then efficiency rises.
- FIG. 5, B+B (66 g/m2, dP 2.8): P 1.2% -> 4.6% (100 mg) -> 9.7% (200) -> 16.5% (300) -> 22.5% (400) -> 29.6% (500) -> 37.4% (600).
  - Captured (trapezoid on 1-P): 97 mg (5.3 g/m2) at 100 mg; 190 mg (10.4 g/m2) at 200; 277 (15.2) at 300; 357 (19.6) at 400; 431 (23.6) at 500; 498 mg (27.3 g/m2) at 600.
  - Retained -lnP: 0.70 at 5.3 g/m2; 0.53 at 10.4; 0.41 at 15.2; 0.34 at 19.6; 0.28 at 23.6; 0.22 at 27.3. No discharged value given.
- FIG. 6, B upstream + A downstream (dP 7.8): 0.40% -> 1.17 (100) -> 1.86 (200) -> 2.34 (300) -> 2.52 (400) -> 2.73 (500) -> 2.93% (600).
- FIG. 7, D+D (aged B; dP 3.5): 6.7% -> 12.6 (100) -> 18.9 (200) -> 23.7 (300) -> 29.4 (400) -> 36.3 (500) -> 42.4% (600). Retained -lnP 0.77 / 0.62 / 0.53 / 0.46 / 0.38 / 0.32.
- FIG. 8, A upstream + B downstream (Ex 1, dP 7.4): 0.63% -> max 0.87% at ~100 mg -> 0.75 (200) -> 0.55 (300) -> 0.46 (400) -> 0.41 (500) -> 0.42% (600+).
- FIG. 9, A + D (Ex 2, dP 6.9): 2.5% -> max 3.0% at ~60-90 mg -> 2.1 (200) -> 1.4 (300) -> 1.0 (400) -> 0.75 (500) -> 0.65% (600).
- Reading: the light hydrocharged layer (QF 1.6) loses ~half its -lnP by ~10 g/m2 of captured DOP; the heavy fluorochemical quenched/annealed corona layer does not degrade at all over 33 g/m2 incident (penetration falls after a small early rise).

---

## US6802315 (Hollingsworth & Vose, Gahan & Choi, filed 2001, granted 2004) - vapour-deposited fluoroacrylate + corona; DOP loading with an uncharged control
Link: https://patents.google.com/patent/US6802315B2/en ; Tables 1-3 verified on PDF p.10 (cols. 11-12); Tables 4-6 on p.11.
- Media: 30 g/m2 PP meltblown containing 1 wt% Acrawax C (ethylene bis-stearamide) on a 0.45 oz/yd2 (15 g/m2) PP spunbond. Ex 1: plasma + ~1 g/m2 fluoroacrylate vapour-deposited + e-beam cured, then corona (Simco bars -20 kV). Comp A: same coating, NOT charged. Comp B: charged, NOT coated. Number of plies in the tested stack not stated (dP ~18-20 mmH2O implies several plies).
- Test: NIOSH 42 CFR 84 style DOP loading, 85 L/min on 170 cm2 (8.33 cm/s, "16.4 fpm"); "DOP load (mg)" to 250 mg. 10 mg = 0.59 g/m2; 200 mg = 11.8 g/m2 (load ~ captured because P is small, except Comp A).
- Table 1 penetration (%), load 0/10/20/30/40/50/60/70/80/100/150/200/250 mg:
  - Ex 1 (coated + charged): 0.012/0.013/0.014/0.015/0.015/0.016/0.017/0.018/0.020/0.022/0.027/0.034/0.041
  - Comp A (coated, uncharged): 6.2/6.2/6.1/6.1/6.1/5.9/6.0/6.0/6.0/5.9/6.1/6.5/7.2
  - Comp B (charged, uncoated; amide additive only): 0.016/0.088/0.240/0.590/1.100/2.500/3.400/5.300/6.600/7.200/9.100/11.400/14.400
- Table 3 resistance (mmH2O): Ex 1 18.2 -> 19.7 (200 mg); Comp A 18.3 -> 22.9; Comp B 20.5 -> 22.4.
- Comp B, lost-electrostatic (P_discharged = Comp A 6.2%): 0.29 at 0.59 g/m2; 0.45 at 1.18; 0.61 at 1.76; 0.71 at 2.35; 0.85 at 2.94; 0.90 at 3.5; 0.97 at 4.1; ~1.0 from ~4.7 g/m2 (its P passes the uncharged web at ~75 mg). Retained -lnP: 0.80 / 0.69 / 0.59 / 0.52 / 0.42 (50 mg) / 0.34 (70 mg) / 0.30 (100 mg) / 0.25 (200 mg).
- Ex 1: retained -lnP 0.89 at 200 mg (11.8 g/m2); lost-electrostatic 0.17.
- Initial QF: Ex 1 0.50 /mmH2O = 51 kPa^-1; Comp B 0.43 /mmH2O = 43 kPa^-1 (8.33 cm/s, stack).
- Tables 4-6 (Ex 2, 3: 35 g/m2 meltblown + 14 g/m2 spunbond, coated, 2- and 4-ply, "DOP load" 0-30 mg): penetration roughly doubles over 30 mg (Ex 2 2-ply 0.310 -> 0.586%; Ex 3 2-ply 0.589 -> 1.22%; 4-ply 0.003 -> 0.009% and 0.009 -> 0.020%), but the printed resistance FALLS 23-26% with load (44.8 -> 34.3 mmH2O) - physically odd; the load column may be minutes and/or the units are wrong. Low weight.

## US6780226 (Hollingsworth & Vose, Cox et al., priority 1995, granted 2004) - charge-stabilising additives (fluorochemical FX-1801, fatty amide Acrawax C)
Link: https://patents.google.com/patent/US6780226B1/en (Tables 3, 4, 5A verified on PDF p.21, cols. 9-10)
- Media: PP meltblown, 40 g/m2 per ply (Ex 1), AC/DC corona. Test: 100 mg/m3 DOP at 32 L/min on 100 cm2 (5.3 cm/s), 22 min, scaled from a 265 cm2 mask at 85 L/min loaded with 200 mg -> ~7.0-7.5 g/m2 incident. 1-4 plies tested.
- Table 3, H&V alpha (= -100 log10 P / dP[mmH2O]) initial -> after the 22-min DOP challenge (dP changes ~5%, so retained -lnP ~ 1.05 x alpha ratio): I (no additive) 24 -> 8 (retained ~0.35); J (0.6% amide) 31 -> 14 (0.47); C (0.5% FX-1801) 38 -> 13 (0.36); A (1% FX) 44 -> 18 (0.43); B (2% FX) 45 -> 27 (0.63); D (0.5% FX + 0.6% amide) 46 -> 26 (0.59); E (0.5% FX + 1.2% amide) 45 -> 29 (0.68); H (1% FX + 0.6% amide) 48 -> 31 (0.68); F (AC only) 30 -> 24 (0.84). Ply count for Table 3 not stated.
- Table 4: basis weight needed for 5% DOP penetration after the 200 mg-equivalent load: no additive 125 g/m2; best additive mix (E) 70 g/m2.
- Tables 5A-6B (Ex 2): minute-by-minute DOP P, dP, alpha for very light webs (dP 0.4-0.9 mmH2O, P ~46-55% initial): e.g. no-additive control 46.5% -> 72% at 20 min (retained -lnP 0.43); 1% FX-1801 45.6% -> 66.9% at 19 min (0.51); 3% Zonyl FTS 53.8 -> 72% (0.53). Flow/area for Ex 2 not restated (if as Ex 1, 20 min ~ 6.4 g/m2 incident, ~2.5-3 g/m2 captured).
- Table 8: heat-treating the web at 115 C 15 min BEFORE charging left P at 77-88% (charging largely ineffective) - a de facto near-uncharged reference.

---

## US10940415 (Toyobo, Kitagawa, priority JP 2015-10-02, granted 2021; = US2018/0272259, WO2017/057148) - tobacco smoke and PAO durability, with a discharged control
Link: https://patents.google.com/patent/US10940415B2/en ; read from USPTO image PDF pp. 1, 14-21 (cols. 21-36); all values below verified on the page images.
- Media (Table 2, second invention): PP meltblown 30-30.3 g/m2, 0.23-0.24 mm, EFD 5.5-5.7 um, fibre surface area 23.4-24.2 m2 per m2, dP 2.6-2.9 mmAq at 5 cm/s, corona charged. Ex 2-1: 0.30 g/m2 n-C18F38 from solution; Ex 2-2: 0.30 g/m2 n-C18F38 vapour-deposited; Ex 2-3: 0.30 g/m2 fluoro-methacrylate copolymer particles; Comp 2-1: plain corona PP; Comp 2-2: discharged by ethanol immersion.
- Tobacco smoke loading (cols. 26, 32): 4 Mevius cigarettes burned in a 1 m3 box (JEM 1467); 72 mm disc in a 50 mm-diameter holder (19.63 cm2) ventilated at 12 L/min (10.2 cm/s) for 10 min per cycle; filter weighed before/after each cycle (collected mass; volatiles partly evaporate between cycles; NaCl from the efficiency test adds mass). Cycles repeated until retention < 15%.
- Efficiency: initial = 0.3-0.5 um COUNT efficiency (Rion KC-01E, ambient dust, 5 cm/s); during loading = TSI 8130, NaCl modal 0.075 um, neutralised, 5 cm/s, photometric (stated to coincide with the 0.3-0.5 um count value).
- Retention = ln P_end / ln P_initial (exactly the brief's metric). Deterioration rate = least-squares slope of ln(retention) vs smoke mass per m2 of FIBRE surface, forced through (0,1) (Table 2 values reproduce ln-based slopes: ln 0.08/0.27 = -9.35).
- Table 2 (col. 35): initial E 99.3/99.4/99.4/99.3% (Ex 2-1/2-2/2-3/Comp 2-1); discharged Comp 2-2 28.2%. Initial QF 1.77/1.76/1.89/1.84 /mmAq (180/180/193/188 kPa^-1 at 5 cm/s); Comp 2-2 0.13 (13 kPa^-1). Smoke collected 13.8/27.4/14.2/12.6 mg per sheet = 7.0/14.0/7.2/6.4 g/m2 of media (mg / 19.63 cm2). E at cycle end 70.2/61.3/55.7/33%. Retention 0.24/0.19/0.16/0.08. Deterioration rate -4.78/-2.92/-5.94/-9.17 per (g/m2 of fibre surface).
- Per m2 of MEDIA (ln(retention)/media load): Comp 2-1 plain corona PP k = 0.39 per g/m2 -> half of -lnP gone at 1.8 g/m2 of smoke; 92% gone and E 99.3% -> 33% (vs 28.2% discharged) at 6.4 g/m2. Lost-electrostatic at 6.4 g/m2 = (ln 0.67 - ln 0.007)/(ln 0.718 - ln 0.007) = 0.98.
  - Ex 2-1: k = 0.20 per g/m2 (half of -lnP gone at 3.4 g/m2); Ex 2-2 (vapour-deposited): k = 0.12 (5.8 g/m2); Ex 2-3: k = 0.25 (2.7 g/m2).
- Text (col. 22): the deterioration rate "of the polypropylene fibers obtained by a general melt-blowing method is approximately -9/(g/m2)" (per fibre area). For 30 g/m2 at 5.6 um that is ~0.39 per g/m2 of media. The patent normalises by fibre surface area, i.e. assumes the per-fibre-area rate is the material constant, so a web with more fibre area per m2 would tolerate proportionally more smoke per m2 of media (not tested across fibre sizes here).
- Table 1 (first invention; PP meltblown 30 g/m2, 3 um mean fibre, 0.25 mm, 0.75 g/m2 perfluoroalkane deposit, corona or hydro-charged): "Tobacco smoke durability life" = smoke collected when NaCl efficiency (5 cm/s) falls to 50%: 30.0-37.7 mg/sheet = 15.3-19.2 g/m2. "PAO durability life" (Emery 3004 PAO, modal 0.184 um, 100 mg/m3, 5 cm/s, neutralised; mass collected at E = 50%): 23.7-29.8 mg/sheet = 12.1-15.2 g/m2. Charged E (0.3-0.5 um count, 10 cm/s) 97.0-99.94%; uncharged (charge removed by impregnating with 0.5% MegaFac F410 solution and drying) 30.4-32.4%. With P0 = 2.8% and P_uncharged 68%, E = 50% means ~90% of the electrostatic -lnP lost. No untreated-PP control in Table 1.

## US10213716 (Toyobo, Kitagawa & Enjoji, priority JP 2014-04-04, granted 2019; WO2015/152207) - same two durability tests, WITH plain-PP controls
Link: https://patents.google.com/patent/US10213716B2/en ; test methods col. 15-16 (USPTO image p.10), Tables 1-1 to 3-12 (pp. 12-26), all read from the page images.
- Carrier for all examples: PP meltblown 30 g/m2, 3 um average fibre diameter, 0.25 mm. Charging by corona or "liquid contact" (hydrocharging). Some carriers contain Irganox 1010 or Chimassorb 944 at 0.01-20 wt%.
- PAO durability life: TSI 8130, PAO (Emery 3004) neutralised, number modal 0.184 um, 100 mg/m3, 6 L/min through a 50 mm-diameter area (19.63 cm2; 5 cm/s), photometric; endpoint = efficiency 50%; PAO collected on the 50 mm area weighed. Tobacco smoke durability life: Mevius / JEM 1467 cycles as in US10940415; endpoint E = 50% (NaCl, TSI 8130, 5 cm/s). mg/sheet / 19.63 cm2 -> g/m2 (x 0.509).
- Efficiency test for "after charging" and "no charge" columns: ambient dust, 0.3-0.5 um count, 10 cm/s. Charge removed for the "no charge" value by impregnating with 0.5% MegaFac F410 and drying.
- Plain PP controls (no fluorine treatment):
  - Comp 1-1 (corona; Table 1-3, col. 21): E charged 97.4% / uncharged 30.4%; tobacco smoke life 8.1 mg = 4.1 g/m2; PAO life 9.8 mg = 5.0 g/m2.
  - Comp 1-2 / 1-3 (corona, PTFE powder m.p. 330 C did not deposit): smoke 8.0 / 7.8 mg (4.1 / 4.0 g/m2); PAO 7.1 / 8.2 mg (3.6 / 4.2 g/m2).
  - Comp 3-15 to 3-19 (hydrocharged, Irganox 0-20%; Table 3-11, cols. 45-48): E 96.4-99.73% / 30.3-32.8%; smoke life 7.7-10.6 mg (3.9-5.4 g/m2); PAO life 9.5-12.1 mg (4.8-6.2 g/m2).
- Perfluoroalkane-deposited (0.75 g/m2 n-C10F22...n-C20F42 or Cefral Lube V), corona: smoke life 29.7-34.7 mg (15.1-17.7 g/m2), PAO 23.5-27.4 mg (12.0-13.9 g/m2) (Tables 1-1, 1-2). Hydrocharged: smoke 32.3-44.2 mg (16.4-22.5 g/m2), PAO 25.2-36.5 mg (12.8-18.6 g/m2), higher with 5-15% Irganox or Chimassorb (Tables 2-2 to 3-10).
- An acrylate oil repellent (Unidyne TG-5502/5503) suppressed charging (E 32.6-62.1%), so life 2.3-3.7 mg.
- Endpoint meaning: with P0 ~2.6% and P_uncharged ~70% (10 cm/s count values), E = 50% corresponds to ~90% of the electrostatic -lnP lost. So: plain PP electret (corona or hydro), 30 g/m2, 3 um: ~90% of the charge benefit gone after ~4-5 g/m2 of PAO or tobacco smoke collected; fluorine-surface-treated: after ~12-22 g/m2 (3-4x more).

---

## EP1874430B1 / US7717986 (3M, Lotgerink-Bruinenberg, priority 2005) - cabin filter, SOLID dust (SAE coarse A4) loading
Link: https://data.epo.org/publication-server/rest/v1.2/patents/EP1874430NWB1/document.html (paras. 0054-0060; text read in full).
- Media: co-pleated (i) corona-charged split-fibre (fibrillated film) nonwoven < 70 g/m2 + scrim, upstream; (ii) electret meltblown, EFD > 10 um, < 60 g/m2, with a charge additive (fluorochemical / triazine / HALS etc.); (iii) support layer. Filter face 250 x 200 mm, 29 pleats x 30 mm at 8.5 mm pitch -> media area 29 x 2 x 0.030 x 0.200 = 0.35 m2 (my calc).
- Test: E DIN 71460-1, 23 C, 50% RH, 225 m3/h (face 1.25 m/s; media ~18 cm/s), ISO 12103-1 A4 coarse dust at 160 mg/m3 from a TSI 3400 fluidised bed, efficiency at 0.4 um geometric by TSI APS 3321 on the dust's own fine fraction (charge state of the test dust not stated - fluidised-bed dust is usually charged, so this may overstate the neutral-particle efficiency).
- Ex 1 (SF/M3/SL, loose co-pleated): 0.4 um efficiency 98% initial, 97% at +50 Pa, 98% at +100 Pa; 51 g of dust held at +100 Pa = 51 / 0.35 = 146 g/m2 of media. Ex 2: 99% initial, 52 g. Ex A (layers laminated with spray adhesive): 98% initial, only 28 g.
- So: ~150 g/m2 of coarse mineral dust (mostly captured on the coarse split-fibre layer) did not reduce 0.4 um efficiency. The fine meltblown electret layer's own deposit is unknown and probably small.

---

## US6419871 (Ogale, 2002; plasma-fluorinated meltblown) - SAE fine dust, low weight
Link: https://patents.google.com/patent/US6419871B1/en ; USPTO image p.3 (cols. 3-4).
- Ex 1: 40 g/m2 PP meltblown, hexafluoropropylene plasma (0.25 g/m2 deposit), water-rinsed (charging step not stated for Ex 1; claims include charging). Pleated 10 x 10 cm x 0.5 cm, 5 pleats/inch (~0.02 m2 media by my estimate). Neutralised KCl, laser counter, "0.3-5 um", 30 CFM. 87% -> loaded with 2 g SAE fine dust (~100 g/m2 of media), then RINSED with water -> 87.8%. The rinse confounds it; only says SAE fine dust + water did not discharge this media.
- Ex 2 (water-wash only, no dust; 50 g/m2, corona 15 kV, NaCl at 10 cm/s): plasma 0.05 g/m2 P 10.25% -> 1.2% after wash (sic); 0.025 g/m2 22.6 -> 40.6%; untreated 40.0 -> 41.0%.

---

## US4886527 (Carl Freudenberg, Foettinger et al., priority DE 1987, granted 1989) - SOLID carbon black loading, average efficiency only
Link: https://patents.google.com/patent/US4886527A/en ; USPTO image pp. 4-5 (cols. 4-5), read from the page images.
- Pack: (a) PP staple 1.7 dtex (22 um) 80 g/m2, 2.8 mm; (b) polycarbonate 8 um, 16 g/m2 (ba) or 8 g/m2 (bb); (c) as (a). Layers electret (alternating polarity) or uncharged as stated.
- Test: carbon black aerosol x50 = 0.02 um, 67 mg/m3, 25 cm/s, ~1 g/m2/min, loaded to dP 600 Pa; A = total (gravimetric) degree of filtration over the whole loading; SSV = dust held at 600 Pa.
- Results (col. 5 table): outer layers uncharged + electret middle (ba): A 96.4%, SSV 34.3 g/m2; all three electret: A 98%, SSV 70.6 g/m2; all electret with the lighter middle (bb): A 96.1%, SSV 81.1 g/m2 (initial dP 50, 50, 35 Pa).
- Reading: the all-electret pack held 98% average mass efficiency across 71 g/m2 of fine carbon black. Average over the run only, with a cake forming; it shows no catastrophic loss with solid soot, not the charge-decay curve.

---

## Mitsui Petrochemical cigarette-smoke / ageing patents (no deposited mass - qualitative only)
- US5304227 (Mitsui, 1994), https://patents.google.com/patent/US5304227A/en, Table 1 (col. 8, verified on USPTO image p.6): split-film electret fibres, needle-punched 100 g/m2, 2 mm. Smoke test: 1 m3 box, aspirator with a 150 x 150 mm sample at 0.5 m/s face velocity; efficiency = NaCl 0.3 um COUNT (Rion KC-01B5) at 50 cm/s; "retention" = E1/E0 (efficiency ratio, not ln). After 10 / 20 cigarettes: PMP film fibre (Ex 1) 52% / 40%; FEP 50 / 43; PP + 0.1-1% silicone oils 43-57 / 30-45; homopolymer PP (Comp 1*) 27 / 16; PET 23 / 12; PMMA 20 / 11; PC 24 / 13; PP/MAH-PP/PC 30 / 19. Retention tracks water contact angle (95-103 deg vs 66-89 deg). E0 and smoke mass on the filter not given, so no g/m2 or ln-ratio.
- US4592815 (1986), https://patents.google.com/patent/US4592815A/en, Table 1 (col. 5): SHELF ageing, no loading. 0.3 um tobacco-smoke particle COUNT efficiency at 10 cm/s, early vs after 6 months storage: Ex 1 92 -> 90.5%; Ex 2 80 -> 77.5%; Ex 3 98 -> 96.7%; Control 2 23 -> 9%; Control 3 79.3 -> 71.2%. Storage conditions not stated.
- US4626263 (Mitsui, 1986), Table 1: film surface-charge retention (not filter efficiency) after hot/humid exposure; plain PP film sigma ratio 0.71 at 40 C/90% RH, 0.30 at 60 C/90% RH, 0.07 at 86 C/18% RH; three-component blends 0.94-1.0 / 0.56-0.71 / 0.23-0.37. Exposure durations on an earlier page (not read). Table 2 is instantaneous smoke efficiency only.

---

## Cross-patent synthesis (my calculations; inputs as cited above)

### 1. Normalising by fibre surface area collapses the oily / smoke data for plain PP
Fibre surface area per m2 of media S = 4 BW / (rho d) for round fibres (rho 0.90-0.91 PP, 0.83 PMP); for the 10 x 40 um split-film fibres S = (BW / rho) x 2.5e5 per m (perimeter/area of a 10 x 40 um rectangle; the patent gives the cross-section only as "about 10 by 40 um").
- US4874399 PP meltblown, 1 layer (51 g/m2, 7 um, S = 32 m2/m2): Q halved at 2.4-2.7 g/m2 DOP collected = 0.075-0.084 g per m2 of fibre surface; 4 layers (S = 130): 0.10.
- US4874399 PP split-film (129-644 g/m2, S = 36-179): 0.059-0.078 g per m2 of fibre surface, across 1 to 6 layers.
- US10940415 plain corona PP meltblown (30 g/m2, 5.6 um, S = 23.4), tobacco smoke: -lnP halved at 0.076 g per m2 of fibre surface (= ln2 / 9.17).
- US10213716 plain PP meltblown (30 g/m2, 3 um, S = 44): E = 50% end-point (~85-90% of the electrostatic -lnP gone) at 0.094 (smoke) and 0.114 (PAO) g per m2 of fibre surface - 2-2.7x faster than the three series above if the decay were exponential; the end-point efficiency is a 5 cm/s NaCl number whose initial value is not printed, so this comparison is loose.
- So for plain PP electrets and liquid / semi-liquid aerosol (DOP, PAO, tobacco smoke), half of the electrostatic -lnP goes per ~0.06-0.10 g of deposit per m2 of fibre surface, and the per-media-area tolerance scales with BW / d. Example conversions at 0.06-0.10 g/m2 of fibre surface: 30 g/m2 at 3 um (S 44) -> 2.6-4.4 g/m2 of media; 50 g/m2 at 7 um (S 32) -> 1.9-3.2; 100 g/m2 at 20 um (S 22) -> 1.3-2.2 (the last is an extrapolation, not measured).
- Surface chemistry multiplies that number: PMP blends 0.17 (1% PMP) to 0.22-0.27 (10-100%) (x2-3.5, meltblown; only x1.3-1.7 for split film); vapour-deposited perfluoroalkane 0.24 (x3); solution-deposited 0.12-0.15 (x1.5-2).

### 2. Additive / process, DOP on corona PP meltblown at ~7 cm/s (retained -lnP)
- No additive: 0.24-0.29 after ~2-4 g/m2 captured (US5411576 C4/C7); half Q at 2.4-2.7 g/m2 (US4874399); H&V no-additive alpha 24 -> 8 after ~7 g/m2 incident (US6780226).
- Melt fluorochemical (oxazolidinone, 1%, annealed): 0.78-0.91 at 50 mg and 0.78-0.86 at 100 mg exposure (~6-7.5 g/m2 captured) for the good additives (US5411576 Ex 1-3, 5); two other fluorochemicals only 0.42-0.45. Annealing essential (unannealed 0.18).
- Fluorochemical + quench + anneal: penetration does not start rising until (Min@Chl) an average 21-35 g/m2 incident, best ~49 g/m2, on a 2-layer ~140 g/m2 stack (US6068799 Table 9B); a 2 x 100 g/m2 stack of the same kind of media showed no degradation over 33 g/m2 incident (US6627563 FIG. 4).
- Surface fluorination (US6398847): corona + C5F12 plasma 0.97 at 21 g/m2 captured; hydro-charged 0.72-0.77 at 9.7 g/m2 and 0.56-0.57 at 24 g/m2.
- H&V vapour-deposited fluoroacrylate (US6802315): 0.89 at 11.8 g/m2 vs 0.25 for the same web charged without the coating.
- Fatty amide alone (Acrawax C, H&V): small gain (alpha 31 -> 14 vs 24 -> 8).

### 3. Charging method
- Hydrocharging gives 2-3x the initial QF of corona at equal chemistry (US6398847 Table II: 193-207 vs 59-66 kPa^-1 at 6.9 cm/s) but does not reduce the fractional loss per gram: US6398847 hydro-charged lost 26-49% of the electrostatic -lnP at 5-24 g/m2 while corona + C5F12 lost 5% at 21 g/m2; US6627563 hydro layer (QF 1.6 /mmH2O) kept 0.53 of -lnP at 10 g/m2. Toyobo: liquid-contact charging gave 27-31% longer smoke / PAO life to E = 50% than corona with the same fluorine treatment, but from a higher start (99.9 vs 97.2-98.5%), so per gram the fractional -lnP loss is not smaller (US10213716 Ex 1-6 vs 1-7, 1-13 vs 1-14).

### 4. Solid vs liquid
- No patent found shows a solid aerosol degrading electret efficiency with mass stated. H&V US6780226 (col. 8): during NaCl loading "the maximum penetration is achieved in the first reading and ... penetration of NaCl particles decreases over time" (~7 g/m2 incident; Figs 2-3, not tabulated). 3M EP1874430: ~146 g/m2 of SAE coarse dust with 0.4 um efficiency unchanged (charged dust, multilayer). US6419871: ~100 g/m2 SAE fine dust then a water rinse, efficiency unchanged.
- Freudenberg US4886527: all-electret 3-layer pack averaged 98% (gravimetric) on 0.02 um carbon black while taking up 71 g/m2, vs 96.4% with uncharged outer layers.
- Liquid / tar aerosols all degrade the charge, as quantified above.

### 5. Real-world / ambient
- Only US5496507 Table 11 (ambient air, 290 h at 250 m3/h, PMP hydro-charged 40 g/m2 pleated): retained -lnP 0.52 at 0.3 um and 0.68 at 1 um, dP +43%. Mass not reported; every 10 ug/m3 of captured particulate corresponds to 2.5 g/m2 of media over the 290 h (1.15 g/m2 at 133 h).

### 6. Heat ageing without load
- PP meltblown at 70 C: Q 1.23 -> 0.64 after 72 h (US4874399 Table I); fluorochemical webs 60-70 C 47-73 h then loaded behave like unaged (US5411576 Table IV); Toyobo 80 C 30 min (ln-ratio retention): plain PP 92-94%; with perfluoroalkanes melting at 36-76 C only 20-49%; melting >= 103 C 83-96% (US10213716 Tables 1-1 to 1-3).

---

## Read but no usable loading data (coverage record)
- 3M: US5908598, US6119691 (reprints US5496507 examples), US6375886, US6406657, US6454986, US6743464, US7244291 / US7244292 (Q9 = QF after 9 h at 100 C, unloaded), US7765698, US8613795; US6214094 / US6238466 / US6237595 / US6319452 duplicate US6068799 / US6213122.
- H&V: US10814261 (tribo acrylic/PP needled; dust-holding vs dP only), US7883562 (waved media; NaCl-loading resistance and DHC only).
- Others: US7655076 (Darwin, active 8 kV fluted collector + corona field charger, not an electret: 0.3 um efficiency 98.7% -> 36% after ASHRAE dust equal to 150 g per 24 x 24 in without prefilter, 98.6 -> 97.9% with one); US11426690 (Daikin PTFE membrane); US2016/0250649 (YUPO electret film channels); US9701178 (K&N cabin); US8057583 (Johns Manville glass, E3 only); US6815383 (Kimberly-Clark, composite average efficiency only); CN111909455A (claims oil-particle efficiency >= 95%, no loading table).

## Gaps
- Chinese CN and Japanese JP national patents not mined: Google Patents returned 503 for the last ~70 min of the session (WebFetch too), and no other full-text CN/JP search was reachable (Espacenet behind Cloudflare, Patentscope JS-only, patentguru 468, freepatentsonline 403).
- No patent states the particulate mass gained in ambient or field use. No patent loads at controlled RH as a variable.
- Leads for other pools, not read: PMC4730493 (office-room portable air cleaners; an electret medium reportedly fell to 60% efficiency after 25 x 10^4 m3 of air per m2 of media); Ji et al. 2003 J Aerosol Sci, electret cabin filter loading; a Xi'an Univ. Arch. Tech. journal article (2022) reportedly on electret media after 5-7 months of real use (URL 404'd).
