# Pool: mechanism, scaling laws and modifiers of electret loading degradation

Research standard: Matt's CLAUDE.md note applies (hard question) - primary documents read where reachable; every number carries its location; walled sources listed with links.

Conventions used below
- P = penetration (fraction). "Retained -lnP" = ln P_loaded / ln P_initial (1 = no loss, 0 = all filtration gone).
- "Electrostatic part lost" = (ln P_loaded - ln P_initial) / (ln P_discharged - ln P_initial), where a discharged / mechanical reference exists.
- Deposited mass M in g per m2 of media area (flat sheet: media area = face area).
- Brown et al. 1988 degradation law (see entry 2): ln(P_T(M)/P_T(0)) = beta_TL * M. beta in m2/g when M in g/m2.

---

## 1. Otani, Emi & Mori 1993 (KONA 11:207-214; English translation of Kagaku Kogaku Ronbunshu 18(2):240-247, 1992)

- Link: https://www.jstage.jst.go.jp/article/kona/11/0/11_1993023/_article/-char/en (open, CC BY). Read in full; figures read off rendered PDF pages 6-7 (journal pp. 212-213).
- Media: electret filter (polymer not stated), fibre diameter df = 1.3 um, thickness L = 0.71 mm, packing density alpha = 0.0612. Fitted fibre charge density sigma = 5.1 uC/m2 (back-fitted from neutral-particle data via their own Eq. 11 - not independently measured; authors say measuring it is "very difficult"). Basis weight not given; if PP (910 kg/m3) it would be 0.0612 x 910 x 0.71e-3 = ~40 g/m2 (my estimate).
- Velocity: u = 0.05 m/s (5 cm/s) for all loading runs.
- Loading aerosols: DMA-classified monodisperse 0.1 um DOS droplets (uncharged, and uni-charged), and 0.1 um iron alum solid particles (charged). Inlet concentration Ci = 3e-9 to 2e-8 kg/m3 (uncharged droplets) and ~5e-9 to 6e-8 kg/m3 (charged droplets) (Fig. 12 caption; the "5 x 10-3" in the scan is evidently 5e-9).
- Efficiency test: same monodisperse aerosol (penetration of the loading aerosol itself), CPC count basis.
- Humidity (Fig. 10): unloaded filter in particle-free air at 20% and 90% RH; P of 0.1 um uni-charged DOS constant at ~4.5e-3 for 800 h (33 days) at both RH. Quote: "the particle penetration remains constant for over a month, indicating that the electret charge is quite stable in humid air."
- Fig. 11 (charged 0.1 um particles, x-axis = challenge mass per area Ci*u*t, g/m2 after x1e3 scaling):
  - DOS droplets: P 2e-3 at 0 -> ~1.3e-2 at 0.25 g/m2 -> ~0.1 at 0.8 g/m2 -> ~0.17-0.2 at 1.15 g/m2 (read off log axis, +-20% in P). Delta p flat at ~33 Pa.
  - Iron alum solid: P 1.5e-3 -> ~1e-3 at 0.45 -> ~4e-4 at 0.8 -> ~1e-4 at 1.1 g/m2 (P FALLS). Delta p 33 -> ~100 Pa.
  - NB the translated text says solid-particle penetration "gradually increases" and liquid "decreases"; the figure legend (open = solid, filled = droplet) shows the opposite. Figure taken as primary; text appears to have swapped the verbs (the same paragraph's reasoning - interception gain for solids, field weakening for liquids - matches the figure).
  - Retained -lnP for DOS (charged): ln(0.17)/ln(0.002) = 1.77/6.21 = 0.29 at ~1.15 g/m2 challenge (deposited ~1.0 g/m2 since mean efficiency >85%).
- Fig. 13 (single-fibre efficiency eta vs accumulated mass per filter volume m, kg/m3; m = (1/L) * integral of E d(Ci u t) = deposited mass / filter volume):
  - Uncharged 0.1 um DOS: eta 0.028 at m=0 -> mechanical value 0.019 (dashed "initial efficiency without electrostatic force") at m ~0.5 kg/m3. Quote: "the single fiber efficiency for neutral particles decreases with particle accumulation and becomes equal to that of uncharged fibers at about m = 0.5 kg/m3".
  - Converting: M = m x L = 0.5 kg/m3 x 0.71e-3 m = 0.36 g/m2 deposited per m2 of media. => 100% of the electrostatic enhancement for neutral 0.1 um particles gone at ~0.36 g/m2 of DOS.
  - In lnP terms (lnP = -4 alpha L eta / (pi (1-alpha) df) = -45.3 eta here): -lnP 1.27 -> 0.86; retained -lnP 0.68; electrostatic part lost 100%.
  - Uni-charged 0.1 um DOS: eta ~0.125 -> ~0.045 at m = 1.5 kg/m3 (M = 1.07 g/m2): electrostatic part lost (0.125-0.045)/(0.125-0.019) = 75%.
  - Authors' model: fibre charge inferred from the neutral-droplet decay, then used to predict the charged-droplet decay -> "the covering of the fiber surface with a liquid layer is the main cause of penetration increase even for charged droplets" (i.e. neutralisation by the droplets' own charge is secondary).
- Scale check (my arithmetic, not the authors'): fibre surface per filter volume = 4 alpha/df = 1.9e5 m2/m3; 0.5 kg/m3 DOS (914 kg/m3) = 5.5e-4 m3/m3 => equivalent uniform film 2.9 nm (about 5 nm at the face, given the exponential depth profile). The electrostatic gain is gone long before anything like a continuous dielectric coating exists - consistent with charge being neutralised/mobilised where oil wets the fibre, not with field "screening" by a thick layer.
- Mechanism quotes: "it is gradually attenuated when exposed to organic droplets because the collected organic droplets spread over the fibers and weaken the electric field around them." ... "Since the covering of the electret fiber surface with a liquid layer is dependent on the wetting property of the liquid, special attention is required in the electret filtration of organic droplets."
- Caveat: unusual fine-fibre (1.3 um) electret; the solid-particle result (P falls) reflects strong dendrite gain on fine fibres - for 10-30 um fibres the mechanical gain per g is much smaller.

## 2. Brown, Gray, Blackford & Bostock 1988 - degradation law (via Ji et al. 2002; primary is walled)

- Primary: Ann Occup Hyg 32(3):271-294, doi:10.1093/annhyg/32.3.271, https://academic.oup.com/annweh/article/32/3/271/172048 - Cloudflare-walled to curl and refused by WebFetch. MATT TO DOWNLOAD. Key source: on-site exposures (foundry fettling, foundry burning, lead operations, coal-tar fume, coal) of respirator electret media; defines the degradation coefficient.
- Model as reproduced by Ji, Kang, Hwang & Bae 2002 (KSME Trans B 26(8):1102-1114, pp. 1105-1106, Eqs. 1-7; they cite Brown et al. 1988 as their ref. 13):
  - Layer efficiency for test particle T falls linearly with local deposited mass per unit volume mu_L: alpha_T(mu_L) = alpha_T - beta_TL * mu_L (Eq. 4).
  - Integrating through the depth with an exponential deposit profile gives ln[P_T(M_L)/P_T(0)] = beta_TL * M_L (Eq. 7), M_L = deposited mass per unit filter area. Ji: beta_TL "is not affected by filter thickness or the particle-layer efficiency" (my translation).
  - Consequence: the ABSOLUTE rise in ln P per g/m2 is set by beta, so a thicker / higher-PF filter loses a smaller FRACTION of its -lnP for the same g/m2 (until the electrostatic part runs out).
  - Values quoted by Ji from Brown 1988 for resin-wool electret: coal dust ~0.028; foundry lead-burning fume ~1.0 (units not restated by Ji; consistent with m2/g given Ji's own value below). Ji: "beta_TL varies especially when the size distribution and composition of the generated particles differ."
- UNVERIFIED until Brown 1988 itself is read: units of beta, test-particle size, full table of aerosols.

## 3. Ji, Kang, Hwang & Bae 2002 (Trans KSME B 26(8):1102-1114, Korean) - beta measured for 0.07 um NaCl

- Link: https://koreascience.kr/article/JAKO200211921125101.page (open; scanned PDF, read pages 3-12 as images). English sequel: Ji, Bae, Kang & Hwang 2003 J Aerosol Sci 34:1493-1504 (doi:10.1016/S0021-8502(03)00103-4, walled).
- Media: commercial cabin-air-filter electret media (Sungchang Air Tech), two layers: polyester prefilter (~35 um fibres) + main electret layer of polycarbonate fibres ~10 um "made by electrically spun process of polymer solution" (p. 1107). Basis weight, thickness not given. Initial delta p 1.9 mmH2O (18.6 Pa) at 8.4 cm/s (Fig. 4, p. 1108).
- Loading/test velocity 8.4 cm/s. Loading = test aerosol (polydisperse; CPC overall count efficiency; SMPS fractional efficiency). Concentration 1e5-1e6 /cm3 (~100x indoor).
- Aerosols (Table 1, p. 1107): NaCl from 0.1% solution (CMD 0.05 um, GSD 1.67); NaCl from 1% solution (CMD 0.07 um, GSD 1.9); DOS (CMD 0.25 um, GSD 1.7). NaCl either through Po-210 neutraliser (Boltzmann) or not (spray-electrified, bipolar, 2-3x the mean Boltzmann charge per ref. 14); DOS neutralised.
- Mass basis: deposited mass computed from SMPS upstream/downstream size distributions (p. 1111) - estimated, not weighed.
- Fig. 11 (p. 1111): ln(P_T(M_L)/P_T(0)) vs M_L, 0.07 um NaCl. Linear to M_L ~0.25 g/m2 with slope beta_TL ~ 3.4 m2/g (stated in text: "in the region where the penetration ratio increases linearly, beta_TL is about 3.4"). Read-off: ln ratio 0.21 at 0.07, 0.42 at 0.14, 0.72 at 0.24 g/m2 for both charge states; Boltzmann-charged then flat/declining (0.68 at 0.38, 0.58 at 0.6 g/m2 - mechanical gain); spray-charged continues to ~0.95 at 0.36, 1.0 at 0.52, 0.95 at 0.65 g/m2.
- Fig. 8 (p. 1110): overall efficiency 0.80 (Boltzmann) / 0.87 (spray) -> ~0.48 at ~150 min; Boltzmann then rises to ~0.57 at 250 min with normalised delta p 1 -> 3.9; spray-charged stays ~0.5 with delta p only 1.2x by 280 min (more charge -> more uniform depth deposition).
  - Retained -lnP (Boltzmann, overall count): ln(0.52)/ln(0.20) = 0.41 at the minimum (~0.25-0.4 g/m2).
- 0.05 um NaCl (Figs 6-7, p. 1109): fractional efficiency 0.70-0.87 -> steady ~0.2 at 0.1-0.5 um (count), delta p rise <10% at steady state; steady-state fractional efficiency the same for both charge states (Fig. 7). Authors note it matches Lehtimaki's 4-month on-road cabin filter at 0.3-0.5 um.
- DOS (Fig. 12, p. 1112): overall efficiency 0.75 -> 0.4 at 10 min -> 0.12 at 45 min; delta p +10% at 40 min. Fig. 13: after "charge depletion", efficiency at 0.1-0.3 um is ~0.37-0.45 (NaCl 0.07 um loaded), ~0.2 (NaCl 0.05 um loaded), <0.1 (DOS loaded, minimum ~0.05 at 0.15 um) - DOS-loaded media equal to fully discharged media in their earlier work (ref. 9).
- Mechanism text (pp. 1104-1105, my translation): three causes per Brown et al. 1988 - (1) neutralisation of fibre charge by charged deposits, (2) "screen" effect of deposits blocking the field, (3) chemical action; conductive deposits screen more. Quotes Walsh & Stenhouse 1997: TiO2 (permittivity 90) degrades efficiency faster than stearic acid (permittivity 2.2).
- Ji's own reading of size effect (p. 1112): smaller loading particles -> lower minimum efficiency (deposits contribute less mechanical capture), consistent with Walsh & Stenhouse stearic acid 0.46-1.4 um.

## 4. Mahdavi, Haghighat, Bahloul, Brochot & Ostiguy 2015 (Ann Occup Hyg 59(5):629-640) - RH during NaCl loading

- Accepted manuscript (open): https://pharesst.irsst.qc.ca/cgi/viewcontent.cgi?article=1046&context=etudes-primaires (image PDF; read MS pages 3-15). Journal page (walled): doi:10.1093/annhyg/mev005.
- Media: one commercial N95 FFR model, "electrostatically charged microfibers", sealed on manikin. No basis weight/area given.
- Loading: polydisperse NaCl (Collison, 0.1 v/v, silica-gel dried, Kr-85 neutralised), CMD 45-50 nm at 10/50% RH, 65-70 nm at 80% RH, GSD ~1.7 (MS p. 8). Total 1.2-2.4e6 /cm3 (Table 1). 25 +- 3 C. 6 h. Flows 85 and 170 L/min constant, and cyclic (85 L/min minute volume, 270 PIF).
- Test: SMPS 10-205 nm, count penetration, measured at 0, 2, 4, 6 h. Mass not reported.
  - My rough estimate (flag: not the authors'): ~0.8 mg/m3 NaCl in 10-205 nm x 85 L/min x 6 h = ~25 mg per FFR; over ~0.015-0.02 m2 of media = ~1.2-1.7 g/m2 challenged (order of magnitude only).
- MPPS penetration, initial -> 6 h (MS pp. 10-12):
  - 10% RH: 85 L/min 2.70 +- 0.60 -> 1.06 +- 0.19%; 170 L/min 6.92 -> 3.08%; cyclic 6.80 -> 4.33%. (P FALLS; retained -lnP 1.26 and 1.30 - i.e. -lnP rises ~26-30%.)
  - 50% RH: 85 L/min 3.47 +- 0.56 -> 4.57 +- 0.58% (p = 0.069); 170 L/min 7.79 -> 9.44% (p<0.05); cyclic 7.44 -> 7.89 (ns). Retained -lnP 0.92 (85), 0.92 (170). [MS text heading says "At 10% RH" for these numbers; context (Fig. 4a, section 3.2) shows it is 50% RH - typo in MS.]
  - 80% RH: 85 L/min 3.63 +- 0.65 -> 5.21 +- 0.63%; 170 L/min 8.49 -> 11.10%; cyclic 8.15 -> 9.05 (ns). Retained -lnP 0.89 (85), 0.89 (170).
  - Control: 80% RH, 85 L/min, 6 h, no particles -> no significant change (Fig. 6, MS p. 15). Quote: "testing filters under high humidity conditions (for 6 hour target period), in absence of loading however, revealed no significant change in penetration".
- So for the same NaCl challenge, going from 10% to 50-80% RH swings the MPPS -lnP change from +26-30% to -8-11%. Authors' explanations: at high RH NaCl is "partially or totally hydrated"/liquid and neutralises/weakens fibre charge (no measurement of charge). NB 50% RH is below NaCl deliquescence (75%), yet already shows the "humid" behaviour - points to adsorbed surface water on salt deposits, not only full deliquescence (my inference).
- Initial P also rises with RH (2.70 -> 3.47 -> 3.63% at 85 L/min) - different filter samples, so not a clean RH effect.
- Literature RH pointers given (MS p. 5): Yang & Lee 2005 no significant change 30-70% RH for electrets (ultrafine); Ikezaki et al. 1995 and Lowkis & Motyl 2001 significant surface-potential loss after long humid exposure.

## 5. Shimokobe & Inoue 1986 (Earozoru Kenkyu 1(3):186-, Japanese) - incense smoke on thick HVAC-type PP electret, gravimetric

- Link: https://www.jstage.jst.go.jp/article/jar/1/3/1_3_186/_article/-char/en (open). Read pp. 187-188 (Figs 2-5, Tables 2-4) from rendered PDF.
- Media (Table 4): PP nonwoven, 4 mm thick. Electret EF-1: df 33 um, alpha 0.11; EF-2: 33 um, alpha 0.12; conventional (uncharged) SF: 28 um, alpha 0.11. Basis weight not given (my estimate 0.11 x 910 x 0.004 = ~400 g/m2). Clean delta p 40 (EF-1), 57 (EF-2), 59 (SF) Pa at 40 cm/s; no change over the test (p. 188).
- Loading (Table 2): joss-stick (incense) smoke, 8.5-255 mg/m3, 40 cm/s (!), 25-30 C, RH 50-70%, 46.6 cm2 samples; mass by weighing (gravimetric).
- Efficiency = gravimetric mass efficiency per loading step, E = captured/inflow (Eq. 1).
- Concentration independence: EF-1 at 8.5 vs 85 mg/m3 fall on the same captured-vs-load curve (Fig. 2; text p. 187: 6.1 g/m2 x 10 passes = 61 g/m2 x 1 pass).
- Fig. 4 (E vs captured g/m2; read to +-0.01 in E, +-1 g/m2):
  - SF (uncharged): E ~0.06 flat to 30 g/m2.
  - EF-1: 0.28 at ~1 g/m2 -> ~0.18 at ~6-7 -> ~0.15 at 8-9 -> ~0.09 at 21 g/m2.
  - EF-2: 0.34 at 16 -> 0.21 at 30 -> 0.11 at 40 -> 0.08 at 45 -> 0.065 at 53 g/m2 (curve extrapolates to ~0.4-0.45 at ~10).
  - Electrostatic part lost (lnP form, SF as mechanical reference): EF-1 50% at ~6-7 g/m2, ~88% at 21 g/m2; EF-2 ~50% at roughly 25-30 g/m2, ~95% at 53 g/m2.
- Mechanism (p. 187-188, my translation): "when filtering high-concentration particles containing water as in this experiment, the electret fibre charge is shielded by the deposit"; SEM (Fig. 5) shows fibre surface "uniformly covered with a tar-like substance"; at E = 0.05 the surface charge "has almost entirely disappeared". EF-1 vs EF-2 difference attributed to fibre charge density, not packing.
- Use: an oily/tarry combustion aerosol needs ~5-30 g/m2 per m2 of thick (~400 g/m2, 33 um) media to lose half its electrostatic gain - vs 0.36 g/m2 for DOS on Otani's thin 1.3 um medium. Per m2 of FIBRE surface (4 alpha L/df = 53 m2/m2 here vs 134 m2/m2 for Otani) the gap is still ~50-100x, so fibre-surface coverage alone does not collapse these two (different aerosols, velocities, charge densities). Flag: velocity 40 cm/s.

## 6. Ando, Takahashi, Togashi & Okumura 1993 (Sen'i Gakkaishi 49(6):323-330, Toray) - ambient aerosol vs test dust on the same electret, with surface potential

- Link: https://www.jstage.jst.go.jp/article/fiber1944/49/6/49_6_323/_article/-char/en (open). Read pp. 325-330 (Table 1, Figs 6-17) from rendered PDF.
- Media (Table 1): PP meltblown electret No. 6-EL: df 1.94 um, alpha 0.171, H 0.64 mm, surface charge density Q = 9.0e-10 C/cm2 (= 9 uC/m2). My basis-weight estimate 0.171 x 910 x 0.64e-3 = ~100 g/m2 (text p. 324 mentions 20-40 g/m2 PP nonwovens - not reconciled; possibly plied). Fibre surface 4 alpha H/df = 226 m2 per m2 media.
- Charge vs P (Fig. 6, 0.1-0.2 um): Q = 0 -> P ~5e-2; 3.8 uC/m2 -> ~5e-4; 6.5 -> ~7e-5; 9.0 -> ~2e-6. (-lnP 3 -> 13: electrostatic part is ~75% of -lnP for 6-EL.)
- Humidity / heat (Figs 8-10): P unchanged up to ~100 C (rises above; TSD peak ~425 K, Fig. 9); 60 C and 95% RH for 1 week (Fig. 10, ~10 d axis): P ~2e-6, no change. Text: polarisation charge "stable against humidity".
- Loading, 2.5 cm/s, P at 0.3 um, x-axis = challenge Ci*v*t (g/m2; P so small that deposited = challenge):
  - JIS-15 test dust (0.8 um mean; JIS Z 8901 class 15 = Kanto loam + carbon black + cotton linter mix), 13 mg/m3 (Fig. 12): P 1.5e-7 -> 4e-8 at ~3 g/m2 -> 2.8e-8 flat to 30 g/m2 (P only FALLS). delta p ~120 -> 480 Pa at 30 g/m2 (axis is dp x 1e-2 Pa). Surface potential (Fig. 14): front face E/E0 1.0 -> 0.62 at 30 g/m2; back face 1.0 throughout -> surface (cake) deposition.
  - Ambient room air (0.07 um mean, 0.04 mg/m3) (Fig. 15): P 7e-7 -> 1e-6 at ~1.5 g/m2 -> 1.4-1.8e-6 at 4-5 g/m2 (max) -> 3.5e-7 at 7.5 -> 5e-8 at 10 g/m2. delta p ~60 -> 130 Pa at 10 g/m2. Surface potential (Fig. 17): front 1.0 -> 0.42 at 5 -> 0.15 at 10 g/m2; back 1.0 -> 0.7 at 5 -> 0.58 at 10 g/m2 -> depth deposition, both faces discharged.
  - beta (Brown form) for ambient: ln(1.8e-6/7e-7)/5 g/m2 = ~0.19 m2/g at 0.3 um test (my arithmetic). Retained -lnP at max 0.93 (thick, very high-PF medium: big -lnP budget).
  - Per g/m2, ambient fine aerosol knocked down front-face surface potential ~7x faster than JIS-15 dust (0.085 per g/m2 = 0.85 drop in 10 g/m2, vs 0.013 per g/m2 = 0.38 drop in 30 g/m2). Mean-size ratio 0.8/0.07 = 11: mass-specific projected-area ratio ~11x, number ratio ~1500x - the ~7x is closer to an area/coverage scaling than to number or mass (my inference; deposition location also differs - cake vs depth - and JIS-15 contains conductive carbon black, so not a clean test).
  - Inconsistency to flag: 10 g/m2 at 0.04 mg/m3 and 2.5 cm/s needs ~116 days, while the Fig. 16 caption says "for three days" (3 days gives ~0.26 g/m2). Either the concentration or the duration in the captions is wrong; the loading axis may be overstated by up to ~40x. Treat the ambient beta as uncertain.
- Authors' conclusion (p. 330, my translation): "the dust-loading behaviour of electret filters changes with the particle size and the amount deposited"; ambient: early internal filtration, electrostatic loss > mechanical gain, P rises; later mechanical gain wins.

## 7. Shimokawa 2023 (J. Japan Air Cleaning Assoc. 61(3):158-162, Japanese) - tobacco smoke, gravimetric, with and without oleophobic surface treatment

- Link: https://www.jstage.jst.go.jp/article/jaca/61/3/61_158/_article/-char/ja (open PDF). Read pp. 161-162 (Table 1, Figs 5-6) from rendered pages.
- Media (Table 1): PP meltblown base; tested at 5.3 cm/s with atmospheric dust 0.3-0.5 um (count, presumably OPC):
  - uncharged, untreated: wetting tension 37 mN/m, dp 19 Pa, efficiency 23%;
  - charged, untreated: 37 mN/m, 20 Pa, 99.8% (QF = 6.2/0.020 = ~310 kPa-1 at 5.3 cm/s - my arithmetic);
  - charged + surface treatment: <30 mN/m, 19 Pa, 99.7% (treatment does not hurt initial charge).
  - Basis weight, fibre diameter, charging method not given.
- Loading: cigarettes burned in a sealed 1 m3 chamber; smoke drawn through the filter; captured mass by weighing before/after (p. 161) - gravimetric, per m2 of media.
- Fig. 5 (efficiency vs captured smoke g/m2; read +-2% and +-0.1 g/m2):
  - charged/untreated: 100 -> 91% at 1.0 -> 72% at 1.5 -> 49% at 2.0 -> 28% at 2.5 -> 24% at 2.9 g/m2 (= uncharged level).
  - charged/treated: 100% to 1.0 -> 99% at 2.0 -> 87% at 3.0 -> 73% at 3.8 -> 59% at 4.6 -> 40% at 5.7 -> 26% at 6.9 -> 24% at 7.5 g/m2.
  - Electrostatic part lost (lnP form, uncharged 23% as reference): untreated ~64% at 1.0 g/m2, ~90% at ~1.9, 100% at ~2.7 g/m2; treated ~27% at 2.0, ~70% at 3.0, 100% at ~7 g/m2.
  - Initial beta (Brown form, my arithmetic): untreated ln(0.09/0.002)/1.0 = ~3.8 m2/g.
  - Author: smoke mass needed to reach the uncharged efficiency rose "about 2.5x" with the treatment.
- Mechanism quotes (p. 161, my translation): tobacco-smoke particulate is "mainly water, nicotine and tar, liquid at room temperature"; after capture it "wets and spreads over the fibre surface, covering it, so that the electret charge is lost or shielded". Fig. 6: untreated fibres coated by spread smoke; treated fibres carry discrete spherical droplets. Also effective "for oil mists such as DOP" (no data shown).
- Related, walled: Hayashi & Kitagawa 2017, "Improvement of tobacco-smoke durability of electret filters", J. Soc. Powder Technol. Japan 54(6):406, https://www.jstage.jst.go.jp/article/sptj/54/6/54_54.406/_article/-char/ja (subscriber-only) - same idea (surface modification stops smoke spreading; also works for oil mist).

## 8. Humidity and water without particle deposits (charge stability) - several open sources

- Otani et al. 1993 (entry 1, Fig. 10): unloaded electret, particle-free air at 20% and 90% RH for 800 h - P constant (~4.5e-3 at 0.1 um).
- Ando et al. 1993 (entry 6, Fig. 10): 60 C + 95% RH for 1 week - P ~2e-6 unchanged; P unchanged to ~100 C (Fig. 8).
- Mahdavi et al. 2015 (entry 4, Fig. 6): N95 at 80% RH, 85 L/min, 6 h, no particles - no significant change.
- Stoll & Antonyuk 2025, "Influence of humidity on FFP masks with electret filter media under real-life wearing conditions", Atmosphere 16:62, https://doi.org/10.3390/atmos16010062 (open; PDF https://mdpi-res.com/d_attachment/atmosphere/atmosphere-16-00062/article_deploy/atmosphere-16-00062.pdf). Read pp. 8-13.
  - 98% RH saturated breath-like air for 75 min through flat FFP2 samples, no entrained droplets: efficiency and mass unchanged (Table 2: e.g. type A 98.99 -> 98.76 -> 98.93%).
  - With entrained liquid droplets (water content +12 to +34% of sample mass): FE drops 0.3-2 points (A 98.99 -> 98.73; B 96.24 -> 94.30; C 98.44 -> 98.31; Table 3) and recovers after drying.
  - Apparent surface charge density from surface potential (Table 4, mask A): outside 8.75e-7 C/m2 dry -> 1.86e-7 moistened (+25% water) -> 5.24e-9 saturated (+90%); inside 1.20e-6 -> 8.75e-8 -> 1.79e-8. Liquid water screens the field; reversible on drying.
  - Sealed masks on headform, 98% RH 30 C cyclic breathing: total FE drop ~5% with "zig-zag" (drop when wet, partial recovery when dried).
- Liu, Dai, He & Ke 2020, "The effect of temperature and humidity on the filtration performance of electret melt-blown nonwovens", Materials 13:4774, PMC7662889 (open; read via Europe PMC full text): corona-charged PP meltblown; 50-70 C for 24 h - small decline (from ~98%); 90-110 C large decline; 90% RH at the same temperature adds further loss; worst case 110 C + 90% RH 24 h: 95.49% -> 38.16% (at the higher test flow), surface potential to about -1 kV. Thermal/humid charge escape from shallow traps first.
- Pierlot, Alexander & Schutz 2022 (CSIRO), "Impact of wearing on filtration performance of electrostatic filter face masks", IJERPH 19:5032, PMC9100139 (open): wool/PP tribo media worn up to 8 h by office/lab staff; penetration rose over the first ~4 h then plateaued; attributed to "exhaled moisture (vapor and aerosolized) and non-volatile excretions as well as particles"; the media had already doubled its penetration over 4 years' storage (charge loss in storage).
- Net: vapour humidity alone, at room temperature, over days to weeks, does little to a good PP electret; liquid water on fibres screens the field (reversibly); heat (>~70-90 C) and heat+humidity cause irreversible charge loss. The humidity effect that matters for loading is the interaction with DEPOSITS (entry 4: NaCl at 50-80% RH turns loading from net-improving to net-degrading).

## 9. Surface oleophobicity / fluorination vs oil loading (additive-type modifier)

- Shimokawa 2023 (entry 7): oleophobic surface treatment (wetting tension 37 -> <30 mN/m) raised tobacco-smoke capacity to reach the uncharged efficiency ~2.5x (2.8 -> ~7 g/m2); initial beta from ~3.8 m2/g to ~0.8 m2/g over the first 2 g/m2.
- Roh, Kim, et al. 2019, "Facile functionalization via plasma-enhanced chemical vapor deposition for the effective filtration of oily aerosol", Polymers 11:1490, PMC6780184 (open; Table 5): electrospun PS webs, 40 cm2 samples, 11.8 cm/s, TSI 8130.
  - DOP: initial P 29.9% (PS ES), 37.1% (C4F8-fluorinated PS ES, DOP contact angle 145 deg), 37.6% (PP meltblown), 57.6% (O2-plasma, charge lost); P at 200 mg DOP (= 50 g/m2 challenged): 77.0, 73.0, 75.8, 75.3% - all converge; fluorinated media had the best QF only "until about 50 mg" (12.5 g/m2).
  - NaCl max P: PS ES 13.0 -> 17.8% at 8.8 mg (2.2 g/m2); fluorinated 27.3 -> 30.0% at 5.8 mg (1.45 g/m2); PP MB 28.7 -> 29.4% at 1.1 mg (0.28 g/m2) then falling.
  - Reading: lowering surface energy delays oil-film coverage but does not change the end state at tens of g/m2.
- Patents on fluorochemical melt additives (3M) belong to the patent pool.

## 10. Fibre diameter / nanofibre electrets (modifier)

- Sun & Leung 2020, "Enhanced nano-aerosol loading performance of multilayer PVDF nanofiber electret filters", Sep Purif Technol 240:116606, PMC7108370 (open): PVDF nanofibre (525 nm) electret, 3.06 g/m2 total, NaCl loading at 5.3 cm/s. Electrostatic loss was barely visible - "the largest reduction in efficiency of particles was only 2.7%" - because mechanical gain from dendrites on sub-micron fibres outran it; only a low-concentration run showed the dip. With sub-um fibres, solid-particle loading is net-improving almost immediately (cf. Otani's 1.3 um fibres, entry 1: solid P falls).

## 11. Charge distribution and discharge reference

- Kerner, Schmidt, Schumacher, Asbach & Antonyuk 2021, "Electret filters - from the influence of discharging methods to optimization potential", Atmosphere 12:65 (open: https://kluedo.ub.rptu.de/files/6247/atmosphere-12-00065-v2.pdf). Liquid-IPA immersion can under-discharge small-pore media vs 24 h IPA vapour (Table 3: e.g. 300 nm efficiency after 5 min liquid IPA 0.95 vs 24 h vapour 0.80 for one medium) - so "IPA-discharged" references are not always fully discharged. Simulation: deposits neutralise charge "from the upstream to the downstream side"; charge placed deeper in the medium delays decay at some cost in initial efficiency (qualitative, no loading numbers).

## 12. Combustion smoke / soot - composition at the extreme

- Holder, Halliday & Virtaranta 2022, "Impact of do-it-yourself air cleaner design on the reduction of simulated wildfire smoke...", Indoor Air 32:e13163, PMC9828579 (open; section 3.6 read in full text). 20-inch box fan + one 1-inch MERV 13 electret furnace filter. Filters smoke-loaded at the EPA Open Burn Test Facility (pine straw smoke; three air cleaners run "until the air cleaners ceased to reduce smoke concentrations" - so this is an END-POINT mass, not a threshold): "only 10.0 +- 1.1 mg of smoke deposited" (pre/post weighing on an Ohaus Scout balance) -> CADR 4.3 +- 0.9 CFM (repeat 9.7) vs clean baseline 79.7-111.2 CFM (fan low-high; text p. 3.1) - i.e. ~90-96% loss at the same (high) fan setting; filter dp 0.27 -> 0.29 inH2O at 819 CFM. Dust-loaded filters (53 +- 4 g test dust, ~5000x the mass) kept 22.9 CFM with dp 2 inH2O. Authors' mechanism: fresh smoke particles carry charge and build up surface charge that repels incoming charged smoke (no measurement).
  - My conversion (assumption: a 20x20x1 MERV 13 pleat pack has ~0.4-0.7 m2 of media): 10 mg = ~0.015-0.025 g/m2. Taken at face value the end-point beta would be tens of m2/g - two orders above tobacco or salt. Treat as an outlier needing confirmation: weighing a whole furnace filter (frame + media, hundreds of g) to +-1 mg on a Scout-class balance is doubtful (moisture uptake by the frame alone can exceed 10 mg), and semi-volatile loss before weighing is possible.
- Wang, Ou, Wang, Pan, Park, Krishnakumar, Hua, Romay, Juidici, Chung, Lee, Hong, Park & Pui 2026, "Charge-driven degradation of residential electret HVAC filters under wildfire smoke exposure", Environ Sci Technol 60(38), doi:10.1021/acs.est.6c03046 (WALLED; abstract from Europe PMC, PMID 42916414). Abstract claims: efficiency "can collapse rapidly at particle loadings far below those associated with appreciable pressure drop increases"; "driven primarily by soot-rich particles, which induce rapid and irreversible neutralization of electret charge rather than by progressive mechanical clogging or organic aerosol deposition alone"; filter life in smoke events "reduced from months to days". MATT TO DOWNLOAD - the best current source on composition (soot vs organic) per unit mass.
- Shirman, Zamani & Liu 2025 (Metalmark), "Wildfire smoke: a rigorous challenge for HVAC air filters", arXiv:2505.01622 (open). 17 HVAC media (MERV 10-15), pine-needle smoke ~400,000/cm3, ~1500 ug/m3 (60-380 nm, median ~160 nm), 33 cm/s, 24-28 C, 45-65% RH, ~5 cm2 samples, SMPS 116-365 nm average. Charged media "dropped below 20% quickly", e.g. MERV 13/15 from one maker lost 72% (relative) of efficiency after 80 min; mechanical media <10% loss; charged-media dp essentially unchanged. No deposited mass reported. My estimate: challenge 1.5 mg/m3 x 0.33 m/s x 80 min = 2.4 g/m2, deposited ~0.5-1.5 g/m2 (flag: assumes constant concentration). SEM: "beads on a string" droplet deposits, more coverage on charged media.
- Schumacher, Banda Sanchez, Caspari, Staack & Asbach 2022, Atmosphere 13:1538 (open, mdpi-res PDF): 8 household air cleaners (nominal CADR 300-500 m3/h) aged with 100 3R4F cigarettes = ~3000 mg smoke (30 mg/cigarette by weighing); CADR loss ~10% to ~70% (>7x spread between products); loss strongest for smallest particles; dp change negligible; cites earlier IUTA work that up to 400 cigarettes takes efficiency to the IPA-discharged state (Schumacher et al. 2018 Chem Eng Technol 41:27 - walled). Filter areas not given -> no g/m2. GB/T 18801-2015 CCM uses exactly this 3000 mg tobacco-smoke metric (standards pool).

## 13. Particle charge (loading aerosol) - what the readable data say

- Ji et al. 2002 (entry 3): spray-electrified NaCl (2-3x Boltzmann mean charge) gave the same initial slope (beta ~3.4 m2/g) as Boltzmann-charged NaCl but kept degrading to ln(P/P0) ~1.0 (vs ~0.72), with much smaller delta p rise (more uniform depth deposition).
- Otani et al. 1993 (entry 1): uni-charged vs neutral 0.1 um DOS - fibre charge decay inferred from the neutral data reproduces the charged-droplet curve -> coverage, not neutralisation by the droplets' own charge, is the main cause. Initial beta for charged droplets ~7.5 m2/g (Fig. 11: ln(1.3e-2/2e-3)/0.25 g/m2); for neutral ~1.1 m2/g (Fig. 13, budget-limited). Electrostatic single-fibre efficiency eta_E (eta minus mechanical 0.019, Fig. 13): neutral 0.009 -> 0 by 0.5 kg/m3 (50% lost at ~0.25 kg/m3 = ~0.18 g/m2); uni-charged 0.106 -> 0.08 (0.5 kg/m3) -> 0.056 (0.9) -> 0.026 (1.5) (50% lost at ~0.95 kg/m3 = ~0.67 g/m2). The authors' model takes ONE fibre-charge decay vs deposited mass (fitted on the neutral run) and reproduces the charged run; the different fractional losses follow from capture physics - induced-force (neutral particle) capture falls faster with remaining fibre charge (roughly with its square) than Coulomb (charged particle) capture (roughly linear). Consequence: for the same deposit, the electrostatic gain for NEUTRAL particles - most of an ambient MPPS challenge - disappears first (my reading of Figs 11-13 and the paper's Eqs. 7/11).
- Walsh & Stenhouse 1998 AS&T 29:419 (walled; abstract text known only via search snippet - unverified): experiments on particle size and charge "prove conclusively that the reduction in filtration efficiency of this material during loading is not a charge neutralization process."
- Order-of-magnitude check (my arithmetic): one elementary charge cancels fibre charge over e/sigma = 1.6e-19/(5-30e-6 C/m2) = (0.07-0.18 um)^2. A Boltzmann-charged 0.1-0.3 um particle carries <~1 e on average, so its carried charge can cancel roughly its own footprint - too little to explain the observed potency of salts (entry 14) and far too little for oil films. Neutralisation by carried charge can dominate only for strongly or unipolarly charged aerosols (spray-electrified lab aerosols, fresh flame/soot smoke at tens of e per particle) and for conductive deposits (soot) that short out charge patches.

## 14. Models of loading-induced decay (Kanaoka group; Brown) - what is readable

- Sae-lim, Tanthapanichakoon & Kanaoka 2005, "Structural improvement to quadruple service life of a high-efficiency electret filter", Sci Technol Adv Mater 6:307-311 (open: https://www.nstda.or.th/openarchive/wp-content/uploads/tainacan-items/2494/117745/Structural-improvement-to-quadruple-service-life-of-a-high-efficiency-electret-filter.pdf). Eqs. 1-2: eta = eta0E(1 + lambdaE m) + eta0M(1 + lambdaM m), lambdaE = b ln m + g (electrical enhancement factor vs dust load m per unit filter volume, kg/m3) - "the electrical collection efficiency can be approximated as a logarithmic function of the dust load"; fitted to published experiments (Otani 1993, Walsh & Stenhouse, Ji 2003) in Sae-lim's thesis (Chulalongkorn 2005, https://digital.car.chula.ac.th/chulaetd/65624 - PDF server unreachable from here) and in Sae-lim et al. 2006 J Aerosol Sci 37:228 (walled). Coefficient values NOT obtained. Simulation (df 20 um, dp 1 um, alpha 0.04, 0.1 m/s, fibre charge 1.2e-4 C/m2): grading packing density loose-front/dense-back quadruples dust load to clogging while max penetration only doubles (to 4%) - deposit distribution in depth matters.
- Maneeintr 2000 thesis abstract (Chula ETD 63599): stochastic dendrite simulation; eta/eta0 linear in dust load for weak electrical forces; two linear regimes (low/high load) for strong forces.
- Brown et al. 1988 abstract claims (via a search-engine summary of the OUP abstract - NOT verified against the paper): "Equal masses of different aerosols are found to cause widely different changes in performance. In general dry dusts cause little loss of performance"; "Different types of filter material are degraded at about the same rate, and this is shown to be consistent with a charge-screening process"; coal-tar fume effect "consistent with solvent action on soluble polymers". If confirmed, beta is mainly a property of the AEROSOL (and test size), not of the media type.
- Brown 1993, "Air Filtration" (Pergamon) - the standard monograph; on archive.org lending only (https://archive.org/details/airfiltrationint0000brow). Matt can borrow it for the electret-loading chapter.

---

# SYNTHESIS (my analysis - every step below is mine unless a source is named)

## A. What physically does it (ranked by evidence I could read)
1. Liquid/tarry deposits spreading over fibres - dominant for oils and smoke. Otani 1993 (DOS: coverage, not droplet charge, explains both neutral and charged runs); Shimokawa 2023 (tobacco smoke spreads; an oleophobic treatment that keeps droplets spherical buys ~2.5x capacity); Shimokobe 1986 (incense tar coats fibres); Shirman 2025 and Wang 2026 (smoke: "beads on a string", charge loss without dp rise).
2. Screening by solid deposits sitting on the charge - Brown 1988 (abstract: "consistent with a charge-screening process"); Walsh & Stenhouse 1998 (abstract: "not a charge neutralization process"); potency rises with deposit permittivity/conductivity (Walsh & Stenhouse via Ji 2002: TiO2, eps 90, degrades faster than stearic acid, eps 2.2) and with adsorbed water on hygroscopic deposits (Mahdavi 2015).
3. Neutralisation by charge carried in - real but secondary for near-Boltzmann aerosols (my e/sigma estimate, entry 13); can dominate for strongly charged or conductive smoke (Wang 2026 abstract: soot, "rapid and irreversible neutralization"; Holder 2022).
4. Bulk charge decay unrelated to loading (heat above ~70-90 C, heat plus humidity, solvents) - slow at room conditions (entry 8).

## B. Scaling law that fits the readable data
- Early phase (Brown 1988, as reproduced by Ji 2002): ln P_T(M) - ln P_T(0) = beta_TL x M, M in g per m2 of media. beta is independent of thickness (model property) and - per Brown's abstract - roughly independent of media type; it depends on the loading aerosol and on the test particle (it scales with how much of the test particle's capture is electrostatic: Otani's charged vs neutral runs).
- Measured / derived beta (m2/g), initial slope:
  - coal dust on resin wool ~0.03; foundry lead fume ~1.0 (Brown 1988 via Ji; units inferred)
  - stearic acid 0.46-1.4 um on 92 g/m2 tribo media, 0.3 um test: ~0.08 (from the brief's Walsh & Stenhouse numbers: ln(0.31/0.16)/8)
  - indoor ambient aerosol (0.07 um mean), thick clean-room electret, 0.3 um test: ~0.2 (Ando 1993; loading axis uncertain). Cross-check: the US5496507 ambient run gives ~0.2 IF ambient PM was ~20 ug/m3 (my assumption; no mass reported).
  - 0.07 um NaCl, cabin media, overall count: 3.4 (Ji 2002, stated)
  - tobacco smoke, 99.8% PP meltblown, 0.3-0.5 um test: ~3.8 untreated, ~0.8 oleophobic (Shimokawa 2023)
  - 0.1 um DOS, charged test droplets: ~7.5 (Otani 1993)
  - open-burn smoke on MERV 13: end-point tens of m2/g (Holder 2022; mass doubtful)
- Spread: ~0.03 to ~8 m2/g (x250) robustly, perhaps x1000 with soot. Size alone explains little: projected area per gram 3/(2 rho d32) is ~3.5 m2/g for Ji's NaCl vs ~2 m2/g for 0.8 um stearic acid (x1.75) against a ~x40 beta difference. The rest is composition (wetting oil/tar >> hygroscopic salt >> dry low-permittivity organics or mineral dust) and the electrostatic share of the test particle's capture (velocity, fibre size, charge).
- Exhaustion: the law runs until the electrostatic part of -lnP is gone; then mechanical gain (dendrites) wins for solids, while liquids sit at the discharged level. Mass to lose half the electrostatic log-PF (M50), readable data:
  - 0.1 um DOS, 1.3 um-fibre medium: ~0.18 g/m2 (neutral test) / ~0.67 g/m2 (charged test) (Otani)
  - 0.07 um NaCl, cabin media: ~0.2 g/m2 (~60% lost by 0.24 g/m2; Ji)
  - tobacco smoke, PP meltblown: ~0.7 g/m2 untreated, ~2.6 g/m2 oleophobic (Shimokawa)
  - incense smoke, 4 mm 33 um PP at 40 cm/s: ~6-7 g/m2 (EF-1), ~25-30 g/m2 (EF-2) (Shimokobe)
  - indoor ambient, clean-room electret: front-face surface potential halved at ~4 g/m2 (Ando; uncertain axis)
- Coverage collapse (my model, consistent with A2 and with Brown's thickness-independence): if each gram of deposit deactivates k x (its projected area) of fibre surface, the electrostatic gain is exhausted at M* ~ S_f/(k a), where S_f = fibre surface per m2 of media = 4 BW/(rho_f d_f) and a = projected area per gram of deposit. For spreading liquids write a = 1/(rho h), so M* ~ S_f rho h. Back-calculated: DOS h ~3 nm (Otani, S_f 134 m2/m2); incense smoke h ~400 nm (Shimokobe, S_f 53); tobacco h ~50 nm if S_f ~50 (assumed). Solids: k ~0.3-0.9 for stearic acid (Walsh numbers, S_f ~17 estimated), ~10-20 for 0.07 um NaCl (Ji, S_f assumed 10-20). So capacity per m2 of media should scale with fibre surface per m2 (basis weight / fibre diameter) - finer, heavier media last longer per m2 - and composition sets k or h. A hypothesis built on 4-5 datasets, with assumed S_f in two; none of the readable papers tests it directly.

## C. Modifiers, quantified where possible
- RH during loading (hygroscopic salt): NaCl on an N95 over 6 h, MPPS -lnP +26-30% at 10% RH vs -8 to -11% at 50-80% RH (Mahdavi 2015) - RH flips the sign of the loading effect, a ~35-40 point swing in -lnP; 50% RH (below the NaCl DRH of 75%) already shows it.
- RH without deposits: nil over 6 h to 33 d at room temperature (Otani; Ando 60 C/95%/1 week; Mahdavi; Stoll); liquid water films screen reversibly (Stoll: apparent surface charge x1/5 to x1/14 at +25% water, recovers dry); irreversible loss needs heat (Liu 2020: 110 C + 90% RH for 24 h, 95.5% -> 38.2%).
- Time after loading: Moyer & Bergman 2000 (abstract): weekly 5 mg NaCl doses kept degrading N95s week on week with no dp warning; controls stored on a desk first degraded at the same rate once dosed - storage alone mattered much less. Full text walled. Partial recovery (Raynor & Chae 2004) is consistent with drying of hygroscopic or water-bearing deposits (Stoll's reversible water screening; Mahdavi's RH effect) - my inference.
- Loading-particle charge: 2-3x Boltzmann charge left the initial slope unchanged but deepened the total loss ~40% (ln ratio 1.0 vs 0.72) and cut the dp rise (Ji 2002). Strongly charged fresh smoke may degrade by neutralisation (Holder hypothesis; Wang 2026).
- Media: oleophobic surface (wetting tension 37 -> <30 mN/m): x2.5 tobacco capacity (Shimokawa); C4F8 plasma fluorination: no change in end state at 50 g/m2 DOP challenge (Roh 2019). Sub-micron fibres: electrostatic loss masked by fast mechanical gain for solids (Sun & Leung 2020; Otani). Charge density: higher sigma gives more log-PF to lose (Ando Fig. 6: -lnP 3 -> 13 for sigma 0 -> 9 uC/m2), not obviously slower loss. Deeper charge distribution delays decay (Kerner 2021, simulation only). Charge-control and thermal-stability additives: no loading data read.
- Lab vs real world: ambient aerosol degraded a clean-room electret ~7x faster per gram than JIS-15 test dust (Ando); ambient beta ~0.2 m2/g vs lab fine NaCl 3.4 and tobacco 3.8 - lab fine salts and smoke are 10-20x harsher per gram than mixed ambient PM in the readable data, while fresh combustion smoke may be far harsher than either.

## D. Walled sources that would settle the open points (Matt to download)
1. Brown, Wake, Gray, Blackford & Bostock 1988, Ann Occup Hyg 32:271, https://doi.org/10.1093/annhyg/32.3.271 - beta for many industrial aerosols; media-independence claim.
2. Walsh & Stenhouse 1997, J Aerosol Sci 28:307, https://doi.org/10.1016/S0021-8502(96)00434-X and 1998, AS&T 29:419, https://doi.org/10.1080/02786829808965580 (free to read on tandfonline but Cloudflare-walled for me) - size, charge, composition (TiO2 vs stearic acid), "not neutralisation".
3. Li, Chen, Zhou & Chen 2020, Build Environ 171:106669, https://doi.org/10.1016/j.buildenv.2020.106669 - RH and particle hygroscopicity on electret HVAC media ageing.
4. Wang, Lin & Zhang 2020, Build Environ 179:106962, https://doi.org/10.1016/j.buildenv.2020.106962 - particle charging, media, humidity, aerosol type on electret loading.
5. Cai, Lu & Zhang 2021, Powder Technol 382:133, https://doi.org/10.1016/j.powtec.2020.12.061 - degradation mechanisms during neutral particle loading.
6. Wu, Cai & Zhang 2022, Build Environ 207:108554 (https://doi.org/10.1016/j.buildenv.2021.108554); Cai, Cai & Zhang 2024, Particuology 93:87 (https://doi.org/10.1016/j.partic.2024.06.007); Cai, Cai & Zhang 2025, Sep Purif Technol 362:131892 (https://doi.org/10.1016/j.seppur.2025.131892) - loading models for neutral and charged PM2.5.
7. Wang ... Pui 2026, Environ Sci Technol 60(38), https://doi.org/10.1021/acs.est.6c03046 - soot-driven neutralisation.
8. Ji, Bae, Kang & Hwang 2003, J Aerosol Sci 34:1493, https://doi.org/10.1016/S0021-8502(03)00103-4 - English version of entry 3, likely with the discharged-media reference.
9. Tanthapanichakoon et al. 2003, J Aerosol Sci 34:1505, https://doi.org/10.1016/S0021-8502(03)00104-6; Sae-lim et al. 2006, J Aerosol Sci 37:228, https://doi.org/10.1016/j.jaerosci.2005.05.001 - correlation coefficients for eta_E vs dust load.
10. Moyer & Bergman 2000, AOEH 15:600, https://doi.org/10.1080/10473220050075608 - time/storage between loadings.
11. Barrett & Rousseau 1998, AIHAJ 59:532 - NaCl vs DOP loading of 3M N/R/P media.
12. Zhou et al. 2025, Build Environ 288:114017, https://doi.org/10.1016/j.buildenv.2025.114017 - MPPS shift in use at different RH.
13. Soft Matter 2024, https://doi.org/10.1039/d4sm01105h (open access, Cloudflare-walled for me) - droplets on electret fibres.
14. Hayashi & Kitagawa 2017, J Soc Powder Technol Japan 54:406 (subscriber-only) - tobacco-smoke durability by surface modification.
15. Schumacher et al. 2018, Chem Eng Technol 41:27 - new vs artificially aged electret filters in air cleaners (cigarette smoke to the IPA-equivalent state).
16. Janssen, Bidwell, Mullins & Nelson 2003, J Int Soc Respir Prot 20:71-80 and 81-90 - electret efficiency after real workplace aerosols.
