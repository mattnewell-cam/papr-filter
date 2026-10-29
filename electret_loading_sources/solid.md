# Pool: solid-particle laboratory loading of electret media

All penetrations P as fractions unless marked %. Derived quantities:
- retained fraction of −ln P = ln P_loaded / ln P_initial
- fraction of electrostatic capture lost = (ln P_loaded − ln P_initial)/(ln P_discharged − ln P_initial)

---

## 1. Martin & Moyer 2000 — continuous NaCl loading of certified respirator filters, with IPA reference

**Source (primary, NOT obtained):** S.B. Martin Jr. & E.S. Moyer, "Electrostatic respirator filter media:
filter efficiency and most penetrating particle size effects", Appl. Occup. Environ. Hyg. 15(8):609–617 (2000).
Full text sits on CDC Stacks, record 198418 — <https://stacks.cdc.gov/view/cdc/198418/cdc_198418_DS1.pdf>.
**Blocked from this network (HTTP 403 Access Denied at the Akamai edge for every stacks.cdc.gov URL).** Matt should download it.

**Source actually read (secondary, flagged):** T.J. Nelson (3M), "Spurious research on electrostatic filter
performance", 3M JobHealth Highlights 19(1), 2001, pp. 1–2, 4–5, 13.
<https://multimedia.3m.com/mws/media/99824O/spurious-research-on-electrostatic-filter-performance-2001.pdf>
(downloaded, `dl/solid/3m_spurious.pdf`). It is 3M's own summary of Martin & Moyer; it reproduces their
numbers as its Tables 1 and 2. Treat the numbers as second-hand until the CDC PDF is read.

Conditions (from 3M p. 2, cross-checked against 42 CFR 84.174 below): NaCl, CMD 0.075 ± 0.02 µm, GSD < 1.86,
Boltzmann-neutralised; 85 L/min for the filtering facepieces, 42.5 L/min for the cartridge filters; no
pre-humidification. Filters "tested with the NaCl aerosol **until maximum filter penetration was reached**".

**3M Table 1 — penetration, averages of three filters each**

| Filter | NaCl initial P (%) | NaCl maximum P (%) | DOP initial P (%) | DOP max P (%) at 200 mg |
|---|---|---|---|---|
| N95 mfr A | 0.467 | 0.763 | 1.48 | 20.8 |
| N95 mfr B | 2.43 | 2.54 | 6.22 | 18.4 |
| N95 mfr C | 2.08 | 2.11 | 5.39 | 35.5 |
| N99 mfr D | 0.188 | 0.234 | 0.758 | 2.55 |
| R95 mfr D | 0.019 | 0.019 | 0.163 | 1.03 |
| P100 mfr A | 0.002 | 0.002 | 0.000 | 0.000 |

**3M Table 2 — maximum NaCl penetration (most penetrating size range), controls vs 15 s isopropanol dip**
(same six filters, in the same row order; IPA-dipped filters were dried, then run through the NaCl test):

| Filter | control final P (%) | after IPA dip, final P (%) |
|---|---|---|
| N95 A | 0.494 | 34.8 |
| N95 B | 2.44 | 39.0 |
| N95 C | 3.10 | 42.4 |
| N99 D | 0.229 | 51.2 |
| R95 D | 0.028 | 46.8 |
| P100 A | 0.002 | 2.94 |

**Derived (my arithmetic, Table 1 maxima against Table 2 IPA values):** fraction of the electrostatic capture
lost at the NaCl penetration maximum = **11.4% (N95 A), 1.6% (N95 B), 0.5% (N95 C), 3.9% (N99 D), ~0 (R95, P100)**.
Retained fraction of −ln P at the maximum = 90.9%, 98.8%, 99.6% for N95 A/B/C.

**Mass:** not reported in the 3M summary. Under 42 CFR 84.174 the run stops at the efficiency minimum or at
200 ± 5 mg challenge, so the maximum was reached at **≤ 200 mg NaCl per filter**. Disposable half-mask media
area ≈ 170 cm² total, ≈ 120 cm² effective after the valve and face seal (see §7), so **≤ 12 g/m² (total media)
or ≤ 17 g/m² (effective)**, times the ≈95–99% capture fraction. Pressure drop change not given.

> "For all filters tested, the maximum penetration of the NaCl aerosol was less than the penetration allowed
> by the NIOSH certification test." (3M, p. 2)

---

## 2. Moyer & Bergman 2000 — intermittent NaCl loading, 5 mg a week

**Source (primary, NOT obtained):** E.S. Moyer & M.S. Bergman, "Electrostatic N-95 respirator filter media
efficiency degradation resulting from intermittent sodium chloride aerosol exposure", Appl. Occup. Environ.
Hyg. 15(8):600–608 (2000). CDC Stacks record 198430 —
<https://stacks.cdc.gov/view/cdc/198430/cdc_198430_DS1.pdf> — **blocked (403) from this network.**

**Source read (secondary, flagged):** same 3M JobHealth Highlights article, pp. 4–5, Table 3.

Method (3M p. 4): new electret N95 FFRs from three manufacturers; first a standard 200 mg NaCl run confirming
P < 5%; then separate filters loaded with **5 mg NaCl**, stored in an office for a week, re-tested with a
further 5 mg, repeated for up to 200 days. Same 42 CFR 84 conditions except pre-humidification.

**3M Table 3 — penetration (%) vs cumulative NaCl loading**

| Week | cumulative NaCl (mg) | A | B | C |
|---|---|---|---|---|
| 1 (initial) | 5 | 1.4 | 1.8 | 0.8 |
| 5 | 25 | 3.4 | 3.0 | 1.3 |
| 11 | 50 | 5.6 | 4.5 | 1.8 |
| 16 | 75 | 7.9 | 6.0 | 2.3 |
| 21 | 100 | 10.1 | 7.5 | — |
| 27 | 125 | 12.4 | 9.0 | — |

(Row/column alignment reconstructed from the pdftotext layout of 3M Table 3; the week list, the mass list and
the three penetration triplets are unambiguous but the pairing should be re-checked against the CDC PDF.)

**Derived:** on 170 cm² of media, 125 mg = **7.4 g/m²** (10.4 g/m² on 120 cm² effective). Over 5→125 mg,
mfr A rises 1.4 → 12.4%: retained fraction of −ln P = 2.088/4.269 = **48.9%**; mfr B 4.017→2.408 = **59.9%**;
mfr C (to 75 mg) 4.828→3.772 = **78.1%**. Penetration is near-linear in cumulative mass for A and B
(≈0.092 %-points per mg ⇒ ≈1.6 %-points per g/m² of media). No IPA reference in this study; using the
Martin & Moyer IPA values (≈35–42% for N95s) as the discharged state, mfr A at 125 mg has lost
(ln 0.124 − ln 0.014)/(ln 0.39 − ln 0.014) = **65%** of its electrostatic capture — against ~1–11% for
continuous loading to a larger mass.

> "It is concluded that intermittent, low-level sodium chloride aerosol loading of N-95 respirators has a
> degrading effect on filter efficiency. This reduction in filter efficiency was not accompanied by a
> significant increase in breathing resistance." (abstract, via search result; not verified in the PDF)

3M adds two observations that matter here (p. 4–5):
- "at each loading event, NaCl penetration decreased during the test... initial penetration measured during
  each loading session was higher than that measured in the previous session" — i.e. penetration falls while
  loading and rises during the week of rest;
- office-stored control filters, once put into the same intermittent scheme, showed the same rising pattern,
  so simple storage is not the cause;
- 3M's own unpublished experiment: filters intermittently loaded with **silica dust** instead of NaCl showed
  "little or no increase in test aerosol penetration over time", while an NaCl-loaded control in the same
  experiment degraded as before.
- 3M quotes R.C. Brown for the relaxation effect: "a filter loaded with NaCl then left for several hours will
  exhibit higher penetration than it did at the end of loading."

**This continuous-vs-intermittent gap is the single biggest contradiction in the pool.** Same aerosol, same
standard, similar media: ≤200 mg continuous costs ≤11% of the electrostatic capture; 125 mg in 5 mg weekly
doses costs ~65%. Per unit deposited mass the intermittent case is ~30–40× worse.

---

## 3. Wang, Ou, Pui et al. 2026 — residential MERV-13 electret, gravimetric mass axis in mg/cm²

**Source:** S. Wang, Q. Ou, X. Wang, Z. Pan, D. Park, N. Krishnakumar, Y. Hua, F.J. Romay, R.A. Juidici,
H. Chung, K. Lee, J. Hong, H. Park, D.Y.H. Pui, "Charge-driven degradation of residential electret HVAC
filters under wildfire smoke exposure", Environ. Sci. Technol., DOI 10.1021/acs.est.6c03046 (published
30 Jul 2026). Main text is bot-walled (pubs.acs.org returns a Cloudflare challenge, HTTP 403).
**Supporting Information is open** on ACS figshare and was downloaded:
<https://acs.figshare.com/articles/journal_contribution/33121135> → `dl/solid/wildfire_si.pdf`.

Media (SI Table S1): three commercial MERV-13 residential electret filters, flat during testing.
A: 0.55 ± 0.08 mm thick, fibre 17.08 ± 1.26 µm, porosity 86.69 ± 0.72%.
B: 1.17 ± 0.18 mm, 21.26 ± 2.58 µm, 78.46 ± 2.99%.
C: 3.61 ± 0.18 mm, 17.65 ± 3.05 µm, 96.75 ± 0.36%.

**SI Fig. S2 (Brand A, smouldering red-oak smoke, 700 °C furnace, 10.5 cm/s face velocity).** Read off the
figure against gridlines, ±1 percentage point and ±0.03 mg/cm²; x-axis is **loading mass in mg/cm² — multiply
by 10 for g/m²**:

| loading (mg/cm²) | g/m² | η at 300 nm (%) | η at 50 nm (%) |
|---|---|---|---|
| 0 | 0 | 65 | 57 |
| 0.26 | 2.6 | 56.5 | 52 |
| 0.41 | 4.1 | 44.5 | 50.5 |
| 0.56 | 5.6 | 25.5 | 42 |
| 0.73–0.76 | 7.3–7.6 | 17 / 14 | 34 / 31 |
| 0.94 | 9.4 | 11 | 31 |
| 1.11 | 11.1 | 6 | 26.5 |
| 1.57 | 15.7 | 3 | 18.5 |

Δp over the same range: **+1.6652 Pa per mg/cm² (R² = 0.978)**, i.e. +0.167 Pa per g/m²; equivalently
+13.495% of initial Δp per mg/cm² (R² = 0.935). Total rise over the whole run ≈ 2.3 Pa / ≈ 18%.
So the medium loses essentially all of its 300 nm capture while Δp rises by under 20% — no warning from pressure.

Derived: 50% of the clean 300 nm efficiency is reached at **≈ 5 g/m²**; at 15.7 g/m² retained fraction of
−ln P = 0.0305/1.0498 = **2.9%**.

**SI Fig. S8 (same medium grade, 300 nm, 10.5 cm/s), efficiency vs loading mass for five aerosols:**
smouldering smoke 65% → 0% by ~1.9 mg/cm² (19 g/m²); DEHS (liquid) 65 → 38.5 (0.75), 28.5 (1.15), 8 (1.65),
0 (1.9 mg/cm²); viscosity-standard oil N140 65 → 63 (1.5), 52 (2.4), 53 (5.2), 46 (6.8 mg/cm²);
oils N415 and N750 flat or rising to ~70% out to 7 mg/cm². Smoke degrades ~1.5–2× faster per unit mass than
DEHS and ~6× faster than the low-viscosity oil; the two high-viscosity oils do not degrade it at all.

The **dry-soot (flaming, solid) loading runs are in the main text, not the SI** — diffusion-flame propane soot,
lognormal mode 72 nm, GSD 1.64 (SI Fig. S12, Note/Fig. S11 give the burner). Those are the solid-particle
numbers from this group and they are behind the ACS wall.

SI Note 3 is important for the IPA baseline: "the post-IPA-treatment efficiencies of the tested filters were
consistently lower than the stabilized efficiencies observed after prolonged exposure to smoldering smoke...
the smoke-loaded filters should not be interpreted as fully discharged clean-media states." So "fraction of
electrostatic capture lost" computed against an IPA reference can exceed 100% only if deposits also change
mechanical capture — here deposits add mechanical capture, so the loaded plateau sits above the IPA floor.

SI Note 2 defines their lifetime metric: the loading at which 300 nm efficiency falls to 50% of the clean value,
chosen as an analogue of the 50% CADR decay endpoint in China GB/T 18801-2022.

---

## 4. Sun & Leung 2020 — NaCl loading of PVDF nanofibre electret; loading **rate** changes the answer

**Source:** Q. Sun & W.W.-F. Leung, "Enhanced nano-aerosol loading performance of multilayer PVDF nanofiber
electret filters", Sep. Purif. Technol. 240:116606 (2020), DOI 10.1016/j.seppur.2020.116606. Open at
<https://pmc.ncbi.nlm.nih.gov/articles/PMC7108370/> (read in full).

Media: electrospun PVDF nanofibre, mean fibre 525 nm, total basis weight 3.060 g/m² ("gsm"), corona-charged (C)
or uncharged (U); single layer (S-3.060) or four layers of 0.765 gsm (M4-0.765). Clean Δp 21–25 Pa.
Aerosol: polydisperse NaCl, Boltzmann-neutralised, loading-mode 80–90 nm, number concentration > 3.9 × 10⁵ cm⁻³
(high-rate runs). Face velocity 5.3 cm/s. Deposited mass **computed** from size distribution × efficiency ×
velocity × area, explicitly not gravimetric (they argue weighing destroys dendrites and is below balance
resolution).

Results that bear on the question:
- Uncharged single layer: efficiency rises monotonically; clogging point (Δp extrapolation) **4.31 g/m²**;
  ~100% efficiency by 6.48 g/m² (4 h). Uncharged 4-layer: clogging point **10.16 g/m²**, ~100% at 16.76 g/m² (14 h).
- Charged single layer at **high** loading rate (S-3.060-C-1): efficiency never fell measurably — the mechanical
  gain outran the charge loss. Repeat with denser sampling (C-2): efficiency did dip in the first 10 min but
  "the largest reduction in efficiency of particles was only 2.7%".
- Charged single layer at **low** loading rate (S-3.060-C-3, the only change): "After 0.25-h loading, there were
  remarkable decreases in filtration efficiency for all-sized particles... Particles of 350 nm experienced a
  reduction of 22.4% from 77.6% to 55.2%", then further 0.8–4.3 points at 0.5 h before recovering.
  Small particles barely moved ("efficiency for 50-nm particles slightly varied").
- Δp per deposited mass: 33 Pa per g/m² (charged single layer) vs 40 Pa per g/m² (uncharged) — charged media
  build a more porous cake. Second charged replicate 29 Pa/gsm.
- MPPS falls with loading for uncharged media (250 → 80 nm) — deposits add interception faster than diffusion.

**Load-bearing point:** the same medium and same aerosol give a 2.7-point dip or a 22.4-point dip depending only
on the loading concentration. Accelerated lab loading systematically understates electret degradation.
Deposited mass at the low-rate dip is not stated numerically in the text (it is on Fig. 5's x-axis); from the
companion numbers (3.82 g/m² at 28.7 Pa for C-3) it is of order 1 g/m² or less at 0.25 h.

---

## 5. Kerner et al. — NaCl ageing of ten electret media, and the IPA-discharged floor

**Ageing paper (primary, NOT obtained):** M. Kerner, K. Schmidt, S. Schumacher, C. Asbach, S. Antonyuk,
"Ageing of electret filter media due to deposition of submicron particles – experimental and numerical
investigations", Sep. Purif. Technol. 251:117299 (2020), DOI 10.1016/j.seppur.2020.117299. Paywalled
(Elsevier); no open version found (Unpaywall/Semantic Scholar return no OA PDF). Abstract, verbatim:
"The experiments revealed a decreasing filtration efficiency with increasing exposure to sodium chloride
particles. A detailed consideration of the particle size and charge distribution indicated that **charge
neutralization is the dominant effect for filter ageing in this case**."
No deposited mass is quoted in the abstract. Matt should get this one — it is the cleanest NaCl ageing dataset
in the pool and the same group's media characterisation (below) is open.

**Open companion, read in full:** M. Kerner et al., "Electret filters — from the influence of discharging
methods to optimization potential", Atmosphere 12(1):65 (2021), <https://kluedo.ub.rptu.de/files/6247/atmosphere-12-00065-v2.pdf>
(`dl/solid/atmos_kerner2021.pdf`). Also the FILTECH 2020 paper with the same tables:
<https://exhibitors.filtech.de/media/g08-01_-_kerner_-_technische_universitaet_kaiserslautern_-_germany.pdf>.

Media (Table 1/2 — basis weight, permeability at 200 Pa, porosity, thickness, mean fibre diameter):
1 corona PP 133 g/m², 2527 L m⁻² s⁻¹, 77.2%, 647 µm, 31.8 µm;
2 PP meltblown 51 g/m², 101, 87.3%, 447 µm, 1.9/1.5 µm;
3 corona PP meltblown 152 g/m², 705, 79.4%, 847 µm, 14.4/13.7 µm;
4 polyamide nanofibre on spunbond 108 g/m², 895, 86.7%, 934 µm, 0.1 µm nanofibre layer;
5 corona PP meltblown on PET 114 g/m², 712, 85.8%, 655 µm, 3.4/28.9 µm;
6 PP spunbond 153 g/m², 444, 92.6%, 2377 µm, 15.6/17.1 µm;
7–10 triboelectric polymer blends 56/67/99/149 g/m², 4473/4407/3105/1889, 95–96%, 1.6–3.3 mm, ~18–19 µm.

Test aerosol NaCl from a Collison nebuliser, diffusion-dried, neutralised (TSI 3012A), 14–500 nm, mode 35 nm,
10⁶ cm⁻³, SMPS up/downstream.

**Table 2 (FILTECH) / Table 3 (Atmosphere) — efficiency at 300 nm, untreated vs discharged.** This is the
IPA-discharged floor for nine of the media:

| medium | 1 | 2 | 3 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| untreated | 0.77 | 1.00 | 0.97 | 0.97 | 0.85 | 0.93 | 0.90 | 0.97 | 0.99 |
| 5 min liquid IPA (EN 779) | 0.26 | 0.95 | 0.36 | 0.47 | 0.67 | 0.11 | 0.19 | 0.19 | 0.43 |
| 24 h liquid IPA | 0.13 | 0.87 | — | 0.35 | 0.55 | 0.09 | — | — | 0.35 |
| 24 h IPA vapour (ISO 16890-4) | 0.13 | 0.80 | — | 0.21 | 0.42 | 0.13 | — | — | 0.10 |

Caveat the group raises itself: liquid-IPA immersion under-discharges low-permeability (small-pore) media
because air is not displaced from the pores; for medium 4 the liquid treatment also changed the structure.
So "IPA-discharged" is not one number — the choice of EN 779 vs ISO 16890-4 moves the floor by up to a factor
of 4 in efficiency (e.g. medium 10, 0.43 → 0.10).

Related thesis, likely to contain the whole NaCl ageing dataset in German: M. Kerner, "Abscheidung submikroner
Aerosolpartikeln in elektrostatisch ausgerüsteten Vliesstoffen — experimentelle und numerische Untersuchungen",
RPTU Kaiserslautern, defended 9 Dec 2021 (<https://mv.rptu.de/en/dpts/mvt/news/detail/news/promotionsvortrag-von-maximilian-kerner>).
The KLUEDO repository search is behind an Anubis proof-of-work gate, so I could not locate its record;
**direct file URLs on kluedo.ub.rptu.de do work** (the Atmosphere PDF above came from there), so if Matt finds
the docId the PDF is one fetch away.

---

## 6. Composition and conditions: what the (walled) HVAC literature claims

- **Cai, Lu & Zhang 2021**, "Mechanisms of performance degradation and efficiency improvement of electret
  filters during neutral particle loading", Powder Technol. 383:1–? DOI 10.1016/j.powtec.2020.12.061.
  Simulation (immersed boundary–lattice Boltzmann) with explicit fibre-charge decay by gas neutralisation and
  by conduction through the deposit. Abstract, verbatim: "**With the same loaded mass, carbon particles with
  higher conductivity cause more charge decay and efficiency degradation than NaCl and Al2O3 particles.
  The fiber charge is mainly lost through conduction, and gas neutralization becomes important only for
  high-resistivity materials.**" Paywalled; no OA copy found. Ranking at equal mass: carbon > NaCl > Al₂O₃.
- **Wang, Lin & Zhang 2020**, "Comparison of effects of particle charging, media characteristics, humidity and
  aerosols on loading performance of electret media", Build. Environ. 179:106962,
  DOI 10.1016/j.buildenv.2020.106962. Experiment: medium-efficiency electret media loaded with **neutralised
  KCl at low RH** as the baseline, then conditions varied. Abstract, verbatim: "1) Particle composition had the
  most remarkable effect on the loading performance; 2) RH produced a larger effect on the loading behavior
  than medium characteristics if it could affect the surface morphology of the particles. Otherwise, medium
  characteristics had a more significant impact; 3) Particle charging had a minimum influence when compared to
  other factors." Paywalled — **this is the single most on-point ranked comparison I found and Matt should get it.**
- **Zhou, Zhang, Yuan, Lin, Zhang & Wang 2026**, "The variation of the most penetrating particle size of electret
  filter media during usage under different humidity levels", Build. Environ. 288:114017,
  DOI 10.1016/j.buildenv.2025.114017. KCl and Al₂O₃ loading at 30/50/70/80% RH. Secondary report of its result
  (search summary, NOT verified against the paper): at **≈9 g/m² loading the dendrites restore mechanical
  capture and the MPPS shifts to 284.1 nm with efficiency rebounding**. Paywalled. Flagged as unverified.
- **Wu, Cai & Zhang 2022**, "Modeling and prediction of loading characteristics of electret filter media for
  PM2.5", Build. Environ. 207:108554. Model with charge screening + conduction-driven decay + humidity-dependent
  deposit morphology, no fitted parameters. Paywalled.
- **Tang, Thompson, Chang, Chen & Pui 2018**, "Filtration efficiency and loading characteristics of PM2.5
  through commercial electret filter media", Sep. Purif. Technol. 195:101–109, DOI 10.1016/j.seppur.2017.11.067.
  Paywalled (publisher has suppressed the abstract). Companion: Tang et al. 2018, Build. Environ. 141:206–214,
  "Evaluation of different discharging methods on HVAC electret filter media".
- **Tien, Chen, Li, Li, Zheng, Peng, Zhou, Tsai & Chen 2020**, "Experimental and theoretical analysis of loading
  characteristics of different electret media...", Sep. Purif. Technol. 233:116002. Abstract gives the useful
  general result: "the charges of electret media did enhance the holding capacity. The decline of efficiency was
  found to closely relate to the holding capacity of each media. **Higher capacity resulted in a higher decline
  of efficiency.**" Best composite reached 14.1 g m⁻² holding capacity at 1 in-H₂O. Paywalled.
- **Ji, Bae, Kang & Hwang 2003**, J. Aerosol Sci. 34:1493–1504 (electret cabin filter). Paywalled; the Korean
  predecessor (Trans. KSME B 26(8):1102–1114, 2002) states: "Smaller particles loaded in electret fibers cause a
  more rapid degradation in collection efficiency and have lower minimum efficiency with time. The pressure drop
  of a filter media do rarely increase when the collection efficiency decreases to the minimum value."
  (secondary, from the Korean abstract). Also: liquid DOS gave much lower steady-state efficiency than solid NaCl.

---

## 7. Standards: how much solid mass the certification tests actually put on

- **42 CFR 84.174** (non-powered N/R/P filters), read from eCFR: N-series challenged with solid NaCl, **CMD
  0.075 ± 0.020 µm, GSD ≤ 1.86**, Boltzmann-neutralised, 25 ± 5 °C, RH 30 ± 10%, concentration ≤ 200 mg/m³,
  85 ± 4 L/min single filter (42.5 L/min in pairs). "The test will continue **until minimum efficiency is
  achieved or until an aerosol mass of at least 200 ± 5 mg has contacted the filter**." Note *contacted*, i.e.
  challenge mass, not deposited mass.
- **42 CFR 84.180** (PAPR100-N/P): identical 200 ± 5 mg challenge at 85 L/min, with 25 h at 38 °C / 85% RH
  pre-conditioning before the test.
- Media-area conversion. Best-anchored figure: a 3M 1860 half-face respirator has a filter area of **150 cm²**,
  giving a mask-averaged face velocity of **~9.3 cm/s at the NIOSH 85 L/min** (Kähler & Hain, arXiv:2006.02470,
  <https://arxiv.org/pdf/2006.02470>). A second, unpinned search result quotes "about 170 cm²" of media reduced
  to "about 120 cm²" effective by the exhalation valve and face seal — needs a source before use.
  So **200 mg over 150 cm² = 13.3 g/m²** (range 11.8–16.7 g/m² over 170–120 cm²), and the 125 mg of the
  intermittent study = **8.3 g/m²** (7.4–10.4 g/m²). Flat-sheet rigs are typically 100 cm² (confirmed for
  ATI 100X and Palas MFP 3000; **the TSI 8130A datasheet does not state its holder area** — I checked it),
  which would make 200 mg = 20 g/m².
- **ASHRAE 52.2 Appendix J** (ANSI/ASHRAE Addendum b to 52.2-2007, free PDF:
  <https://www.ashrae.org/File%20Library/Technical%20Resources/Standards%20and%20Guidelines/Standards%20Addenda/52_2_2007_Supplement_FINAL.pdf>):
  conditioning aerosol is **solid-phase KCl** from a Laskin generator fed with 1.00 g KCl per 1.00 L water.
  Incremental steps of CT ≥ 6.4 × 10⁷ particles cm⁻³ min; stop when efficiency stops dropping or at a cumulative
  **CT of 1.2 × 10⁹ particles cm⁻³ min**. RH must stay below 65% "to prevent deliquescence of the KCl".
  Replaces the old non-mandatory 30 g dust conditioning load.
  Rough conversion (mine, assumption-heavy): particles per unit media area = CT × media velocity. At a media
  velocity of 20 cm/s (1200 cm/min) the ceiling CT gives 1.4 × 10¹² particles cm⁻²; with a Laskin KCl
  distribution of CMD ≈ 0.05 µm, GSD ≈ 1.8, mean particle mass ≈ 6 × 10⁻¹⁶ g, that is ≈ 0.9 mg cm⁻² challenged
  ⇒ **order 4–9 g/m² deposited**. Both the size distribution and the media velocity are assumed, so treat this
  as an order-of-magnitude bracket only — but it lands in the same 5–10 g/m² band as everything else here.

---

## 8. Modelling of solid dust loading (for the functional form)

- **Sae-lim, Tanthapanichakoon & Kanaoka 2005**, "Structural improvement to quadruple service life of a
  high-efficiency electret filter", Sci. Technol. Adv. Mater. 6:307–311, open copy at
  <https://www.nstda.or.th/openarchive/wp-content/uploads/tainacan-items/2494/117745/Structural-improvement-to-quadruple-service-life-of-a-high-efficiency-electret-filter.pdf>
  (read in full). Their fitted form for a dust-loaded electret fibre, from their own earlier experiments
  (Sae-lim et al., RSCE Bangkok 2004, ref [16] — conference paper, not located):
  η = η₀E(1 + λE m) + η₀M(1 + λM m), with **λE = β ln m + γ** — the electrical single-fibre efficiency changes
  as a **logarithmic** function of dust load m, while the mechanical part is linear in m.
  Dust load m is per unit **filter volume** (kg/m³), so multiply by thickness for g/m² (their 3 mm filter:
  1 kg/m³ = 3 g/m²). Simulation conditions: α = 0.04, 20 µm electret fibres, 1 µm particles, 0.1 m/s,
  fibre charge 1.2 × 10⁻⁴ C/m². Penetration peaks early (max ≈ 2–4%) then falls to zero at clogging; the
  uniform-packing filter clogs at 60 kg/m³ ≈ 180 g/m², the graded one at ~4× that.
  This is a simulation; the underlying experiments are Kanaoka/Emi-group work that I did not obtain.
- Walsh & Stenhouse's own series is the primary experimental body for solid loading and remains the gap here:
  1996 Part. Part. Syst. Charact. 13:63–?; 1997 J. Aerosol Sci. 28(2):307–321 (particle size, charge and
  composition — DOI 10.1016/S0021-8502(96)00434-X, closed); 1997 Powder Technol. 93:63–75 (pressure drop only);
  **1998 Aerosol Sci. Technol. 29:419–432, DOI 10.1080/02786829808965580 — Unpaywall reports this one as
  BRONZE open access at <https://www.tandfonline.com/doi/pdf/10.1080/02786829808965580?needAccess=true>**;
  I was blocked from fetching it here (bot wall) but Matt should be able to download it free.
  Thesis: D.C. Walsh, "The behaviour of electrically active and prefilter fibrous filters under solid aerosol
  load", PhD, Loughborough University of Technology, 1995 — not found online; Loughborough's repository search
  returned nothing and figshare has no record.

---

## 9. Not pursued / handed to other pools

- Otani, Emi & Mori 1993 (KONA) — assigned to the liquid pool.
- Zhang et al. 2020, "Research on loading filtration performances of electret polypropylene melt blown
  nonwovens", J. Nantong Univ. (Nat. Sci.) 19(3):61–67, DOI 10.12194/j.ntu.20191018003 — bilingual CN/EN,
  DOAJ-listed, full text only on CNKI. Abstract (verbatim, from the DOAJ record): "the efficiency of electret
  melt-blown nonwoven initially presents a decreasing trend, and **reaches the lowest value of 98.04% after
  8 minutes**, followed by an increase and reaches a constant value after loading 29 minutes. Meanwhile, the
  pressure drop increases gradually." Tested on a TSI 8130. If the holder is 100 cm² and the 8130 runs the
  standard NaCl challenge, 8 min at 85 L/min and ~18 mg/m³ ⇒ order 1 g/m² at the minimum. Flagged for the
  non-English pool.
- Bioaerosol loading of electret media: **not found.** Every search phrasing combining micro-organisms with
  filter loading was refused by the search tool's summariser, and Crossref title searches returned nothing on
  point. Gap.

## 10. Sources that matter and are walled from this network

Network notes: **the whole of cdc.gov is blocked from here** — stacks.cdc.gov, www.cdc.gov/niosh and
NIOSHTIC-2 all return HTTP 403 from the Akamai edge, so every NIOSH primary document is out of reach.
pubs.acs.org, tandfonline.com, aaqr.org, mdpi.com, conservancy.umn.edu and kluedo's search are behind
Cloudflare/Anubis bot walls. Direct static-file URLs on kluedo.ub.rptu.de, ashrae.org, nstda.or.th,
figshare/ndownloader, pmc.ncbi.nlm.nih.gov, jstage and multimedia.3m.com all worked.


| Source | Link | Why it matters |
|---|---|---|
| Martin & Moyer 2000 | https://stacks.cdc.gov/view/cdc/198418/cdc_198418_DS1.pdf | the continuous-NaCl + IPA dataset of §1, primary |
| Moyer & Bergman 2000 | https://stacks.cdc.gov/view/cdc/198430/cdc_198430_DS1.pdf | the intermittent dataset of §2, primary |
| Walsh & Stenhouse 1998 | https://www.tandfonline.com/doi/pdf/10.1080/02786829808965580?needAccess=true | bronze OA; the empirical max-penetration equation |
| Walsh & Stenhouse 1997 | doi:10.1016/S0021-8502(96)00434-X | particle size / charge / composition scaling |
| Kerner et al. 2020 | doi:10.1016/j.seppur.2020.117299 | cleanest NaCl ageing series, charge-resolved |
| Wang, Lin & Zhang 2020 | doi:10.1016/j.buildenv.2020.106962 | ranked comparison: composition > RH > media > particle charge |
| Zhou et al. 2026 | doi:10.1016/j.buildenv.2025.114017 | KCl + Al₂O₃ at four RHs, MPPS shift, g/m² axis |
| Cai, Lu & Zhang 2021 | doi:10.1016/j.powtec.2020.12.061 | conduction mechanism, carbon vs NaCl vs Al₂O₃ |
| Tang et al. 2018 | doi:10.1016/j.seppur.2017.11.067 | PM2.5 loading of commercial electret HVAC media |
| Wang/Ou/Pui 2026 main text | doi:10.1021/acs.est.6c03046 | the dry-soot (solid) loading curves; SI already in hand |
| Ji et al. 2003 | doi:10.1016/S0021-8502(03)00103-4 | loading particle size effect, solid vs liquid |
