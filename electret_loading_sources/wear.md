# Electret meltblown degradation when worn (breath, wear, valves)

Compiled 23 Nov 2026 for the Amodo x O3P plan ("Degradation under breath", doc
`1uXqzeZOI1zxR6VZhToUn_K-fpIWlSxnvi4U01LlaN3M`). Every entry was read in full text unless
marked. Penetration figures are whole-respirator NaCl penetration on a TSI 8130/8130A at
85 L/min (NIOSH 42 CFR 84 style, photometric, CMD ~0.075 um) unless stated.

## 1. Real wear, filter penetration measured afterwards

### Wang et al. 2024, JAMA Netw Open 7(10):e2441663, doi:10.1001/jamanetworkopen.2024.41663 (PMC11581496; eAppendix read)
- 6 US emergency departments, Apr 2021-Jul 2022. 365 worn N95s + 30 unworn. Models: 3M 1860
  (148), 3M 1870 (119), Halyard Fluidshield (98). None has an exhalation valve.
- Each worn for 1-5 clinical shifts of 8-12 h (shift length from the parent study,
  doi:10.1001/jamanetworkopen.2023.53631), <=5 don/doffs per shift asked. Worn "until fit
  failure occurred, the N95 FFR became soiled or deformed, or five clinical shifts had
  elapsed", so every tested respirator had failed fit or been retired. Not randomised.
- Test: VHP decontamination first, then sealed with beeswax to a plate, TSI 8130A, 85 L/min.
  If penetration was above baseline, sealant was added and the test repeated up to 3 times,
  lowest value kept.
- All models, median FE (IQR), mean (SD), share <95%:
  - 0 shifts (n=30): 99.6 (99.3-99.7), 99.5 (0.3), 0%
  - 1 (170): 99.5 (99.0-99.9), 99.2 (1.3), 1.8%
  - 2 (89): 98.8 (97.4-99.2), 97.8 (2.4), 10.1%
  - 3 (52): 97.9 (94.0-98.8), 96.0 (4.5), 28.8%
  - 4 (29): 96.9 (93.5-98.0), 95.2 (4.3), 34.5%
  - 5 (25): 96.3 (92.7-97.9), 94.2 (6.6), 40.0%
- By model, median FE at 0 -> 5 shifts: 3M 1860 99.7 -> 97.1 (n=15 at 5); 3M 1870 100.0 -> 96.3
  (n=2 at 5; 96.5 at 3 shifts, n=8); Halyard 99.3 -> 92.4 (n=8 at 5; 93.9 at 3, n=14).
  Adjusted OR for FE <95%: 5.68 (2 shifts), 35.4 (3 shifts) vs 1 shift; Halyard 9.84.
- Median penetration (mine): 0.4 -> 0.5 -> 1.2 -> 2.1 -> 3.1 -> 3.7%, about +0.7 points per
  shift; mean 0.5 -> 5.8%, about +1.1 per shift.
- Cannot separate charge loss from damage to the shell or media (creases, holes). Tested dry
  after shipping and VHP, so the loss is not just dampness.

### Du et al. 2020, Medicine 99(50):e23709, doi:10.1097/MD.0000000000023709 (PMC7738039)
- Beijing Chest Hospital. One N95 model (Sinovo, Beijing; valve not stated). Volunteers wore
  it 4 h + 4 h per day with a 2 h break; stored in a vented envelope otherwise. Tested within
  1 h of removal (may still have been damp). "All the experiments had been performed in 50
  times by different volunteers" - read as 50 respirators per time point.
- Fig. 2A, read off the plot (+-0.3): FE 97.4 (new), 97.0 (0.5 d), 96.8 (1 d), 95.3 (2 d),
  94.7 (3 d), 93.5 (4 d), 92.0 (5 d), 90.9 (6 d), 88.9 (7 d), 80.5 (14 d = 112 h).
  Penetration 2.6 -> 11.1% in 7 days, about +1.2 points per 8 h day; 19.5% at 14 days.
- DISCREPANCY: abstract and text say "3 days ... 97.0%"; their own figure shows 97.0% at
  0.5 day and ~94.7% at 3 days. Text gives 80.4% at 14 days, consistent with the figure.
- Breathing resistance fell 13.8 -> 11.5 mmH2O within the first half day and stayed there
  (11.6 at 14 d). Charge loss does not lower resistance, so some structural change or leak
  path is likely part of the result (my inference).

### Weaker or indirect
- Chen et al. 2022, Ecotoxicol Environ Saf 242:113908 (PMC9301359): fitted filtration
  efficiency on the face (includes fit), one mask per condition on one person, 40 h of wear.
  ~50 nm: 3M 9205+ 99.5 -> 99.0, Honeywell DC300 96.7 -> 83.7 (no nose foam; authors blame
  fit), KF94 95.7 -> 93.3, KN95 86.9 -> 97.0 (fit improved). >150 nm changes smaller.
- Lee, Kim, Joo, Cho & Park (GIST), Aerosol Air Qual Res, doi:10.4209/aaqr.210370: KF80
  electret mask worn 2 h/day for 5 days, sprayed with water and dried 12 h between uses: -4%;
  uncertified mask -18 to -30%. Abstract, methods and the Fig. 7 paragraph read; sample
  count not checked.
- Pierlot, Alexander & Schutz 2022, IJERPH 19:5032 (PMC9100139): NOT meltblown. Needled
  wool/PP triboelectric media, 10 volunteers, 1-8 h; 0.3 um penetration ~2% -> >10% for some
  samples within 4 h, no further rise to 8 h.
- Duncan et al. 2020, J Occup Environ Hyg 17:546 (abstract only): one surgical-style N95, up
  to 19 uses over 5 days; total inward leakage, protection factor stayed >=10. Fit, not media.
- Varanges et al. 2022 (PMC8943131, in `../testing/RESULTS.md`): surgical-mask meltblown,
  8 h-1 week in artificial sweat or saliva, 74.4 -> 70.6% at 100 nm for sweat.

## 2. Simulated breath

### Zhu et al. 2022, J Hosp Infect 127:91, doi:10.1016/j.jhin.2022.06.016 (PMC9250162) - the only valve comparison
- Breathing simulator, sinusoidal flow, exhaled air 37 C / 100% RH. Respirator taped to a
  headform inside a 2.2 m chamber with NaCl aerosol (TSI 8026 generator, 0-200 nm) present
  throughout; chamber concentration not given. Count penetration by TSI 3910 NanoScan.
- Three N95 models: "medical", "particulate without exhalation valve", "particulate with
  exhalation valve". Different products, so the media differ as well as the valve. ONE
  respirator per condition (3 models x 3 flows x 2 disinfection methods). 8 h cycles with
  70 C / 30 min dry heat or UV in between, until penetration reached 5%.
- First 8 h, slope in penetration points per hour at 15 / 50 / 85 L/min mean inhalation flow
  (Fig. 3): medical 0.060 / 0.079 / 0.091; no valve 0.066 / 0.084 / 0.097; valve 0.049 /
  0.057 / 0.073. Valve is 25-32% lower.
- Hours to 5% (Fig. 5, dry heat / UV): medical 100/96, 58/55, 30/32; no valve 106/101, 63/60,
  37/34; valve 134/140, 80/87, 52/55. Valve lasts 1.3-1.5x as long.
- Curves are smooth quadratics across cycles with no recovery after the 70 C drying step, so
  the loss is not reversible wetting. NaCl loading and humid breath are not separated.

### Clean humid breath, no aerosol loading
- Guan et al. 2022, Materials 15:7918 (PMC9696921): headform, saturated 37 C air, 20
  breaths/min x 2 L, lab at 20 C / 65% RH, then TSI 8130 at 85 L/min, n=3. Respirator ("PM"):
  97.53 (0 h), 97.38 (2 h), 97.48 (4 h), 96.98 (6 h), 96.70 (8 h). Surgical mask: 67.57,
  65.40, 66.60, 67.87, 60.83. Not stated whether masks were dried before testing.
- Ramirez & O'Shaughnessy 2016, J Occup Environ Hyg, doi:10.1080/15459624.2016.1143950 (CDC
  Stacks 202519, text extracted; table digits unreadable): 3M 8510 and Moldex 2200, cyclic
  55 L/min, exhaled 36.7 C / 95% RH, inhaled air up to cool-saturated, 120 min, 5 FFRs per
  condition, 4 conditions. NaCl SMPS penetration before vs after: no significant change
  (FFR 1 p = 0.34); MPPS unchanged. Breathing resistance rose significantly.
- Roberge et al. 2010, Ann Occup Hyg 54:671, doi:10.1093/annhyg/meq042 (CDC Stacks 188175,
  text extracted): 9 models x 5 (3 N95, 3 surgical N95, 3 valved N95: 3M 8211, 8511, Moldex
  2300), breathing simulator 40 L/min, exhaled 33.9 C saturated, 4 h, lab 20.4 C / 52% RH.
  Water retained: N95 0.19 g, surgical N95 0.35 g, valved 0.23 g (P = 0.10 between classes;
  per 100 cm2: 0.09, 0.16, 0.13, n.s.). Valves did not reduce retained moisture. Filtration
  NOT measured.
- Stoll & Antonyuk 2025 and Mahdavi 2015: see `mechanism.md` section 8. Stoll's worn-mask
  cycles are 75 min wear + 30 min drying at 15 L/min, 30 C / 98% RH; sealed masks lose ~5
  points over the run and recover partly in each drying phase.

## 3. Exhaled air kept off the filter entirely (elastomerics)
- Baffoe-Bonnie et al. 2022, Infect Control Hosp Epidemiol, doi:10.1017/ice.2021.104
  (PMC8027558): 3 pairs of expired P100 cartridges after 5-6 months of hospital use; mostly
  >95% across sizes, one pair slightly lower, not significant.
- J Occup Environ Hyg 2022, doi:10.1080/15459624.2022.2041649 (abstract only): MSA P100
  cartridges >=99.97% and little change in resistance after 12 months of repeated hospital
  use. P100 media, not N95 meltblown.

## 4. What this adds up to (my analysis)
- Unvalved N95, per 8-12 h of wear, the 85 L/min NaCl penetration rises by roughly 0.6-1.2
  percentage points: Wang median +0.7 and mean +1.1 per shift; Du +1.2 per day; Zhu +0.6-0.8
  per 8 h (85 L/min, with NaCl); Guan +0.8 in 8 h (clean humid air). First day: little change
  in all of them. Model matters as much as time (Wang: 3M 1860 vs Halyard).
- Valve: one n=1 simulator comparison across different products (1.3-1.5x life), against
  Roberge's finding that valved models hold as much water. No real-wear data on valved FFRs.
- Not covered anywhere: wear beyond 112 h; cause (breath vs handling vs skin oils vs
  alcohol vapour vs ambient aerosol); bare media or supplier grades (all data are finished
  branded respirators); size-resolved penetration at 0.3-1 um+ after wear (all real-wear data
  use the ~0.075 um CMD NaCl test, where electret loss shows most).
- Not obtained: Ramirez 2016 table values (font-encoded), Duncan 2020 and the 12-month
  elastomeric paper (Taylor & Francis paywall).
