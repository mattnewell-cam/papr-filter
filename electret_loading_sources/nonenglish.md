# Non-English literature: electret filter degradation under particle loading (pool `nonenglish`)

Conventions: E = fractional efficiency, P = 1 - E. "Retained -lnP" = ln P_loaded / ln P_initial. "Electrostatic part lost" = (ln P_loaded - ln P_initial)/(ln P_discharged - ln P_initial). All g/m2 are per m2 of media area unless stated. Curve readings were digitised from the canvas pixels where marked "digitised" (precision about +/-0.01 in E); otherwise read by eye (+/-0.02-0.03).

---

## 1. IUTA / TU Kaiserslautern, IGF 19145 N final report (German, 2020)

Source: Schumacher S., Antonyuk S. et al., "Experimentelle und numerische Untersuchungen zum Abscheideverhalten neuer und gealterter Elektretfilter" (Experimental and numerical studies of the separation behaviour of new and aged electret filters), Schlussbericht IGF-Vorhaben 19145 N, IUTA Duisburg + TU Kaiserslautern, 14 Jan 2020. https://www.iuta.de/igf-docs/abschlussbericht_19145.pdf (open). Note PDF page = report "Seite" + 1.

### 1a. Flat-sheet F1 loaded with neutralised NaCl (section 3.8.1, Seite 99-103, Abb. 53, 54; aerosol Abb. 13 Seite 25)
- Media F1: PP meltblown, corona charged; 133 +/- 7 g/m2; fibre mean 31.8-32.8 um (modal 32.5 um); thickness 636 um; porosity 76.7 %; air permeability 2190 l/m2/s at 200 Pa (Tabelle 4, Seite 13).
- Loading aerosol: NaCl from Collison atomiser, diffusion-dried (solid cubic crystals), neutralised with Kr-85 (bipolar equilibrium: 72 % neutral, 12 % +1, 16 % -1). Total 1e6 /cm3, 14-500 nm, mode ~35 nm (Seite 24). I digitised Abb. 13: CMD 31 nm, mass-median 0.11 um, diameter of average mass d30 = 55 nm; 53 % of mass above 0.1 um, 16 % above 0.2 um, <1 % above 0.3 um.
- Velocity: 0.02 m/s (stated for FS2 flat-sheet tests, Seite 123; consistent with N = c v t: 560e6 /mm2 in 8 h at 1e6 /cm3 gives 1.94 cm/s).
- Loading: N incident = 560e6 /mm2 (8 h), 1680e6 (24 h), 2240e6 (32 h), 3360e6 (48 h), 5040e6 (72 h). Report's own mean deposition probability over 14-500 nm and 0-72 h = 0.57 (Seite 102).
- Deposited mass (my estimate, not in report): particle mass at d30 = 2.165 g/cm3 x pi/6 x (55 nm)^3 = 1.89e-16 g (mobility diameter treated as volume-equivalent; cubic NaCl would make this ~20 % lower). Mass conc = 189 ug/m3. Deposited = N x E(mass-relevant sizes, ~0.55-0.68 averaged over the run) x 1.89e-16 g -> 8 h 0.07, 24 h 0.20, 32 h 0.26, 48 h 0.37, 72 h ~0.52 g/m2. Uncertainty roughly +/-40 % (shape of tail, cubic shape factor, mean efficiency).
- Efficiency test: same NaCl aerosol, SMPS, count-based, fractional, 2 cm/s; discharged reference = 24 h in IPA-vapour-saturated air per ISO 16890-4.
- Digitised Abb. 53 (fractional efficiency):

| d (um) | Initial | 8 h (~0.07 g/m2) | 24 h (~0.20) | 32 h (~0.26) | 48 h (~0.37) | 72 h (~0.52) | IPA-discharged |
|---|---|---|---|---|---|---|---|
| 0.035 | 0.62 | 0.60 | 0.59 | 0.57 | 0.54 | 0.51 | 0.46 |
| 0.05 | 0.63 | 0.61 | 0.59 | 0.55 | 0.52 | 0.47 | 0.36 |
| 0.10 | 0.72 | 0.675 | 0.605 | 0.544 | 0.487 | 0.41 | 0.21 |
| 0.15 | 0.77 | 0.705 | 0.60 | 0.53 | 0.46 | 0.39 | 0.15 |
| 0.20 | 0.79 | 0.717 | 0.596 | 0.52 | 0.44 | 0.36 | 0.13 |
| 0.30 | 0.79 | 0.72 | 0.60 | 0.505 | 0.42 | 0.37 | 0.12 |

- At 0.2 um: -lnP initial 1.56, discharged 0.139. Retained -lnP: 8 h 0.81, 24 h 0.58, 32 h 0.47, 48 h 0.37, 72 h 0.29. Electrostatic part lost: 0.21, 0.46, 0.58, 0.69, 0.78.
- Pressure drop unchanged after 72 h (Abb. 54: ~5-6 Pa at 0.1 m/s, both curves overlap), so no cake; all loss is electrostatic.
- Report's interpretation (Seite 103): charge carried in by deposited particles = 1.41e-10 C per mm2 of media = ~35 % of the fibre charge (3.95e-10 C/mm2 from a model-fitted surface charge density 25e-6 C/m2 - that density is back-fitted to the initial efficiency, flag). Shadowing by particle cross-section judged negligible. Quote: "Daher scheint die Neutralisation der Faserladung durch die Ladung der abgeschiedenen Partikel der dominierende Effekt ... zu sein" (Thus neutralisation of the fibre charge by the charge of the deposited particles appears to be the dominant effect). Also: after 72 h efficiency still above the IPA level -> "keine vollständige Entladung" (no complete discharge).
- Larger sizes lose first, smaller later (Seite 101).

### 1b. Pleated cabin filters loaded with DEHS vs glycerol vs NaCl (section 3.8.2, Seite 104-115, Abb. 55-62)
- Filters: three car cabin filters, identical geometry 307.5 x 212 mm, 60 pleats x 28 mm, media area 0.71 m2 (Seite 14). Type F1: PA nanofibre layer on bicomponent PE/PP spunbond, 110 +/- 10 g/m2, 0.9 mm. F2: PP meltblown + PET carrier, 115 +/- 17 g/m2, 0.7 mm. F3: PP meltblown, 140 +/- 15 g/m2, 1.15 mm. All corona charged (Tabelle 5).
- Flow 200 m3/h -> 7.8 cm/s through media. Test/loading aerosols neutralised (Kr-85) DEHS, glycerol (heated atomiser, similar size distribution to DEHS), NaCl. Raw-gas count 8e4 /cm3. SMPS 0.04-1 um, count-based.
- Mass: report estimate "in der Größenordnung von 0,5 g" (of the order of 0.5 g) per single fractional-efficiency measurement (~20 min) for DEHS and glycerol, extrapolated from a lognormal fit and dominated by droplets > 1 um; weighed gain ~2 g after four consecutive measurements (Seite 111). Per media area: ~0.7 g/m2 per measurement / per 20 min; ~2.8 g/m2 after four. Order-of-magnitude only.
- Abb. 62 (total count efficiency during DEHS dosing, read by eye): F1 0.68 -> 0.60 (20 min, ~0.7 g/m2) -> 0.55 (40) -> 0.50 (60 min, ~2.1 g/m2); F2 0.84 -> 0.78 -> 0.72 -> 0.68; F3 0.79 -> 0.72 -> 0.67 -> 0.63. Retained -lnP at 60 min: F1 0.61, F2 0.62, F3 0.64. Report: "während einer typischen Messzeit von 20 min ... die Gesamteffizienz bereits um 10 Prozentpunkte reduziert" (within a typical 20-min measurement the total efficiency already falls by 10 percentage points).
- Abb. 61 (repeated DEHS measurements, each ~0.7 g/m2; read by eye at 200 nm): F2 DEHS 1x 0.73, 3x 0.50, 9x 0.18, IPA-vapour 0.20. F3 DEHS 1x 0.68, 3x 0.47, 12x 0.23, IPA 0.15. F1 DEHS 1x 0.62, 3x 0.40, 4x 0.32, IPA 0.42 (F1 goes below the IPA state; report says the ISO 16890-4 vapour treatment does not fully discharge F1). Fresh reference at 200 nm from Abb. 58 (neutralised NaCl / glycerol): F2 ~0.92 / ~0.95; F3 ~0.83 / ~0.90.
  - F3 at 200 nm, NaCl as fresh reference: electrostatic part lost 0.39 (1x, ~0.7 g/m2), 0.72 (3x, ~2.1 g/m2), 0.94 (12x, ~8.5 g/m2). F2: 0.53 (1x), 0.80 (3x), ~1.0 (9x, ~6.3 g/m2).
  - Saturation (no further change) reached after 4 (F1), 9 (F2), 12 (F3) DEHS measurements = roughly 2.8, 6.3, 8.5 g/m2. End state ~equal to IPA-vapour discharged state. Pressure drop did not change noticeably.
- Glycerol: two consecutive glycerol measurements gave identical curves - "Die Beladung mit Glycerin hat also keinen Einfluss auf die Abscheideeffizienz" (loading with glycerol thus has no effect on the efficiency) at ~0.7-1.4 g/m2 (Abb. 60, Seite 110). Glycerol efficiency ~= NaCl efficiency (Abb. 58). Dielectric constant (glycerol 42.5 vs DEHS 5.1) ruled out; report attributes difference to wetting: DEHS forms barrel droplets enclosing PP fibres, glycerol sits on the side ("clam-shell") - Seite 114. Mechanism stated as hypothesis, not tested.
- Report's note: in an ISO 16890 HVAC test (15 cm/s, 600 /cm3, 20 min) the DEHS dose per area is only 1-2 % of theirs.

### 1c. Humidity/temperature, IPA, storage (sections 3.9-3.10)
- 3 h at 80 % RH and 23/40/60 C: surface potential fell up to 70 % but fractional efficiency fell only "einige Prozentpunkte" (a few percentage points) (Abb. 66-67, Seite 119-121).
- Medium of F1, 3 h: no efficiency change at 20-60 C (87 % RH) or at constant 15 g/m3 absolute humidity up to 80 C/5 % RH; clear drop only at 80 C + 87 % RH (253 g/m3) (Abb. 68, Seite 122-123).
- Storage 8-10 months under standard conditions: no significant change in fractional efficiency for either cabin filters (0.08 m/s) or flat sheets (0.02 m/s) (Seite 123).
- IPA liquid soak (5 min) vs ISO 16890-4 vapour (24 h): neither reliably complete; F2/F3 needed two soaks to match vapour; F1 vapour less complete than soak (Seite 115-119).

---

## 2. Li Shihang et al. 2022, China University of Mining and Technology (Chinese)

Source: 李世航, 温国祥, 王路宇, 吕伟鹏, 刘凌妤, "驻极体滤料的空气湿度和静电效应影响机理研究" (Study on influence mechanism of air relative humidity and electrostatic effect of electret filter media), 西安建筑科技大学学报(自然科学版) J. Xi'an Univ. Arch. & Tech. (Nat. Sci.) 54(5):734-741, Oct 2022. DOI 10.15986/j.1006-7930.2022.05.012. Landing page https://jdxbz.xauat.edu.cn/thesisDetails#1006-7930(2022)05-0734-08 (abstract open; full-text PDF via the site's own "阅读全文PDF" button, read in the browser).

- Media #3: commercial 3M MERV 13 residential pleated filter (Fig. 4 photo shows the 3M label), electret; fibre 13.1 +/- 0.9 um; thickness 0.45 mm; charge density 7.0e-5 C/m2 (method not stated); "filtration efficiency" 86.6 % (test basis not stated); initial dp 7.9 Pa at 10 cm/s (Tab. 1, p.736). Basis weight not given. (Also #1 HEPA purifier media 2.0 um, 0.11 mm, 99.9 %, 90.9 Pa; #2 lab composite.)
- Real-environment ageing: #3 "在真实环境中使用了5、6和7个月" (used in the real environment for 5, 6 and 7 months) - samples #3-1, #3-2, #3-3. Location, device and face velocity not stated.
- Mass by weighing (p.737): "滤料#3-1、#3-2和#3-3的质量较未使用滤料分别增加3.55、3.96和4.76 g/m²" (mass increased by 3.55, 3.96 and 4.76 g/m2 vs unused) -> 0.71, 0.66, 0.68 g/m2 per month. dp 7.47 Pa (#3-0) -> 10.07, 10.44, 11.03 Pa (0.50-0.52 Pa/month).
- Test: discharged (neutralised) monodisperse NaCl from DMA, 15-500 nm (data to ~700 nm), UCPC (count), 10 cm/s, 30 % RH. Discharge: IPA-vapour-saturated 24 h per ISO 16890-4.
- Fig. 7 (p.739), read by eye, E (%):

| d (nm) | #3-0 fresh | #3-1 5 mo 3.55 g/m2 | #3-2 6 mo 3.96 | #3-3 7 mo 4.76 | discharged (#3-0 / #3-3) |
|---|---|---|---|---|---|
| 20 | 65 | 65.5 | 65 | 64.5 | 43 |
| 50 | 70 | 62 | 58 | 56.5 | 18 |
| 100 | 80 | 61 | 53 | 49.5 | 9.5 |
| 200 | 85.5 | 61 | 51 | 45 | 6 |
| 300 | 86.5 | 61 | 50.5 | 42 | 6 / 7 |
| 500 | 87 | 65 | 54 | 43.5 | 10 / 13 |
| 700 | 88 | 70 | 57 | 46 | 15 / 21 |

  - At 300 nm: -lnP fresh 2.00, discharged 0.062. Retained -lnP: 0.47 (5 mo), 0.35 (6 mo), 0.27 (7 mo). Electrostatic part lost: 0.55, 0.67, 0.75. At 100 nm: lost 0.44 (5 mo).
  - MPPS moved from ~20 nm to ~300 nm.
- Lab loading (Fig. 8, p.739-740): same media loaded in the lab at 10 cm/s, 30 % RH, to 1.1, 2.1, 3.8, 6, 8, 9, 10 g/m2; loading time < 1 day. Loading aerosol composition not separately stated; the only generator described is a TSI 9302 atomiser with NaCl solution, so presumably polydisperse NaCl (flag). Read by eye, E (%):

| d (nm) | 0 | 1.1 | 2.1 | 3.8 | 6 | 8 | 9 | 10 g/m2 |
|---|---|---|---|---|---|---|---|---|
| 20 | 62 | 70 | 76 | 82 | 88 | 94 | 96 | 98 |
| 100 | 84 | 83 | 78 | 73 | 78 | 86 | 90.5 | 96 |
| 300 | 90 | 86 | 82 | 77 | 81 | 91 | 95 | 97.5 |

  - Minimum at 3.8 g/m2, then mechanical recovery ("当加载质量小于3.8 g/m²时，滤料#3的过滤效率降低，当加载质量大于3.8 g/m²时...增加"). At 300 nm and 3.8 g/m2: retained -lnP 0.64, electrostatic part lost ~0.37 (vs 0.55 for the 5-month field sample at 3.55 g/m2). Note the lab "0" curve (90 % at 300 nm) differs from Fig. 7's fresh #3-0 (86.5 %); different sample/aerosol.
  - Key claim: "在相似的加载质量下，实验室中加载滤料的过滤效率明显高于真实环境中加载滤料的过滤效率" (at similar loaded mass, lab-loaded media have clearly higher efficiency than field-loaded media), attributed to > 5 months' exposure vs < 1 day.
- Humidity: 10 -> 60 -> 90 -> 10 % RH (Fig. 5) and 24 h water immersion (Fig. 6) did not change initial efficiency or dp for any media.

---

## 3. Otani, Emi (Kanazawa Univ.) & Mori 1992 (Japanese)

Source: 大谷吉生, 江見準, 森治朔, 「エレクトレットフィルターの初期捕集効率と集塵性能の安定性」 (Initial collection efficiency of electret filters and stability of their dust-collection performance), 化学工学論文集 Kagaku Kogaku Ronbunshu 18(2):240-247 (1992). https://www.jstage.jst.go.jp/article/kakoronbunshu1975/18/2/18_2_240/_pdf (open). English counterpart is KONA 11 (1993); the figures below are from the Japanese original.

- Media: PP electret fibres df = 1.3 um, eps_f 2.2; L = 0.71 mm; packing 0.0612 (p.243). Basis weight not stated; alpha x L x rho_PP = 0.0612 x 0.71 mm x 910 kg/m3 = ~40 g/m2 (my calculation). Charging method not stated. Mean fibre charge density 5.1 uC/m2 is back-fitted to initial-efficiency data (p.244) - flag.
- Test: DMA-classified monodisperse DOS (dioctyl sebacate, rho 920, eps_p 4.01), CNC count, flat sheet, u = 0.05 m/s in the loading figures. Loading with the same 0.1 um DOS (uncharged or singly charged) and with singly charged monodisperse solid iron alum (鉄みょうばん).
- Humidity (Fig. 10, p.245): ~800 h at 90 % and at 20 % RH, P for 0.1 um singly charged DOS unchanged at ~4e-3. "ほぼ1カ月間，湿度90%，20%の空気に曝しても，透過率は初期値のままであり" (even ~1 month in 90 % or 20 % RH air left penetration at its initial value).
- Fig. 11 (p.245), P vs incident mass Ci*u*t (kg/m2 of filter = media, flat sheet), read by eye on the log axis (dp and u for Fig. 11 not printed on the figure; presumably as Fig. 12, 0.1 um and 0.05 m/s):
  - Singly charged DOS droplets: P 2.5e-3 (0) -> 1e-2 (0.2 g/m2) -> 2e-2 (0.4) -> 4e-2 (0.55) -> 0.1 (0.8) -> 0.15 (1.0) -> 0.22 (1.12 g/m2). dp ~35 Pa constant. -lnP retained 0.65 at 0.4 g/m2, 0.32 at 1.0 g/m2. With P = 0.46 as the no-electrostatics reference (Fig. 13 dashed line, eta = 0.017 -> P = exp(-45.3 eta), my conversion), electrostatic part lost 0.40 at 0.4 g/m2 and 0.78 at 1.0 g/m2 incident.
  - Singly charged solid iron alum: P 1e-3 -> ~1e-4 at 1.1 g/m2 (efficiency rises); dp ~35 -> ~100 Pa by 1.15 g/m2. Paper: with 1.3 um fibres, interception growth by deposits outpaces neutralisation.
- Fig. 12-13 (p.245-246): uncharged 0.1 um DOS (Ci 3-20 ug/m3, ~800 h). Single-fibre efficiency falls from 0.027 to the measured no-electrostatics value (~0.017-0.019) by accumulated mass m = 0.5 kg/m3 of filter volume. Quote: "m=0.5kg/m3程度で、無帯電繊維の初期捕集効率（実測値）と等しくなり、誘起力による捕集が全くなくなっている" (at about m = 0.5 kg/m3 it equals the measured initial efficiency of an uncharged fibre: capture by the induced (polarisation) force has completely disappeared). Conversion: 0.5 kg/m3 x 0.71 mm = 0.36 g/m2 of deposited DOS. So ~100 % of the neutral-particle electrostatic capture was gone at ~0.36 g/m2 of 0.1 um oil on a 1.3 um, ~40 g/m2 medium. Charged-droplet single-fibre efficiency 0.12 -> ~0.045 at m = 1.5 kg/m3 (1.07 g/m2).
  - Conclusion (p.246): uncharged and singly charged droplets gave the same rate of charge loss, so the cause is organic droplets wetting/covering the fibre (field shielding) or neutralisation by the organic liquid, not the particles' own charge.

## 4. Toray: Ando, Takahashi, Togashi, Okumura 1993 (Japanese)

Source: 安藤勝敏 他, 「極細繊維ポリプロピレン不織布を用いたエレクトレットフィルターの特性」 (Properties of electret filters made of nonwoven fabrics of ultrafine PP fibres), 繊維学会誌 Sen-i Gakkaishi 49(6):323-330 (1993). https://www.jstage.jst.go.jp/article/fiber1944/49/6/49_6_323/_pdf (open).

- Media 6-EL: PP ultrafine nonwoven df 1.94 um, packing 0.171, H 0.64 mm, surface charge density 9.0e-10 C/cm2 (Table 1, p.325). Basis weight ~100 g/m2 (my alpha x H x rho). Uncharged twin (No.1) penetration ~5e-2 near 0.2 um at 2.5 cm/s (Fig. 4). Clean-room (ULPA-class) electret.
- Test at 0.3 um, 2.5 cm/s; flat sheet; x-axis Ci*v*t = incident g/m2.
- JIS-15 test dust (mean 0.8 um, solid, 13 mg/m3), Fig. 12 p.328: P fell from ~1.5e-7 to ~3e-8 by 5 g/m2 and stayed; dp 80 -> 480 Pa at 30 g/m2 (surface cake); upstream surface potential unchanged (Fig. 14).
- Room air (大気塵, mean 0.07 um, 0.04 mg/m3), Fig. 15 p.329, read by eye on the log axis: P 7.6e-7 (0) -> 9e-7 (1 g/m2) -> 1.3e-6 (~4 g/m2) -> peak ~1.3-2e-6 near 4.5-5 g/m2 -> 5e-7 (7.5) -> 5e-8 (10 g/m2). dp 60 -> 160 Pa at 10 g/m2. -lnP 14.1 -> ~13.4 at the peak (0.95 retained); with ~0.06 as the uncharged P, electrostatic part lost only ~5-8 % at the worst point. Surface-potential retention (Fig. 17): downstream face 0.75 (1 g/m2), 0.4 (5), 0.12 (10 g/m2); upstream face 0.7 (5), 0.58 (10). Quote: "大気塵負荷において、ELフィルターは内部堆積、HEPAは表層堆積を示す" (under atmospheric-dust loading the EL filter shows depth deposition, HEPA surface deposition); penetration "一度増加し、その後反転して減少する" (first rises, then reverses and falls).

## 5. Hitachi: Shimokobe & Inoue 1986 (Japanese)

Source: 下河辺伊久夫, 井上雅貴, 「エレクトレットフィルタの煙粒子捕集特性」 (Collection performance of electret filter for smoke particles), エアロゾル研究 Earozoru Kenkyu 1(3):186-192 (1986). https://www.jstage.jst.go.jp/article/jar/1/3/1_3_186/_pdf (open).

- Media (Table 4, p.187): PP nonwoven, cylindrical fibres; EF-1 df 33 um, L 4 mm, alpha 0.11; EF-2 df 33 um, L 4 mm, alpha 0.12; uncharged SF df 28 um, alpha 0.11. Basis weight ~400 g/m2 (my alpha x L x rho). dp 59 (SF), 40 (EF-1), 57 Pa (EF-2) at 0.4 m/s, unchanged during loading.
- Aerosol: incense (joss-stick) smoke, 28.5 mg smoke per stick (Table 1), "含水" (water-containing) sub-micron particles; 8.5-255 mg/m3; 25-30 C, 50-70 % RH; u = 0.4 m/s (40 cm/s); 46.6 cm2 flat sample (Table 2).
- Efficiency = gravimetric mass efficiency, E = captured / incident mass (eq. 1).
- Fig. 4 (p.188), E vs captured g/m2 (read by eye): EF-2 0.40 (~12 g/m2, start of curve) -> 0.34 (16) -> 0.21 (31) -> 0.11 (40) -> 0.085 (45) -> 0.065 (53 g/m2). EF-1 0.28 (~2) -> 0.15 (8) -> 0.13 (10) -> 0.09 (21) -> ~0.07 (30). Uncharged SF flat at 0.05-0.06.
  - Electrostatic part lost (SF as reference): EF-2 0.60 at 31 g/m2, 0.87 at 40 g/m2; EF-1 0.70 at 10 g/m2, 0.86 at 21 g/m2.
  - Quote: "エレクトレット繊維表面が煙粒子に被れ，表面電荷は減少し，E＝0.05ではほとんど消失している" (the electret fibre surface is covered by smoke particles, the surface charge falls, and at E = 0.05 it has almost entirely gone). SEM (Fig. 5): fibres uniformly tar-coated.
- Context: coarse 33 um fibres, 400 g/m2, 40 cm/s, low capture (E 0.06-0.4); fibre surface ~53 m2 per m2 of media vs ~134 for Otani's 1.3 um medium.

## 6. Toyobo Elitolon: Hayashi 2008 and Ueda, Moriguchi, Hayashi 2009 (Japanese; manufacturer data)

Sources: 林敏昭, 「エレクトレットフィルター「エリトロン®」」, 膜 Membrane 33(4):188-191 (2008), https://www.jstage.jst.go.jp/article/membrane/33/4/33_188/_pdf (open). 植田和宏, 森口実紀, 林敏昭, 「エレクトレットフィルター「エリトロン®Rタイプ」の濾過特性」, 繊維機械学会誌 62(2):126-128 (2009), https://www.jstage.jst.go.jp/article/transjtmsj/62/2/62_126/_pdf (open).

- Test (2009 p.126): Japanese national dust-respirator test (2000 MHLW Notice 88): 100 cm2 effective area, 85 L/min (14.2 cm/s), NaCl 31 mg/m3 (Shibata AP-9000) loaded to 100 mg, DOP 64 mg/m3 (TSI 8130) loaded to 200 mg. 1 mg on 100 cm2 = 0.1 g/m2 incident. Efficiency from the mask testers (presumably photometric, mass-weighted - not stated).
- Media: R-type = short-fibre nonwoven with "不織布内部で高密度の電荷" (high-density charge generated inside the nonwoven), mean fibre ~15 um, 150/300/600/900 g/m2, non-halogen flame-retardant polymer (2008 p.190). AA-type = meltblown with injected charge, ~2 um, 30 g/m2.
- DOP, AA-type 30 g/m2 (2008 Fig. 5, linear axis, by eye): E 84.5 % (0) -> 79 % (5.5 g/m2 incident) -> 68 % (10) -> 55 % (13) -> 50 % (14.3 g/m2); dp ~90-100 Pa flat. 2009 Fig. 8 (log-penetration axis; cropped): ~83 % (0.5 g/m2) -> ~77 % (4.5) -> ~61 % (10) -> ~16 % (20.5 g/m2). The two AA curves differ by ~7 points at 10 g/m2 (different runs?). -lnP retained ~0.37 at 14 g/m2 (2008).
- DOP, R-type 300 g/m2 (2009 Fig. 5, cropped and digitised, P %): 0.50 (0.5 g/m2) -> 0.90 (3.4) -> 1.30 (5.3) -> 2.83 (10) -> 5.46 (15) -> 8.71 (18.7) -> 10.4 % (20.6 g/m2 incident); dp 53 -> 57 Pa. -lnP retained 0.67 at 10 and 0.43 at 20.6 g/m2.
- DOP, R-type 600 g/m2 (Fig. 6): P 0.01 % (to 4.6 g/m2) -> 0.02 (5.5) -> 0.03 (9.5) -> 0.05 (14.3) -> 0.10 % (20 g/m2); dp ~107-112 Pa; -lnP retained 0.75. R-type 900 g/m2 (Fig. 7): P <= 0.01 % (instrument floor) throughout to 20 g/m2.
- NaCl, R-type 300 g/m2 (2009 Fig. 1, digitised, P %): 0.039 (0.2 g/m2) -> 0.13 (1.3) -> 0.26 (2.3) -> 0.59 (3.8) -> 1.04 (5.3) -> 1.96 (7.3) -> 3.8 % (10.1 g/m2 incident); dp 45 -> 75 Pa. -lnP retained 0.42 at 10 g/m2: solid NaCl degraded this thick coarse-fibre electret as fast per g/m2 as DOP. R-type 600/900: P stayed <= 0.01 % to 10 g/m2. AA-type with NaCl: P <= 0.01 % but dp 90 -> >1000 Pa by ~5.5 g/m2 (cake).
- No discharged references given.

## 7. Toyobo: Shimokawa 2023 - tobacco smoke on PP meltblown electret, with and without liquid-repellent finish (Japanese)

Source: 下川晃太朗, 「合成繊維ろ材」 (Synthetic fibre filter media), 空気清浄 (J. Japan Air Cleaning Assoc.) 61(3):158-162 (2023). https://www.jstage.jst.go.jp/article/jaca/61/3/61_158/_pdf (open). Same topic as the walled Hayashi & Kitagawa, 粉体工学会誌 54(6):406-409 (2017), https://www.jstage.jst.go.jp/article/sptj/54/6/54_54.406/_article/-char/ja/ (subscription).

- Media: PP meltblown base; three variants (Table 1, p.161): uncharged/untreated (37 mN/m, 19 Pa, 23 %), charged/untreated (37 mN/m, 19 Pa, 99.8 %), charged/surface-treated (<30 mN/m, 20 Pa, 99.7 %); dp and efficiency at 5.3 cm/s for 0.3-0.5 um atmospheric dust (count). Basis weight, fibre size and charging method not given.
- Loading: cigarettes burned in a sealed 1 m3 chamber, smoke then drawn through the filter; captured mass by weighing; efficiency re-measured with atmospheric dust; repeated. Quote: "タバコ煙負荷前後のフィルタの質量差からタバコ煙粒子の捕集量を算出する" (captured smoke mass from the filter mass difference before/after loading).
- Fig. 5 (p.162; cropped and read, +/-1 %), E (0.3-0.5 um) vs captured smoke g/m2:
  - charged/untreated: 99.8 (0) -> 91.0 (1.0) -> 71.9 (1.5) -> 48.9 (2.0) -> 28.1 (2.5) -> 24.7 (2.7) -> 23.6 % (2.9)
  - charged/treated: 99.7 (0) -> ~99.7 (1.0) -> 98.1 (2.0) -> 87.1 (2.9) -> 72.8 (3.7) -> 58.8 (4.5) -> 39.9 (5.7) -> 25.8 (6.9) -> 23.6 % (7.5)
  - uncharged: 22.5-23 % flat to 2 g/m2
  - Electrostatic part lost (uncharged 23 % as discharged reference): untreated 0.64 (1.0 g/m2), 0.83 (1.5), 0.93 (2.0), ~1.0 (2.5); treated 0.33 (2.0), 0.68 (2.9), 0.81 (3.7), 0.89 (4.5), 0.96 (5.7). Half of the electrostatic -lnP gone at roughly 0.8-0.9 g/m2 (untreated) and ~2.4 g/m2 (treated) - interpolated.
  - Quote: "無帯電のフィルタの捕集効率に到達する時のタバコ煙粒子捕集量を比較すると、表面処理によりタバコ煙粒子の捕集量が約2.5倍に増加" (the smoke load at which efficiency reaches the uncharged level rises ~2.5x with the treatment). Also claimed equally effective against DOP oil mist - no data shown.
  - Mechanism (p.161): the smoke particles are liquid at room temperature (water, nicotine, tar) and spread over the fibres (Fig. 6: film on untreated fibres, discrete beads on treated).
- Cites JEM 1467 (Japanese household air purifiers) and GB/T 18801-2015 as standards with tobacco-smoke durability tests (both walled).

## 8. Shinohara (AIST) et al. 2025 - 73-day indoor-air loading and 2-year bus field data (Japanese)

Source: 篠原直秀, 西谷崇, 兼吉輝 (Japan Vilene), 達晃一 (Isuzu), 道志智, 谷英明, 金勲, 「実験室および公共交通機関における中性能フィルターの粒子除去性能とその経時的変化」 (Changes in particle removal performance of medium-performance filters due to usage time), 室内環境 Indoor Environment 28(2):137-141 (2025). https://doi.org/10.7879/siej.28.137 (open).

- Filters: three commercial charged (帯電) medium filters A, B, C from different makers, 135 x 218.5 x 25 mm pleated; pleats 55/39/54 at 4/5.5/4 mm spacing; BET 0.39/0.21/0.19 m2/g (p.138). Media, basis weight, charging method not stated. Media area not stated; my estimate (pleat height ~24 mm, pleat length 135 mm) ~0.36/0.25/0.35 m2, so media velocity ~8.6/12/8.7 cm/s at 110 m3/h (1.04 m/s at the frontal opening). Flag: estimate.
- Lab ageing: fan drawing room air continuously for 73 days at 110 m3/h; single-pass efficiency for 0.3-0.5 um ambient particles by OPS 3330 (count). No mass weighed and no room concentration given - deposited g/m2 unknown.
  - E: A 79 -> 43 %, B 48 -> 6.7 %, C 69 -> 21 % after 73 days (Fig. 3; p.139). dp at 1.04 m/s: 27 -> 32, 42 -> 48, 22 -> 25 Pa. Unloaded controls in the same room, 38 days: 77 -> 75, 48 -> 45, 69 -> 65 %; dp unchanged.
  - -lnP retained: A 0.36, B 0.11, C 0.20. IPA-vapour-discharged new filters at 0.35 um (Fig. 5, Kanto-loam test): 9.2, 0.41, 2.4 % (from 75/40/73 %), so the electrostatic part lost after 73 days is ~0.68 (A), ~0.90 (B), ~0.82 (C) (mixes the 0.3-0.5 um ambient and 0.35 um Kanto-loam tests - flag).
  - Quote: "経時的な粒子捕集効率の低下は，フィルターの目詰まりによるものではなく，フィルターの帯電性の低下によるものと考えられる" (the decline is attributed not to clogging but to loss of the filters' charge).
  - Loaded with JIS No. 8 Kanto loam to 200 Pa at 1.04 m/s: A and C efficiency rose and IPA still lowered it (charge retained); B's small-particle efficiency fell and IPA did not lower it further (charge gone).
- Field: route bus, filter C, 2 years / 90,271 km: equivalent ACH (0.3-0.5 um) 21 /h vs 48 /h with a new filter -> estimated single-pass efficiency 22 % vs 53 % at 3500 m3/h, 2.64 m/s face. Commuter buses (from Dec 2023, 6 months): filter A 39-43 -> 21-26 /h, filter B 26-32 -> 10-15 /h; estimated single-pass efficiency A 45 -> 27 %, B 32 -> 15 % (the text says "2年間使用" here, apparently a slip for 6 months). No mass.

## 9. Arakawa (TEPCO), Tani (Takenaka) et al. 2024 - 8-month office AHU comparison (Japanese)

Source: 荒川祥子 他, 「アフターコロナ要素技術に関する実証研究（第6報）粒子捕集性能及び消費電力に関する帯電フィルタと非帯電フィルタの比較」, 空気調和・衛生工学会大会学術講演論文集 2024 vol.4, G-41, p.161-164. https://www.jstage.jst.go.jp/article/shasetaikai/2024.04/0/2024.04_161/_article/-char/ja/ (open).

- Two medium filters from one maker, both colorimetric 90 % (JIS B 9908:2001) and MERV 13; electret dp 66 Pa vs non-electret 108 Pa at 36 m3/min; 465 x 690 x 65 mm, two per AHU; face 1.75-1.85 m/s. Office building, Jul 2023-Feb 2024; prefilter removed during measurements; Rion KC-52 OPC (count).
- Electret: 0.3-0.5 um efficiency 78 % at installation -> 64 % after 231 days; fit E = 75.643 exp(-8e-4 t[days]). Non-electret: 28.5 -> 40.4 % (rising), fit E = 28.974 exp(0.0018 t); projected crossover ~370 days. -lnP retained by the electret: 0.67 after 8 months. Mass and media area not reported.
- Quote: "繊維ろ材表面に粒子が付着・堆積したことで、帯電量の減衰等によって静電気力による粒子捕集性能が低下" (particle deposition on the fibre surface lowered electrostatic capture through charge decay etc.); "小さい粒径ほど低下率が大きく" (the smaller the particle, the larger the fall).

## 10. Korean sources

- KSME 2001 conference (KIST group; Korean precursor of Ji et al., J. Aerosol Sci. 2003): 「승용차용 정전 필터 내의 정전 섬유의 보유 하전 감쇄에 의한 미세 입자 포집효율 변화」 (Charge depletion effect on collection efficiency of an electret cabin air filter for submicron particles), pp.71-76, https://koreascience.kr/article/CFKO200123513942933.page (scanned; read as images). Cabin media: prefilter ~35 um + main ~10 um fibre layers; 8.4 cm/s; dp 1.8-2.0 mmH2O. NaCl from 0.1 % solution (GMD 0.05 um), 1e5-1e6 /cm3, CPC/SMPS (count). Total efficiency 0.85 -> 0.33 (spray-charged) and 0.80 -> 0.41 (neutralised) by ~150 min, then steady (Fig. 2); fractional 0.1-0.5 um ~0.7-0.8 -> ~0.2 (Fig. 4-5). GMD 0.07 um (1 % solution): efficiency 0.86 -> 0.5 then rising; dp x4 by 250 min (Fig. 6). No mass; my bounding estimate for 150 min of the 0.05 um aerosol is ~0.02-0.3 g/m2 deposited (10x concentration range) - consistent with IGF entry 1a. Conclusion quote: "입자 퇴적의 영향이 나타나기 전에 정전 필터의 성능이 저하될 수 있다" (electret performance can degrade before any effect of particle deposition appears), so loading-test dusts should match real (number-dominated, sub-micron) size distributions.
- Park, Kim, Jo 2013, J. KOSAE 29(5):625-633, https://koreascience.kr/article/JAKO201334064307959.pdf: electret pleated filter (EGIS MERV 10 media) behind a prefilter in a Seoul subway AHU, 28 days: mass efficiency ~70 % PM10, 50-60 % PM2.5, steady; inlet PM10 34-53 ug/m3. No mass. Minor.
- Noh, Kim, Hwang 2024, Particle and Aerosol Research 20(2):69-77, https://koreascience.kr/article/JAKO202430372072346.pdf: 30 subway-platform air cleaners (filter type not stated): in-use filter efficiency 98.73 % vs 99.37 % new; CADR loss mainly airflow. Not shown to be electret - minor.

## 11. Other non-English items checked (little or no loading data)

- INRS (France), Chazelet & Masson, ND 2373 (2013), Hygiène et sécurité du travail 230: RH/temperature cycles, EM fields and ESD did not lower efficiency of respirator electret or glass filters; only forced IPA neutralisation did. No particle loading. https://inrs.fr/dam/inrs/CataloguePapier/HST/TI-ND-2373.pdf
- RPTU/IUTA follow-up IGF project on wetting/adsorption and air-purifier test methods (Stoll): no results published on the project page (updated Feb 2025).
- Chinese: open full texts are scarce (CNKI walled); entry 2 is the only Chinese field + lab g/m2 study found.
- VTT (Finland), Kulmala, Kalliohaka, Kataja, Leppälä, "Reaaliaikainen tuloilmasuodattimen toimintakunnon mittausjärjestelmä", Sisäilmastoseminaari 2015, SIY raportti 33:277-282, https://sarjaweb.vtt.fi/julkaisut/muut/2015/OA-Reaaliaikainen-tuloilmasuodattimen.pdf: Lifa 3G bag filter (electret + activated carbon) behind a wire charger in a Helsinki office AHU, Jul-Oct 2014; 0.39 um efficiency > 95 % with the charger, 64 % average with the charger off (4 Aug 2014, after ~1 month). States, citing older work, that passive electret efficiency weakens "nopeasti, jopa muutamien päivien käytön jälkeen" (quickly, even after a few days of use). No mass.
- Not retrieved: SHASE 2023 part 4 (J-STAGE connection resets; initial-performance paper), Sen-i Gakkaishi 51(8):P332 (1995 review "静電フィルターの機能と応用", download kept failing), 繊維製品消費科学 62(9):554 (2021 review, subscription page), JEM 1467 and GB/T 18801-2015 (paid standards defining tobacco-smoke durability / CCM tests).
- Web-search budget for the session ran out before Chinese mask/oily-loading (GB 2626 paraffin oil) papers could be searched for.

---

## Synthesis (my reading across the pool)

Retained -lnP and electrostatic-part-lost at the stated loads, sorted by aerosol type:

| Aerosol (size) | Media | Velocity | Load (g/m2 media) | Electrostatic part lost | Source |
|---|---|---|---|---|---|
| NaCl, neutralised, CMD 31 nm | PP meltblown corona 133 g/m2, 32 um | 2 cm/s | ~0.07 / 0.2 / 0.52 (est.) | 0.21 / 0.46 / 0.78 (0.2 um) | IGF 19145 Abb. 53 |
| NaCl (lab, presumably atomised) | 3M MERV 13, 13 um | 10 cm/s | 3.8 | ~0.30-0.37 | Li 2022 Fig. 8 |
| NaCl, mask test | Toyobo R-type 300 g/m2, 15 um | 14.2 cm/s | 10 incident | -lnP retained 0.42 | Ueda 2009 Fig. 1 |
| Solid iron alum 0.1 um, charged | PP 1.3 um, ~40 g/m2 | 5 cm/s | 1.1 | none (P fell 10x) | Otani 1992 Fig. 11 |
| JIS-15 dust 0.8 um | PP 1.94 um, ~100 g/m2 | 2.5 cm/s | 30 | none (P fell) | Toray 1993 Fig. 12 |
| DOS oil 0.1 um, uncharged | PP 1.3 um, ~40 g/m2 | 5 cm/s | 0.36 deposited | ~1.0 of induced-force capture | Otani 1992 Fig. 13 |
| DOS oil 0.1 um, singly charged | same | 5 cm/s | 0.4 / 1.0 incident | 0.40 / 0.78 | Otani 1992 Fig. 11 |
| DEHS (mass mostly > 1 um) | cabin PP meltblown 115-140 g/m2 | 7.8 cm/s | ~0.7 / ~2.1 / 6-8.5 | 0.39-0.53 / 0.72-0.80 / ~1.0 | IGF 19145 Abb. 61-62 |
| Glycerol | same | 7.8 cm/s | ~0.7-1.4 | ~0 | IGF 19145 Abb. 60 |
| DOP, mask test | Toyobo AA meltblown 30 g/m2, 2 um | 14.2 cm/s | 14 incident | -lnP retained ~0.37 | Hayashi 2008 Fig. 5 |
| DOP, mask test | Toyobo R-type 300 / 600 / 900 g/m2 | 14.2 cm/s | 20 incident | -lnP retained 0.43 / 0.75 / ~1 | Ueda 2009 Fig. 5-7 |
| Cigarette smoke | PP meltblown electret (19 Pa at 5.3 cm/s) | 5.3 cm/s (test) | 1.0 / 2.0 / 2.5 | 0.64 / 0.93 / ~1.0 | Shimokawa 2023 Fig. 5 |
| Cigarette smoke | same + liquid-repellent finish (<30 mN/m) | 5.3 cm/s | 2.0 / 2.9 / 4.5 / 5.7 | 0.33 / 0.68 / 0.89 / 0.96 | Shimokawa 2023 Fig. 5 |
| Incense smoke | PP 33 um, ~400 g/m2 | 40 cm/s | 10-31 / 21-40 | 0.60-0.70 / 0.86-0.87 | Hitachi 1986 Fig. 4 |
| Real ambient, 5-7 months | 3M MERV 13 | n.s. | 3.55 / 3.96 / 4.76 (weighed) | 0.55 / 0.67 / 0.75 (300 nm) | Li 2022 Fig. 7 |
| Room air 0.07 um | Toray ULPA-class electret | 2.5 cm/s | 4-5 incident | ~0.05-0.08 | Toray 1993 Fig. 15 |
| Indoor air 73 days (mass unknown) | three commercial pleated medium filters | ~9-12 cm/s (est.) | n.m. | ~0.68 / 0.90 / 0.82 | Shinohara 2025 |
| Office AHU 8 months (mass unknown) | MERV 13 electret | n.s. | n.m. | -lnP retained 0.67 | Arakawa 2024 |

Controls, as quantified in this pool:
1. Wetting liquid vs non-wetting or solid. Same rig, same ~0.7-1.4 g/m2: DEHS -10 points per 20 min, glycerol nothing (IGF). Lowering fibre surface tension 37 -> <30 mN/m multiplied the cigarette-smoke load to full loss by ~2.5 (Shimokawa). Oils (DOS) erase neutral-particle (induced-force) capture by ~0.4 g/m2 on a 1.3 um medium (Otani).
2. Particle size (number per gram): ultrafine NaCl (CMD 31 nm) took 78 % of the electrostatic -lnP at ~0.5 g/m2 (IGF), whereas 0.8 um dust and 0.1 um solid on very fine fibres only improved efficiency (Toray, Otani). The Korean KIST work found 0.05 um NaCl drove the medium to a low steady state, 0.07 um recovered by deposition.
3. Media depth/charge reserve: at 20 g/m2 DOP, Toyobo R-type kept 43 %, 75 %, ~100 % of -lnP at 300, 600, 900 g/m2; a ULPA-class electret lost only 5-8 % of electrostatic -lnP at 4-5 g/m2 of room aerosol (Toray).
4. Field vs lab: at ~3.6-3.8 g/m2 the field-aged MERV 13 had lost ~0.55 vs ~0.35 of its electrostatic part in the lab (Li 2022). Shinohara (lab room air, 73 days) and the 2-year bus data show large losses with negligible dp rise.
5. Humidity and storage alone: no measurable effect (Otani 800 h at 90 % RH; Li 2022 10-90 % RH and 24 h immersion; IGF 3 h 80 % RH up to 60 C, 8-10 months storage; INRS). Only 80 C + 87 % RH discharged IGF's F1 medium.
