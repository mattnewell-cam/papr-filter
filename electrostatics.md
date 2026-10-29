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

**Household carding tool: the pet slicker brush.** An estimated **10–30% of US households** own one. No survey measures slicker ownership directly, so this rests on two estimates:

- **Ownership surveys, ~25% (18–33%).** 45.5% of households have dogs and 32.1% have cats ([AVMA 2024](https://www.avma.org/news/pet-population-continues-increase-while-pet-spending-declines)). APPA data say 23% of dog owners and 32% of cat owners own no brush ([Frontiers, 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8907591/)). That puts some dog or cat brush in 45–55% of households. Assuming 40–60% of brush owners have a slicker gives the range. The 40–60% is an assumption, not data, and drives most of the uncertainty.
- **Sales, ~9–16%.** [NielsenIQ Homescan](https://www.supermarketnews.com/consumer-trends/increased-pet-grooming-at-home-creates-an-opportunity-for-retailers) counted 12.3 M households buying any grooming product in the year to Oct 2020, about 10% of households. Assuming a third bought a slicker and a slicker lasts 3–5 years gives the range. Homescan likely undercounts online sales, which were 53% of grooming dollar sales. Market-research reports on slicker sales contradict each other and were discarded.

The two methods do not fully reconcile, so 10–30% is the tightest range the evidence supports.

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

## Loading: how many hours electret media keep their charge benefit

Question (27 Oct 2026): how much deposit an electret takes before its efficiency degrades
significantly, what sets the number, and what that means in hours. From a seven-pool
literature sweep (solid lab loading, liquid/smoke lab loading, field, standards, mechanism,
patents, non-English); the per-source extractions, with page/figure locations, conditions
and arithmetic, are in `electret_loading_sources/` (their `scratchpad\dl\...` paths were a
session's download folder and no longer exist). ✓ = re-read against the page image in
the main session; everything else was read by one agent from the primary document unless it
says "secondary" or "abstract only".

### Hours

The media load at c·v, so **hours = 27,800 × M / (c × v)**, with M in g/m² of media, c in
µg/m³ and v the velocity through the media in cm/s, if the media catches everything that
reaches it (fine aerosol is ~50-90% caught by mass, so for deposited masses the real hours
run up to ~2× longer). Unless a row says otherwise, hours below are at a reference duty of
10 µg/m³ through 20 cm/s media - an HVAC filter on outdoor air - where 1 g/m² = 140 h. A PAPR
at 200 L/min through ~0.1 m² (3.3 cm/s) gets 6× those hours; smoke at 150 µg/m³ gets 1/15.
Field rows are measured calendar hours. In homes the fan runs only part of the time
(median runtime 9.6% in the RP-1649 Toronto homes), so home calendar hours overstate fan
hours.

### Conventions

- −ln P of an electret = mechanical part + electrostatic part. "Electrostatic part lost" =
  (ln P_loaded − ln P_0)/(ln P_disch − ln P_0), with P_disch from an IPA-discharged or
  uncharged twin. "Retained −ln P" = ln P_loaded / ln P_0, used where there's no discharged
  reference.
- g/m² is per m² of media (filtering) area. "Fed" = c·v·t, what reached the media
  (Nordtest, field estimates). "Deposited" = what stayed on it (weighed or integrated:
  patents, Wang 2026, Shimokawa, Li 2022).
- Fibre surface per m² of media, S = 4·BW/(ρ·d_f) for round fibres.
- Brown et al. 1988's loading law (via [Ji et al. 2002](https://koreascience.kr/article/JAKO200211921125101.page),
  Eqs 4-7): ln P(M) − ln P(0) = β·M, M deposited g/m². β (m²/g) is independent of thickness
  in their derivation, so a filter with more electrostatic −ln P to lose loses a smaller
  fraction per gram. Linear until the electrostatic part runs out.

### Headline

- No threshold. Loss starts with the first deposit and is roughly linear in ln P per gram.
- Oily, tarry and combustion deposits (oil mist, tobacco/wood/incense smoke, diesel) remove
  the electrostatic gain. On ordinary PP electret media a quarter goes by ~80-125 h
  (0.6-0.9 g/m², patent PP webs), half by ~140-560 h (1-4 g/m²), ~all of it by ~700-2,100 h
  (5-15 g/m²), at the reference duty. Δp nearly flat throughout.
- Outdoor air, measured in HVAC duty (20-35 cm/s, 6-15 µg/m³): half the electrostatic part
  gone after ~300-1,000 h, the IPA-discharged or ASHRAE Appendix J level after ~1,000-3,000 h.
  In deposited mass that's half at ~1-3.5 g/m² where the field mass can be pinned down (Li 2022
  weighed, Purdue computed, Tampere and US5496507 estimated; Raynor's whole-filter weighing is
  ×5-10 higher).
- Coarse mineral dust: little or no loss to 60-146 g/m² (8,000-20,000 h), and the cake raises
  efficiency.
- Fine solid salt depends on fibre size and time: 30-70 nm NaCl on 10-32 µm fibres halves the
  electrostatic part at ~0.2 g/m² (~30 h); fine-fibre N95 media under fast lab NaCl loading lose
  ≤11% by ≤13 g/m² (>1,800 h); the same NaCl dosed every 168 h halves one N95 model by
  ~5 g/m² (~700 h).
- Slow or intermittent loading is several to 30-40× worse per gram than accelerated lab
  loading. In the one weighed field-vs-lab comparison (Li 2022, same MERV 13, lab aerosol
  probably NaCl) the field loss per gram was ~1.5× the lab loss.
- Normalised by fibre surface, plain PP loses half its electrostatic part at ~0.06-0.10 g of
  oily/smoke deposit per m² of fibre in three independent patent series. Coarse 17 µm MERV 13
  needed ~3× more per m² of fibre (similar per gram of media).
- Fluorochemical/oleophobic surfaces push the oily numbers out ×2-10.
- Humidity alone (20-98% RH at room temperature, 1.25-800 h) does nothing. With hygroscopic
  salt deposits, RH ≥ 50% flips salt loading from improving to degrading.

### Oily, tarry and combustion deposits (lab)

Half of the electrostatic part gone at:

| aerosol | media | v (cm/s) | g/m² | h at ref. duty | other points | source |
|---|---|---|---|---|---|---|
| diesel fume, MMD ~0.2 µm | EU7 bag "A", 15-20 µm fibres | 33 | 1.3 fed | 180 | 71% at 3.1, 97% at 5.3 fed (430, 740 h); Δp unchanged | [NT TR 320](http://nordtest.info/images/documents/nt-technical-reports/NT%20TR%20320_Development%20of%20test%20methods%20for%20electret%20filters_Nordtest%20Technical%20Report.pdf) Fig 4.5 ✓ (IPA ref ~16%) |
| diesel fume | EU7 bag "B", flat 5×15 µm fibres | 21 | <0.94 fed | <130 | at IPA level by 0.94 fed; author: "approximately ... 1 g/m²" | NT TR 320 Fig 4.7, p.17 |
| sidestream cigarette smoke, MMD ~0.2 µm | EU7 "A" | 33 | 3.3 fed | 460 | 12% at 0.9, 84% at 8, 95% at 12 fed (125, 1,110, 1,670 h) | NT TR 320 Fig 4.10 |
| sidestream cigarette smoke | EU7 "B" | 21 | <1 fed | <140 | IPA level by ~2 fed (280 h) | NT TR 320 Fig 4.12 |
| tobacco smoke | PP meltblown, 99.8% at 5.3 cm/s | 5.3 (test) | ~0.8 | 110 | 64% at 1.0, ~100% at 2.7-2.9 (140, 375-400 h) | [Shimokawa 2023](https://www.jstage.jst.go.jp/article/jaca/61/3/61_158/_article/-char/ja) Fig 5 |
| tobacco smoke | corona PP meltblown, 30 g/m², 5.6 µm (S 23) | 10.2 | 1.8 (half of total −ln P) | 250 | 98% at 6.4 (890 h): E 99.3 → 33%, ethanol twin 28% | [US10940415](https://patents.google.com/patent/US10940415B2/en) Table 2 |
| tobacco smoke / PAO | PP meltblown, 30 g/m², 3 µm (S 44), corona or hydro | 5 | - | - | ~90% at 3.9-5.4 smoke, 3.6-6.2 PAO (500-860 h) | [US10213716](https://patents.google.com/patent/US10213716B2/en) Comp 1-1 to 1-3, 3-15 to 3-19 |
| cigarette smoke | electret sheet, 100 cm² | ? | - | - | 92.5 → 33.3% at 2.04 (84% of −ln P; 280 h) | [Heo et al. 2022](https://doi.org/10.1016/j.scitotenv.2021.150754), abstract only |
| DOP | corona PP meltblown, 51 g/m², 7 µm (S 32) | 7.6 | 2.4-2.7 (Q halved) | 330-380 | Q at 0.75 by 0.85 (120 h) | [US4874399](https://patents.google.com/patent/US4874399A/en) Table II ✓ |
| DOP | PP meltblown + amide, uncoated (H&V Comp B) | 8.3 | ~1.3 | 180 | 29% at 0.59, 61% at 1.76, ~100% by 4.7 (80, 245, 650 h) | [US6802315](https://patents.google.com/patent/US6802315B2/en) Table 1 |
| DOP | corona PP, no additive (3M C4/C7) | 6.9 | - | - | 88-95% by ~2-4 captured (280-560 h) | [US5411576](https://patents.google.com/patent/US5411576A/en) Tables III-VI |
| DOP | hydrocharged PP, 2 × 33 g/m² | 7.8 | - | - | retained −ln P 0.70 / 0.53 / 0.22 at 5.3 / 10.4 / 27 (740 / 1,450 / 3,800 h; stack) | [US6627563](https://patents.google.com/patent/US6627563B1/en) Fig 5 |
| smouldering oak smoke | MERV 13 flat, 0.55 mm, 17 µm, α 0.13 (S 17) | 10.5 | 4.2 | 580 (39 h at 150 µg/m³) | 23% at 2.6, 79% at 5.6, ~100% by 9-16 (below the 9% IPA value by the end) | [Wang et al. 2026](https://doi.org/10.1021/acs.est.6c03046) SI Fig S2, S5 ✓ ([SI](https://acs.figshare.com/articles/journal_contribution/33121135)) |
| DEHS | same MERV 13 | 10.5 | ~6 | 830 | ~100% by ~17 (2,400 h) | Wang 2026 SI Fig S8 ✓ |
| mineral oils 257-2345 cP | same MERV 13 | 10.5 | N140 (257 cP) ~70; N415, N750 not reached | ~9,500; >9,700 | N140 65 → 46% at 68 g/m² (~45% lost); N415, N750 no loss to 70 g/m² | Wang 2026 SI Fig S8 ✓ |
| 0.1 µm DOS droplets | fine-fibre electret, 1.3 µm, α 0.061, 0.71 mm (S 134) | 5 | ~0.18 (neutral test particles) | 25 | 100% at 0.36 (50 h); charged test particles 75% at ~1.1 | [Otani, Emi & Mori 1993](https://www.jstage.jst.go.jp/article/kona/11/0/11_1993023/_article/-char/en) Figs 11-13 |
| incense smoke | thick PP electret, 4 mm, 33 µm (S ~53) | 40 | 6-7 (EF-1), 25-30 (EF-2) | 830-970, 3,500-4,200 | gravimetric mass efficiency | [Shimokobe & Inoue 1986](https://www.jstage.jst.go.jp/article/jar/1/3/1_3_186/_article/-char/en) Fig 4 |
| DEHS | pleated cabin filter, 0.71 m² | 7.8 | - | - | IPA level by ~3-8.5 (420-1,200 h; report's own rough masses); glycerol 0.7-1.4 g/m² no effect | [IGF 19145 N](https://www.iuta.de/igf-docs/abschlussbericht_19145.pdf) Abb. 60-62 |
| pine-needle smoke, ~1.5 mg/m³ | charged MERV 11-15 media | 33 | not measured | ~330 fed-equivalent | 80 min: MERV 13 62.9 → 17.8%, all charged media 9-21%; glass/uncharged ≤14% relative | [Shirman et al. 2025](https://arxiv.org/pdf/2505.01622) Table 1 |

Respirator-scale oil loading (multi-layer, mass per whole filter, mostly no media area given):
N95 FFR DOP 0.85 → 13% at 200 mg, retained −ln P 0.43 ([Rengasamy 2013](https://stacks.cdc.gov/view/cdc/195150)
Fig 1); FFP2 paraffin oil 834 mg over 8 h, 0.4-0.6 → 2.2-3.2%, retained 0.65-0.72, glass P2 flat
P but Δp doubled ([Plebani 2010](https://mattioli1885journals.com/index.php/lamedicinadellavoro/article/download/212/179/214)
Table 1); 3M AS-140 electret PAPR filter (754 cm², 4.97 cm/s) DOP continuous 0.02 → 0.25-0.85%
at 26.5 g/m² (charged DOP) or 1.2-1.9% (neutralised), ~10% at 44-52 g/m² - at the PAPR's own
4.97 cm/s and 10 µg/m³ that's ~15,000 h and ~25,000-29,000 h
([Martin, Moyer & Jensen 2006](https://stacks.cdc.gov/view/cdc/191412) Table IV).

Composition per gram: diesel soot ~2× sidestream smoke on both Nordtest media; smouldering
wood smoke ~1.5× DEHS on the same MERV 13; tobacco smoke ≈ DOP ≈ PAO per gram on PP
(Toyobo lives within ~25%); high-viscosity oils and glycerol did nothing over the loads tested.
Wang 2026's abstract blames soot for "rapid and irreversible neutralization" - their soot
curves are in the walled main text.

End state: diesel and smoke end at about the IPA level. Oils can end below it: oil loading
also raised penetration of already-discharged media ([Tombolini 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC5054281/)
FFP2 IPA-treated 38 → 48% at 0.3 µm; [Roh 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6780184/)
weak-charge web 58 → 75%). IPA itself under-discharges some media (liquid vs vapour IPA differ by
up to 4× in efficiency, [Kerner 2021](https://kluedo.ub.rptu.de/files/6247/atmosphere-12-00065-v2.pdf)
Table 3), so "below IPA" can also mean the IPA reference was high.

### Outdoor and room air (field)

| setting | media | hours | mass | result | source |
|---|---|---|---|---|---|
| Tampere outdoor, 6.4 µg/m³ | EU7 "A", 33 cm/s | 576 | 4.4 g/m² fed (~3-4 collected, ~1 of it sub-µm, estimated) | 0.4 µm 88.5 → 55%: 69% lost | NT TR 320 Fig 3.8 ✓ |
| Tampere outdoor, ~10 µg/m³, behind EU3 | EU7 "A", "B" | ~2,900 | 36 / 18 g/m² fed upstream of the EU3 | A 88 → 21-24%, B 77 → 43-45%: both at their IPA level | NT TR 320 Figs 3.6-3.7 ✓, p.10 ✓ |
| real use (site, velocity, runtime not stated) | 3M MERV 13 | 3,650 / 4,380 / 5,110 calendar | 3.55 / 3.96 / 4.76 g/m² weighed | 300 nm 86.5 → 61 / 50.5 / 42% (discharged 6%): 55 / 67 / 75% lost. Lab-loaded to 3.8 g/m² in <24 h (probably NaCl), the same media lost ~37% | [Li et al. 2022](https://jdxbz.xauat.edu.cn/thesisDetails#1006-7930(2022)05-0734-08) |
| "ambient air" at 250 m³/h | PMP (not PP), hydro + corona, 40 g/m², 14 µm, pleated ~0.29 m², ~24 cm/s | 133, 290 | not reported; 0.6-6.6 g/m² at 290 h for 5-35 µg/m³, central ~2.4 | 0.3 µm 70.5 → 53.8 → 47%: retained −ln P 0.63, 0.52; Δp +43% | [US5496507](https://patents.google.com/patent/US5496507A/en) Table 11 ✓ |
| Indiana outdoor, behind MERV 8 | MERV 13 electret bag | 2,860 | ~22 g per filter computed, ~2.3-3.8 g/m² for an assumed 5.6-9.3 m² | ePM1 62 → 50 (840 h) → 42 (1,340 h) → 27% (2,860 h), retained 0.33, not yet at minimum | [Huang 2021](https://ndownloader.figshare.com/files/27807084) Figs 5.13, 5.21 |
| Minneapolis outdoor, behind prefilter | ~MERV 14 PE/PP, 4.65 m², ~20 cm/s | 3,216; minimum at 1,680-2,520 | 49 g/m² weighed at 3,216 h (±12); ~17-28 pro-rated at the minimum | 0.58 µm 87 → 45% at the minimum, retained 0.29-0.49; then mechanical recovery to 66% | [Raynor & Chae 2004](https://stacks.cdc.gov/view/cdc/188464) p.466, Fig 4 |
| NC outdoor-air plenum | rigid-cell electret | 336, 1,680 | none | 0.35 µm 81 → 45% (336 h), ~29% (1,680 h) | [Hanley et al. 1999](http://www.aivc.org/sites/default/files/members_area/medias/pdf/Conf/1999/paper097.pdf) Fig 1 |
| homes, MN/NC/GA | 1" MERV 11 electret | 1,100-2,560 calendar | in the walled report | E1 37 → 12-15%, = the Appendix J value (13%) | ASHRAE RP-1360, secondary ([vendor table](https://www.texairfilters.com/what-happens-to-the-electret-charge-on-a-merv-11-pleated-filter-in-service/)) |
| room air | three charged medium filters | 1,750 | none | 79/48/69 → 43/6.7/21%, Δp +3-6 Pa: 68-90% lost | [Shinohara et al. 2025](https://doi.org/10.7879/siej.28.137) |
| Tampere outdoor, F7 electret | - | ~1,000, then flat to ~5,800 | ~3-9 g/m² fed by 1,000 h (estimate) | PM2.5 mass efficiency 85 → ~40% | [NT TR 531](http://nordtest.info/images/documents/nt-technical-reports/NT%20TR%20531_Field%20test%20method%20for%20the%20easurement%20of%20filter%20efficiency_Nordtest%20Technical%20Report.pdf) Fig 14 |
| hospital HVAC | charged synthetic | 2,180 | none | 0.7-1.0 µm 92 → 44%; culturable bioaerosol efficiency unchanged | [Raynor et al. 2008](https://pubmed.ncbi.nlm.nih.gov/18093124/), abstract |
| office AHU | MERV 13 electret | ~5,800 calendar | none | 78 → 64%, retained 0.67 | Arakawa et al. 2024, SHASE G-41 (`electret_loading_sources/nonenglish.md`) |

The field loss tracks the fine combustion/secondary fraction, not total mass. Nordtest's
diesel + PTI dust mixtures (Figs 5.29-5.35): with ≥25% diesel by mass the loss followed the
diesel grams (~3 g/m² diesel fed for two-thirds of −ln P) whatever the dust; 15% diesel
capped the minimum at 50% efficiency, 10% at 72%, dust alone barely moved it. A prefilter
makes it worse, because the electret then sees mostly fine aerosol. Recovery in the field
(Raynor, RP-1360 GA home) is mechanical capture by the deposit, not charge coming back.

### Solids

- Fine NaCl on coarse fibres, slow: corona PP 133 g/m², 32 µm (S 18), Boltzmann NaCl CMD
  31 nm at 189 µg/m³ through 2 cm/s for 72 h. At 0.2 µm, 21 / 46 / 58 / 69 / 78% of the
  electrostatic part lost after 8 / 24 / 32 / 48 / 72 h, ≈0.07 / 0.2 / 0.26 / 0.37 / 0.52 g/m²
  (agent's mass estimate ±40%; 10 / 28 / 36 / 51 / 72 h at the reference duty), Δp flat
  ([IGF 19145 N](https://www.iuta.de/igf-docs/abschlussbericht_19145.pdf) Abb. 53). Cabin media
  with ~10 µm fibres, 0.07 µm NaCl: β 3.4 m²/g, minimum at ~0.25-0.4 g/m² (35-56 h; Ji 2002
  Fig 11). Toyobo R-type (15 µm, 300 g/m²): NaCl penetration 0.04 → 3.8% at 10 g/m² (1,390 h)
  ([Toyobo 2009](https://www.jstage.jst.go.jp/article/transjtmsj/62/2/62_126/_pdf)).
- NaCl on N95, fast and continuous (NIOSH 42 CFR 84 conditions, to the penetration maximum,
  ≤200 mg ≈ ≤13 g/m², loaded in well under 1 h): only 0.5-11% of the electrostatic part lost
  against a 15 s IPA-dip reference (Martin & Moyer 2000, via [3M JobHealth Highlights 2001](https://multimedia.3m.com/mws/media/99824O/spurious-research-on-electrostatic-filter-performance-2001.pdf)
  Tables 1-2; primary walled).
- NaCl on N95, 5 mg every 168 h with office storage between doses: mfr A 1.4 → 12.4% by 125 mg
  (~8 g/m², over ~4,500 h), ~half the electrostatic part by ~5 g/m², ~65% by 8; B and C less
  (Moyer & Bergman 2000, same 3M source Table 3; primary walled). 30-40× worse per gram than
  the continuous run. Penetration fell during each loading session and rose during the
  168 h rests. Silica dust loaded the same way did nothing.
- Solids on fine fibres (≤2 µm) raise efficiency: iron alum on 1.3 µm fibres (Otani Fig 11),
  JIS dust on 1.9 µm PP (Ando 1993), NaCl on 0.5 µm PVDF nanofibres - the 2.7-point dip
  becomes 22 points if the same NaCl is fed at lower concentration ([Sun & Leung 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7108370/)).
- Stearic acid 0.6-1.4 µm on a 92 g/m², 20 µm tribo felt: 0.3 µm penetration ~16 → ~31% by
  7-9 g/m² (970-1,250 h), peak 25-40% near 17 g/m² (2,400 h), then falling as a cake forms.
  β ~0.08 m²/g (Walsh & Stenhouse 1998).
- Coarse mineral dust: ASHRAE dust to 139 g/m² fed, no loss (NT TR 320 Fig 3.3); SAE coarse
  to 146 g/m², 0.4 µm efficiency unchanged ([EP1874430](https://data.epo.org/publication-server/rest/v1.2/patents/EP1874430NWB1/document.html));
  PTI fine dust 88 → 80% at ~60 g/m² then rising (NT TR 320); coal dust β ~0.03 (Brown 1988).
- 20 nm carbon black: an all-electret pack averaged 98% over 71 g/m² ([US4886527](https://patents.google.com/patent/US4886527A/en));
  run average only, cake forming. A simulation ranks equal masses carbon > NaCl > Al₂O₃ by
  conduction through the deposit (Cai, Lu & Zhang 2021, abstract).

Fibre diameter decides the sign for solids: on coarse fibres there is little mechanical gain
to offset the charge loss; on fine fibres the dendrite gain is larger than the loss.

### What sets the number

- Particle size and composition of the deposit. Per gram, smaller and wetter is worse.
  Liquids and tars spread into films (Otani: the DOS deposit acted like a ~3 nm film when the
  gain was gone; Shimokawa Fig 6: with an oleophobic finish, smoke stays as beads and
  capacity is ×2.5). Solids screen or, if fine and charged, neutralise: one elementary charge
  cancels a (0.07-0.18 µm)² patch of fibre at 5-30 µC/m². IGF's NaCl (d30 55 nm, ~25%
  charged) carries ~1.5 × 10¹⁵ charges per gram, enough to cancel ~6-50 m² of fibre charge per
  gram against 18 m² of fibre per m² of that medium - the right order for half lost at
  ~0.2 g/m². Boltzmann-charged 0.3 µm particles carry ~40× less per gram (my arithmetic).
- Fibre surface per m² of media. Plain PP, oily/smoke: 0.075-0.085 g per m² of fibre
  (US4874399 meltblown), 0.059-0.078 (split film), 0.077 (US10940415 tobacco). Coarse MERV 13
  (S 17): 0.25 smoke, 0.34 DEHS. Otani's 1.3 µm web: ~0.001-0.005. So capacity per m² of media
  rises with BW/d_f, but not proportionally across fibre sizes.
- Electrostatic −ln P budget. At equal g/m² heavier media lose a smaller fraction: Toyobo R-type
  kept 43 / 75 / ~100% of −ln P at 20 g/m² DOP for 300 / 600 / 900 g/m² media. Consistent with
  Brown's fixed β per gram. 3M's 4-layer PP web needed ~5× the DOP of one layer to halve Q.
- Surface chemistry. Melt fluorochemical, annealed: retained −ln P 0.78-0.86 at ~6-7.5 g/m² DOP
  vs 0.24-0.29 at ~2-4 without (US5411576; unannealed no better than plain). Fluorochemical +
  quench + anneal: penetration doesn't start rising until 21-35 g/m² (2,900-4,900 h)
  ([US6068799](https://patents.google.com/patent/US6068799A/en) Table 9B), no loss over 33 g/m²
  (US6627563 Fig 4). Surface fluorination + corona: 0.97 at 21 g/m²
  ([US6398847](https://patents.google.com/patent/US6398847B1/en)). Vapour-deposited
  perfluoroalkane ×3-4 smoke/PAO life (Toyobo); H&V fluoroacrylate 0.89 at 11.8 g/m² vs 0.25.
  PMP blends ×2-3.5. C₄F₈ plasma on electrospun PS delayed DOP loss ×5-20 but all webs ended at
  73-77% penetration by 50 g/m² challenged (Roh 2019).
- Charging method. Hydrocharging gives 2-3× the initial QF of corona (193-207 vs 59-66 kPa⁻¹
  at 6.9 cm/s, US6398847 Table II) but doesn't slow the fractional loss per gram.
- Charge on the loading aerosol. Neutralised DOP degraded the AS-140 faster than as-generated
  DOP (Martin 2006). Spray-charged NaCl (2-3× Boltzmann) gave the same initial β but a deeper
  total loss (Ji 2002). For the same deposit, neutral test particles lose their electrostatic
  capture first (Otani) - most of an ambient MPPS challenge is neutral.
- Time and loading rate. NaCl dosed every 168 h vs continuous ×30-40 per gram (Moyer & Bergman
  vs Martin & Moyer). AS-140 DOP at 400 mg per 24 h reached 2.8-4.4% at 21 g/m² vs 0.25-0.85%
  at 26.5 g/m² continuous; a 72 h sealed rest with ~60 mg added took 0.35-0.71% to 0.96-1.76%
  (Martin 2006, 200 mg per 24 h series). Sun & Leung: same NaCl at lower concentration, 22 points
  lost instead of 2.7. Field vs lab on the same MERV 13 at similar weighed load: 55% lost at
  3.55 g/m² after ~3,650 h in use vs ~37% at 3.8 g/m² loaded in <24 h (Li 2022; the lab aerosol
  was probably NaCl, not stated). Hanley 1999: even submicron KCl conditioning "significantly
  underestimated" the field loss.
- Humidity. Clean media: no change at 20 and 90% RH over 800 h (Otani Fig 10), 80% RH for 6 h
  (Mahdavi), 60 °C / 95% RH for 168 h (Ando), 98% RH for 1.25 h (Stoll 2025), 10 → 90 → 10% RH
  and 24 h water immersion (Li 2022 Figs 5-6), 5,800-7,300 h storage (IGF). Liquid water on
  fibres screens reversibly: apparent surface charge ×1/5 to ×1/14 at +25% water, back on
  drying ([Stoll 2025](https://doi.org/10.3390/atmos16010062) Table 4). With salt deposits RH
  flips the sign: N95, 6 h of NaCl at 85 L/min, MPPS penetration 2.70 → 1.06% at 10% RH
  (−ln P +26-30%) vs 3.47 → 4.57% at 50% and 3.63 → 5.21% at 80% (−8 to −11%)
  ([Mahdavi 2015](https://pharesst.irsst.qc.ca/cgi/viewcontent.cgi?article=1046&context=etudes-primaires)
  pp.10-12). 50% is below NaCl's 75% deliquescence point, so adsorbed surface water on the
  deposit is enough. That's the only quantified RH relationship found; no field study isolates
  RH. ASHRAE Appendix J keeps KCl conditioning below 65% RH to prevent deliquescence.
- Heat. Irreversible loss needs heat: PP Q 1.23 → 0.64 after 72 h at 70 °C (US4874399 Table I);
  110 °C + 90% RH for 24 h 95.5 → 38.2% ([Liu 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7662889/));
  80 °C + 87% RH discharged an IGF medium.

### Reconciliations

- The old "~2 g/m² per layer for a 20% loss of log PF" (Walsh & Stenhouse stearic acid,
  previously in `testing/RESULTS.md`) was the gentle end. Oily/smoke deposits on plain PP lose
  20-25% of the electrostatic part at ~0.6-0.85 g/m² (US4874399, US6802315), ambient air
  ~0.5-1 g/m² (Tampere, Purdue): 70-140 h at the reference duty instead of ~280 h. Stearic-acid
  loss also turned over as a cake formed; oily and ambient losses run on to the discharged floor.
- US5496507 Table 11 is consistent with the rest: at a central ~2.4 g/m² (290 h at ~24 cm/s),
  retained −ln P is 0.52, between Li 2022's field MERV 13 (55% lost at 3.55 g/m²) and Tampere
  (69% lost after 576 h). 290 h at 24 cm/s and 10 µg/m³ is 2.5 g/m² fed.
- Weighed field masses disagree ×5-10. Raynor & Chae weighed 49 g/m² in 3,216 h (whole filter
  with frame, ±12 g/m²; coarse debris and moisture included) and reached the minimum at
  ~17-28 g/m² pro-rated; Li 2022 weighed 3.6-4.8 g/m² for a similar loss; Purdue computed 2-4.
  Raynor's mass is probably not the relevant (fine) mass.
- Holder 2022 (EPA, box fan + 1" MERV 13): CADR 111 → 4.3 cfm with "10.0 ± 1.1 mg" of smoke per
  filter (§3.6, [PMC9828579](https://pmc.ncbi.nlm.nih.gov/articles/PMC9828579/)). Whole furnace
  filter on a Scout-class balance, loaded "until the air cleaners ceased to reduce smoke" - the
  mass is below what that balance can resolve. Treat as "small, unknown", not as 0.02 g/m².
- "Fluorinated media are immune" - no; delayed. Roh's webs all converge by 50 g/m², and
  US6068799's metric (Min@Chl) only says when degradation starts.

### Standards and what they encode

- NT VVS 117 (1997) → EN 779:2002 Annex A: IPA immersion, or diesel fume in 5 g/m² fed steps
  (700 h each at the reference duty) to ≥15 g/m², taking the minimum ([NT VVS 117](http://nordtest.info/images/documents/nt-methods/polymers/NT%20vvs%20117_Electret%20filters_Determination%20of%20the%20electrostatic%20enhancement%20factor%20of%20filter%20media_Nordtest%20Method.pdf)).
  Calibrated on NT TR 320, where 1-6 g/m² of diesel removed the electrostatic effect.
- EN 779:2012: IPA on media; F7/F8/F9 minimum efficiency ≥35/55/70% at 0.4 µm. ISO 16890-4:
  whole filter 24 h in IPA vapour, ePM = mean of initial and conditioned. §5.1: the drop "can
  vary by filter type, service location and atmospheric air conditions". No dataset behind the
  50/50 weighting was found; field filters reached about the IPA level (Nordtest, Li 2022).
- ASHRAE 52.2 Appendix J ([Addendum b](https://www.ashrae.org/File%20Library/Technical%20Resources/Standards%20and%20Guidelines/Standards%20Addenda/52_2_2007_Supplement_FINAL.pdf)):
  ultrafine KCl dosed as number × time (CT, up to 1.2 × 10⁹ cm⁻³·min - ~2,000 h at a typical
  urban 10⁴ cm⁻³), RH < 65%, no mass specified. Estimated 1-7 g KCl per 0.94 m³/s filter, i.e.
  per unit flow, so dose per m² of media falls with media area. RTI (RP-1360): needed "to
  bracket the minimum in-situ efficiency". Hanley 1999: still underestimates.
- NIOSH 42 CFR 84: 200 ± 5 mg "contacted" (≈13 g/m² on a ~150 cm² N95), NaCl CMD 75 nm or DOP
  CMD 185 nm; P-series continue while efficiency is still falling. 1995 preamble: "not designed
  to simulate loading of the filter at the worksite". 3M's P-series rule for oil-only
  atmospheres: discard after 40 h of use or 720 h from first use. EN 149/143: 120 mg (~6-8 g/m²;
  from lab test reports, the standard itself is paywalled).
- GB/T 18801-2015 CCM: cigarette smoke (8 mg tar) in 50-cigarette steps until CADR ≤ 50%. 3M's
  media version: a Filtrete HEPA-type PP electret (4.9 µm, 42 g/m²) halves its capture at
  ~520 cigarettes/m² (US12409401) - ~5-8 g/m² if 10-15 mg reaches the media per cigarette
  (assumed).

### Sources not obtained

Checked Europe PMC, Unpaywall, Semantic Scholar and Crossref for open copies (28 Oct 2026).
Free to read, but the host blocks automated access from here - one click each in a normal
browser:
- Moyer & Bergman 2000 (weekly NaCl doses, primary): https://stacks.cdc.gov/view/cdc/198430/cdc_198430_DS1.pdf
- Martin & Moyer 2000 (continuous NaCl + IPA, primary): https://stacks.cdc.gov/view/cdc/198418/cdc_198418_DS1.pdf
- Walsh & Stenhouse 1998 (bronze open access): https://www.tandfonline.com/doi/pdf/10.1080/02786829808965580
- Pistochini et al. 2025 (Corsi-Rosenthal boxes, 40 weeks, open access): https://pubs.rsc.org/en/content/articlepdf/2025/em/d4em00406j

Paywalled, no open copy found (PDF links work only with access):
- Wang et al. 2026, ES&T (soot vs organic per gram): https://pubs.acs.org/doi/pdf/10.1021/acs.est.6c03046
- Li, Chen, Zhou & Chen 2020 (RH and hygroscopicity): https://www.sciencedirect.com/science/article/pii/S0360132320300275/pdfft
- Zhou et al. 2026 (KCl/Al₂O₃ at 30-80% RH): https://www.sciencedirect.com/science/article/pii/S0360132325014878/pdfft
- Wang, Lin & Zhang 2020 (composition > RH > media > particle charge): https://www.sciencedirect.com/science/article/pii/S0360132320303218/pdfft
- Kerner et al. 2020 (NaCl ageing): https://www.sciencedirect.com/science/article/pii/S1383586620317731/pdfft
- Heo et al. 2022 (cigarette smoke): https://www.sciencedirect.com/science/article/pii/S0048969721058320/pdfft
- Brown et al. 1988 (β for industrial aerosols; OUP article page, PDF button there): https://academic.oup.com/annweh/article/32/3/271/172048
- ASHRAE RP-1189 (VTT lab + field, the Appendix J evidence; paid): https://store.accuristech.com/standards/rp-1189-investigation-of-mechanisms-and-operating-environments-that-impact-the-filtration-efficiency-of-charged-air-filtration-media?product_id=1711879
- ASHRAE RP-1360 (in-home weight gain vs efficiency; paid): https://www.techstreet.com/ashrae/standards/ny-14-032-how-do-pressure-drop-efficiency-weight-gain-and-loaded-dust-composition-change-throughout-filter-lifetime-rp-1360?product_id=1876220

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
