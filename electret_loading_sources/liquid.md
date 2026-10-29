# Pool: liquid, oily and combustion aerosol loading of electret media

Conventions. P = penetration. "Retained −lnP" = ln P_loaded / ln P_initial (1 = no loss, 0 = filter passes everything). "Electrostatic part lost" = (ln P_loaded − ln P_initial)/(ln P_discharged − ln P_initial), only where a discharged/uncharged reference exists. QF = −ln P / Δp in kPa⁻¹ at the stated velocity. "Read off Fig. N" = digitised by eye from a rendered page unless stated; precision given.

---

## 1. Otani, Emi & Mori 1993 — DOS droplets vs iron-alum solids, fine-fibre electret

Source: Otani Y, Emi H, Mori J (1993) "Initial collection efficiency of electret filter and its durability for solid and liquid particles", KONA Powder Part J 11:207–214 (translated from Kagaku Kogaku Ronbunshu). Open: https://www.jstage.jst.go.jp/article/kona/11/0/11_1993023/_article/-char/en (PDF read in full; Figs 10–13 rendered at 2.5x and read).

Media: electret filter, polymer and charging method NOT stated. d_f = 1.3 µm, L = 0.71 mm, α = 0.0612 (all from figure legends). Basis weight not stated; = α·L·ρ ≈ 39 g/m² if PP (ρ 900), ≈ 52 g/m² if PC — not given, my arithmetic. Electret charge back-fitted as σ = 5.1 µC/m² from the same clean-filter data (back-fitted, not measured — p. 211).

Loading aerosols: 0.1 µm DOS (dioctyl sebacate, liquid) and 0.1 µm iron alum (solid), DMA-classified, either neutralised ("uncharged") or singly charged ("uni-charged"). Inlet concentration 3e-9 – 2e-8 kg/m³ (3–20 µg/m³) for uncharged droplets, "5e-3 [sic, presumably 5e-9] – 6e-8 kg/m³" for charged droplets (Fig. 12 caption). Velocity u = 0.05 m/s (Figs 10, 12, 13; Fig. 11 velocity not printed — same rig, assume 0.05). Duration up to ~800 h (Fig. 12 top axis). RH/T for loading not stated.

Mass: x-axes of Figs 11–12 are challenge mass per filter face area C_i·u·t in kg/m² (×10³ → g/m²). Fig. 13 uses deposited mass per filter VOLUME m = (1/L)∫E d(C_i u t) [kg/m³] (Eq. 14); per face area = m × L = m × 0.71 mm. Since this is a single flat sheet, face area = media area.

Efficiency test: same 0.1 µm aerosol as loading (in-situ penetration), count by CNC presumably (not stated in loading section).

Series (read off figures, precision ±0.1 decade on P, ±0.03 g/m² on x):
- Fig. 11, charged 0.1 µm DOS droplets: P ≈ 4e-3 at 0 → ~2e-2 at 0.3 g/m² → ~6e-2 at 0.6 → ~2e-1 at 1.15 g/m² challenge. Δp flat ≈ 33 Pa. Retained −lnP at 1.15 g/m² ≈ ln0.2/ln0.004 = 0.29.
- Fig. 11, charged 0.1 µm iron alum (solid): P ≈ 1.5e-3 → 1e-4 at 1.1 g/m² (efficiency RISES); Δp 33 → ~100 Pa. NB text on p. 212 says solid "penetration ... gradually increases" and liquid "decreases" — contradicts its own figure (translation slip; the figure and the explanation that follows both say droplets degrade and solids build dendrites).
- Fig. 12, NEUTRAL 0.1 µm DOS: P ≈ 0.22 at 0 → ≈ 0.45 by ~0.6 g/m² challenge, then flat. Δp ≈ 34 Pa constant.
- Fig. 12, uni-charged 0.1 µm DOS: P ≈ 6e-3 → 1e-2 (0.3 g/m²) → 0.1 (~0.85 g/m²) → 0.2–0.3 (1.2–1.5 g/m²).
- Fig. 13 (single-fibre efficiency η vs deposited m): neutral droplets η ≈ 0.028 → equals the uncharged-fibre value (≈ 0.019, dashed line) "at about m = 0.5 kg/m³" (verbatim, p. 213) = 0.5 × 0.71e-3 = **0.36 g/m² deposited**. Charged droplets η ≈ 0.12 → 0.045 by m ≈ 1.4 kg/m³ (≈ 1.0 g/m² deposited).
- Check: P = exp(−4αLη/(π(1−α)d_f)) = exp(−45η) → η 0.028 → P 0.28; η 0.019 → P 0.43. Consistent with Fig. 12.

Degradation (neutral 0.1 µm DOS): electrostatic part lost = 100% at ~0.36 g/m² deposited; retained −lnP ≈ ln0.43/ln0.25 ≈ 0.61 (here the electret only added ~45% to η for neutral 0.1 µm, so the absolute loss is small). QF clean ≈ −ln(0.25)/0.034 kPa ≈ 41 kPa⁻¹ at 5 cm/s, 0.1 µm neutral DOS; loaded ≈ 25 kPa⁻¹ (my arithmetic, Δp read off Fig. 12).

Humidity: Fig. 10 — no change in P (0.1 µm uni-charged DOS, 5 cm/s) over 800 h of particle-free air at 20% and 90% RH.

Mechanism (verbatim, p. 213): "the covering of the fiber surface with a liquid layer is the main cause of penetration increase even for charged droplets." Conclusion: "Since the covering of the electret fiber surface with a liquid layer is dependent on the wetting property of the liquid, special attention is required in the electret filtration of organic droplets."

Caveat: the uncharged-fibre comparison filter is "an uncharged filter having the same filter property" (p. 210), not the same sheet discharged.

---

## 2. Heo, Lee, Doh & Jung 2022 — cigarette smoke on electret meltblown (the "92.5% → 33%" number)

ATTRIBUTION CORRECTION: the brief credits "~2 g/m² of cigarette smoke took an electret 92.5% → 33%" to https://pmc.ncbi.nlm.nih.gov/articles/PMC8694494/. That PMC article is Eun, Lee & Jeon 2021, "Regeneration of an electret filter by contact electrification", RSC Adv 11:4610 — Arizona dust and E. coli, no smoke, no 92.5% (checked full text). The number is from:

Source: Heo KJ, Lee GD, Doh SJ, Jung JH (2022) "Effect of cigarette smoke on the lifetime of electret air filters", Sci Total Environ 807(Pt 1):150754, doi:10.1016/j.scitotenv.2021.150754 (PubMed 34619223; not OA per OpenAlex; ScienceDirect-walled — Matt to download: https://doi.org/10.1016/j.scitotenv.2021.150754).

What the abstract says (verbatim, read from PubMed XML): "After loading up to 204 μg/cm2 of cigarette smoke on 100 cm2 of electret filter medium, the filtration efficiency of some filters decreased from 92.5% to 33.3% (-Δ59.2%)." and "we founded no changes in pressure drop following cigarette smoke exposure despite the reduction in filtration efficiency" and "standard test particles of a similar loading weight did not affect filtration efficiency."
- 204 µg/cm² = 2.04 g/m² of media (flat 100 cm² sheet, so media = face area).
- Retained −lnP = ln(0.667)/ln(0.075) = 0.405/2.59 = 0.16 (i.e. 84% of the log-removal gone at ~2 g/m²).
- UNVERIFIED (abstract only): test particle size/method, media basis weight, loading velocity, whether 204 µg/cm² is measured gravimetrically, and which "some filters". Need full text.

---

## X. Cross-pool find (ambient, not my pool): Raynor & Chae 2004 DID weigh their filters

Source: Raynor PC, Chae SJ (2004) J Occup Environ Hyg 1:463–471, doi:10.1080/15459620490467783. Full text read via CDC Stacks copy (https://stacks.cdc.gov/view/cdc/188464). p. 465–466 "Filter Mass Measurements" and Results: "the four glass fiber filters ... gained an average of 341 g (0.75 lb) while the four polyolefin fiber filters gained an average of 227 g (0.50 lb). These loadings are equivalent to 73 g/m2 for the glass fiber filters and 49 g/m2 for the polyolefin fiber filters." Media area 4.65 m² per 2×2 ft filter (15 pleats, 28 cm deep × 54 cm). Weighing precision 56.8 g (0.125 lb) → ±12 g/m². Mass is end-of-test (134 days). Face velocity 565–748 ft/min at 80–100% fan (Table I) → ~2.9–3.8 m/s face, ≈ 0.23–0.30 m/s through media (my arithmetic: face 0.372 m², media 4.65 m²). Efficiency minimum for ≥0.58 µm at weeks 10–12, 0.29 µm at ~13 weeks, 0.15 µm at ~15 weeks (p. 469); 0.3 µm fell "to as low as 45%". Δp_norm polyolefin rose 42% over test. If mass accrued linearly, the minimum came at roughly 49 × (10–15)/19 ≈ 26–39 g/m² (my estimate, assumes constant intake concentration). Literature cited there that is in MY pool: Tennal et al. 1991 (oil aerosol on electret, Particul Sci Technol 9:19) and Schürmann & Fissan 1984 (J Aerosol Sci 15:317).

---

## 3. Tombolini, Listrani, Campopiano & Plebani 2016 — 500 mg paraffin oil on an FFP2, with IPA reference

Source: Tombolini F, Listrani S, Campopiano A, Plebani C (2016) "Evaluation of performance loss of paraffin oil loaded filtering facepieces", Ind Health 54(5):403–409, doi:10.2486/indhealth.2015-0227. Open: https://pmc.ncbi.nlm.nih.gov/articles/PMC5054281/ ; PDF read in full from https://www.jniosh.johas.go.jp/en/indu_hel/doc/IH_54_5_403.pdf ; Fig. 3 rendered and digitised (crop at ~247 px/decade; reading precision ±0.02 decade).

Media: Mandil FFP2 NR (D.P.I. Sekur), no valve, EN 149. Electret middle layer: t = 636 ± 9 µm, α = 0.031 ± 0.002 (manufacturer), geometric mean fibre diameter 1.8 µm (SEM, 200 fibres). Polymer, charging method, basis weight NOT given (if PP: α·t·ρ ≈ 18 g/m² — my arithmetic). **Filter area NOT given** → the brief's "~30 g/m²" is an assumed ~170 cm² facepiece area, not a number in the paper. Flag.

Loading: polydisperse paraffin oil (WOP 40 PB, Merkur), Lorenz AGW/BM VI generator, AP2E photometer, "conform to the European Standard EN 13274-7:2008" (size details deferred to their ref. 12 = Plebani et al. 2012 JOEH 9:556). 500 mg per facepiece; "took about four hours in the IPA untreated facepieces" (p. 404) — consistent with EN 13274-7's ~20 mg/m³ at 95 L/min (500 mg/(20 mg/m³ × 0.095 m³/min) ≈ 4.4 h, my check). Mass is the nominal loaded amount (photometer-controlled), not weighed. RH/T not given.

Test: monodisperse DEHS 0.03–0.40 µm, neutralised (TSI 3160) or singly charged (Lorenz), count-based, 95 ± 1 L/min (face velocity unknowable without area; ~9 cm/s if 170 cm²). IPA treatment: 60 min dip, 24 h air dry.

Δp (Table 1, 95 L/min): 139 Pa clean → 142 Pa after 500 mg (untreated); IPA 139/137 → 141/142 Pa. Essentially unchanged.

Penetration, neutralised DEHS, read off Fig. 3b (untreated) and 3d (IPA-treated), %:
| d (µm) | N0 clean | N500 | N0_IPA | N500_IPA |
|---|---|---|---|---|
| 0.03 | 2.8 | 3.4 | 5.2 | 6.5 |
| 0.05 | 3.8 | 5.5 | 13 | 16 |
| 0.07 | 3.5 | 5.6 | 18 | 25 |
| 0.10 | 2.1 | 4.1 | 30 | 38 |
| 0.15 | 1.2 | 2.8 | 35 | 43 |
| 0.20 | 0.82 | 2.2 | 37.5 | 47 |
| 0.30 | 0.44 | 1.4 | 38 | 47.5 |
| 0.40 | 0.23 | 0.78 | 36 | 43 |
(Singly charged, Fig. 3a: S0 0.40% → S500 1.3% at 0.3 µm; 0.03 µm not measurable, <1e-5 %.)

Derived (my arithmetic from the readings):
- 0.3 µm: retained −lnP = ln(0.014)/ln(0.0044) = 0.78. Electrostatic part lost vs clean IPA = (5.42−4.26)/(5.42−0.97) = 0.26.
- 0.1 µm: retained −lnP = 0.83; electrostatic part lost = 0.25.
- 0.4 µm: retained −lnP = 0.80; electrostatic part lost = 0.24.
- QF (0.3 µm neutral): 39 kPa⁻¹ clean → 30 kPa⁻¹ loaded, at 95 L/min.
- Penetration rose ×3.2 at 0.3 µm (0.44 → 1.4%) — well short of the IPA level (38–48%). After 500 mg the filter is nowhere near discharged.
- The oil ALSO raised penetration through the IPA-discharged facepiece (0.3 µm: 38 → 47.5%). So oil loading does not add mechanical capture here; if anything it reduces it (or screens residual charge — authors note residual Coulomb capture after IPA).

Authors' own number (p. 407–408, verbatim): "the mean ratio between ECou0 and ECou500 for d < 0.15 µm is 1.14 ± 0.07 while the mean ratio between Epol0 and Epol500 for d > 0.15 µm is 1.120 ± 0.004. These results highlight that both Coulomb and polarization efficiency are attenuated by loading 500 mg of paraffin oil of about 12% and 11%, respectively." CONTRADICTION: recomputing their Eq. 7 ratio from their own Fig. 3b/3d readings gives Epol0/Epol500 ≈ 1.27 (0.2 µm) – 1.29 (0.3 µm), i.e. ~21–23% attenuation, not 11%. They say only one of three trials is shown; Fig. 4 may average differently. Treat "12%" as the paper's claim and ~25% of the electrostatic log-term as what the plotted trial shows.

Scale context (p. 404): workplace oil mist 0.07–4 mg/m³ (10 mg/m³ unventilated) at 38.5 L/min → 1.3–185 mg per 8-h shift; 500 mg exceeds a shift.

---

## 4. Rengasamy, Miller, Vo & Eimer 2013 — DOP loading of N95 vs P100 FFRs (NIOSH)

Source: Rengasamy S, Miller A, Vo E, Eimer BC (2013) "Filter performance degradation of electrostatic N95 and P100 filtering facepiece respirators by dioctyl phthalate aerosol loading", J Eng Fibers Fabrics 8(3):62–69. Full text read (CDC Stacks copy https://stacks.cdc.gov/view/cdc/195150 ; Figs 1 and 3 rendered at 3x and read, ±0.05 decade).

Media: 2 N95 and 2 P100 FFR models (unnamed), no valves. Area, basis weight, fibre diameter NOT given. Table I: N95 middle layers hydrophobic, inner hydrophilic; P100-A outer+middle hydrophobic; P100-B all three hydrophobic.

Loading: TSI 8130, polydisperse DOP, CMD 185 ± 20 nm, GSD < 1.60 (NIOSH R/P aerosol), 85 L/min, 10/30/50/100/200 mg per FFR; mass from calibrated time × concentration (concentration found by weighing a 102 mm glass filter after 40 min at 30 L/min — "divided by 1.2 [m³]"; loading linear in time, verified). Mass per FFR, not per m²; FFR area NOT given — per 100 cm² of media: 200 mg = 20 g/m²; for a typical ~150–200 cm² FFR, 200 mg ≈ 10–13 g/m² (my assumption, flagged).

Test: TSI 8130 photometric (mass-weighted light scattering) — DOP (CMD 185 nm) and NaCl (CMD 75 nm, GSD < 1.86); also TSI 3160 monodisperse NaCl 20–400 nm (count). 85 L/min.

Fig. 1 (N95, polydisperse, %), read off bar tops:
| DOP load (mg) | 0 | 10 | 30 | 50 | 100 | 200 |
|---|---|---|---|---|---|---|
| N95-A, DOP test | 0.85 | 1.4 | 1.7 | 2.4 | 4.1 | 13 |
| N95-A, NaCl test | 0.16 | 0.44 | 0.60 | 1.15 | 2.1 | 8.7 |
| N95-B, DOP test | 1.0 | 1.5 | 1.9 | 2.65 | 5.5 | 18 |
| N95-B, NaCl test | 0.18 | 0.44 | 0.60 | 1.15 | 2.0 | 8.5 |
Text (p. 64): "DOP aerosol penetration exceeded NIOSH allowed maximum penetration (5%) at 100 and 200 mg DOP loads."
Retained −lnP (DOP test): N95-A 0.90 (10 mg), 0.78 (50), 0.67 (100), 0.43 (200 mg); N95-B 0.91, 0.79, 0.63, 0.38. NaCl test N95-A: 0.85 (10 mg) → 0.38 (200 mg). Degradation roughly linear in log P with mass, no sign of saturation by 200 mg. No IPA reference in this paper.
Fig. 2 (monodisperse NaCl, N95): MPPS ~40 nm clean, shifting larger with load; N95-A at 300 nm: ~0.01% (control) → ~3.5% (200 mg).

Fig. 3 (P100): DOP-test penetration ≈ 3e-4 – 1e-3 % (P100-A) and 6e-3 – 1e-2 % (P100-B), flat from 0 to 200 mg — "no filter degradation". BUT P100-B NaCl-test penetration jumped from ~0.003% (0 mg) to ~0.5% at 10 and 30 mg DOP and 0.14% at 50 mg, then back to ~0.0015% at 100–200 mg (authors: NaCl test after small DOP loads degrades the charge; at higher DOP loads "DOP ... may form a heavy coat"). Odd, unexplained, two models only.

Cited but not obtained (in my pool): Romay FJ & Liu BYH (1998) "Degradation of electret filters during DOP loading", Adv Filtr Sep Technol 12:193–200 (AFS proceedings) — per Rengasamy p. 67: penetration measured during DOP loading of several electret media and one mechanical medium "up to 5 mg/cm2" [= 50 g/m²]; "filter degradation occurred in two regimes, with an initial fast period followed by a slow second phase"; another group of electrets "behaved like mechanical filters, with a single slow degradation regime". Also Lifshutz N (1997) "Performance decay in synthetic electret filter media", Adv Filtr Sep Technol (AFS 1997) 307–311. Both are AFS conference papers — not found online yet.

---

## 5. Plebani, Listrani & Di Luigi 2010 — 8 h paraffin oil (EN 143 aerosol) on FFP1/2/3 and a glass P2

Source: Plebani C, Listrani S, Di Luigi M (2010) "Facciali filtranti: effetto dell'accumulo di aerosol oleoso sulla penetrazione attraverso il materiale filtrante" [Filtering facepieces: effect of oily aerosol load on penetration through the filtering material], Med Lav 101(4):293–302. Open PDF read in full (Italian): https://mattioli1885journals.com/index.php/lamedicinadellavoro/article/download/212/179/214

Media: 3 samples each of FFP1, FFP2, FFP3, "same manufacturer and same model [line]" (unnamed), electret, single-shift use. Area, basis weight, fibre size NOT given. Comparison: one EN 143 P2 cartridge filter of uncharged glass fibre with binder.

Loading aerosol (p. 295): paraffin oil WOP 40 PB, Lorenz AGW/BM VI atomiser + separator, "diametro mediano in massa di 0,47 µm e deviazione standard geometrica di 1,82" (MMD 0.47 µm, GSD 1.82); "poco più del 5% della massa" in particles > 1 µm (p. 299). Concentration 18.4 ± 0.5 mg/m³ (photometer, gravimetrically checked), 95.0 ± 0.5 L/min, 480 min continuous → "834 mg" exposure; authors treat exposure ≈ deposit since efficiency ≥ ~90% throughout (p. 296). Charge state of the aerosol not characterised (they say no data exist for atomised paraffin oil). RH/T not given.

Test: same aerosol, photometric (AP2E, 45° scatter at 670 nm) i.e. MASS-weighted penetration, every second, at 95 L/min.

Table 1 (initial → final after 834 mg, %):
| | n1* | n2 | n3 | EN max |
|---|---|---|---|---|
| FFP1 | 2.7 → 9.7 | 2.0 → 10.1 | 2.5 → 11.2 | 20 |
| FFP2 | 0.59 → 3.23 | 0.41 → 2.79 | 0.50 → 2.23 | 6 |
| FFP3 | 0.014 → 0.97 | 0.017 → 1.02 | 0.021 → 0.90 | 1 |
| P2 glass | 0.32 → 0.32 (unchanged throughout) | | | |
Table 2 Δp at 95 L/min (mbar): FFP1 0.93/0.96/1.03 → 0.95/0.98/1.06; FFP2 1.37/1.40/1.29 → 1.48/1.52/1.42; FFP3 1.74/1.66/1.82 → 2.01/1.90/2.04; P2 glass 2.16 → 4.41.
Shape (p. 296–298): P rose linearly with mass for FFP1 (R² 0.998) and FFP2 (R² 0.990); for FFP3, log P linear in mass (R² 0.994). Max penetration at the end (834 mg) — no plateau within 8 h. Only one FFP3 exceeded its class limit, in the last 3 min.

Derived (my arithmetic): retained −lnP after 834 mg: FFP1 0.65 (n1); FFP2 0.67/0.65/0.72; FFP3 0.52/0.53/0.56. QF FFP2 n1: 37 → 23 kPa⁻¹; glass P2: 27 → 13 kPa⁻¹ (all on 0.47 µm MMD paraffin oil, photometric, 95 L/min; face velocity unknown). Per area: NOT given; per 100 cm² of media 834 mg = 83 g/m²; for a ~150–200 cm² cup, ~40–55 g/m² (my assumption).
Note the contrast: the glass filter keeps its efficiency but doubles Δp; the electrets keep Δp but lose efficiency.

---

## 6. Plebani, Listrani, Tranfo & Tombolini 2012 — paraffin oil time series on FFP2 with IPA reference (abstract only; walled)

Source: J Occup Environ Hyg 9(9):556–561, doi:10.1080/15459624.2012.709433 (PubMed 22862434). Walled (tandfonline) — Matt to download: https://doi.org/10.1080/15459624.2012.709433
Abstract (PubMed XML, verbatim parts): FFP2 exposed 8 h at 95.0 ± 0.5 L/min to polydisperse paraffin oil at 20.0 ± 0.5 mg/m³ (→ ~910 mg nominal, my arithmetic); monodisperse neutralised DEHS 0.03–0.40 µm measured at 0, 1, 4, 8 h; IPA-treated unloaded facepieces as discharged reference. "Penetration value measured after 8 hr for 0.03-μm particles was on average 1.6 times the initial value, whereas it was about 8 times for 0.40-μm particles." MPPS 0.05 µm at start shifted slightly larger; IPA-treated MPPS 0.30 µm. Area not in abstract. Full text needed for the actual P values and 1/4 h points.

---

## 7. Shirman, Zamani & Liu 2025 — pine-needle smoke on 17 HVAC media (arXiv preprint; journal version Urban Sci 2026)

Source: Shirman T, Zamani H, Liu S (Metalmark Innovations) "Wildfire Smoke: A Rigorous Challenge for HVAC Air Filters", arXiv:2505.01622 (2025), https://arxiv.org/pdf/2505.01622 — read in full; Table 1 (p. 8) and Fig. 1 (p. 7) rendered. Journal version: "When Smoke Enters the City: Challenges for HVAC Filters in Resilient Buildings", Urban Sci 2026, 10(2):99, doi:10.3390/urbansci10020099 (MDPI; Akamai-blocked to curl). Earlier: Shirman T, Shirman E, Liu S (2023) Atmosphere 14:1729 (MERV 11 charged vs glass, PN smoke) — not yet read.

Media: 17 flat media from 4 makers, MERV 10–15: charged polymer (electret), uncharged polymer, fibreglass. Specs in SI Table S1 (not in preprint text). ~5 cm² exposed circles.
Loading aerosol: pine-needle smoke (125 mg needles burnt into a chamber), ~400,000 #/cm³, "~1500 µg/m³" (Table 1 caption; text says "g/m³" — typo), unimodal 50–400 nm, median ~160 nm, nothing > 400 nm. 24–28 °C, 45–65% RH. Charge state not measured (they note smoke carries charge). Composition: >90% organic per their intro (literature, not measured).
Velocity: 10 L/min through ~5 cm² ≈ 33 cm/s (~6× the 52.2 media velocity they quote, 5.32 cm/s). Duration: efficiency after ~5 (initial), 20 and 80 min of continuous deposition.
Test: SMPS count efficiency averaged over 116, 154, 205, 274, 365 nm bins (caption says 50–300 nm range).
Mass: NOT measured. My estimate: challenge = 1.5 mg/m³ × 0.33 m/s × t = 0.59 g/m² at 20 min, 2.4 g/m² at 80 min (if chamber concentration stayed ~1500 µg/m³; they say stable ~1 h). Deposited ≈ challenge × mean efficiency → roughly 0.2–0.3 g/m² at 20 min and 0.5–0.8 g/m² at 80 min for the charged media. Order-of-magnitude estimate only.

Table 1 (initial → 80 min efficiency %, Δp Pa initial → 80 min):
| Media | MERV | FE initial | FE 80 min | Δp | retained −lnP (mine) |
|---|---|---|---|---|---|
| Charged A | 11 | 17.5 | 10.5 | 15 → 15 | 0.58 |
| Charged A | 13 | 53.3 | 18.1 | 29 → 31 | 0.26 |
| Charged B | 10 | 20.8 | 12.5 | 12 → 13 | 0.57 |
| Charged B | 11 | 23.1 | 10.9 | 12 → 12 | 0.44 |
| Charged B | 12 | 33.3 | 16.3 | 30 → 29 | 0.44 |
| Charged B | 13-nano | 15.8 | 9.0 | 8 → 9 | 0.55 |
| Charged C | 11 | 37.5 | 19.7 | 47 → 48 | 0.47 |
| Charged C | 13 | 62.9 | 17.8 | 47 → 47 | 0.20 |
| Charged C | 15 | 74.8 | 20.6 | 66 → 70 | 0.17 |
| Uncharged polymer D | 11 / 13 / 14 | 22 / 32.2 / 54.7 | 19.7 / 27.7 / 48.1 | 93→96 / 158→181 / 259→345 | 0.88 / 0.84 / 0.83 |
| Glass A | 11 / 13 | 30.8 / 37.2 | 29.6 / 35.2 | 92→100 / 125→139 | ~0.95 |
| Glass D | 11 / 13 / 14 | 14.6 / 32.4 / 53.5 | 13.9 / 34.7 / 51.8 | 40→43 / 103→116 / 184→221 | ~1.0 |
Fig. 1: at 20 min the charged media had already lost a large part (e.g. C13 62.9 → ~43%, C15 74.8 → ~58%, A13 53 → ~36%; read off bars ±2%).
Key quotes: "charged media's smoke removal efficiency dropped below 20% quickly" and "higher MERV grades correlate with faster efficiency decay" (p. 8–11). SEM: "droplet-like deposits resembling a 'beads on a string' morphology" after 80 min, film-like coatings early; more coverage on charged media (p. 9).
Note: the 80-min charged values (9–21%) converge regardless of initial MERV — consistent with loss down to roughly the mechanical floor, but no IPA test was done to confirm.
Cites Holder, Halliday & Virtaranta 2022 (Indoor Air 32:e13163): "the CADR of air cleaners with charged filters dropped by 95% with only a 7% increase in pressure after just 10 mg of pine needle (PN) smoke deposition" — to verify in the original.

---

## 8. Holder, Halliday & Virtaranta 2022 — box fan + 1" MERV 13 electret, pine-straw smoke loaded (US EPA)

Source: Holder AL, Halliday HS, Virtaranta L (2022) "Impact of do-it-yourself air cleaner design on the reduction of simulated wildfire smoke in a controlled chamber environment", Indoor Air 32:e13163, doi:10.1111/ina.13163. Open: https://pmc.ncbi.nlm.nih.gov/articles/PMC9828579/ (full text read; §2 Methods "Filter loading" and §3.6 "Filter condition").

Media: 1" MERV 13 furnace filters "with electrostatic media (electret filters) from a single manufacturer" (unnamed), 20" box fan. Media area NOT given (my estimate for a 20×20×1 pleated filter: ~0.4–0.7 m²).
Loading: EPA Open Burn Test Facility "filled with smoke from small batches of pine straw and three air cleaners were operated simultaneously ... The process was repeated until the air cleaners ceased to reduce smoke concentrations in the chamber." Mass by pre/post weighing on an Ohaus Scout balance. So the loading end-point is FAILURE, not a dose chosen in advance. Size/concentration of the loading smoke not given (chamber CADR tests used tube-furnace pine-needle smoke, flaming+smouldering mix).
Results (§3.6, verbatim): "The CADR for the smoke loaded filter was 4.3 ± 0.9 CFM and repeated with a second smoke loaded filter (CADR = 9.7 CFM) ... The smoke loaded filters had only 10.0 ± 1.1 mg of smoke deposited ... the pressure drop across the filter was only slightly higher (0.29 ± 0.01 in H2O at 819 CFM) than the clean filter (0.27 ± 0.01 in of H2O at 819 CFM)." Clean baseline CADR 79.7–111.2 CFM depending on fan speed. Dust-loaded comparison (ASHRAE 52.2 dust, 53 ± 4 g, 2 in H₂O): CADR 22.9 ± 0.8 CFM — "five times higher CADR compared to the smoke loaded filters, despite having three orders of magnitude greater mass loading."
Derived: CADR down ~96% (111 → 4.3). 10 mg over ~0.4–0.7 m² ≈ 0.015–0.025 g/m² (my estimate; area assumed).
FLAGS: (1) a Scout-series balance reads to 1–10 mg at best and most models with enough capacity for a 20×20×1 filter read to 0.01–0.1 g, so "10.0 ± 1.1 mg" is at or below the likely weighing resolution — treat the mass as very uncertain (my inference; model not stated). (2) Authors' mechanism (charge build-up repelling charged smoke) is a hypothesis, untested. (3) They cite IPA restoring effectiveness — their ref. 36 = Schumacher S et al. 2018 Chem Eng Technol 41:27 "Performance of new and artificially aged electret filters in indoor air cleaners"; cigarette smoke loss ref. 35 = Schumacher et al. 2022 Atmosphere 13:1538.

---

## 9. Martin, Moyer & Jensen 2006 — DOP on an electrostatic HEPA PAPR filter (3M AS-140), with MEDIA AREA, charged vs neutralised, continuous vs intermittent

Source: Martin S, Moyer E, Jensen P (2006) "Powered, air-purifying particulate respirator filter penetration by a DOP aerosol", J Occup Environ Hyg 3:620–630, doi:10.1080/15459620600953995. Full text read (CDC Stacks https://stacks.cdc.gov/view/cdc/191412). Tables I–IV and text pp. 622–628.

Media: 3M AS-140 electrostatic high-efficiency PAPR filter (user instructions: not for oil). "Approximate Surface Area" 754 cm² ("Calculated from actual filter measurements", Table I note E). Tested at 225 L/min (max of TSI 8122) → 4.97 cm/s media velocity (Table I). Comparators: four mechanical (glass) PAPR HEPA filters at 1.25–1.36 cm/s.
Loading = test aerosol: TSI 8122 DOP, CMD 0.185 ± 0.020 µm, GSD ≤ 1.60, "mass median diameter (MMD) of 0.36 µm ± 0.04 µm" (p. 623); either as generated ("charged") or neutralised. Concentration gravimetric (two 1-h samples daily); loads are cumulative challenge mass (≈ deposited, P < 20%). Photometric (forward light scattering) penetration, every ~10 min.

Continuous loading (Table IV), 5 filters each; per-area conversion uses 754 cm² (2000 mg = 26.5 g/m²; 3900 mg = 52 g/m²):
| | P initial % | P at 2000 mg (26.5 g/m²) % | P max % | total load at stop mg |
|---|---|---|---|---|
| Charged DOP #1–5 | 0.017–0.023 | 0.854, 0.384, 0.254, 0.651, 0.468 | 6.63, 11.10, 8.64, 12.24, 10.09 (mean 9.74) | 3100–4300 (mean 3900 = 52 g/m²) |
| Neutralised DOP #1–5 | 0.017–0.027 | 1.206, 1.202, 1.662, 1.548, 1.865 | 18.14, 6.72, 8.32, 11.01, 10.44 (mean 10.9) | 3000–4200 (mean 3300 = 44 g/m²) |
Retained −lnP (my arithmetic): at 26.5 g/m² charged 0.56–0.70, neutralised 0.47–0.51; at P ≈ 10% (≈ 44–52 g/m²) ≈ 0.27. No plateau — tests were stopped at ~10% penetration.
Mechanical glass PAPR filters: stayed < 0.03% until ~8,600–33,000 mg DOP per filter (oil dripping from saturated media); no charge-state effect.

Intermittent loading (p. 626–628), 4 filters per condition, daily loads for 4 days, 3-day sealed storage, then 5 min (~60 mg) on Day 5. Max penetration per day (%):
| Daily load | Day 2 | Day 3 | Day 4 | Day 5 (after 3-day rest) |
|---|---|---|---|---|
| 200 mg/day charged | — | 0.080–0.154 (600 mg) | 0.352–0.708 (800 mg) | 0.957–1.76 (~860 mg = 11.4 g/m²) |
| 200 mg/day neutralised | — | 0.113–0.258 | 0.646–1.27 | 1.94–3.21 |
| 400 mg/day charged | 0.061–0.126 (800 mg) | 0.600–1.190 (1200 mg) | 2.78–4.41 (1600 mg = 21 g/m²) | 7.77–9.89 (~1660 mg = 22 g/m²) |
| 400 mg/day neutralised | 0.137–0.172 | 1.09–1.85 | 5.04–8.08 | 10.74–14.08 |
| 100 mg/day | Day 5: charged 0.105–0.518; neutralised 0.327–0.556 (~460 mg = 6 g/m²) | | | |
KEY TIME EFFECT (my comparison of their numbers): intermittent 400 mg/day reached 2.8–4.4% at 1600 mg and 7.8–9.9% after a 3-day rest at ~1660 mg, whereas continuous loading gave only 0.25–0.85% at 2000 mg. Penetration also jumped across the 3-day storage with only ~60 mg added (200 mg/day: 0.35–0.71% → 0.96–1.76%). Degradation per gram is several-fold worse when loading is spread out in time, and continues during storage — i.e. part of the loss is a slow process after deposition (oil spreading / charge decay), not just the mass. Directly relevant to slow real-world loading.
Charge state: neutralised DOP degraded faster than as-generated (charged) DOP; difference significant from ~3400 mg (continuous) or from Day 2–3 (intermittent).
Quote (p. 628): "The effectiveness of the static charge to aid in filtration was greatly affected by aerosol charge and aerosol loading rate."
Leads cited there: Blackford, Bostock, Brown et al. 1986 (4th World Filtration Congress, 7.27–7.33); Fissan, Neumann & Schürmann 1984 (Aerosols, Elsevier, 581–584: DOP on polycarbonate electret); Larson 1999 PhD, Colorado State (asphalt fume on electrostatic respirators); Berardinelli et al. 2001 AIHce abstract (N/R/P filters vs diesel exhaust).

---

## 10. Roh, Kim & Kim 2019 — DOP loading of corona PP meltblown vs electrospun PS, with a FLUORINATED (C4F8 PECVD) variant — open-literature fluorochemical effect

Source: Roh S, Kim S, Kim J (2019) "Facile functionalization via plasma-enhanced chemical vapor deposition for the effective filtration of oily aerosol", Polymers 11(9):1490. Open: https://pmc.ncbi.nlm.nih.gov/articles/PMC6780184/ (full text read; Tables 1, 2, 4, 5; Fig. 5 image read, 756×420 px, ±3% P, ±5 mg).

Media (Table 1): PP MB corona-charged electret (KITECH) 30 ± 2 g/m², 0.32 mm, EFD 5.1 µm, surface potential −3.5 kV; PS electrospun (ES) 14 g/m², 0.13 mm, EFD 3.7 µm, +3.7 kV; PS_f ES (C4F8 PECVD, fluorinated) 13 g/m², EFD 3.5 µm, −3.9 kV, DOP contact angle 149° vs 0° for all others (Table 2); PS_O2 ES (O2 plasma, charge mostly lost, +1.2 kV) 10 g/m². Single layer between spunbond scrims.
Loading = test: TSI 8130 DOP, CMD ~0.185 µm, neutralised, 28.3 L/min over 40 cm² = 11.8 cm/s, to 200 mg challenged (= 50 g/m² challenge); also NaCl to 40 mg. Photometric. Mass is CHALLENGE mass, not deposited.
Table 5 (DOP): initial → at 200 mg penetration %: PP MB 37.6 → 75.8; PS ES 29.9 → 77.0; PS_f ES 37.1 → 73.0; PS_O2 ES 57.6 → 75.3. Initial resistance 5.4/4.8/5.3/6.6 mmH2O (PS ES/O2/f/PP MB); DOP loading left resistance unchanged (Fig. 4b).
Fig. 5b read-off (penetration vs DOP challenge, 1 mg = 0.25 g/m² challenge):
- PS ES: 30% → ~65% within ~5–10 mg (1.3–2.5 g/m² challenge), ~70% by 40 mg.
- PP MB: 38% → ~55% at ~12 mg (3 g/m²), ~65% at ~30 mg, ~70% at ~45 mg.
- PS_f ES (fluorinated): 37% → dips to ~35% at 5–10 mg, ~40% at 30 mg, ~50% at 50 mg, ~60% at 80 mg, ~65% at 100 mg, 73% at 200 mg.
- PS_O2 ES (weakly charged): 58% → ~68% at 20 mg → 75% at 200 mg.
Derived: half of the eventual rise is reached at ~3 mg (PS ES), ~12 mg (PP MB) and ~60 mg (PS_f ES) of DOP challenge → fluorination delays degradation ~5× vs the corona PP and ~20× vs the same untreated web, but at 200 mg (50 g/m² challenge) all four end at 73–77% — the oleophobic surface postpones, it does not prevent. Deposited mass at PP MB's half-rise ≈ 3 g/m² challenge × ~0.5 capture ≈ 1.5 g/m² (my estimate). Retained −lnP at 200 mg: PP MB ln0.758/ln0.376 = 0.28; PS_f ES 0.32.
Saturation: all webs, including the O2-plasma one, converge to ~75% — ABOVE the weakly charged web's own initial 58%. Oil loading here costs more than the electrostatic part (or the O2 web's residual 1.2 kV is also screened). Same pattern as Tombolini's IPA-treated FFP2 (oil raised P of the discharged facepiece 38 → 48%).
Quote: "As DOP penetration keeps increasing until 200 mg of loading, the maximum penetration was observed until 200 mg of DOP aerosol was challenged."

---

## 11. Lehtimäki 1996, Nordtest NT TR 320 — DIESEL FUME and SIDESTREAM CIGARETTE SMOKE on two EU7 electret bag-filter media, in g/m², with IPA reference and diesel+dust mixtures (KEY SOURCE)

Source: Lehtimäki M (1996) "Development of test methods for electret filters", Nordtest Technical Report NT TR 320 (VTT, project 1164-94), 57 pp. Open PDF (scanned, no text layer): http://nordtest.info/images/documents/nt-technical-reports/NT%20TR%20320_Development%20of%20test%20methods%20for%20electret%20filters_Nordtest%20Technical%20Report.pdf (landing page https://www.nordtest.info/wp/1996/03/06/development-of-test-methods-for-electret-filters-nt-tr-320). Pages rendered and read; the loading curves digitised from 2× renders (precision ±2 efficiency points, ±0.1 g/m²). This is the fuller report behind Lehtimäki & Heinonen 1994 (Build Environ 29:353, walled) and Indoor Air '93 vol 6 pp 463–468.

Media (§2.5, Table 2.1): two commercial EU7 electret pocket (bag) filters. "A": electret layer of "relatively coarse fibers (approximately 15 ... 20 µm in diameter)"; full-size unit 4 bags, 2.8 m², 0.94 m³/s → 0.33 m/s through media. "B": "flat fibers (approximately 5 x 15 µm)"; 8 bags, 5.6 m², 1.18 m³/s → 0.21 m/s. Polymer, charging method, basis weight NOT given. Samples Ø150/200 mm cut from bags, tested at the nominal media velocity. B samples inhomogeneous (Fig. 2.5: 42–64% at 0.15 µm); A homogeneous (~80% at 0.15 µm).
Efficiency test: neutralised polydisperse KCl, optical particle sizer 0.12–5 µm (PSL-equivalent), count; single-size index 0.4 µm.
Loading metric (§2.2, Eq. 4): m/A = mass FED per filter area = v_f·c_m·t, c_m gravimetric upstream. Verbatim: "It must be emphasized that Δmi or Δmi/A does not correspond to the amount of particles collected by the filter." So all g/m² below are CHALLENGE mass per media area; deposited ≈ challenge × (1 − P), roughly 0.3–0.8 × here.
Aerosols (§2.4, Figs 4.3, 4.8, low-pressure impactor): diesel fume from a Yanmar L40E-D single-cylinder engine (0.199 L) loaded to ~850 W; mass distribution peaks in the 0.12 and 0.21 µm stages (~33% and ~36% of mass), ~14% at 0.38 µm → MMD ≈ 0.2 µm. Sidestream cigarette smoke from freely burning cigarettes: ~34% (0.12 µm stage) and ~41% (0.21 µm stage), ~10% at 0.38 µm → MMD ≈ 0.2 µm. RH/T and charge state of loading aerosols not stated.

IPA reference (§4.1, Figs 4.1–4.2; immersion in technical IPA, 24 h dry): A at 0.4 µm 89% → ~16% (±3; scatter 12–20%); at 0.15 µm ~83% → ~13%. B at 0.4 µm ~72% → ~40% (different B sample from the loading tests).

Diesel fume, 0.4 µm efficiency vs m/A (Fig. 4.5, A; Fig. 4.7, B):
| A: g/m² | 0 | 1.5 | 3.1 | 5.3 | 7.4 | 10.6 |
|---|---|---|---|---|---|---|
| eff % | 89.5 | 67 | 54 | 21 | 19.5 | 20 |
| B: g/m² | 0 | 0.93 | 2.0 | 3.4 | 4.8 | 6.9 |
| eff % | 57 | 29 | 29 | 31 | 32 | 36 |
Size-resolved after loading: A at 10.6 g/m² ~80% → ~15% at 0.15 µm (Fig. 4.4); B at 6.9 g/m² ~45% → ~20% at 0.15 µm (Fig. 4.6).
Text p. 17 (verbatim): "the amount of diesel fume aerosol necessary to remove the electrostatic removal mechanism is approximately 6 g/m² (filter "A") and 1 g/m² (filter "B"). It is worth mentioning that these loading levels did not cause any increase in the pressure drop of the filters."

Sidestream cigarette smoke, 0.4 µm efficiency vs m/A (Fig. 4.10, A; Fig. 4.12, B):
| A: g/m² | 0 | 0.9 | 2.7 | 4.4 | 8.0 | 12.0 |
|---|---|---|---|---|---|---|
| eff % | 90 | 87.5 | 76 | 63 | 41 | 24 |
| B: g/m² | 0 | 0.6 | 1.7 | 2.9 | 5.2 | 7.5 |
| eff % | 69 | 49 | 41 | 41 | 42 | 42.5 |
Size-resolved: A at 12 g/m² ~82% → ~25% at 0.15 µm (Fig. 4.9); B at 7.5 g/m² ~55% → ~30% (Fig. 4.11).
Text p. 17: "the amount of cigarette smoke needed to remove the electrostatic filtration effect is approximately 12 g/m² (filter "A") and 2 g/m² (filter "B"). These values are somewhat higher than in the case of diesel fume aerosol. These loading level were high enough to cause a slight increase in the pressure drop."

Derived for A (0.4 µm; P_IPA = 0.84; my arithmetic):
- Diesel: retained −lnP 0.50 (1.5 g/m²), 0.34 (3.1), 0.10 (5.3), 0.10 (10.6). Electrostatic part lost 55% (1.5), 71% (3.1), 97% (5.3) — saturates at ≈ the IPA level (20% vs IPA ~16%), does not go below it.
- Cigarette: retained −lnP 0.89 (0.9), 0.62 (2.7), 0.43 (4.4), 0.23 (8.0), 0.12 (12.0). Electrostatic part lost 12%, 41%, 62%, 84%, 96%. Roughly linear in mass at ~8%/g·m⁻² until near-complete at 12 g/m².
- So per gram, diesel fume (soot-rich) was ~2× as damaging as sidestream cigarette smoke (tar/liquid-rich) of the same ~0.2 µm MMD on A, and ~2× on B (1 vs 2 g/m²).
For B: cigarette plateau 41–42% ≈ IPA level (40%). Diesel took B to 29% at 0.93 g/m² — BELOW the 40% IPA value measured on another B sample — then efficiency recovered slowly (36% at 6.9 g/m²) as deposits added mechanical capture. B sample-to-sample spread (Fig. 2.5) is large enough that "below IPA" is not proven.
A vs B: 6× difference in the mass needed (6 vs 1 g/m² diesel; 12 vs 2 cigarette) between two EU7 media — coarse round 15–20 µm fibres at 0.33 m/s vs flat 5×15 µm fibres at 0.21 m/s; basis weights not given, so cannot normalise by fibre surface. B starts with less electrostatic enhancement (57–69% vs 90%).

Diesel + coarse dust mixtures (§5.2; PTI Fine test dust, MMD ~5 µm, plus diesel fume; "10/90" = 10% fine/diesel : 90% dust by mass — Fig. 5.12 shows ~9% of mass below 0.4 µm; "35/65" etc.). No pre-filter. Loading also expressed as c·t (µg/m³·year); for A 1 µg/m³·yr = 10.4 g/m² (0.33 m/s × 3.156e7 s), checked against Fig. 5.29.
- A, "35/65" (Fig. 5.29, 0.4 µm): 88% (0) → 69 (3.3 g/m²) → 53 (6.6) → 34 (10.5) → 26 (23, minimum; = ~8 g/m² of diesel) → 30 (42) → 36 (58) → 43 (78 g/m²). Δp (Fig. 5.28 legend): 88 → 92 → 93 → 97 → 101 → 110 → 122 → 139 Pa.
- B, "35/65" (Fig. 5.31): 77% → 61 (2.1) → 52 (4.3, minimum) → 54 (6.8) → 63 (14.8) → 73 (27) → 83 (38) → 87 (51 g/m²); Δp 141 → 150 → 157 → 165 → 195 → 254 → 333 → 461 Pa.
- A, all mixtures (Fig. 5.32, read ±3 points): PTI Fine alone dips only to ~80% (from 88) at ~60 g/m² then rises (Fig. 5.9); "10/90" minimum ~72% at ~70 g/m²; "15/85" ~50% at ~40–80 g/m²; "25/75" ~30% at ~45 g/m²; "35/65" ~26% at ~23 g/m². Max penetration at 0.4 µm rose ×6 for A and ×2 for B (p. 43, verbatim: "The particle penetration can increase as much as by a factor of 6 in the case of filter "A" and by a factor of 2 in the case of filter "B"").
- Reading: the electret loss tracks the DIESEL mass (~4–8 g/m² of diesel to reach the trough on A whatever the mix), while the co-deposited coarse dust rebuilds mechanical efficiency and Δp; the depth of the trough is set by the fine-combustion fraction. Conclusion (p. 44, verbatim): "Increasing the amount of diesel fume led to faster and stronger decrease in the efficiency."

Ambient comparison in the same report (cross-pool, §3.2, Figs 3.6–3.9): half-size A and B behind EU3 pre-filters, suburban Tampere, 4 months, mean ~10 µg/m³ → ~50 g fed per filter ≈ 36 g/m² (A) and 18 g/m² (B) challenge; A at 0.15 µm ~80% → ~15% (i.e. ≈ IPA level); B ~63% → ~22%. Short 24-day ambient exposure on samples: 4.4 g/m² (A) 80% → ~50% at 0.15 µm; 2.8 g/m² (B) ~46% → ~30%. Standard ASHRAE-dust tests on full units showed no decrease (A) or an increase (B) (Figs 3.2–3.5).

---

## 12. Ji, Bae, Kang & Hwang 2003 — liquid DOS vs solid NaCl on cabin-air electret media (abstract; full text walled)

Source: J Aerosol Sci 34(11):1493–1504, doi:10.1016/S0021-8502(03)00103-4 (walled, ScienceDirect). Abstract read on the KIST repository: https://pubs.kist.re.kr/handle/201004/138133 . Korean-language precursor: Trans KSME B 26(8):1102 (2002), doi:10.3795/KSME-B.2002.26.8.1102, PDF on KoreaScience (JAKO200211921125101).
Abstract (verbatim): "Polydisperse solid NaCl particles with 0.1%, and 1% solutions or liquid dicotyl sebacate (DOS) particles were generated from an atomizer, and they were loaded on the filter media ... The collection efficiency of the electret filter media degraded as more particles were loaded, and showed minimum efficiency at steady state ... At steady state, the filter media loaded with smaller NaCl particles showed lower collection efficiency. The filter media loaded with liquid DOS particles showed collection efficiency much lower than those loaded with solid NaCl particles." Two particle charge states: spray-electrified (as atomised) vs neutralised; highly charged particles were captured more efficiently during the transient. No g/m² in the abstract.

## 13. Walled or abstract-only sources in my pool that matter (Matt to download)

- Barrett LW, Rousseau AD (1998) "Aerosol loading performance of electret filter media", Am Ind Hyg Assoc J 59:532–539, https://doi.org/10.1080/15428119891010703 (3M; flat-sheet electret media vs glass, NaCl and DOP). Only a secondary description was available (Martin et al. 2006, p. 621): "Against a DOP aerosol, a high level of electrostatic charge leads to improved initial efficiency but a more rapid increase in penetration with increased aerosol loading"; Martin quotes B&R p. 538: "the oily liquid aerosol droplets can spread over fiber surfaces, reducing the filtration enhancement from electrostatic charge, resulting in increasing penetration as a function of loading" and "the user may have no warning as the filter efficiency decreases." No loading masses seen. HIGH PRIORITY.
- Tennal KB, Mazumder MK, Siag A, Reddy RN (1991) "Effect of loading with an oil aerosol on the collection efficiency of an electret filter", Particul Sci Technol 9:19–29, https://doi.org/10.1080/02726359108906574 . Spun-fibre electret; monodisperse bis(2-ethylhexyl) sebacate droplets, equilibrium-charged and uncharged. UNVERIFIED (seen only as a search-engine summary of the Scilit abstract; Scilit and T&F block access): for 1 µm droplets with equilibrium charge the model predicted complete discharge at roughly 200 g/m², but the experiment needed only about 0.3 g/m². Per Rengasamy et al. 2013 (p. 64): charged and neutral BES gave "similar increases in filter penetration" and "electrostatic filter degradation by liquid aerosols was not due to direct neutralization of the charge on the fibers by the net charge of test particles. Oil aerosol was believed to discharge the fibers by ionic conduction through an oil film on the fibers." HIGH PRIORITY.
- Brown RC, Wake D, Gray R, Blackford DB, Bostock GJ (1988) "Effect of industrial aerosols on the performance of electrically charged filter material", Ann Occup Hyg 32:271–294, https://doi.org/10.1093/annhyg/32.3.271 (OUP, Cloudflare-blocked; WebFetch refused). Field exposures of resin-wool and other electret materials at foundries, lead smelting, coking (coal-tar fume) etc. Abstract content seen only via a search summary (unverified): dry dusts reduced performance slightly; foundry aerosols were more damaging to all filter types; coal-tar fume affected some; different materials degraded at roughly the same rate, attributed to charge screening. Companion: Blackford, Bostock, Brown et al. 1986, 4th World Filtration Congress, Ostend, pp. 7.27–7.33.
- Lehtimäki M, Heinonen K (1994) "Reliability of electret filters", Build Environ 29:353–355, https://doi.org/10.1016/0360-1323(94)90033-7 — its data are in the open NT TR 320 (entry 11).
- Heo KJ et al. (2022) Sci Total Environ 807:150754 (entry 2) — https://doi.org/10.1016/j.scitotenv.2021.150754 . Need test particle size, media, mass method.
- Wang S, Ou Q, Wang X, Pan Z, Park D, Krishnakumar N, Hua Y, Romay FJ, Juidici RA, Chung H, Lee K, Hong J, Park H, Pui DYH (2026) "Charge-driven degradation of residential electret HVAC filters under wildfire smoke exposure", Environ Sci Technol 60(38):27316–27331, https://doi.org/10.1021/acs.est.6c03046 (ACS returns 403; abstract says "© 2026 The Authors", so probably open on ACS, not yet in PMC). Abstract (PubMed and Semantic Scholar, verbatim parts): lab flaming and smouldering wood smoke, prescribed-burn field sampling and "controlled soot particle challenges"; "filtration efficiency can collapse rapidly at particle loadings far below those associated with appreciable pressure drop increases. This behavior is driven primarily by soot-rich particles, which induce rapid and irreversible neutralization of electret charge rather than by progressive mechanical clogging or organic aerosol deposition alone"; modelled "effective filter lifetime during wildfire episodes can be reduced from months to days". No numbers in the abstract. HIGHEST PRIORITY in this pool (UMN Center for Filtration Research with LG; residential electret HVAC media; separates soot from organic aerosol).
- Schumacher S, Spiegelhoff D, Schneiderwind U, Finger H, Asbach C (2018) "Performance of new and artificially aged electret filters in indoor air cleaners", Chem Eng Technol 41:27–34, https://doi.org/10.1002/ceat.201700105 (Wiley). Content unseen.
- Hayashi T, Kitagawa Y (Toyobo) (2017) "Improvement of durability of electret filter for tobacco smoke", J Soc Powder Technol Japan 54(6):406–409, https://doi.org/10.4164/sptj.54.406 (J-STAGE subscription). Abstract (CiNii, verbatim): "Electret filters severely lose electrostatically enhanced particle collection efficiency when they are exposed to tobacco smoke. Tobacco smoke particles consist mainly of liquid substances at room temperature. Thus, captured tobacco smoke particles spread over an electret fiber and seriously weaken an electrical field around it. We have developed a novel surface modification treatment to avoid the spreads of tobacco smoke particles on the fiber ... the surface modification was effective also for many kinds of liquid particles such as oil mist." No numbers in the abstract.
- Plebani et al. 2012 JOEH 9:556 (entry 6), https://doi.org/10.1080/15459624.2012.709433 .
- Penconek A, Drążyk P, Moskal A (2013) "Penetration of diesel exhaust particles through commercially available dust half masks", Ann Occup Hyg 57:360–373, https://doi.org/10.1093/annhyg/mes074 . Abstract: FFP2 filtered 84–89% and FFP3 only 75–86% of DEP mass from three fuels in 80-min tests; Δp stayed acceptable; most penetrating DEP 30–300 nm. Whether penetration rose over time is not in the abstract.
- Not found online (book chapters / AFS proceedings): Kanaoka C, Emi H, Ishiguro T (1984) "Time dependency of collection performance of electret filters", in Aerosols (Liu, Pui, Fissan eds), Elsevier, 613–616; Fissan HJ, Neumann S, Schürmann G (1984) "Electrostatic enhanced filtration", same volume, 581–584 (DOP on polycarbonate electret); Schürmann G, Fissan HJ (1984) J Aerosol Sci 15:317–320 (oil on electrostatically spun fibre filter); Romay FJ, Liu BYH (1998) "Degradation of electret filters during DOP loading", Adv Filtr Sep Technol 12:193–200 (loaded to 5 mg/cm² = 50 g/m²; two-regime degradation per Rengasamy 2013); Lifshutz N (1997) "Performance decay in synthetic electret filter media", Adv Filtr Sep Technol 307–311; Larson DL (1999) PhD thesis, Colorado State (asphalt fume on electrostatic respirators); Berardinelli S et al. (2001) AIHce abstract (N/R/P filters vs diesel exhaust).
- Springer chapter (ISHVAC 2019 proceedings) "Comparisons of the different discharge performances and the effect of long-term loading with the liquid aerosol on electret media", https://doi.org/10.1007/978-981-13-9520-8_81 — walled; content unseen.

## 14. Cross-pool notes picked up on the way (not my pool)

- Kerner M et al. (2020) Sep Purif Technol 251:117299 — NaCl ageing of electret media; abstract: charge neutralisation dominant for NaCl. Walled.
- Hanley JT, Ensor DS, Foarde KK, Sparks LE (1999) Indoor Air '99 (open: http://www.aivc.org/sites/default/files/members_area/medias/pdf/Conf/1999/paper097.pdf): electrodynamically spun rigid-cell, corona pleated-panel and split-fibre residential filters; ambient and in-home exposures all lost efficiency substantially over 2–12 weeks; ASHRAE-dust conditioning (incl. carbon black) mostly raised efficiency; only submicron KCl came close (and still underestimated). No masses.
- Küpper M et al. (2019) Aerosol Air Qual Res 19:1655 (open via Springer PDF): purifier CADR with new vs IPA-"aged" electret filter ~165–172 → 64–77 m³/h; cigarette smoke used only as a CADR aerosol (no loading).
- NT TR 320 ambient data (entry 11): 4 months of suburban air ≈ 36 g/m² challenge took EU7 electret A to ≈ the IPA level at 0.15–0.4 µm.
- Raynor & Chae 2004 masses (entry X).
---

## 15. Ji, Kang, Hwang & Bae 2002 (Korean precursor of Ji et al. 2003) — DOS droplets on a cabin-air electret, time series

Source: 지준호, 강석훈, 황정호, 배귀남 (Ji JH, Kang SH, Hwang J, Bae GN) (2002) "Effect of particle loading on the collection performance of an electret cabin air filter for submicron particles", Trans Korean Soc Mech Eng B 26(8):1102–1114, doi:10.3795/KSME-B.2002.26.8.1102. Open scanned PDF: https://www.koreascience.kr/article/JAKO200211921125101.pdf (Korean; English abstract; figures read from renders, ±0.02 efficiency).
Media (p. 1107, my reading of the Korean): two-layer cabin-air filter media, polyester pre-layer ~35 µm fibres and polypropylene main electret layer ~10 µm fibres (charging described as electrostatic spinning — my translation, not certain). Face velocity fixed at 8.4 cm/s (Δp 1.9 mmH2O at that velocity).
Aerosols (Table 1): NaCl from 0.1% (GMD 0.05 µm, GSD 1.67) and 1% solutions (0.07 µm, 1.9); DOS 100% (GMD 0.25 µm, GSD 1.7), neutralised; upstream 1e5–1e6 #/cm³. Count efficiency by SMPS/CPC.
DOS result (Fig. 12, p. 1112): overall efficiency 0.75 at t = 0 → ~0.4 at 10 min → ~0.25 at 20 min → ~0.15 at 30 min → 0.12 at 45 min. Text (my translation): efficiency fell below 10% after about 40 min while Δp had risen only ~10% over its initial value; the DOS film on the fibres "easily reduces the charge held by the electret fibres". Fig. 13 (after charge depletion): DOS-loaded media 5–12% at 0.1–0.3 µm (minimum ~5% near 0.15 µm), vs 20–25% (NaCl 0.1%) and 36–45% (NaCl 1%); the authors say the DOS result matches their fully discharged media. English abstract: "For DOS particles it is shown that the charging level of an electret filter severely decreases and the collection efficiency is below 10% in some particle size range."
Mass: NOT reported for DOS (M_L in g/m² is given only for NaCl, Fig. 11, up to ~0.6 g/m²). My order-of-magnitude estimate from Table 1 conditions: 1e5–1e6 #/cm³ of 0.25 µm/GSD 1.7 DOS ≈ 2.6–26 mg/m³ → 0.6–6 g/m² challenge in 45 min at 8.4 cm/s. Too uncertain to use as a number.
Retained −lnP (overall): ln(0.88)/ln(0.25) = 0.09 at 45 min.

## 16. Obadi et al. 2026 — in-duct MERV 7 and MERV 13 furnace filters vs simulated wildfire smoke, 100 exposures (NRC Canada)

Source: Obadi I, Elsagan N, Jones B, Naboka O, Collins P, Bénichou N, Gomaa I (2026) "Bench-scale evaluation of in-duct air filter performance against simulated wildfire smoke: assessing long-term efficiency", Indoor Air 2026, doi:10.1155/ina/4736684 (open access on Wiley but Cloudflare-blocked from here; not in PMC). Abstract text read via the Synapse page (https://synapsesocial.com/papers/69c37b41b34aaaeb1a67d88d). Set-up: NRC report NR24-116/2023E (Elsagan & Adelzadeh 2023, https://publications.gc.ca/site/eng/9.921708/publication.html): tube furnace burning pine needles and wood chips.
Abstract (verbatim parts): "Each filter was subjected to 100 measured exposures ... MERV 13 filter particle removal efficiency, based on mass, dropped from 80% initially to 30% in the final test. The efficiency, based on particle count, dropped from an initial value of 35%–20%." MERV 7 ~18% → ~8%. SEM: captured particles included droplet-like tar balls.
Missing: whether the MERV 13 was electret, deposited mass, face velocity, Δp. Matt to download.

## 17. Pistochini et al. 2025 — DIY box-fan filters over an academic year (cross-pool, ambient)

Source: Pistochini T, Jaeger ?, Cappa CD, Corsi RL et al. (2025) "Longevity of size-dependent particle removal performance of do-it-yourself box fan air filters", Environ Sci Process Impacts, doi:10.1039/D4EM00406J (RSC open access, Cloudflare-blocked). Abstract (Crossref): "Filtration performance of do-it-yourself (DIY) box fan air filters deployed across a university campus was assessed over an academic year." A newspaper summary (Inquirer 2025, unverified) says efficiency fell >30% over ~2,500 h. Ambient, not smoke — relevant to Matt's DIY units; for the ambient agent.

---

## SYNTHESIS (my pool)

1. Mass for a 20% loss of −lnP (my interpolations; challenge = fed, dep = deposited):
- Small droplets / smoke on single sheets or HVAC media: Otani DOS 0.1 µm neutral ≈ 0.15–0.2 g/m² dep (all electrostatic gone at 0.36 g/m² dep); Tennal BES 1 µm full discharge 0.3 g/m² (unverified); Shirman pine smoke on charged MERV 13 ≈ 0.15 g/m² dep (estimated mass); NT TR 320 diesel on EU7-A ≈ 0.6 g/m² fed, cigarette ≈ 1.5 g/m² fed; Heo cigarette ≈ 0.5 g/m² (if linear to 2.04 g/m²); Roh corona PP meltblown + DOP ≈ 1 g/m² fed (~0.6 dep).
- Oils on multi-layer respirator media (per total media area): Rengasamy N95 + DOP ≈ 50 mg/FFR (≈2.5–5 g/m² for 100–200 cm²); Martin AS-140 + DOP ≈ 10–15 g/m² continuous, ≈ 8 g/m² intermittent; Plebani FFP2 + paraffin ≈ 25 g/m² (area assumed); Tombolini ≈ 500 mg/FFP2 (area unknown).
- Fluorinated web (Roh PS_f) + DOP ≈ 11 g/m² fed vs ≈ 1 for corona PP — ~10× delay, same end state at 50 g/m².
2. What controls it, in order of size of effect:
- Deposit concentration in depth. Thin single sheets and low-efficiency HVAC media spread the deposit through the whole electret; high-efficiency multi-layer respirator media load the front layers first, so per TOTAL media area they look 10–50× more tolerant. A per-layer (or per fibre-area) basis is the right normalisation; most papers do not give basis weight to do it.
- Aerosol type: combustion aerosol (diesel ~2× cigarette per gram, NT TR 320; soot-driven per Wang 2026) and small droplets ≫ larger oil droplets (paraffin MMD 0.47 µm, DOP MMD 0.36 µm). Solid dust alone barely degrades (PTI dust: 88 → 80% at ~60 g/m², NT TR 320).
- Oleophobic/fluorochemical surface: ~5–20× more mass to the same loss (Roh 2019); P100/R-type media show no DOP degradation to 200 mg/FFR (Rengasamy 2013).
- Loading rate / time: intermittent loading with overnight and weekend rests degraded ~5–10× more per gram than continuous loading, and penetration rose 2–3× across a 3-day sealed storage with ~60 mg added (Martin 2006). Slow real-world loading is likely worse per gram than accelerated lab loading.
- Charge state of the loading aerosol: neutralised DOP worse than as-generated charged DOP (Martin 2006).
- Co-deposited coarse dust: rebuilds mechanical efficiency and Δp; trough depth set by the combustion fraction (10% diesel: 88 → 72%; 35%: 88 → 26%, NT TR 320).
3. End state: smoke and diesel took EU7 media to about the IPA-discharged level and held there (NT TR 320 A, B-cigarette; Otani neutral DOS). Oils also raised penetration of already-discharged media (IPA FFP2 38 → 48% at 0.3 µm, Tombolini; O2-plasma PS 58 → 75%, Roh), so for oils the loaded state can be worse than the clean-IPA reference. One case below IPA (NT TR 320 B + diesel, 29% vs 40%) is within sample-to-sample spread.
4. Δp is no warning: +0–10% for oils/smoke in every electret study here, while glass P2 doubled Δp at constant efficiency (Plebani 2010).
5. Incense (Matt's bench aerosol): no direct study found. Closest analogues: sidestream cigarette smoke (MMD ~0.2 µm) and pine-needle smoke (CMD ~0.16 µm). On those, losses start at a few tenths of a g/m². A bench test at 1 mg/m³ and 10 cm/s deposits ~0.06 g/m² per 10 min at full capture — enough to matter if the same coupon is re-used across tests.

6. QF (kPa^-1, -lnP/dp, my arithmetic): NT TR 320 A at 0.4 um, 0.33 m/s, dp 88 Pa: 25.6 clean -> 2.7 after 5.3 g/m2 diesel (dp unchanged). B at 0.21 m/s, dp 141 Pa: 6.0 -> 2.4 after 0.93 g/m2 diesel. Shirman charged C MERV 13 (116-365 nm, 33 cm/s, 47 Pa): 21 -> 4.2 after 80 min pine smoke. Roh PP meltblown (DOP, 11.8 cm/s, 65 Pa): 15 -> 4.3 at 50 g/m2 DOP challenge. Plebani FFP2 (paraffin, 95 L/min): 37 -> 23. Tombolini FFP2 (0.3 um DEHS, 95 L/min): 39 -> 30. Otani (0.1 um neutral DOS, 5 cm/s): ~41 -> ~25. Glass P2 (Plebani): 27 -> 13 because dp doubled.
