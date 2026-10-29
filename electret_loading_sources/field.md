# Pool: field / ambient-air loading of electret filters

Conventions used below
- P = penetration (count-based unless stated). "Retained −lnP" = ln P_loaded / ln P_initial. "Electrostatic part lost" = (ln P_loaded − ln P_initial)/(ln P_discharged − ln P_initial), only where a discharged (IPA) reference exists.
- "Fed" mass = upstream concentration × flow × time ÷ media area (what reached the filter). "Collected" = what stayed on it. Field papers almost never weigh filters; where I estimate, the arithmetic is shown.
- Curve readings: read off rendered figures against gridlines; precision about ±2 percentage points of efficiency unless stated.

---

## 1. Lehtimäki M. (VTT, Tampere), 1996. "Development of test methods for electret filters". Nordtest Technical Report NT TR 320, Nordtest project 1164-94. 57 pp, scanned.
Link: http://nordtest.info/images/documents/nt-technical-reports/NT%20TR%20320_Development%20of%20test%20methods%20for%20electret%20filters_Nordtest%20Technical%20Report.pdf (landing page https://www.nordtest.info/wp/1996/03/06/development-of-test-methods-for-electret-filters-nt-tr-320). Read in full (rendered pages). Report page numbers below are the printed ones.

Media (§2.5, Table 2.1, p.5–6): two commercial EU7 (≈ F7 / MERV 13) electret bag filters. Polymer and charging method not stated.
- "A": electret layer of "relatively coarse fibers (approximately 15 ... 20 µm in diameter)". 600×600 unit: 4 bags, 2.8 m² media, nominal 0.94 m³/s → 0.33 m/s through media. Half-size (300×600): 2 bags, 1.4 m².
- "B": electret layer of "flat fibers (approximately 5 x 15 µm)". 600×600: 8 bags, 5.6 m², 1.18 m³/s → 0.21 m/s. Half-size: 4 bags, 2.8 m². Sample-to-sample variation large (Fig 2.5: 42–62 % at 0.12–0.2 µm).
- Basis weight, thickness: not given.

Efficiency method (§2.1): PMS LAS-X optical counter, 0.12–5 µm (PSL-equivalent), count-based, polydisperse KCl, dried and Kr-85 neutralised. Material samples ø150/200 mm at the nominal media velocity (33 cm/s A, 21 cm/s B).

Loading definition (§2.2, eq. 4, p.4): m/A = v_f × c_m × t = mass FED per m² of media, c_m measured gravimetrically upstream. Report stresses: "Δm_i or Δm/A does not correspond to the amount of particles collected by the filter."

### 1a. Field test, Tampere suburban, 4 months from December (§3.2, p.8–11, Figs 3.6–3.7)
- Half-size A and B units, each behind an EU3 pre-filter (added because of snow), 0.5 m³/s each → media velocity 0.36 m/s (A, 1.4 m²) and 0.18 m/s (B, 2.8 m²). Outdoor air, suburban Tampere. Efficiency measured on the whole unit (pre-filter + electret) before and after.
- p.10, verbatim: "The mean aerosol mass concentration during the field test was approximately 10 µg/m³. Thus, the amount of dust to which each filter system was exposed is approximately 50 g. This corresponds approximately to the values of 36 g/m² (filter "A") and 18 g/m² (filter "B"). It must, however, be emphasized that the amount of dust collected by the electret filters is lower ... Also, the EU3 pre-filter captures some of the dust."
- Arithmetic check: 0.5 m³/s × ~120 d × 86 400 s × 10 µg/m³ = 52 g; 52/1.4 = 37 g/m²; 52/2.8 = 19 g/m². OK. These are FED values upstream of the EU3 pre-filter.
- Ambient composition: not analysed for the field period. The report's own cascade-impactor survey (§5.1, Figs 5.2–5.6) shows Tampere-area mass distributions swinging from ~6 % below ~1.4 µm (city street in spring, road sand) to ~47 % (suburban winter, parking area). So the fine fraction of the 36 g/m² is somewhere around 15–50 %.

Readings (Fig 3.6, A; Fig 3.7, B), efficiency %:

| size | A clean | A 4 months | B clean | B 4 months |
|---|---|---|---|---|
| 0.12–0.2 µm | 79 | 15.5 (14–18) | 62.5 | 26 (23–28) |
| 0.3 µm | 84 | 16.5 | 70 | 31 |
| 0.4 µm | 88 | 21 | 77 | 43 |
| 0.5 µm | 92 | 29 | 82.5 | 52 |
| 0.7 µm | 95 | 39 | 88 | 65 |
| 1.0 µm | 97 | 51 | 94 | 78 |
| 2.0 µm | 99 | 92 | 98.5 | ~97 |

IPA-discharged reference (§4.1, Figs 4.1–4.2, p.13–14; material samples, immersion in technical-grade IPA, 24 h dry; flow resistance unchanged):
- A: before 83 % (0.12–0.2 µm), 90.5 % (0.4 µm), 99 % (1 µm) → after IPA ~13 %, ~15 % (scatter 11–20), ~32 %.
- B: before 60 %, 73 %, 96 % → after IPA ~27 %, ~40 %, ~84 %.

Derived (my arithmetic):
- A at 0.4 µm: P 0.12 → 0.79. Retained −lnP = ln0.79/ln0.12 = 0.11. With P_IPA ≈ 0.85: electrostatic part lost = (ln0.79 − ln0.12)/(ln0.85 − ln0.12) = 1.88/1.96 ≈ 0.96.
- A at 0.12–0.2 µm: P 0.21 → 0.845, P_IPA ≈ 0.87 → lost ≈ 0.98.
- B at 0.4 µm: P 0.23 → 0.57, P_IPA ≈ 0.60 → lost ≈ 0.95; retained −lnP = 0.38.
- B at 0.12–0.2 µm: P 0.375 → 0.74, P_IPA ≈ 0.73 → lost ≈ 1.0.
- So after 4 Finnish winter months (≈36 / 18 g/m² fed, behind an EU3), both filters sat at their IPA-discharged efficiency within reading error. The 1 µm efficiency of A fell 97 → 51 %.
- Collected-mass estimate (mine, rough): fine (<~1 µm) share of fed mass 15–50 % → 5–18 g/m² fine fed to A; mean submicron efficiency over the period maybe 0.3–0.6 → ~2–10 g/m² of fine ambient PM collected by A at the end. Coarse mostly taken by the EU3. Uncertainty at least ×2.
- Δp for the field units: not reported.

### 1b. 24-day ambient exposure of material samples (§3.2, p.12, Figs 3.8–3.9)
- Material samples "exposed to atmospheric particles for 24 days"; loading stated in captions: A 4.4 g/m² fed, B 2.8 g/m² fed. Whether a pre-filter was used is not stated.
- Back-calculated ambient concentration: 4.4 g/m² ÷ (0.33 m/s × 24 d × 86 400 s) = 6.4 µg/m³; B 2.8 ÷ (0.21 × 2.07e6) = 6.4 µg/m³. Consistent.

| size | A clean | A 24 d (4.4 g/m² fed) | B clean | B 24 d (2.8 g/m² fed) |
|---|---|---|---|---|
| 0.12–0.2 µm | 80 | 50 (48–52) | 45 | 30 (26–33) |
| 0.3 µm | 84 | 53.5 | 49 | 41.5 |
| 0.4 µm | 88.5 | 55 | 58 | 43 |
| 0.5 µm | 92 | 62 | 68 | 59 |
| 1.0 µm | 97 | 78 | 84 | 83 |

Derived: A at 0.4 µm P 0.115 → 0.45; retained −lnP 0.37; electrostatic part lost (P_IPA 0.85) ≈ 0.68. A at 0.12–0.2 µm lost ≈ 0.62. B (P_IPA uncertain because B samples vary): lost ≈ 0.85 at both sizes, but treat as ±0.2.
- Collected-mass estimate (mine): if fine (<1 µm) ≈ 30–50 % of fed mass and A's mean submicron efficiency over the 24 d ≈ 0.65, fine collected ≈ 0.9–1.4 g/m²; total collected ≈ 3–4 g/m². So about two-thirds of A's electrostatic capture at 0.4 µm went with ~1 g/m² of fine ambient PM (plus ~2–3 g/m² coarse), at 6.4 µg/m³ and 33 cm/s.

### 1c. Same media, standard ASHRAE 52-76 dust (§3.1, Figs 3.2–3.5; VTT Building Technology, Holmberg 1995 pers. comm.)
- Full 600×600 units, 1.0 m³/s, ASHRAE dust, DEHS efficiency by LAS-X. A: 0.4 µm efficiency 73 → 75 (30 g) → 73 (90 g) → 69 (210 g) → 73 (315 g) → 74 % (390 g, 461 Pa). 390 g/2.8 m² = 139 g/m² fed with no loss. B: 0.4 µm 54 → 62 → 68 → 82 → 91 → 96 % (0–305 g; 305 g/5.6 m² = 54 g/m²). Report: "electret filters should be expected to operate reliably" by this test — contradicted by 1a/1b.

### 1d. Bimodal lab aerosols built to mimic ambient (§5.2, Figs 5.7–5.35, p.29–43) — lab, but it is the composition dependence of the field effect
- Mixtures of diesel fume (Yanmar 0.2 L single-cylinder; mass mode 0.12–0.21 µm, Fig 4.3) and PTI Fine test dust (mass mode 2.8–5.7 µm). Labels = approximate mass % diesel / % PTI ("10/90", "15/85", "25/75", "35/65"). Material samples, no pre-filter, KCl efficiency at 0.4 µm.
- x-axis of the summary figures is "concentration × time (µg/m³·year)" = fed mass ÷ flow. Conversion to fed g/m² of media: × v_f × 3.156e7 s/yr ⇒ ×10.4 for A (33 cm/s), ×6.6 for B (21 cm/s). Check: Fig 5.31 (B, 35/65) 4.3 g/m² ↔ 0.65 µg/m³·yr in Fig 5.33. OK.
- A, 0.4 µm efficiency, Fig 5.32 re-read at 2× (x in µg/m³·yr, ±0.1; y ±2 %):
  - PTI only: 88, 85 (1.7), 82.5 (2.9), 80 (4.0), 79 (6.1), 80 (9.6), 81 (12.8), 84 (16.8).
  - 10/90: 86, 82 (1.4), 78 (2.8), 77 (4.4), 72 (6.9), 75 (10.1), 82 (13.7), 89 (16.5).
  - 15/85: 88, 72 (1.1), 60 (2.2), 51.5 (3.7), 50 (7.6), 64 (11.1), 91 (14.4).
  - 25/75: 90, 66 (0.6), 49 (1.1), 33 (2.1), 30 (4.5), 45 (7.6), 75 (11.0).
  - 35/65: 87, 70 (0.3), 53 (0.65), 34 (1.0), 26 (2.2), 31 (4.1), 36.5 (5.6), 43 (7.5).
  - Diesel mass FED to reach ~50 % (P ≈ 0.5, i.e. retained −lnP ≈ 0.33) (mine, ×10.4 g/m² per µg/m³·yr × diesel fraction): 35/65 ≈ 0.7 → 2.6 g/m² diesel; 25/75 ≈ 1.1 → 2.9 g/m²; 15/85 ≈ 3.7 → 5.8 g/m²; pure diesel (Fig 4.5) ≈ 3.3 g/m²; 10/90 never got below 72 %. So with ≥25 % fine combustion mass, loss tracks the diesel grams (~3 g/m² fed for two-thirds of −lnP) and the coarse dust barely matters; at 10–15 % fine the co-deposited coarse cake adds mechanical capture fast enough to cap the loss.
  - Apparent electrostatic part lost at the minimum (P0 0.12, P_IPA 0.85): 35/65 0.93; 25/75 0.90; 15/85 0.73; 10/90 ~0.4; PTI only ~0.3. (Net of the cake's mechanical gain.)
  - Every curve recovers as cake builds; the recovery starts sooner with more coarse dust.
- B (Fig 5.33/5.35): PTI only rises monotonically 78 → 98 %; 35/65 dips 77 → 52 % at ~0.7 µg/m³·yr (4.3 g/m² fed; Fig 5.31 gives 77, 61, 52, 55, 65, 74, 83, 88 % at 0, 2.1, 4.3, 6.8, 14.8, 27, 38, 51 g/m², with Δp 141 → 461 Pa).
- Report text (p.43): "The particle penetration can increase as much as by a factor of 6 in the case of filter "A" and by a factor of 2 in the case of filter "B"." Conclusions (p.45): "the loss of filter efficiency was dependent on the relative amount of diesel fume. Increasing the amount of diesel fume led to faster and stronger decrease in the efficiency."
- Pure diesel (§4.2, Figs 4.5, 4.7): A 0.4 µm 90 → 67 (1.5) → 54 (3.1) → 22 (5.3) → 20 (7.4) → 20 % (10.6 g/m² fed); B 58 → 29 % by 1 g/m² fed, then slowly up to 36 % by 6.9. Text: diesel needed to remove the electrostatic mechanism "approximately 6 g/m² (filter "A") and 1 g/m² (filter "B")"; side-stream cigarette smoke "approximately 12 g/m² (filter "A") and 2 g/m² (filter "B")"; diesel levels "did not cause any increase in the pressure drop".
- Report caveat (p.44): bimodal tests were without pre-filter; with a pre-filter "the electret filter is exposed to fine particle fraction only" and behaviour will differ.

References inside the report worth chasing (field): SINTEF Klima- og kuldeteknikk 1995, "Langtidstesting av filter i virkelig miljø", Rapport STF11 A95027 (long-term testing of filters in real environment, Norway); Gustavsson J. 1993, Energi & Miljö 64(1):49–55 (Swedish); Lehtimäki & Heinonen, Indoor Air '93 vol 6:463–468.

---

## 2. Raynor P.C. & Chae S.J. 2004. "The long-term performance of electrically charged filters in a ventilation system". J Occup Environ Hyg 1(7):463–471. doi:10.1080/15459620490467783
Full text read: local copy downloaded by the liquid-pool agent (scratchpad\dl\liquid\cdc_188464.pdf, CDC Stacks NIOSH-grant copy https://stacks.cdc.gov/view/cdc/188464 — the Stacks PDF is now blocked to my tools; landing page readable). Figures rendered and read.

Setting (Methods, p.464): two near-identical air-handling units, each max ~60 000 cfm, 100 % outside air, University of Minnesota Twin Cities campus (office + lab building), intakes one storey up over "a lightly traveled road". Upstream of the test filters: a bank of thirty 2×2 ft pre-filters that "collected more than 90% of incoming particles 3 µm in diameter or larger". Ran "almost continuously", 134 days (19 weeks + 1 day). Season not stated (Δp dips coinciding with "the three periods of hottest daily high temperatures" in weeks 3–7 suggest a summer start).
Media: "polyolefin fiber filters were made from polyethylene and polypropylene fibers" (charged; charging method not stated; obtained via Camfil Farr; study funded by Johns Manville, a glass-media maker — note the sponsor). Both types: 15 pleats ~28 cm deep × 54 cm tall in 2×2 ft frames, "nominally 90-95% efficient" by ASHRAE 52.1 dust spot (≈ MERV 14). Media area 4.65 m² per filter (stated). 30 filters per AHU.
Velocity: the 2003 companion paper gives the 52.2 test flow 1968 cfm (3346 m³/h) per filter → 0.93 m³/s ÷ 4.65 m² = 0.20 m/s media velocity. Face velocities measured at the end 565–748 fpm (Table I) → roughly 0.20–0.25 m/s through media. Strong local "jets" through the polyolefin filters (non-uniform flow) noted.
Efficiency: count-based, DMPS (0.117–0.457 µm, mobility) and APS (0.504–3.05 µm, aerodynamic), 4 up/down probe pairs, 26 test occasions. Ambient charge state (not neutralised).
Mass (Results, p.466, verbatim): "the four glass fiber filters weighed to determine mass loading gained an average of 341 g (0.75 lb) while the four polyolefin fiber filters gained an average of 227 g (0.50 lb). These loadings are equivalent to 73 g/m2 for the glass fiber filters and 49 g/m2 for the polyolefin fiber filters." Weighing precision "the nearest 56.8 g (0.125 lb)" → ±12 g/m² per filter. Gravimetric, whole filter incl. frame, at the end only. 2003 paper: "most of the mass in the particles collected by the filters in the real HVAC systems was contributed by particles that were smaller than 1 µm" (asserted, not measured).
Sanity check (mine): 0.2 m/s × 1.16e7 s = 2.3e6 m³ per m² of media; at ~10–15 µg/m³ reaching the filter and ~0.5–0.7 mass capture → 12–24 g/m² expected vs 49 ± 12 measured. Within ~×2; whole-filter weighing (frame moisture) could inflate it.
Δp: normalised Δp polyolefin 0.67 → 0.95 in H2O (+42 %); glass 0.60 → 1.0 (+67 %). (2003 paper: polyolefin 163 → 236 Pa, glass 152 → 244 Pa.)

Polyolefin efficiency vs time — second-order regression curves read off Fig. 4 (±0.03); glass alongside:

| size | week 0 | minimum (week of min) | week 19 | glass |
|---|---|---|---|---|
| 0.150 µm | 0.65 | 0.35 (~15) | 0.37 | 0.62 → 0.71 |
| 0.291 µm | 0.68 | 0.43 (~13) | 0.48 | ~0.72–0.74 |
| 0.582 µm | 0.87 | 0.45 (~11) | 0.66 | ~0.87–0.88 |
| 1.03 µm | 0.93 | 0.68 (~12) | 0.76 | ~0.96 |
| 1.98 µm | 0.96 | 0.83 (~10) | 0.95 | ~0.96 |
| 3.05 µm | 0.96 | 0.73 (~10) | 0.93 | ~0.96 |

Text: 0.3 µm "decreased from 70% to as low as 45%"; 0.6 µm "from 85% to as low as 45%"; abstract 0.6 µm "85% to 45% after 11 weeks before recovering to 65%". Differences from glass significant "after about 2 weeks of use". Minimum timing (p.469): ≥0.582 µm at 10–12 weeks, 0.291 µm ~13 weeks, 0.150 µm ~15 weeks — "efficiency reductions continue to mount for a long time". Individual points scatter widely (0–0.8).
Fitted size curves (Eq. 5, η = 1 − exp(−A′d^B − C′d^−2/3), d in µm): polyolefin day 0 A′=2.83, B=0.570, C′=0.00968; day 134 A′=1.59, B=0.874, C′=0.0195. Glass day 0 A′=3.01, B=0.617, C′=0.00333; day 134 A′=2.64, B=0.688, C′=0.0350. (My evaluation, polyolefin day 0 → day 134: 0.63→0.31 at 0.15 µm, 0.77→0.45 at 0.3 µm, 0.88→0.65 at 0.6 µm, 0.94→0.80 at 1 µm.)

Derived (mine):
- Retained −lnP at the minimum (curves re-read at 2× render): 0.150 µm ln0.65/ln0.35 = 0.41; 0.291 µm 0.49; 0.582 µm 0.29; 1.03 µm 0.41. Filter-level QF at ~0.3 µm (Δp 163 Pa, ~20 cm/s media): 1.14/0.163 = 7.0 kPa⁻¹ new → ~0.56/0.19 ≈ 3.0 kPa⁻¹ at the minimum; glass ~1.3/0.152 ≈ 8.6 kPa⁻¹ new. No IPA/discharged reference (the glass filter is a different medium), so "electrostatic part lost" cannot be computed.
- Mass at the minimum: not measured. Pro-rating the end mass by time (continuous running) gives 49 × 77/134 ≈ 28 g/m² at week 11; pro-rating by Δp rise (2003 paper: "After a 15-20% increase in pressure drop, the efficiency decline halted") gives 0.34–0.45 × 49 ≈ 17–22 g/m². So the minimum came at roughly 17–28 g/m² collected (±25 % from weighing alone), mostly submicron outdoor aerosol behind a pre-filter. Efficiency was already significantly below glass by week 2 (≈4–7 g/m² on the same pro-rating).
- Recovery: authors attribute the late rise to "better particle capture by impaction and interception mechanisms as the filters become loaded" (mechanical gain from the deposit, not charge recovery).

## 3. Raynor P.C. & Chae S.J. 2003. "Dust loading on electrostatically charged filters in a standard test and a real HVAC system". Filtration+Separation 40(2):35–39
Full text read: local copy scratchpad\dl\standards\cdc_188536.pdf/.txt (standards-pool agent; CDC Stacks https://stacks.cdc.gov/view/cdc/188536). Same field test as §2.
- Two unused filters of each type sent to a lab for ASHRAE 52.2-1999 at 1968 cfm with five dust loadings: polyolefin efficiency "increased steadily with the accelerated dust loading", glass also increased — no 52.2 dust step reproduced the in-situ loss (Figs 3–5, efficiency vs % Δp increase at ~0.34, 0.62, 1.1 µm).
- In situ, "After a 15-20% increase in pressure drop, the efficiency decline halted and the efficiency began to rise as the pressure drop increased further."
- Explanation offered: 52.2 dust mass mostly >1 µm; collected atmospheric mass mostly <1 µm; and composition — "many of the particles entering an HVAC system are derived from combustion sources and from chemical processes occurring in the atmosphere. These particles are chemically and physically different than the mineral particles, carbon black, and cotton linters comprising the synthetic test dust."

## 4. Raynor P.C., Kim B.G., Ramachandran G., Strommen M.R., Horns J.H., Streifel A.J. 2008. "Collection of biological and non-biological particles by new and used filters made from glass and electrostatically charged synthetic fibers". Indoor Air 18(1):51–62. doi:10.1111/j.1600-0668.2007.00504.x
Only the NIOSH abstract read (https://stacks.cdc.gov/view/cdc/188537; PDF blocked to my tools; Wiley paywall). Hospital HVAC (Minnesota), 13 weeks, charged synthetic vs fibreglass banks. "For particles 0.7-1.0 µm in diameter, efficiency decreased from 92% to 44%." Synthetic Δp "less than half that of the fiberglass filters throughout". Fibreglass efficiency unchanged. "when measured using culturable biological particles in the ambient air, efficiency was essentially the same for new filters and filters used for 13 weeks" for both types; authors hypothesise bioaerosols carry higher charge. Mass loading unknown. Retained −lnP at 0.7–1.0 µm (mine): ln0.56/ln0.08 = 0.23. WALLED — Matt to download (Wiley, or https://stacks.cdc.gov/view/cdc/188537/cdc_188537_DS1.pdf) for media, velocity and any weights.

## 5. Berardinelli S.P., Commodore M.A., Fotta S.A., Hayes J.L., Moyer E.S. 2007. "Real-time evaluation of ventilation filter-bank systems". J Occup Environ Hyg 4(1):58–69
Only the NIOSH abstract read (https://stacks.cdc.gov/view/cdc/185747; public-domain NIOSH paper, PDF 2.02 MB blocked to my tools). Two US government buildings (one recirculating, one 100 % outside air at a NIOSH facility, West Virginia); matched OPCs in situ. Verbatim: replacement eight-pocket medium-efficiency bags "contained electrostatic filter media and lost filtration efficiency rapidly, which was subsequently confirmed in a 30-day study"; "less than 6 months' use was justified"; NIOSH AHU #8 (100 % OA) upgraded from electrostatic bags (9-month change-out) to glass V-banks which "had better filter efficiency after 3 years of service than the electrostatic filters had at 9 months." No numbers in the abstract. WALLED — worth Matt downloading for the 30-day curve.

## 6. Lehtimäki M. & Taipale A. 2004 (approved 2002). "Field test method for the measurement of filter efficiency". Nordtest NT TR 531. http://nordtest.info/images/documents/nt-technical-reports/NT%20TR%20531_Field%20test%20method%20for%20the%20easurement%20of%20filter%20efficiency_Nordtest%20Technical%20Report.pdf
Read §3.3.1–3.3.2 and Figs 12, 14. Data originally from Lehtimäki & Taipale 1999, "Performance of ventilation filters (pilot field study, material test and full scale field test)", TAKE IAQ E Report 26, Finnish Development Center for Building Services (not found online).
- Four F7 filters ("A"–"D"), outdoor air, Tampere, ~8 months; weekly gravimetric upstream/downstream membrane samples. Filter types not given except that B is electret.
- Fig. 14 (PM2.5 mass penetration; upstream behind a 2.5 µm impactor pre-separator, downstream total assumed <2.5 µm): filter B ~15 % (day 0), ~20 % (day ~5), ~35–46 % by days 14–35, ~55–80 % (mostly 55–65 %) from day ~42 to day 245. A, C, D ~20–45 % with no trend. Text: "the penetration of filter "B" increases significantly with time. This is caused by the loss of electrostatic removal mechanism."
- Fig. 12 (total-mass penetration): B ~3 % → 10–45 %; others ~5–20 %; noisy (size-distribution swings).
- Derived (mine): PM2.5 mass efficiency of B 85 % → ~40 % within ~6 weeks, then flat; retained −lnP ≈ ln0.6/ln0.15 = 0.27. No velocity, media area or mass given; at Tampere's ~6–10 µg/m³ (NT TR 320) and a typical F7 bag media velocity 0.1–0.3 m/s, 6 weeks ≈ 0.1–0.3 m/s × 3.6e6 s × 8e-6 g/m³ ≈ 3–9 g/m² fed (my bracket; ×2 uncertainty).

## 7. ASHRAE RP-1360 (RTI International; PI Kathleen Owen; Owen, Pope, Hanley), "How do pressure drop, efficiency, weight gain, and loaded dust composition change throughout filter lifetime?" Final report released March 2013; AFS 2014 paper "How air filters change with use: testing new and used filters" (Owen & Pope, AFS Fall Conference 2014 proceedings p.678)
Primary NOT read (ASHRAE paywall; RTI page https://www.rti.org/publication/pressure-drop-efficiency-weight-gain-loaded-dust-composition-change-throughout-filter-lifetime-rp-13 gives the abstract). RTI abstract (verbatim): "A "Four-City Study" investigated the performance of in-situ filters over their lifetimes for pressure drop, dust weight gain, and changes in filtration efficiency ... The Appendix J conditioning step was needed to bracket the minimum in-situ efficiency of the electret filter. Reporting values calculated from the minimum efficiency curve are much more relevant to in-situ performance than the use of average or final dust-loaded values." Filters: uncharged MERV 7, charged MERV 11 (residential pleated), uncharged MERV 15 (commercial), installed by volunteers, returned at intervals, re-tested by 52.2.
Numbers below are SECONDARY — table as reproduced by a filter vendor with a stated stake against Appendix J (Tex-Air Filters blog, https://www.texairfilters.com/what-happens-to-the-electret-charge-on-a-merv-11-pleated-filter-in-service/ , read through WebFetch's summary; the site blocks curl). MERV 11 electret, 52.2 E1 (0.3–1 µm) / E2 (1–3) / E3 (3–10) %, Δp in. w.g.:

| condition | MERV | E1 | E2 | E3 | Δp |
|---|---|---|---|---|---|
| new, 52.2 initial | 12 | 37 | 80 | 93 | 0.22 |
| new, after Appendix J (KCl conditioning) | 8-A | 13 | 51 | 74 | 0.22 |
| MN home, 2 months | 9 | 14 | 55 | 72 | 0.35 |
| MN home, 4 months | 11 | 21 | 74 | 95 | 0.27 |
| NC home, 1.5 months | 11 | 15 | 66 | 86 | 0.39 |
| NC home, 3.5 months | 10 | 12 | 61 | 91 | 0.26 |
| GA home, 1.5 months | 8 | 13 | 52 | 71 | 0.23 |
| GA home, 5 months | 11 | 35 | 74 | 87 | 0.25 |

- Reading: E1 fell to the Appendix J level (12–15 %) within 1.5–3.5 months in homes in three states; E2/E3 partly recovered with loading. Retained −lnP for E1 at ~13 %: ln0.87/ln0.63 = 0.30. Weight-gain values exist in the report but were not in the blog. Unverified against the primary.
- Same blog, vendor's own test (not RP data): commercial-building MERV 11 electret pleats, 52.2 at 492 fpm: new E1 27 % → 28 % (1 month, 30 % OA), 21 % (1.5 months), 20 % (4 months, 15 % OA). Unverified.

## 8. Li T. & Siegel J.A. 2020. "In situ efficiency of filters in residential central HVAC systems". Indoor Air 30(2):315–325. doi:10.1111/ina.12633 (ASHRAE RP-1649)
Abstract only (Europe PMC). 21 occupied Toronto homes, four filter types (MERV 8–14, electret and non-electret), each installed 3 months; in-duct concentration measurements. Verbatim: "there is no significant difference in efficiency between initial and 3-month non-electret filters, but the efficiency of electret filters generally decreased over time. However, both nominal efficiency and performance change were vastly overshadowed by the wide variety in loading and system conditions across homes". ASHRAE Journal Q&A (https://www.ashrae.org/news/ashraejournal/ashrae-rp-1649-comparing-laboratory-performance-and-in-situ-performance-of-residential-hvac-filters): annual median runtime 9.6 %, so "many of our test filters had relatively low dust loading"; 52.2 results "could provide reasonable bracketing" but "lab-tested results generally overestimate in-situ efficiency but underestimate in-situ pressure drop." Companion: Alavy M. & Siegel J.A. 2020, "In-situ effectiveness of residential HVAC filters", Indoor Air 30(1):156–166 (median PM2.5 effectiveness 36 % electret vs 16 % non-electret at MERV 8). WALLED — RP-1649 final report free to ASHRAE members.

## 9. Purdue / Boor group: Huang C. 2021, "In-situ performance of HVAC filters aged with 100% outdoor air", MS thesis, Purdue University (advisor B. Boor). doi:10.25394/PGS.14515173.v1, PDF https://ndownloader.figshare.com/files/27807084 (read: abstract, §3.2, §4.2–4.4, §5.3, §5.5, Figs 5.13, 5.21)
- Rig: three full-scale ducts, Herrick Labs, West Lafayette IN, 100 % outdoor air, ~2000 cfm (0.94 m³/s) each, ±200 cfm; each duct MERV 8 pleated pre-filter then a test filter. Duct 2 test filter: "MERV13E", a 24×24×30 in bag filter "enhanced with electrostatic charges", rated 0.31 in H2O at 2000 cfm (Table 3.1). Media area, polymer, brand: NOT given. Typical 24×24×30 MERV 13 bags have ~5.6–9.3 m² media (6–8 pockets) → media velocity ~0.10–0.17 m/s (my bracket).
- Period: started ~23 Nov 2020; thesis covers to ~week 18 (late March 2021) — winter/spring, Indiana.
- Efficiency: SMPS + OPS up/downstream (ambient charge state), size-resolved and mass-based ePMx (mass computed from number distributions assuming spherical particles, density 1.5 g/cm³).
- ePMx medians, Duct 2 MERV 13E (Fig. 5.13, read ±2 %): ePM10 66 (wk 2) → 53 (wk 5) → 44 (wk 8) → 36 (wk 11) → 33 (wk 17); ePM2.5 64 → 52 → 44 → 36 → 29; ePM1 62 → 50 → 42 → 35 → 27; ePM0.1 60 → 52 → 46 → 42 → 34 (wk 14) → 38. MERV 8 and MERV 14 (mechanical) showed "no significant change". Size-resolved (text): MERV 13E minimum-efficiency band (200–500 nm) started ~50–60 % and "By Week17, the lower efficiencies have decreased by almost 0.5 to around 30% to 40%"; decrease spanned 20 nm–3 µm. No Δp rise for the electret ("no significant change at all").
- Loaded mass (Fig. 5.21; CALCULATED, not weighed: upstream PM10 from SMPS+OPS × flow × measured efficiency × time, eq. 4-14, gaps interpolated): ~0.5 g (1 Dec), ~10 g (1 Jan), ~16 g (1 Feb), ~20.5 g (1 Mar), ~22.5 g (~20 Mar). Mapping to sampling weeks (mine): wk 2 ≈ 1–2 g, wk 5 ≈ 8 g, wk 8 ≈ 13 g, wk 11 ≈ 16 g, wk 17 ≈ 21.5 g per filter. Per m² of media (5.6–9.3 m²): wk 5 ≈ 0.9–1.4 g/m², wk 11 ≈ 1.7–2.9 g/m², wk 17 ≈ 2.3–3.8 g/m².
- Derived (mine): ePM1 62 → 27 % ⇒ retained −lnP = ln0.73/ln0.38 = 0.33 at ~2.3–3.8 g/m² (calculated) of mostly submicron Indiana winter aerosol. Week-2 value is already after ~1–2 g; true day-0 not measured. No IPA reference.
- Later: ACHR News (8 Sep 2026, https://www.achrnews.com/articles/166653-the-filter-you-install-isnt-the-filter-you-replace), on the same rig run 112 weeks (ASHRAE RP-1734): "The MERV 13 electret filter ... declined to an in-situ rating of MERV 10 after roughly six and a half months"; MERV 14 mechanical stable ~90 weeks; MERV 8 pre-filters rose to in-situ MERV 14 after a year; >80 % of incoming particles by number <100 nm, peak 30–40 nm. PhD (Huang 2025) abstract: https://engineering.purdue.edu/CCE/Academics/Graduate/Current/Abstracts/PhD_Defenses/2025/Huang-Chunxu-Abstract.pdf (dissertation not found online).

## 9b. Hanley J.T., Ensor D.S., Foarde K.K., Sparks L.E. 1999. "The effect of loading dust type on the filtration efficiency of electrostatically-charged filters". Indoor Air '99 / 20th AIVC Conference, Edinburgh, AIVC paper 097. http://www.aivc.org/sites/default/files/members_area/medias/pdf/Conf/1999/paper097.pdf (read in full, Figs 1–2 rendered; EPA-funded, coop. agreement 822870-01)
- Filters: (1) high-efficiency rigid cell, "charged via an electrodynamics spinning process", 610×610×305 mm at 0.71 m³/s; (2) pleated panel, corona-charged, 610×610×50 mm at 0.71 m³/s; (3) residential panel, split-fibre charged, 510×630×25 mm at 0.48 m³/s. Media area, basis weight: not given.
- Exposure: ambient = portable ducts in the outdoor-air intake plenum of an RTI office building (Research Triangle Park NC), run 24 h/day, filters taken to the 52.2 rig every 2 weeks. In-home = nine RTI employees' home systems, 2–12 weeks, one exposure per filter; compared with new filters from the same case.
- Efficiency test: draft ASHRAE 52.2P solid KCl, 0.3–10 µm, OPC, in the RTI test duct (lab measurement of field-aged filters).
- Fig. 1, rigid cell, ambient (read ±3 %): at ~0.35 µm initial ~81 % → 45 % (2 wk) → ~33 % (4 wk) → ~34 % (6 wk) → ~25 % (8 wk) → ~29 % (10 wk). At ~1.1 µm: ~95 % → 77 → 69 → 68 → 69 → 50 %. At ~1.9 µm: ~99 % → 95 → 91 → 91 → 91 → 76 %. Retained −lnP at 0.35 µm (mine): 2 wk ln0.55/ln0.19 = 0.36; 10 wk ln0.71/ln0.19 = 0.21.
- Fig. 2, residential split-fibre, in-home: ~0.35 µm new ~31 % → 20 % (2 wk) → 8–13 % (4–12 wk); ~1 µm ~57 % → 46 % (2 wk) → ~30–40 % (6–12 wk); 3–10 µm ~84 % → 65–80 %. Retained −lnP at 0.35 µm: ln0.9/ln0.69 ≈ 0.28.
- Text: "Results show that all the ambient and in-home exposed filters had substantial decreases in filtration efficiency"; 52.2P ASHRAE-dust conditioning "showed primarily increases in efficiency"; submicron KCl (1 % solution, Laskin nozzle, 8 h) "came closest", but "still significantly underestimated the decrease"; KCl "did not reveal the decrease in efficiency at larger particle sizes", attributed to dendrites and suppressed bounce. Authors did not separate particle collection from "temperature, humidity, and the simple passage of time".
- Mass: none reported. Bracket (mine): rigid cell at 0.71 m³/s × 2 weeks (1.2e6 s) × ~25 µg/m³ (late-1990s NC Piedmont PM2.5 ~15 + some coarse) ≈ 21 g fed; at ~70 % capture and an assumed 5–10 m² of media → ~1.5–3 g/m² by the first 2-week test, ~7–15 g/m² by 10 weeks. Media area is the big unknown.
- This is the RTI work behind ASHRAE 52.2 Appendix J (KCl conditioning).

## 10. US 5,496,507 (3M; Angadjivand et al.), Example 44 / Table 11 — ambient-air loading, with the bracket the brief asked for
Text read from the patent agent's local copy (scratchpad\dl\patent\US5496507.txt, gp_text.txt), cols 15–16 and the "Ambient Air Particle Loading Test" paragraph.
- CORRECTION to the brief: Example 44 is "prepared as in Example 31", and Example 31 is "A web of the poly(4-methyl-1-pentene)" (Mitsui TPX), corona treated then water-jet (hydro) charged — NOT polypropylene. EFD 14 µm, 40 g/m², 1.2 mm; pleated element 29 cm × 10 cm, 52 pleats × 28 mm, on an 80 g/m² Colback scrim → media ≈ 2 × 52 × 0.028 × 0.10 = 0.29 m². Table 10's cigarette-smoke samples (Ex. 42–43) are the same polymer.
- Loading test (verbatim): "Filter samples were subjected to ambient air at a flow rate of 149 ft3/min (250 m3/hr) for extended periods of time using samples 300 mm×116 mm and then challenged with particles of 0.3 micrometers and 1.0 micrometers in size." Efficiency "measured as described in the cigarette smoke adsorption test" (LAS-X, count). Location, indoor/outdoor, concentration, RH: not stated. Media velocity 0.0694 m³/s ÷ 0.29 m² = 0.24 m/s.
- Table 11: 0.3 µm 70.5 → 53.8 (133 h) → 47 % (290 h); 1.0 µm 86.8 → 79.0 → 75 %; Δp 10.8 → 13.8 → 15.5 mm H2O (106 → 135 → 152 Pa).
- Air volume: 250 m³/h × 133 h = 33 250 m³; × 290 h = 72 500 m³.
- Bracket (mine). Collected = C × V × E_mass ÷ 0.29 m². Low: indoor lab/office air, ~5 µg/m³, E_mass 0.5 → 0.62 g/m² at 290 h (0.29 at 133 h). Central: indoor occupied air ~15 µg/m³ total, E_mass 0.65 → 2.4 g/m² (1.1 at 133 h). High: St Paul outdoor air, ~35 µg/m³ PM10/TSP, E_mass 0.75 → 6.6 g/m² (3.0 at 133 h). So 133 h ≈ 0.3–3 g/m², 290 h ≈ 0.6–6.6 g/m², central ~1 and ~2.4. Indoor vs outdoor is the dominant uncertainty (×3–4). Concentrations are my assumptions, not sourced.
- Δp cross-check fails: the element's 106 Pa is mostly pleat-channel loss (Davies for a flat 40 g/m², 14 µm, 1.2 mm web at 0.24 m/s gives ~15 Pa), so the 46 Pa rise cannot be mapped to mass with any confidence.
- Derived: 0.3 µm retained −lnP = ln0.462/ln0.295 = 0.63 (133 h), ln0.53/ln0.295 = 0.52 (290 h); 1 µm 0.77, 0.68. Element-level QF at 0.3 µm (24 cm/s media): 11.5 kPa⁻¹ → 4.2 kPa⁻¹ at 290 h.

## 11. Mahdavi A. & Siegel J.A. 2020. "Extraction of dust collected in HVAC filters for quantitative filter forensics". Aerosol Sci Technol, doi:10.1080/02786826.2020.1774492 — Supplement Table S1 (CC BY 4.0, https://ndownloader.figshare.com/files/23236474), read
- Gives the natural mass loading of residential filters from the RP-1649 Toronto homes (3 months each): loaded dust mass per filter (balance, M0 − Mblank): MERV 8 1.2–19.0 g (n=14); MERV 8E (electret) 1.3–8.6 g (n=11); MERV 11 2.4–12.7 g (n=6); MERV 14 1.1–16.7 g (n=10). Filters 1-inch (Phase 1 size 41 × 64 × 2.5 cm; Phase 2 sizes varied by home).
- Per m² (mine): a 16×25×1 in pleated filter has roughly 0.8–1.2 m² of media → ~1–11 g/m² per 3 months for the electret MERV 8E. Pair with §8: over those same 3 months "the efficiency of electret filters generally decreased". Low runtimes (median 9.6 %) kept these loads low.
- Composition: house dust (vacuum recovery over-represents >10 µm). Mahdavi & Siegel 2021 (Indoor Air, doi:10.1111/ina.12782; abstract via search only) report filter-forensics TSP 2.9–823.7 µg/m³, median 89.8 µg/m³.

## 12. Corsi–Rosenthal (MERV 13 box-fan) units
- Pistochini T., Jaeger N., Cappa C.D., Corsi R.L. 2025, "Longevity of size-dependent particle removal performance of do-it-yourself box fan air filters", Environ Sci Process Impacts 27(6):1629–1639, doi:10.1039/d4em00406j, CC BY 3.0 but Cloudflare-blocked to my tools (https://pubs.rsc.org/en/content/articlelanding/2025/em/d4em00406j). Abstract-level only (via search): four MERV 13 box-fan units, two labs and two offices on a university campus, run daily; size-resolved CADR measured in a lab every 10 weeks for 40 weeks; "each air filter maintained at least 60% of its initial CADR at the end of the 40 week study"; reductions "attributed to a reduction in filtration efficiency, likely due to a loss of filter electrostatic charge over time"; flow not clearly reduced. NOT VERIFIED beyond the abstract; MATT TO DOWNLOAD (open access) for size-resolved efficiency vs weeks.
- Tex-Air Filters blog (vendor; author Jim Rosenthal, CR-box co-originator), "Testing the efficiency of MERV 13 Corsi-Rosenthal boxes in use" (https://www.texairfilters.com/testing-the-efficiency-of-merv-13-corsi-rosenthal-boxes-in-use/, via WebFetch summary): Tex-Air MERV 13 electret 2-in pleats, 24/7 in offices; single-pass efficiency from room vs outlet counts (Lighthouse 3016, "estimates", not 52.2): 0.3 µm 50 % new → 43 % (2 months), 48 % (4), 44 % (6), 36 % (10); 0.5 µm 67 → 58, 49, 51, 42 %; 1 µm 72 → 72, 54, 74, 60 %. Outlet velocity unchanged. Low-quality, vendor, no mass.

## 13. Cabin filters
- Heo K.J., Noh J.W., Kim Y., Jung J.H. 2022. "Comparison of the service life of an automotive cabin air filter under dust loading conditions of the laboratory environment and on-road driving". J Aerosol Sci 162:105972, doi:10.1016/j.jaerosci.2022.105972. WALLED (ScienceDirect). From abstract fragments (search) and a citing paper: lab dust loading raised efficiency as air paths clogged, but "under on-road driving conditions, filter performance dropped to 58.7% with similar dust loading"; authors: dust loading "is not sufficient to characterize the service life". Citing paper (Shim, Noh, Kim 2022, ACS Omega 7:43738, PMC9730776, read): "a decrease in the performance of the filter to 58.7% under weak conditions when driving on road for up to 10 months". Whether 58.7 % is an efficiency or a fraction of initial is unclear. MATT TO DOWNLOAD — likely the best cabin field-vs-lab mass comparison.
- Same ACS Omega paper (PTFE membrane cabin filter, non-electret): after 2336 km / 1 month on a real vehicle, efficiency loss 0.6 % (0.3–0.5 µm) — the contrast case.
- Lee (SAE 960541, 1996) "In-vehicle performances of new and used automotive cabin air filters" and INERIS QABINE 2 (https://hal-ineris.archives-ouvertes.fr/ineris-03319970): not read (walled).

## 14. Other field leads, walled or abstract-only
- Lehtimäki M. & Heinonen K. 1994, "Reliability of electret filters", Build Environ 29(3):353–355 (Elsevier, walled). VTT abstract: efficiency dropped noticeably after diesel fume or cigarette smoke, small decline with Arizona road dust; advised against wide use of electret media in ventilation "until long-term field tests verify their stability". Its data are largely re-presented in NT TR 320 (§1).
- ASHRAE RP-1189 (VTT), "Investigation of mechanisms and operating environments that impact the filtration efficiency of charged air filtration media", Phase II = field testing of full-scale filters and filter materials in urban and suburban environments (https://www.n-standards.com, paid). Basis of 52.2 Appendix J together with RP-1190. MATT TO DOWNLOAD — probably the richest field dataset with masses.
- ASHRAE RP-1360 final report (RTI, 2013) and RP-1649 final report (U Toronto, 2019): ASHRAE paywall (RP-1649 free to members). Contain weight gain vs efficiency for in-home filters.
- CETIAT (Ginestet, Mouradian, Pugnet): Indoor Air 2014 paper "Performances, classification and impact on energy consumption of air filters for balanced ventilation systems with heat recovery for dwellings" (NT 2014/015, https://www.cetiat.fr/?p=12966) — 3-year study, G4/M5/F7 mini-pleated panels run 1 year on real outdoor air; fractional efficiency 0.2–5 µm, Δp and dust holding vs time; abstract: "the efficiency of the electret filters decreases as function of time while that of the mechanical effects only filters increases". Also AIVC 2011 paper "Filters for balanced ventilation systems: design, long-term performances and energy considerations" (NTV 2011/044). Members-only; MATT TO REQUEST.
- Shi B. & Ekberg L. 2015, ES&T 49(11):6891–6898, doi:10.1021/acs.est.5b00974 — field + lab, M6 synthetic filter with/without ionizer over months (Gothenburg). Abstract: ionization +40 %-units "during most of the operation time"; PM0.3–0.5 kept >50 % for half a year with polarity switching; moisture reduced the ionizer gain. The ionizer-off control series would give charged-synthetic field decay. Walled (ACS).
- Li Shihang et al. 2022, "驻极体滤料的空气湿度和静电效应影响机理研究" (humidity and electrostatic effects in electret media), J Xi'an Univ Archit Technol (Nat Sci) 2022(5), doi:10.15986/j.1006-7930.2022.05.012 (CNKI). Search-summary only, UNVERIFIED: media used 5–7 months in a real environment had low areal particle loading and small Δp rise but efficiency "significantly" lower; IPA-type discharge lowered it further (charge not fully gone); lab-loaded samples kept higher efficiency than field-loaded ones at similar loading.
- Gustavsson J. (Camfil) 2000, "New test methods for air filters. Do they reflect the 'real life' performances?", Ventilation 2000 proceedings; SINTEF 1995 STF11 A95027 (Norway, long-term filter testing in real environment); Lehtimäki & Taipale 1999 TAKE IAQ E Report 26 (Finland). None found online.
- Masks worn in polluted cities: no study found that measured efficiency against ambient PM mass collected on the mask. Wear studies are dominated by breath moisture and handling, not ambient loading.
- Hanley, Ensor, Smith & Sparks 1994 (Indoor Air 4:169): lab ASHRAE-dust loading of in-duct cleaners ("A dust load on the air cleaner frequently increased its efficiency; for some, little change or a decrease"); not field. Not read.

---

## 15. Synthesis for the field pool (my analysis; every input is in the entries above)

### 15a. Field series side by side
Mass basis matters: "fed" = upstream × flow × time; "coll." = collected; "calc." = computed from measured upstream concentration × efficiency; "est." = my bracket.

| series | media | media v | air | time | mass, g/m² media | size | E0 → E | retained −lnP | electrostatic part lost |
|---|---|---|---|---|---|---|---|---|---|
| NT TR 320 A, 24 d | EU7 bag, 15–20 µm electret | 33 cm/s | Tampere outdoor, 6.4 µg/m³ | 24 d | 4.4 fed; ~3–4 coll., ~1 fine (est.) | 0.4 µm | 88.5 → 55 | 0.37 | 0.68 |
| NT TR 320 B, 24 d | EU7 bag, flat 5×15 µm | 21 | same | 24 d | 2.8 fed | 0.4 | 58 → 43 | ~0.6 | ~0.85 (±0.2) |
| NT TR 320 A, field unit | as A, behind EU3 | 36 | ~10 µg/m³ | 4 mo | 36 fed; ~2–10 fine coll. (est.) | 0.4 | 88 → 21 | 0.11 | 0.96 |
| NT TR 320 B, field unit | as B, behind EU3 | 18 | same | 4 mo | 18 fed | 0.4 | 77 → 43 | 0.38 | 0.95 |
| NT TR 531 "B" | F7 electret | n/a | Tampere outdoor | 6 wk, flat to 8 mo | ~3–9 fed by 6 wk (est.) | PM2.5 mass | 85 → ~40 | 0.27 | n/a |
| Raynor & Chae 2004 | MERV 14 PE/PP pleated, behind pre-filter | ~20 | Minneapolis 100 % OA | min at 11–15 wk | ~17–28 coll. at min (pro-rated from 49 ± 12 weighed at 19 wk) | 0.15–1.03 µm | e.g. 0.582 µm 87 → 45 | 0.29–0.49 | n/a |
| Huang 2021 (Purdue) | MERV 13 electret bag, behind MERV 8 | ~10–17 (est.) | Indiana winter OA | 17 wk (no min yet) | 2.3–3.8 calc. | ePM1 | 62 → 27 | 0.33 | n/a |
| Hanley 1999 rigid cell | electrospun-charged | n/a | NC intake plenum | 2 wk; 10 wk | ~1.5–3; ~7–15 (est., area assumed) | ~0.35 µm | 81 → 45; → 29 | 0.36; 0.21 | n/a |
| Hanley 1999 residential | split-fibre panel | n/a | 9 NC homes | 4–12 wk | n/a | ~0.35 | 31 → 8–13 | ~0.28 | n/a |
| RP-1360 (vendor-reproduced) | MERV 11 res. electret | n/a | MN/NC/GA homes | 1.5–3.5 mo | in report, not seen | E1 0.3–1 µm | 37 → 12–15 (App. J = 13) | ~0.3 | ≈ App. J level |
| US 5,496,507 Ex. 44 | PMP hydrocharged, 40 g/m², 14 µm | 24 | "ambient air" | 290 h | 0.6–6.6, central ~2.4 (est.) | 0.3 | 70.5 → 47 | 0.52 | n/a |
| Raynor et al. 2008 | charged synthetic | n/a | hospital HVAC | 13 wk | n/a | 0.7–1.0 | 92 → 44 | 0.23 | n/a |

### 15b. What controls degradation in real air, and how strongly
1. Fine combustion/secondary fraction of what lands on the electret. NT TR 320's diesel + PTI mixtures: with ≥25 % diesel by mass, the loss tracks diesel grams (~3 g/m² diesel fed for two-thirds of −lnP; pure diesel 3.3 g/m²) and the coarse dust barely changes it; at 15 % diesel the minimum is capped at ~50 % (0.73 of the electrostatic part); at 10 % ~72 % (~0.4); coarse-only PTI or ASHRAE dust gives ~no loss even at 139 g/m² fed. A pre-filter makes the main filter see mostly fine aerosol, i.e. the bad end of this scale (NT TR 320 field units behind EU3 lost 0.95–0.98).
2. Mass. Roughly 1–4 g/m² collected (mostly submicron) removed one-half to two-thirds of −lnP in every field series with a mass handle (Tampere 24 d, Purdue, Hanley 2 wk, 3M). The discharged/minimum level came at ~5–30 g/m² (Tampere 4 months behind EU3; Raynor ~17–28 g/m² on his weighed basis). Expressed as Δln P per g/m² collected (Brown-type β): Tampere A ~0.35–0.45 (total) or ~1–1.5 (fine only); Purdue ~0.18–0.31; Hanley ~0.35–0.7; 3M ~0.1–1 (central 0.24); Raynor 0.05–0.09 to the minimum (weighed mass, probably high). Spread ~×10, explained mostly by mass basis (fine vs total, weighed vs computed) and media.
3. Time at normal urban levels (5–15 µg/m³, 10–35 cm/s): most of the loss in 2–6 weeks, minimum at 6 weeks–4 months; it scales with C × v × t × capture, not time per se (NT TR 320's c·t normalisation works across its tests).
4. Floor: field minima sit at or near the discharged level — Tampere 0.95–1.0 of the electrostatic part; RP-1360 E1 fell to the Appendix J value; the Chinese 2022 paper (unverified) reports field-aged media still lost more on discharge, i.e. not fully discharged. Media with a bigger mechanical share (NT TR 320 B) keep more −lnP (0.38 vs 0.11 retained).
5. Recovery is mechanical, not charge regeneration: Raynor 0.6 µm 45 → 66 % from week 11 to 19 (~+20 g/m², Δp +15–20 % at the turn); RP-1360 E1 12–15 → 21–35 % at 4–5 months in two homes; NT TR 320 mixtures recover sooner the more coarse dust is present. Hanley's rigid cell and Purdue's bag had not turned by 10 and 17 weeks.
6. RH/season: no field study isolates it (Purdue saw RH/precipitation move Δp only). Gap.
7. Bioaerosol: Raynor 2008 — culturable-particle efficiency unchanged after 13 weeks while 0.7–1.0 µm non-biological fell 92 → 44 %. One study; mechanism (higher bioaerosol charge) is a hypothesis.

### 15c. Contradictions / cautions
- Weighed vs computed mass: Raynor weighed 49 ± 12 g/m² in 19 weeks; a concentration estimate gives ~12–24 g/m²; Purdue computed only 2–4 g/m² in 17 weeks for a similar loss. Whole-filter weighing (frames, moisture, coarse debris) and computed mass (misses >10 µm, assumes ρ = 1.5) bias in opposite directions — a factor of ~5–10 between them.
- Appendix J: RTI (RP-1360) says it is needed to bracket the in-situ minimum; Hanley 1999 says even submicron KCl "significantly underestimated" field loss; a vendor (Tex-Air) says Appendix J overstates field loss; Li & Siegel say 52.2 "could provide reasonable bracketing" but overestimates in-situ efficiency.
- Brief's prior (Walsh & Stenhouse: ~2 g/m² for 20 % loss of log PF): field per-gram loss is similar or faster on a fine-mass basis (20 % of −lnP at ~0.5–1 g/m² for Tampere A and Purdue; ~6 g/m² on Raynor's weighed basis), and field filters go on to near-full discharge.
- Brief's description of US5496507 Ex. 44 as polypropylene is wrong: it is poly(4-methyl-1-pentene).

