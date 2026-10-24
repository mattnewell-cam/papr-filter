# Electret layer calculator (paper-bag guide)

The user enters:

- the opened-out electret sheet (W × H, one ply);
- the centre of its 45 mm inlet hole;
- the filter face (W × H);
- the fan voltage and the airflow needed.

The page gives fold or cut instructions for a stack of equal rectangular layers, with a
drawing of the sheet. The model is in `solver.js`. `node electret_bag_calculator/test.cjs`
checks every candidate layout against a direct sample of where the hole lands.

**Layouts.** There are three kinds:

1. **Fold only:** the whole sheet is zig-zag folded into p × q panels.
2. **Trim, then fold:** strips are cut off the sheet first, then it is folded.
3. **Two pieces:** one straight cut, then each piece is trimmed and folded to the
   same panel size.

Each stack panel must fit the face. Every layer loses 2 cm on each side, so its active
area is (a − 4)(b − 4). The page does not show this margin.

**Hole.** It must end up in one of these places, in this order of preference:

1. In a corner of the stack, or cut off entirely.
2. On an edge of the stack. The hole lies within the 2 cm margin, apart from a sliver
   of at most 0.3 cm; a fold through its centre leaves 0.25 cm.
3. On an outside layer, to be taped. Only a corner panel of the fold grid can be
   brought to the outside.

The hole is never allowed in an inner layer. Candidate panel sizes and offsets include
those that put a fold line or a cut edge through the hole.

**Choice.** The goal is the flow target with at least 4 logs at 0.3 µm. Past 4 logs,
spare pressure goes into airflow, not more layers. Fold only is used if it reaches the
goal, then trim + fold, then two pieces. Within the first kind that reaches the goal,
the page picks the best hole placement, then the most flow. If no layout reaches the
goal, it picks the highest PF that still meets the flow, preferring fold only within
0.05 logs. If none meets the flow, it picks the most flow.

Not every paper bag has an electret layer. Single-ply bags are plain paper, and some
two-ply bags pair the paper with a tissue-paper lining rather than meltblown
([US6045595](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6045595)).
Single-ply bags are still sold, e.g. [Tough Guy 1-ply](https://www.amazon.com/clp/B007IBJHL2).
The calculator only applies to a meltblown lining.

## Model

- **Fan:** p = 0.765·V² − 0.000383·Q² (Q in L/min). This is the p–V–Q fit used in the
  "Vacuum bags & filters" tab of the testing sheet. The closed-end readings in the
  "Motor characterisation" tab give about half of 0.765·V² (93 Pa at 15 V against
  172 Pa), and that discrepancy is unresolved.
- **Per layer, at 0.3 µm:** Δp = R·v and log10PF = D·v^−α.

| electret | R, Pa/(cm/s) | D, α (default) | D, α (electret-only points) | measured v, cm/s |
|---|---|---|---|---|
| Arome Livii | 2.58 | 1.586, 0.307 | 2.348, 0.535 | 4.94–5.93 (inferred) |
| Kenmore | 3.09 | 1.585, 0.350 | 1.146, 0.221 | 8.69–14.40 |

## Where the numbers come from

All rows are from the live testing sheet, retrieved 2026-10-16.

- **Arome R:** a 6 cm diameter outlet at 15 V took 54.5 s to fill 100 L. That is
  110 L/min, 64.9 cm/s and 167 Pa from the fan fit. With the paper added, the same
  run took 154 s, giving 7.47 Pa/(cm/s) total. That total agrees with the whole-bag
  material's fitted 8.2 Pa/(cm/s).
- **Arome PF:** "Vacuum bags & filters" rows 38–39 are 4 layers at 10 V / 30 s and
  9 V / 35.5 s, with PF 4197 and 9906. **No area was recorded.** Face velocity is
  inferred from R and the fan fit, which implies ~565 cm². Only 59 and 25 particles
  were counted downstream.
- **Kenmore PF and R:** rows 35–36 are 5 layers on 198.4 cm² at 13 V / 58 s and
  18 V / 35 s, with PF 3571 and 1517 and 82 and 193 downstream counts. R comes from
  the fan fit (2.88 and 3.29) and is averaged.
- **Default slope:** each brand's two electret-only points span less than a factor
  of 1.7 in velocity. That is too short to fix α. Arome's own α (0.535) would also put
  the electret alone above the whole bag (electret + paper, `Materials summary` fit
  2.04·v^−0.307) below ~3 cm/s, which cannot be right. The default therefore takes α
  from the brand's whole-bag fit, which was measured over a wide velocity range, and
  fits only D to the electret points. With that choice the two brands' D values match
  to 0.1%.

## Basis weight and price

- **Basis weight:** the electret lining is about 20 g/m². This is an estimate; no weighing
  is recorded in the testing sheet.
- **Wholesale price at scale:** about US$2/kg for charged surgical-grade (BFE99) meltblown.
  [Fujian Angel](https://angelnonwoven.en.made-in-china.com/product/SFmaJONbrecu/China-Wholesale-Meltblown-Nonwoven-Fabric-Bfe99-Meltblown-Fabric.html)
  lists 25 g/m² BFE99 at US$2.29/kg for 1–5 t, US$2.19 for 5–10 t and US$1.99 above 10 t.
  [NWFabric](https://www.nwfabric.com/product/bfe-99-meltblown-nonwoven-fabric-for-mask/)
  lists electret-treated BFE99 at US$1.7–2.2. Before COVID, meltblown sold for about
  ¥18,000/t, roughly US$2.6/kg
  ([Global Times, 2020](https://www.globaltimes.cn/content/1180980.shtml)). All retrieved
  2026-10-24; these are asking prices, not transaction prices.
- The electret square calculator uses US$2/kg. At 20 g/m² that is about US$0.04/m².

### Why charged meltblown listings span 10×

1. **Grade, the main cause.** Respirator-grade meltblown (KF94, FFP2, N95) is a different
   product. It is 40–50 g/m² and hydro-charged, and it must stop ≥ 96–97% of a 0.3 µm oil
   aerosol at 55–95 L/min within 90–130 Pa. Surgical grade is about 25 g/m², rated by
   bacterial filtration efficiency (BFE), with ≤ 3 mmH₂O resistance. Qingdao Gon (Shenzhen
   002768) sells both: US$10,000–17,300/t for the
   [hydro-charged respirator grade](https://qdguoen.en.made-in-china.com/product/tXjmZPaLbCpl/China-Hydrocharging-Water-Electret-Meltblown-Fabric.html)
   against US$3,700–5,100/t for its
   [25 g/m² surgical grade](https://qdguoen.en.made-in-china.com/product/hXLxJluEujrG/China-100-PP-Bfe99-Pfe99-Vfe99-25GSM-En14683-Yy-T-0969-Melt-Blown-Fabric-for-Face-Mask.html).
   At about 20 g/m², the bag lining matches surgical grade.
2. **Stale listings.** Many Made-in-China prices were set in 2020–21 and never updated.
   Qingdao Gon's supplier profile was last active in October 2021. Meltblown went from about
   ¥20,000/t before COVID to ¥400,000/t at the 2020 peak
   ([NetEase, 2020](https://www.163.com/money/article/F73T1INM00259DLP.html)), so
   listings from the tail of that spike sit far above today's bulk prices.
3. **Volume.** This is small: Fujian Angel's tiers move the price about 15% between 1 t
   and 10 t.
4. **Missing units.** NWFabric's prices give no unit, and its own range is inconsistent: a
   water-electret N95 grade is listed below its BFE99 grade. Treat it as a rough check only.
