# Electrostatic enhancement of household filters

Working conclusions, 13 September 2026. **Triboelectric charging is worth testing, with PP the strongest starting point.** Persistent benefits are demonstrated in the literature; their size in our household filter bank remains unmeasured.

Here, efficiency **E** is the fraction captured, penetration **P = 1 − E**, and **PF = 1/P**. “Relative improvement” below means a reduction in penetration. PP = polypropylene; PET = polyethylene terephthalate (polyester); PE = polyethylene; POM = polyoxymethylene.

## Initial decay can leave a persistent filtration benefit

**PP loses some benefit over tens of minutes, then retains a substantial remainder overnight.** After 30 seconds of rubbing spunbond PP with latex gloves, Zhao's Figure 3a gives approximately **6% efficiency before charging → 22% immediately → 15% at 30 minutes → 12% at one hour → 13% overnight**. About 60% of the initial added capture disappears in the first hour. These are graph readings at 22°C/40% RH, with photometric NaCl filtration at 5.3 cm/s, rather than size-resolved particle counts. [Zhao et al., 2020, Fig. 3a and supporting methods](https://doi.org/10.1021/acs.nanolett.0c02211)

**PET can retain a benefit for hours, but the demonstrated method was high-voltage corona charging.** Three-layer knitted PET improved from **86.79% to 92.61% efficiency**, falling to **89.02% by seven hours** and staying there through twelve. Equivalently, penetration fell **13.21% → 7.39% → 10.98%**: a **44% initial reduction, settling to 17%**. The experiment used PM2.5 monitors, 30 L/min and 58% RH. A comparable long-duration filtration result from rubbing ordinary PET fabric remains unestablished; Zhao's latex-rubbed polyester returned near baseline within 30 minutes. [Bandi et al., 2021, Fig. 11b/Table 2](https://doi.org/10.1098/rspa.2021.0062); [Zhao, Fig. 3a](https://doi.org/10.1021/acs.nanolett.0c02211)

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

The first permanently charged filter was Hansen's, from the 1930s: wool carded with powdered resin (colophony, i.e. rosin). The resin particles charge negative and cling to the positively charged wool fibres, which are ~17 µm across. It went into military respirators. Some secondary accounts describe soaking wool in resin dissolved in alcohol instead. Feltham (1979) and Hansen's patent haven't been checked to settle which. Resin wool degrades with humidity and oil mist; Brown's storage tests covered wool/acrylic and wool/PP resin wools containing 15–20% resin. [Feltham 1979 and fibre size, cited in AAQR](https://aaqr.org/articles/aaqr-22-11-pui-0405); [Brown, 1982](https://www.researchgate.net/publication/291116637_Degradation_of_electrostatic_filters_at_elevated_temperature_and_humidity)

The later resin-free blends need only two clean fibres of different polymers, carded together.

**PP + modacrylic** (UK patent family). 20 µm PP and 18 µm modacrylic at 60:40 by weight, about 2:1 by surface area. Both fibres were scoured with non-ionic detergent to strip spin finish, then carded and lightly needled. At 0.28 m/s it beat PP/wool about 6× in penetration at equal pressure drop, and pure PP about 150×. Penetration may double in the first 24 h, then rises only ×1.5 by a month and ×1.7 by a year: the same fast-then-flat shape as Zhao's PP. [US4798850A](https://patents.google.com/patent/US4798850A/en)

| Felt at 100 Pa, 0.28 m/s | Penetration | QF (kPa⁻¹) |
|---|---|---|
| PP + modacrylic | 0.07% | 73 |
| PP + wool | 0.40% | 55 |
| PP alone | 10.2% | 23 |

**Wool + PP** (CSIRO). Needle-punched blends work provided the fibres are adequately cleaned. Performance peaks at equal wool and PP surface areas, is ten times better than a blend that doesn't charge, and the charge held for at least 2.5 years. The commercial version claims at least 95% filtration efficiency at low pressure drop. [Schütz & Humphries, 2010](https://journals.sagepub.com/doi/10.1177/0040517509358803); [CSIRO ES3216](https://www.csiro.au/en/work-with-us/ip-commercialisation/marketplace/es3216-electrostatic-particle-filter-media)

**PP + POM** (DuPont): see above.

Every one of these insists on clean fibre, which fits the physics: spin finishes and antistats exist to conduct charge away. Wool and PP can both be had as loose fibre, which makes a hand-carded blend the most promising route to a durable home-made electret. It is a very different object from a rubbed shopping bag.

## Priority experiments and unresolved questions

- Test **wool and polyester rubbed against each other**, measuring each separately and together. For **PP**, compare latex and PTFE, including grounded versus ungrounded backing. Keep untreated controls and check whether rubbing changes pressure drop or damages the fabric. No superior rubbing partner is established for the wool/polyester blankets.
- Measure **penetration and pressure drop immediately, after an hour, overnight, and during sustained airflow/humidity exposure**, at our actual face velocities. Report count-based results by particle size and QF in kPa⁻¹. Storage persistence alone does not establish operating lifetime.
- Hand-card a **wool + PP** blend from scoured loose fibre, roughly equal surface areas, and compare against each fibre carded alone. Measure the day after carding, since the patents expect most of the loss in the first 24 h.
- Compare **as-received versus washed, thoroughly rinsed and dried material**, and separately explore mixed household fibres versus stacked fabrics. No dependable household charging wash or durable blend recipe is established yet.
- Do not assign a universal charge half-life to a polymer. Charge location, fibre structure, finishes and the measurement itself matter; a net-charge or surface-voltage decay curve does not uniquely determine filtration decay. The available evidence also does not establish a general PP-versus-PE ranking. [Oxenham et al., 2019, §§2–3](https://core.ac.uk/download/pdf/298009382.pdf)
