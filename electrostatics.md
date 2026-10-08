# Electrostatic enhancement of household filters

Working conclusions, 13 September 2026. **Triboelectric charging is worth testing, with PP the strongest starting point.** Persistent benefits are demonstrated in the literature; their size in our household filter bank remains unmeasured.

Here, efficiency **E** is the fraction captured, penetration **P = 1 − E**, and **PF = 1/P**. “Relative improvement” below means a reduction in penetration. PP = polypropylene; PET = polyethylene terephthalate (polyester); PE = polyethylene; POM = polyoxymethylene.

## Initial decay can leave a persistent filtration benefit

**PP loses some benefit over tens of minutes, then retains a substantial remainder overnight.** After 30 seconds of rubbing spunbond PP with latex gloves, Zhao's Figure 3a gives approximately **6% efficiency before charging → 22% immediately → 15% at 30 minutes → 12% at one hour → 13% overnight**. About 60% of the initial added capture disappears in the first hour. These are graph readings at 22°C/40% RH, with photometric NaCl filtration at 5.3 cm/s, rather than size-resolved particle counts. [Zhao et al., 2020, Fig. 3a and supporting methods](https://doi.org/10.1021/acs.nanolett.0c02211)

**PET can retain a benefit for hours, but the demonstrated method was high-voltage corona charging.** Three-layer knitted PET improved from **86.79% to 92.61% efficiency**, falling to **89.02% by seven hours** and staying there through twelve. Equivalently, penetration fell **13.21% → 7.39% → 10.98%**: a **44% initial reduction, settling to 17%**. The experiment used PM2.5 monitors, 30 L/min and 58% RH. A comparable long-duration filtration result from rubbing ordinary PET fabric remains unestablished; Zhao's latex-rubbed polyester returned near baseline within 30 minutes. [Bandi et al., 2021, Fig. 11b/Table 2](https://doi.org/10.1098/rspa.2021.0062); [Zhao, Fig. 3a](https://doi.org/10.1021/acs.nanolett.0c02211)

## Corona-charged PET and PTFE filter felts: retention over days

**PET can retain a substantial next-day filtration benefit, but it need not persist for a week.** He et al. tested industrial needle felts after room-temperature corona charging at **15 kV, 2 cm electrode spacing, 10 minutes**. The first filtration measurement was after **24 hours of open-circuit storage**, followed by seven days and one month. Tests used a TSI 9306 particle counter at **1.7 m/min = 2.83 cm/s face velocity**. These are storage-ageing results, not continuous-use lifetimes. [He et al., 2018, §§1.2–2.1 and Fig. 4](https://xuebao.neu.edu.cn/natural/article/html/2018-10-1469.htm)

| Medium | Untreated efficiency, reported 0.3 µm channel | After one day | Later |
|---|---:|---:|---:|
| PET needle felt | ≈60% | ≈75% | ≈60% after seven days |
| PTFE-membrane needle felt | 93.01% | ≈99.33% | ≈98.43% after one month |

PET values are approximate Fig. 4a readings: penetration falls from about 40% to 25%, a **≈38% reduction**, still present a day after charging. The text reports a 15.28-percentage-point gain and a subsequent 14.78-point loss by seven days. PTFE values are reconstructed from the stated 93.01% untreated baseline, 6.32-point gain and 0.90-point loss; corresponding **PF ≈14 → 149 → 64**, leaving **≈4.5 times the untreated PF after a month**. PET was 548 g/m² and 2.13 mm thick; PTFE-membrane felt was 834 g/m² and 0.95 mm thick. This supports testing freshly charged PET for short-duration use, without establishing an ionic-hairdryer or household-blanket result. [Table 1, §2.1/Fig. 4 and §2.3.2](https://xuebao.neu.edu.cn/natural/article/html/2018-10-1469.htm)

Other useful findings from the same study:

- **Material choice affects persistence.** P84 polyimide gained 3.21 percentage points in the 0.3 µm channel, retaining 1.59 points after a month (calculated from the reported loss). PPS+PTFE also retained a benefit; aramid showed little change. These were different industrial constructions, not a controlled comparison of polymer chemistry alone. [§2.1](https://xuebao.neu.edu.cn/natural/article/html/2018-10-1469.htm)
- **PTFE tolerated heat.** Filtration showed no obvious change below 80°C. Following 200°C for 40 minutes, the 15 kV-treated sample still gave 98.25% at 0.3 µm, versus the stated 93.01% untreated baseline. This demonstrates survival of a benefit, not improvement from baking. [§§2.3.1–2.3.2](https://xuebao.neu.edu.cn/natural/article/html/2018-10-1469.htm)
- **Charging dose helped PTFE, but the numerical optimum is unreliable.** Higher voltage, smaller spacing and longer exposure improved capture within the respective series; the smallest spacing also increased breakdown damage. However, nominally identical **15 kV / 2 cm / 20 min** conditions give **≈99.3% in §2.2.1 versus 97.72% in §2.2.3** at 0.3 µm. The paper does not reconcile this discrepancy. [§2.2](https://xuebao.neu.edu.cn/natural/article/html/2018-10-1469.htm)
- **Measure filtration, not just surface charge.** PET's measured surface charge changed little despite its filtration gain. A separate PTFE series retained 62.22% of its measured charge after 27 days. The authors report no obvious pressure-drop change after charging, but give no numerical filtration-test pressure drops, so absolute QF and cross-material QF rankings cannot be established. PTFE here was a membrane on felt, not a rubbing partner or evidence for plumber's tape as filter media. [§§1–2.3.1](https://xuebao.neu.edu.cn/natural/article/html/2018-10-1469.htm)

## Charging results depend on the material and arrangement

**PTFE rubbing has produced persistent benefits in PP.** On meltblown PP, filtration in the 0.3 µm count channel remained **68% after sixteen hours**, versus **45.4% before charging**. An improved arrangement rubbed PTFE film over PP supported on a grounded aluminium plate; its separate twelve-hour filtration trace declined only approximately **96% → 94%**. That trace's caption does not specify the particle-size channel. These results concern meltblown mask media. [R. Zhang et al., 2021, Figs. 1d/2](https://doi.org/10.1016/j.nanoen.2020.105434); [supporting Fig. S8](https://ars.els-cdn.com/content/image/1-s2.0-S2211285520310107-mmc1.docx)

**The solid-PET result does not establish PTFE as a preferred rubbing partner for polyester fabric.** Engineering-grade PET retained **81% of its initial charge after 33 minutes** when rubbed with PTFE, versus **17% with silicone and 2% with PVC**, but PTFE also produced the **smallest initial charge among the polymer partners tested**. A high retained fraction alone does not establish strong charging. The study measured neither fabric filtration nor a comparison against wool. It does not justify recommending PTFE for both wool and polyester blankets. [J. Zhang et al., 2020, Figs. 1a and 3a](https://doi.org/10.1002/adem.201901201)

## Mixing dissimilar fibres can produce durable, strong filtration

**Intimately mixed, oppositely charged fibres can work even when the whole filter has little net charge.** DuPont reported an equal-polymer-volume **PP/POM mixture**, mechanically combed together by carding, with **0.01% penetration after one month: 99.99% capture, PF 10,000**. Conditions were 0.3 µm DOP aerosol, approximately **3 cm/s**, a **6.35 cm-thick bed**, 97% void fraction and roughly 20–25 µm fibres. The separate PP bed had 0.58% penetration immediately and 1.20% after four days. Independent replication of this patent result remains unverified; finish-free POM fibres are not ordinary household materials. [DuPont, US3307332A, 1967, example (a)](https://patents.google.com/patent/US3307332)

**Stacking two fabrics is not a demonstrated substitute.** Our inference is that generating and retaining local charge near individual fibres matters more than simply choosing opposite ends of a triboelectric series.

## Surface condition and humidity can determine whether it lasts

The PP/POM patent reports deterioration after **3–4 days with textile finishes**, versus stability for **months without them**. This motivates testing removal of antistatic residues; it supplies no household charging-wash recipe. [DuPont, example (a)](https://patents.google.com/patent/US3307332)

Humidity sensitivity is material-specific: at **38°C/85% RH**, Zhao's nylon lost its added benefit within a minute, while PP still exceeded 10% efficiency after an hour, versus roughly 6% before charging. [Zhao, Fig. 3c](https://doi.org/10.1021/acs.nanolett.0c02211)

## Why some charge lasts and some doesn't

A trapped charge escapes by thermal activation. Its residence time is roughly τ = ν⁻¹ exp(E/kT), with an attempt frequency ν of 10¹²–10¹³ s⁻¹. At 20 °C every extra 0.058 eV of trap depth makes the charge last ten times longer, so a small spread in depth covers seconds to decades.

| Trap depth | Residence time at 20 °C |
|---|---|
| 0.8 eV | 6–60 s |
| 1.0 eV | 4–43 h |
| 1.1 eV | 9–95 days |
| 1.2 eV | 1.4–14 years |

Depth is set by what sits at the trap site. In polyethylene, conformational disorder along the chains gives traps of about 0.15 eV, all under 0.3 eV. Chemical defects are much rarer but much deeper: an oxidation carbonyl in cross-linked polyethylene is about 1.44 eV. Corona-charged PP shows trap activation energies of 1.1–1.2 eV, extrapolating to lifetimes of over 2 and over 6 years. In PP the deep traps sit inside crystallites and the shallow ones at crystallite boundaries. Annealing meltblown PP at 140 °C raised crystallinity from 41% to 58% and cut two-month filtration loss from 2.1 to 0.73 percentage points. [Meunier & Quirke, 2001](https://pubs.aip.org/aip/jcp/article-abstract/115/6/2876/185375/Molecular-modeling-of-electron-traps-in-polymer); [carbonyl traps in XLPE](https://www.researchgate.net/publication/321328827_Trap-controlled_charge_decay_and_quantum_chemical_analysis_of_charge_transfer_and_trapping_in_XLPE); [TSD lifetimes](https://www.researchgate.net/figure/TSd-peak-temperature-of-polymer-electrets_tbl1_325718227); [annealed meltblown PP](https://pmc.ncbi.nlm.nih.gov/articles/PMC7602006/)

Because the traps form a continuous spectrum, decay has no single half-life. After time t, every trap shallower than kT ln(νt) has emptied: about 1.0 eV after a night, 1.1 eV after a month and 1.15–1.2 eV after a year. Charge at the deep end of the spectrum stays. That predicts a fast loss followed by a flat tail, which is what Zhao's PP does: roughly 60% of the added capture goes in the first hour, then nothing more overnight. Oxenham's ~20-minute half-life for rubbed PP surface voltage is the same fast phase.

Heating the fabric after charging doesn't deepen anything. It moves the cutoff up, so it just runs the clock forward:

| Bake | Equivalent storage at 20 °C |
|---|---|
| 60 °C, 1 h | 5–8 days |
| 80 °C, 1 h | 2–3 months |
| 100 °C, 1 h | 2–4 years |

Charge freed during a bake only re-traps deeper if a field keeps driving it inward and a source keeps topping it up. Industrial thermally stimulated charging works because the corona stays on while the web is hot. Electret microphone films are baked at 100 °C for 3 h straight after corona charging and then show no decay over six months, but that bake is a purge of unstable charge. A rubbed-then-baked fabric should end up about where a rubbed fabric left overnight does. Annealing *before* rubbing, to add crystalline deep traps, is untested for tribo charge. PP melts around 160 °C and oven thermostats overshoot. [microphone electret patent](https://patents.google.com/patent/US6806593B2/en)

## Why hand rubbing loses to corona, and why carding doesn't

Corona ions (CO₃⁻ for negative corona, hydrated protons for positive) arrive with thermal energy and don't penetrate the polymer. They hand over their charge at the surface, and about 5% of it reaches ~7 µm into a PP film. Force isn't what gets charge deep. Deep surface sites fill first, supply continues under a kV field until they saturate, and negative corona oxidises the surface: it put 2.4 times as much oxygen, mainly carbonyl, into PP as positive corona did. [corona charging review](https://www.scielo.br/j/bjp/a/bFKy9Q7MVPf8fRRwX7CqLCN/?lang=en); [charge depth in PP](https://ieeexplore.ieee.org/document/1359993); [XPS of corona-charged PP](https://www.sciencedirect.com/science/article/abs/pii/S0304388607000605)

Triboelectric charging itself is not the weak method. Normalised to 100 g/m², tribo-charged industrial felts filtered 95% against 75% for corona-charged felts. Hand-rubbing a finished fabric falls short for three separate reasons. [Tsai, Schreuder-Gibson & Gibson, 2002](https://www.sciencedirect.com/science/article/abs/pii/S0304388601001607)

1. **Reach.** A glove only touches the outer face, but capture happens throughout the depth. Carding rubs every fibre against its neighbours, and corona ions and hydrocharging water reach the interior.
2. **Mosaic cancellation.** Contact charge is laid down as a random mosaic of positive and negative patches of nanoscopic size, and the net charge you measure is a small residue. The patchwork comes from discharges across the gap as the surfaces separate. [Baytekin et al., 2011](https://www.osti.gov/biblio/1384508-mosaic-surface-charge-contact-electrification); [Sobolev et al., 2022](https://www.nature.com/articles/s41567-022-01714-9)
3. **Dose.** A rubbing pass is brief. It fills sites roughly in proportion to how common they are, and shallow sites are the common ones.

The mosaic point is plain electrostatics. For charge alternating with period L, the field falls as exp(−2πz/L) with distance z from the surface:

| Patch period | Field left at 1 µm | at 5 µm |
|---|---|---|
| 0.1 µm | 5×10⁻²⁸ | ≈0 |
| 1 µm | 2×10⁻³ | 2×10⁻¹⁴ |
| 10 µm | 0.53 | 0.04 |

Charge alternating on the nanometre scale produces no field where particles pass, however much of it there is. In a carded blend each fibre carries one sign, so the patches are whole fibres tens of µm across and their fields reach across the pores. The same argument is why two stacked sheets are unlikely to do much: the opposite charges meet only at one interface plane.

Moisture is the other half of retention. PP takes up under 0.1% water at 65% RH, polyester 0.4% and nylon 3.5–4.5%. After 48 h at 90% RH, charged meltblown PP lost 11–12% of its surface potential, against 72% for polyacrylonitrile and 63.5% for PVDF. Water on or in the fibre gives the charge a conduction path. [moisture regain table](https://weaveessence.com/tech-hub/moisture-regain-data-2/); [Kang et al., 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7183080/)

## Carded fibre blends: resin wool and its successors

The first permanently charged filter was Hansen's, from the 1930s: wool carded with powdered resin (colophony, i.e. rosin). The resin particles charge negative and cling to the positively charged wool fibres, which are ~17 µm across. It went into military respirators. Some secondary accounts describe soaking wool in resin dissolved in alcohol instead. Feltham (1979) and Hansen's patent haven't been checked to settle which. Resin wool degrades with humidity and oil mist; the storage tests covered wool/acrylic and wool/PP resin wools containing 15–20% resin. That degradation paper is **Ackley, *Filtration & Separation* 22(4), 1985, not Brown 1982** — the bibliographic record is [INIST 8407537](https://pascal-francis.inist.fr/vibad/index.php?action=getRecordDetail&idt=8407537); the paper itself has not been read here. [Feltham 1979 and fibre size, cited in AAQR](https://aaqr.org/articles/aaqr-22-11-pui-0405)

Hansen's own specification does not claim electrostatics. The family text (the Swiss member, [CH170238A](https://patents.google.com/patent/CH170238A/en)) gives the recipe as 200 g abietic acid in 1 L carbon tetrachloride, soak dry wool, wring, dry, 25 g per canister, with rosin/alcohol and shellac/alcohol as alternatives, and no efficiency data anywhere in the family. The charge explanation is a later reading back by [US4798850A](https://patents.google.com/patent/US4798850A/en) and [EP0669849B1](https://patents.google.com/patent/EP0669849B1/en).

The later resin-free blends need only two clean fibres of different polymers, carded together.

**PP + modacrylic** (UK patent family). 20 µm PP and 18 µm modacrylic at 60:40 by weight, about 2:1 by surface area. Both fibres were scoured with non-ionic detergent to strip spin finish, then carded and lightly needled. At 0.28 m/s it beat PP/wool about 6× in penetration at equal pressure drop, and pure PP about 150×. The often-quoted ageing figures — penetration doubling in the first 24 h, then ×1.5 by a month and ×1.7 by a year — are **the patent's expectation, not its measurement**: it says "Sufficient time has not elapsed for the stability of the charge on the filters described above to be conclusively established, but from previous experience it is considered that…". [US4798850A](https://patents.google.com/patent/US4798850A/en)

| Felt at 100 Pa, 0.28 m/s | Penetration | QF (kPa⁻¹) |
|---|---|---|
| PP + modacrylic | 0.07% | 73 |
| PP + wool | 0.40% | 55 |
| PP alone | 10.2% | 23 |

**Wool + PP** (CSIRO). Needle-punched blends work provided the fibres are adequately cleaned. Performance peaks at equal wool and PP surface areas, is ten times better than a blend that doesn't charge, and the charge held for at least 2.5 years. The commercial version claims at least 95% filtration efficiency at low pressure drop. [Schütz & Humphries, 2010](https://journals.sagepub.com/doi/10.1177/0040517509358803); [CSIRO ES3216](https://www.csiro.au/en/work-with-us/ip-commercialisation/marketplace/es3216-electrostatic-particle-filter-media)

**PP + POM** (DuPont): see above.

Every one of these insists on clean fibre, which fits the physics: spin finishes and antistats exist to conduct charge away. Wool and PP can both be had as loose fibre, which makes a hand-carded blend the most promising route to a durable home-made electret. It is a very different object from a rubbed shopping bag.

## Which two household materials to pair

**Answer: polypropylene, rubbed with a disposable glove or a PTFE surface.** PP is a
nonwoven bag-for-life, garden fleece, surgical-mask layers or loose PP fibre. The rubbing
partner, in order of what a house actually contains: a latex or nitrile glove (the only
partners with a direct filtration test, below), then a PTFE-coated pan or baking liner, then
plumber's thread-seal tape, which nobody but a plumber has. A polyethylene bag is the obvious
household candidate and is *not* supported: two measured series put PE well below PP and a
third lumps them together. Reasoning below.

One laboratory measured 21 knitted fabrics by sliding each against the same copper track at
65% RH, washed and charge-neutralised first, at a contact pressure past the fabric
densification threshold ([Liu et al., 2018, Table 1](https://doi.org/10.1016/j.nanoen.2018.08.071)).
This is the only same-apparatus, fabric-form, household-humidity series found. Effective
charge density, nC/cm²:

| PTFE | PE | PP | PET | acrylic | cotton | glass | wool | nylon 6 | silk | elastane | nylon 66 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| −2.750 | −1.260 | −0.312 | −0.109 | −0.065 | +0.011 | +0.105 | +0.142 | +0.283 | +0.342 | +0.385 | +0.422 |

Two consequences:

1. **Only differences between two materials mean anything; the zero is the reference
   material.** For polypropylene's candidate partners, the difference from PP is:

   | Partner for PP | Liu, nC/cm² | [AlphaLab](https://www.alphalabinc.com/triboelectric-series/), nC/J | [Zou 2019](https://doi.org/10.1038/s41467-019-09461-x), µC/m² |
   |---|---|---|---|
   | PTFE | 2.44 | 100 | 86 |
   | nylon | 0.73 | 120 | 1 |
   | latex / natural rubber | not tested | 15 | 16 |
   | wool | 0.45 | 90 | not tested |
   | polyethylene | 0.95 | 0 | 44 |

   PTFE is the best or joint-best partner in all three sources; by how much is
   source-dependent (3.3× over nylon in Liu, 86× in Zou, a narrow loss in AlphaLab). Every
   series predicts almost nothing for latex on PP, yet the direct filtration test below
   measured latex as the best of ten partners. Series differences are therefore a weak
   predictor of pair outcomes; use them for sign, and rank partners by direct tests.
2. **Air breakdown caps the pair.** σ_max = ε₀E is 27–29 µC/m² (2.7–2.9 nC/cm²) for a flat
   surface. Liu's PTFE fabric reached 2.75, i.e. the ceiling. PTFE/PP separation is 2.44, about
   85% of it; PTFE/nylon 66 is nominally 3.17, which is unreachable. So PTFE plus *anything*
   collects essentially all the charge available, and chasing a more positive partner buys
   nothing. Carded blends reach the same place from the other direction: DuPont measured a
   paired net charge of 2.28 nC/cm² for carded POM+PP, 40–47× either fibre alone
   ([US3307332A](https://patents.google.com/patent/US3307332A/en)).

Retention then picks the other half of the pair. Charge half-life at 43% RH on finish-free,
solvent-cleaned fabrics, measured into a Faraday cage
([Oxenham et al., 2019, Table 4](https://nopr.niscpr.res.in/bitstream/123456789/52714/1/IJFTR%2044(4)%20411-419.pdf)):

| PP | PET filament | nylon | PET spun | cotton |
|---|---|---|---|---|
| 1200–1366 s | 230–258 s | 169–356 s | 3.2–39 s | 0.64–3.8 s |

Filtration decay agrees: PP keeps its added capture overnight and at 38 °C/85% RH, polyester
falls back in about two hours, nylon collapses within a minute at 85% RH, and all three cotton
samples got *worse* when rubbed ([Zhao et al., 2020, Figs. 2–3](https://doi.org/10.1021/acs.nanolett.0c02211)).
Wool is the surprise: its 13–17% regain does not make it leaky, because it binds water
tightly — at 65% RH it is 1.6 decades more resistive than cotton on Hearle's scale — but it
is still ~5.6 decades below polyester, so in a wool blend the surviving charge should sit on
the synthetic.

Direct evidence for PTFE on PP: rubbing a PP electret filter with a PTFE block took surface
potential from 0.9 kV as-manufactured to 3.2 kV, with efficiency above the fresh filter
([Kim et al., 2021](https://doi.org/10.1039/d0ra09769a)); PTFE film rubbed over meltblown PP
on a grounded plate held 68% at 0.3 µm after 16 h against 45.4% uncharged
([R. Zhang et al., 2021](https://doi.org/10.1016/j.nanoen.2020.105434)).

**The honest gap.** The only identical-protocol comparison of rubbing partners — ten materials
on the same PP spunbond — did not include PTFE. Latex gloves won it, lifting efficiency from
6.2% to 24.0%, with nitrile 18.2%, paper 12.9%, wood 11.1%, and butyl rubber, tape, ceramic,
metal and glass doing nothing ([Zhao, Fig. 4](https://doi.org/10.1021/acs.nanolett.0c02211),
read off the figure). So latex is the best *tested* partner and PTFE is the better one *by
series position*. Test both.

**Wool plus polyester is a weak pair**: 0.25 nC/cm² against 2.44 for PP/PTFE in Liu, 40 nC/J
against 100 in AlphaLab. It is not nothing — a handwoven wool/polyester single layer self-charges at the yarn crossings and
gave 78.4% PM2.5 at QF 28.5 kPa⁻¹, beating a surgical mask
([Fine et al., 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8515584/)) — but the tumble-dryer
experiment is aimed at the bottom of the series.

### Carded blends, ranked by same-document comparisons

| Blend | Result | Conditions | Source |
|---|---|---|---|
| POM + PP, equal volumes | 0.01% penetration at 1 month | 0.3 µm DOP, 3.0 cm/s, 0.97 void | [US3307332A](https://patents.google.com/patent/US3307332A/en) |
| PP + modacrylic 60:40 | 0.07%, QF 72.6 kPa⁻¹ | BS 4400, 0.28 m/s, matched 100 Pa | [US4798850A](https://patents.google.com/patent/US4798850A/en) |
| PP + wool | 0.40%, QF 55.2 kPa⁻¹ | same | same |
| PP alone | 10.2%, QF 22.8 kPa⁻¹ | same | same |
| PP + nylon 6, 75:25 | 99.13%, QF 691 kPa⁻¹ | 0.26 µm NaCl, 5.3 cm/s | [US20040177758A1](https://patents.google.com/patent/US20040177758A1/en) |
| ePTFE + nylon 66, 17:83 | QF 824–1223 kPa⁻¹ | 0.1 µm NaCl, 52 mm/s | [EP0669849B1](https://patents.google.com/patent/EP0669849B1/en) |
| PP + modacrylic (Technostat) | QF 1160–1322 kPa⁻¹ | same rig as above | same |
| PP + acrylic vs PP + standard PET | 78% vs 59% | 0.3 µm NaCl, 30 cm/s, 100 g/m² | [EP1690583B1](https://patents.google.com/patent/EP1690583B1/en) |

Three rules recur across these documents, and matter more than the pair choice once carding
is doing the charging: **equal surface areas** of the two fibres (not equal mass), **similar
diameters** — US4798850A wants cross-sections within a factor of 3 — and **loft**. DuPont's
bed at 0.97 void fraction scored 456 in.H₂O⁻¹ against 16.3 for the same fibres at 0.73, a 12×
loss from compression.

Household modacrylic exists: Kanekalon braiding hair is genuinely modacrylic, 46% acrylonitrile
/ 52% vinyl chloride, a few pounds a pack ([Kaneka's own patent, US11885043B2](https://patents.google.com/patent/US11885043B2/en)).
The catch is fineness — about 69 µm against the patent's 18 µm, so cross-sections differ by
14.7× and the factor-3 rule needs PP nearer 40 µm. At 69 µm, 2:1 surface area means mixing
26% PP to 74% modacrylic by mass. Every source insists the spin finish comes off first;
Kanekalon carries 0.6 wt% of a fatty-ester and surfactant finish.

## Kelvin water dropper: unlikely but possible

**Low-priority household corona-charging candidate, not a validated filter protocol.**
[Li et al. (2024)](https://onlinelibrary.wiley.com/doi/10.1002/dro2.91) demonstrate
water-powered corona charging of copper-backed FEP film: a local peak of 358 µC/m² in
about 1 s. Their generator reaches 5.06–6.08 kV; the roughly −915 V measurement is the
**film's surface potential**, not a generator ceiling. Nor is 7 kV a universal corona
threshold: electrode geometry and spacing matter. Ordinary can-type Kelvin droppers have
reached [10–20 kV between collectors](https://ocw.mit.edu/ans7870/resources/woodson/textbook/emd_part2.pdf#page=81).

Throughput remains unresolved. The paper's ~6 µC/min belongs to a separate droplet-discharge
path, not charge deposited on the film. Integrating its surface-potential map gives roughly
0.6 µC on the film; treating this as a one-second result would suggest an initial 36 µC/min,
but the map's timing is not explicit and this does **not** establish sustained output.
For filters, the plausible adaptation is a separate, dry needle-and-backing charging station.
Household construction must still demonstrate useful current under corona load, retained
charge throughout fibrous media, and improved filtration; smooth-film charging alone does
not establish any of these.

## Priority experiments and unresolved questions

- Rub each blanket with **PTFE tape and with a latex glove**, on a grounded and an ungrounded
  backing, and compare against wool-on-polyester. The series says PTFE should win by ~10× over
  wool/polyester; the only measured ten-way partner comparison says latex, and never tested
  PTFE. Keep untreated controls and check whether rubbing changes pressure drop or damages the
  fabric.
- Measure **penetration and pressure drop immediately, after an hour, overnight, and during sustained airflow/humidity exposure**, at our actual face velocities. Report count-based results by particle size and QF in kPa⁻¹. Storage persistence alone does not establish operating lifetime.
- Hand-card a **wool + PP** blend from scoured loose fibre, roughly equal surface areas, and compare against each fibre carded alone. Measure the day after carding, since the patents expect most of the loss in the first 24 h.
- Compare **as-received versus washed, thoroughly rinsed and dried material**, and separately explore mixed household fibres versus stacked fabrics. No dependable household charging wash or durable blend recipe is established yet.
- Do not assign a universal charge half-life to a polymer. Charge location, fibre structure, finishes and the measurement itself matter; a net-charge or surface-voltage decay curve does not uniquely determine filtration decay. The available evidence also does not establish a general PP-versus-PE ranking. [Oxenham et al., 2019, §§2–3](https://core.ac.uk/download/pdf/298009382.pdf)
