N.B. this file is mainly for agents - it's dense and hard to parse. See PAPR Filtration gdoc for human-written, human-readable explanation of the theory and some testing results. 

# Bundle allocation theory — how to spend a fixed pressure budget

What to do with a given pile of blankets, given a flow rate you need and a pressure you
can afford. Derived from the per-layer model in `../testing/RESULTS.md`; `testing/roll_model.py` computes
the general (non-uniform) case numerically.

These are model predictions. Constructed multi-material builds often achieve only
about half the PF predicted from single-material fits; see `../testing/RESULTS.md`. This is not a universal correction.

Worked examples in §§1–6 use the current `../testing/coefficients.json` (SHA256
`a2dc3a34acd1442e32f8b1dbdfcb061b9910f8744d4e97fc956792c5d6ac8cbe`).
Regenerate the numbers with `python theory/theory_examples.py`. §7 intentionally uses α=0.5.
All tabulated QF values are kPa⁻¹; velocities are cm/s.

Everything here assumes you are free to choose the bundle's **face area**. That freedom
is what folding and core diameter buy you, and it is what makes the conclusions below
different from the usual filter intuition, where frontal area is fixed by a housing.

## Notation

A is face area (cm²), V material volume (cm³), t the per-layer thickness (cm), Q the
flow (cm³/s) and v = Q/A the face velocity (cm/s). Per layer:

```
log10PF = D*v^-alpha + C + B*v^beta
```

Diffusion, interception, impaction. B and beta are absent for materials with no
impaction upturn — see `../testing/RESULTS.md` for which, and the rule. The sections below are
written with the two-term form for readability; the impaction term changes none of the
conclusions, since it is small at the velocities a real bundle runs at.

Per centimetre of wall, dividing by t:

```
a(v) = (D*v^-alpha + C + B*v^beta)/t   logs per cm
Delta p = k*v per cm                   k in Pa per (cm/s) per cm
QF = 1000*ln(10)*a/(k*v)               (kPa^-1, thickness-independent)
```

`../testing/coefficients.json` stores the per-layer fit as `D`, `C`, `B`, `alpha`, `beta`, `k_layer` (= k·t)
and `t_layer`; `../testing/RESULTS.md` uses the same symbols as here.

A bundle of face area A and material volume V has a wall V/A thick, V/(A·t) layers, and
sees v = Q/A.

## 1. The flat plane is the ceiling — and this is the central result

**At a given pressure budget and required flow, no geometry beats a flat sheet with
uniform velocity. Every construction is measured only by how closely it approaches that
plane.** There is no clever shape that does better; there are only shapes that fall
short.

*Proof.* Divide the material into serial stages, each of face area A_j carrying the whole
flow at v_j = Q/A_j. With N_j = V_j/(A_j·t),

    Delta p  = k*t * sum_j N_j*v_j  ∝ sum_j v_j^2
    log10PF  = sum_j N_j*f(v_j)   ∝ sum_j v_j*f(v_j)

so at fixed Δp we maximise Σ v·f(v) subject to Σ v² fixed. Substituting u = v² gives
D·u^((1−α)/2) + C·u^(1/2), and both exponents lie in (0, 1) for any α ∈ (0, 1). The
objective is therefore **concave in u, so the equal split is the strict maximum**. Uniform
velocity is optimal for any physical α, not just the fitted ones. ∎

For 125×90 cm grey fuzzy at Δp = 202 Pa and Q = 180 L/min, the
corrected uniform velocity is 3.05 cm/s. Numerical examples below use only
the current three-ply grey-fuzzy tests; OLD / IGNORE rows are excluded.

### Two kinds of non-uniformity, very different in cost

- **Series** — velocity varying *along* the flow path, as it does across a roll's wall
  (v ∝ 1/r). Costs a few percent. Bounded and forgiving.
- **Parallel** — different flow paths seeing different velocities, the limit case being a
  leak. Parallel paths mix as an arithmetic mean of *penetration*, so the worst path
  dominates and a small bypass costs whole logs.

The one-fold example below loses 9.8% of the uniform-limit logs. A 1% bypass caps PF at 100 whatever
the material does. **These are not the same order of problem**, and every additional seam,
edge, joint and fold in a more elaborate build is a parallel-path risk taken on to chase a
series-path gain that is at most single-digit percent.

### There is also no packing pressure

The required face area is pinned by the constraints, not chosen: A = V/(t·N) with
N = √(V·Δp/(t²·k·Q)). For grey at 180 L/min and 202 Pa that is **0.098 m²**, growing only
as √V — 0.139 m² at double the material, 0.197 m² at quadruple. Pleats, concertinas and
cassettes exist to cram area into a fixed housing. There is no fixed housing here, and the
areas needed are small enough that a rolled bundle reaches them without effort.

### Therefore: build a roll

It hits the ceiling (within 10% in the one-fold example, ~0% with a few folds), it needs no cleverness to
reach the required area, and it has almost no seams. Everything a more elaborate geometry
could add is either unavailable — you cannot beat uniform — or unnecessary.

The one refinement worth considering is **several rolls in series**, to avoid betting
everything on one bundle's seal. In series, leaks multiply rather than dominate: two
bundles each with 1% bypass give a floor of 1e-4 penetration (PF 10,000) instead of 1e-2
(PF 100). And by the concavity result above, splitting the material into equal serial
stages is **exactly as good as a single roll** — the optimum has all stages at the same
velocity, which two equal rolls satisfy. So the redundancy is free in principle. In
practice each roll needs its own wide core and generous folding, or the series-path
penalty of §2 is paid twice.

This changes only if a hard constraint on bulk or shape forces face area down. Then you
are fighting for area again and geometry starts to matter.

## 2. Velocity uniformity in a roll: fold a lot, use a wide core

In a rolled bundle v varies as 1/r, so the inner layers run fast. Folding f times makes
the roll shorter (H = W/f) and, at fixed pressure, pushes the core diameter up, which
flattens the velocity profile. Holding a 125×90 cm grey blanket, Q = 180 L/min and
Δp = 202 Pa, solving for the core radius at each fold count:

| folds | ID (mm) | r_o/r_i | layers | v out→in | PF | QF |
|---|---|---|---|---|---|---|
| 1 | 11 | 6.44 | 10.14 | 1.56→10.07 | 27.5 | 16.41 |
| 2 | 41 | 2.54 | 11.06 | 2.06→5.22 | 35.4 | 17.66 |
| 4 | 108 | 1.59 | 11.34 | 2.46→3.92 | 38.4 | 18.06 |
| 8 | 246 | 1.26 | 11.42 | 2.73→3.44 | 39.2 | 18.16 |
| ∞ | — | 1.00 | 11.44 | uniform 3.05 | 39.5 | 18.20 |

**One fold loses 9.8% of the uniform-limit logs; four folds recover 92% of that gap.** Past that you
are chasing decimals with absurd geometry.

The mechanism is *not* that uniform velocity filters better. Per layer it is marginally
worse: D·v^-alpha + C is convex, so by Jensen a spread of velocities gives a higher mean
protection per layer at the same mean velocity under this two-term fit. The whole
gain is **layer count**, 10.14 → 11.44. Because Δp ∝ ln(r_o/r_i) rather than wall
thickness, a non-uniform bundle spends its pressure budget on the fast inner layers; the
same 202 Pa buys a 3.239 cm wall uniform against 2.870 cm at one fold.

Uniformity does not help the physics. It stops you wasting pressure.

## 3. Optimal allocation: half into depth, half into breadth

In the uniform limit with Q and Δp both fixed, the geometry is fully determined:

```
Delta p = k*t*N*Q/A      and     N*A*t = V
  =>   N = sqrt(V*Delta p/(t^2*k*Q))        A = V/(t*N)        v = Q/A
```

Equivalently, in wall thickness tau = N*t: tau = sqrt(V*Delta p/(k*Q)) and A = V/tau —
the form §7 uses.

There is no freedom left — one bundle shape satisfies both constraints. Doubling the
material gives **√2 more layers and √2 more face area**, with velocity dropping by √2.

## 4. Scaling with material

Since log10PF = N·(D·v^-alpha + C) with N ∝ V^0.5 and v ∝ V^-0.5, the diffusion term
scales as V^(0.5+alpha/2) and interception as V^0.5. For grey (alpha = 0.54491):

| material | layers | v (cm/s) | log10PF | PF | QF |
|---|---|---|---|---|---|
| ×0.5 | 8.09 | 4.32 | 1.047 | 11.1 | 11.9 |
| ×1 | 11.44 | 3.05 | 1.596 | 39.5 | 18.2 |
| ×2 | 16.19 | 2.16 | 2.456 | 286 | 28.0 |
| ×4 | 22.89 | 1.53 | 3.813 | 6.5e+03 | 43.5 |
| ×8 | 32.37 | 1.08 | 5.972 | 9.38e+05 | 68.1 |

Each doubling from ×1 to ×8 multiplies logs by 1.54–1.57. The diffusion-dominated
limit is 2^((1+α)/2) = 1.708. PF itself has no fixed multiplier.

Note Δp is fixed here, so QF scales exactly as log10PF.

## 5. Scaling with pressure budget

Fix the material and the required flow, and vary how much pressure you can spend. The
same optimum gives N ∝ Δp^0.5, A ∝ Δp^-0.5, v ∝ Δp^0.5, so

    log10PF = D' * Delta p^((1-alpha)/2)  +  C' * Delta p^(1/2)

For alpha = 0.54491 that is Δp^0.228 for diffusion and Δp^0.5 for interception. Note the
reversal from §4: here **interception is the term that scales better**, because extra
pressure raises velocity as fast as it raises layer count, and only diffusion is hurt by
velocity.

| Δp (Pa) | layers | v (cm/s) | log10PF | PF | QF |
|---|---|---|---|---|---|
| 50 | 5.69 | 1.52 | 0.950 | 8.91 | 43.7 |
| 100 | 8.05 | 2.15 | 1.224 | 16.7 | 28.2 |
| 202 | 11.44 | 3.05 | 1.596 | 39.5 | 18.2 |
| 400 | 16.10 | 4.29 | 2.085 | 122 | 12.0 |
| 800 | 22.78 | 6.07 | 2.756 | 571 | 7.9 |
| 1600 | 32.21 | 8.59 | 3.673 | 4.71e+03 | 5.3 |

Effective exponent ≈ **Δp^0.40**: doubling the pressure budget multiplies the logs by
1.31, against 1.54 for doubling material. **Pressure is the weaker of the two levers.**

### Why it is a square root, not linear

The tempting intuition is: double the pressure, halve the area, double the velocity —
which would give the diffusion term as Δp^(1-alpha). That is wrong, and the reason is
worth holding onto.

Halving the face area does not just double the velocity. The same material spread over
half the area is also **twice as thick**, so it has twice the layers. Pressure drop is
layers × velocity, so you have doubled *both* factors and needed **4× the pressure**, not
2×. Everything therefore moves on the square root of the pressure budget: √Δp more layers,
√Δp less area, √Δp more velocity.

That is the same reason §3's allocation splits material half into depth and half into
breadth — depth and breadth each cost pressure, and their product is what the budget buys.

## 6. Mixing materials — the practical decision

**If you don't have size constraints, it's usually worthwhile to add material even if
its QF is much worse — especially if you have a lot of it.**

Here "worthwhile" means higher PF, and therefore higher QF, at the same airflow Q and
pressure drop Δp, after resizing the filter's area and thickness. The calculation uses
uniform face velocity through both materials in series, with their available volumes
spread over a common face area; it is not simply adding layers to an unchanged build.

Let material 1 have volume V₁ and material 2 have volume V₂. Using the per-cm properties
a(v) and k defined above, assume pressure drop is linear in velocity and both materials
follow the same pure power law a(v) ∝ v^−α. Define

```
q = QF₂ / QF₁ = [a₂(v_old)/k₂] / [a₁(v_old)/k₁]
x = k₂*V₂ / (k₁*V₁)
```

Thus q compares the materials at the **same face velocity**, and x is their resistance
contribution ratio if spread over the same area; it includes both quantity and
resistivity. Equal volumes only give x = 1 when k₂ = k₁.

Since Δp = Q*(k₁V₁ + k₂V₂)/A², holding Q and Δp fixed gives
A_new/A_old = √(1+x) and v_new/v_old = 1/√(1+x). The lower velocity improves each
material's filtration per layer by (1+x)^(α/2), giving

```
QF_new / QF_old = ln(PF_new) / ln(PF_old)
                = (1 + q*x) / (1 + x)^((1 − α)/2)

Adding material improves protection exactly when, for x > 0:

q > [(1 + x)^((1 − α)/2) − 1] / x
```

Equality is break-even. These are multipliers of **log PF**, not PF itself.

| Velocity exponent α | Threshold q for a tiny addition (x → 0) | Threshold q for equal resistance contributions (x = 1) |
|---|---:|---:|
| 0 | 50% | 41.4% |
| ½ | 25% | 18.9% |
| ⅔ | 16.7% | 12.2% |

The tiny-addition threshold is (1−α)/2. For 0 ≤ α < 1, the threshold decreases as x
increases: a larger supply of poorer material can still help, and diffusion-like
velocity dependence makes the threshold lower still. The fitted diffusion +
interception + impaction curves are not a shared pure power law; evaluate each
material's a(v) at the new velocity for those predictions.

Worked example, calculated with the velocity-dependent fits at the new common
face velocity (equal material volumes; grey blanket V, Q = 180 L/min, Δp = 202 Pa):

| | log10PF | PF | QF | vs grey alone (logs) |
|---|---|---|---|---|
| grey alone (V) | 1.596 | 39.5 | 18.20 | — |
| grey + grey (2V) | 2.456 | 286 | 28.00 | ×1.54 |
| grey + pink, batch-2 fit | 1.861 | 72.6 | 21.21 | ×1.17 |

The old combined-pink fit is absent from the current coefficient catalogue, so its
example is no longer presented as reproducible.

## 7. Size caps: the achievable surface and where its maximum sits

Everything above assumes face area is free to grow. A real build also has a box — an
outer radius cap R_max and a length cap H_max. Those two together, not the cylinder's
shape, are what actually cost you.

**Construction.** A bundle has three geometric freedoms (r_i, r_o, H). Parametrise two of
them as face area A = 2*pi*rbar*H and radius ratio rho = r_o/r_i, and write
x = tau/rbar = 2(rho-1)/(rho+1). The third, wall thickness tau, is *not* free — it is set
by whichever budget binds first:

```
tau_p = Delta p*A*x/(k*Q*ln rho)     pressure exhausted
tau_v = V/A                          cloth exhausted
tau   = min(tau_p, tau_v)
```

Then rbar = tau/x, r_i = rbar - tau/2, r_o = rbar + tau/2, H = A/(2*pi*rbar), and with
K = Q*rbar/A (so v(r) = K/r):

```
log10PF = (D/t)*K^-alpha*(r_o^(1+alpha) - r_i^(1+alpha))/(1+alpha) + (C/t)*tau
```

**The ridge.** tau_p = tau_v at `A*(rho) = sqrt(V*k*Q*ln rho/(Delta p*x))`. Below it
pressure binds and cloth is left over; above it cloth binds and pressure is left over.
log10PF rises with A on one side and falls on the other, so the surface is two faces
meeting along a ridge — the locus where **both budgets are exactly exhausted**. §3's
uniform solution is the rho -> 1 end of that ridge.

**Why the cap contours kink at the ridge.** Because tau is piecewise, so is everything
derived from it. On the pressure face r_o is proportional to A and H does not depend on A
at all (H = k*Q*ln rho/(2*pi*Delta p)); on the volume face r_o goes as 1/A and H as A^2.
So r_o *peaks* exactly at the ridge — which is why the r_o = R_max contour is a closed
loop straddling the ridge rather than a simple curve — and the H = H_max contour runs
dead straight along a constant-rho line across the pressure face before bending.

**The maximum.** Two tangency ratios decide it:

```
rho_C  ridge has r_o = R_max:   2*rho^2/((rho^2-1)*ln rho) = R_max^2*k*Q/(Delta p*V)
rho_H  ridge has H = H_max:     rho_H = exp(2*pi*Delta p*H_max/(k*Q))
```

log10PF falls with rho along the ridge, so the optimum sits at **rho\* = min(rho_C, rho_H)**:

- **rho_C <= rho_H** — the radius cap bites first, the optimum stays *on* the ridge, and
  Delta p, V and r_o are all tight with H slack.
- **rho_C > rho_H** — no point on the ridge is legal. The optimum is *pinched off* it onto
  the pressure face, where Delta p, r_o and H are tight and **cloth goes unused**.

`theory/roll_surface.py` draws the surface and solves this:
`python theory/roll_surface.py out.png --ro 15 --h 50`, or with no caps for the bare ridge.

### Results

Grey fuzzy, Q = 180 L/min, Δp = 200 Pa, V = 20 L, alpha = 0.5. Flat plane = 5.108 logs.

**Radius ratio barely matters.** Cost of being a cylinder at all, at the same Δp and V:

| r_o/r_i | 1.5 | 2 | 3 | 4 | 6 | 8 | 19 |
|---|---|---|---|---|---|---|---|
| vs flat plane | −0.6% | −1.7% | −3.9% | −5.9% | −9.1% | −11.4% | −18.2% |

Any sane roll sits at rho = 2–4, so the shape penalty is **single-digit percent of the
logs**. Leave r_o unconstrained and you simply walk down the ridge toward rho -> 1 and
recover the slab.

**The caps are what sting** — and not by making the shape worse:

| R_max | H_max | log10PF | cloth used | binding |
|---|---|---|---|---|
| — | — | 5.11 | 20.0 L | flat plane |
| 15 | 50 | 5.01 | 20.0 L | Δp, V, r_o |
| 15 | 40 | 5.01 | 20.0 L | Δp, V, r_o |
| 12 | 50 | 4.88 | 19.7 L | Δp, r_o, H |
| 12 | 40 | 4.08 | 14.6 L | Δp, r_o, H |

At R_max = 15 cm the length cap is free: the winning build is only 36.5 cm long, so
tightening H from 50 to 40 costs nothing. Tighten the radius to 12 cm and that same 10 cm
of length now costs **0.80 logs**. The mechanism is the last column — once pinched off the
ridge the build can no longer consume the cloth you own, 14.6 L of 20 L. You are not
paying for a worse shape; you are paying for material that will not fit in the box.

## 8. Fibre diameter: where it matters and where it cancels

The single-fibre theory the project runs on — Lee & Liu (1982) Eq. (38) for capture
(coefficients 1.6 and 0.6, no cross term), Davies × 0.67 for pressure, both as implemented
in `../../../filtration_modelling/src/physics.rs` (`single_fibre`, `davies_dp_real`) — gives d_f a
different exponent in each regime. With Λ = ln PF, L the wall thickness, α the solidity
and Pe = v·d_f/D_B (D_B the particle's Brownian diffusivity — not the fitted D above):

```
diffusion      eta_D ∝ Pe^(-2/3)        =>  Lambda ∝ L * d_f^(-5/3) * v^(-2/3)
interception   eta_R ∝ (d_p/d_f)^2      =>  Lambda ∝ L * d_f^(-3)
Davies         Delta p ∝ L * v / d_f^2
```

(Λ carries an extra 1/d_f over η because a wall L thick presents 4αL/(π·d_f·(1−α))
fibre-diameters of target.) At fixed thickness:

| regime | Λ ∝ | Δp ∝ | QF ∝ |
|---|---|---|---|
| diffusion | d_f^(−5/3) | d_f^(−2) | **d_f^(+1/3)** |
| MPPS (Lee & Liu 1974) | d_f^(−2) | d_f^(−2) | **d_f^0** |
| interception, R ≪ 1 | d_f^(−3) | d_f^(−2) | **d_f^(−1)** |

The MPPS row is the Google Doc's result (`../PAPR Filtration Google Doc.md`, lines
157–190): Λ_MPPS = 0.911·αL·((1−α)Ku)^−½·d_f^−2·v^−½·(C_c·kT/η)^½ against Davies scaled by
0.67, so QF_MPPS ∝ d_f^0 — recorded as a settled position in
`../../../filtration_modelling/CLAUDE.md`. The other two rows put it in context: in the
diffusion regime **finer fibres are slightly worse per pascal**, because drag grows as
d_f^(−2) while capture only grows as d_f^(−5/3); in interception finer fibres win outright.
The MPPS independence is not a coincidence — it is the crossover between the two, which is
what "most penetrating" means.

**This does not make fibre diameter irrelevant.** A finer medium moves its MPPS down, so
for a fixed particle size of interest a fine-fibre medium can be operating on the
interception side of its own MPPS, where QF ∝ d_f^(−1). If the sizes we care about landed
there, the d_f^(1/3) verdict would flip in favour of fine fibres.

**Correction (2026-09-25): the household-cloth MPPS is not ~600 nm.** This section
previously put meltblown at 100–300 nm against ~600 nm for household cloth. Measurement
says otherwise: PF rises monotonically from 0.3 to 1 µm in 95% of the prototype rows, so
these fabrics' MPPS is **at or below 0.3 µm** — the counter's smallest channel — and
0.3 µm is the measured worst case over the RFP's 0.3–10 µm range. See
`../testing/RESULTS.md`, "Particle size". The ~600 nm figure came from a monodisperse
20 µm fibre idealisation; real fleece and napped blanket carry a wide diameter
distribution with fine surface fibres, and interception scales as (d_p/d_f)².

**Our mask data does not show that happening.** Interception is velocity-independent, so a
medium in interception territory would show log PF flat against v. The IIR mask sweep
(`Mask & MERV` tab of the testing sheet; 1–3 µm meltblown; PF at 0.3 µm over 5.1–54 cm/s)
fits D·v^−α + C with α pinned at the 2/3 cap — the full diffusion exponent — and an
interception floor of only C = 0.61 logs. At 0.3 µm the mask is still diffusion-dominated,
so its MPPS has not moved far enough below that size to put it in interception territory.
For now, at that particle size, the d_f^(1/3) regime is the one the data is in.

Davies is a continuum fit. At meltblown sizes (Kn = 2λ/d_f ≈ 0.04–0.13 for 1–3 µm) slip flow
softens the d_f^(−2) drag, so fine fibres recover a little QF relative to these exponents.

### 8.1 Reference table: mechanical QF by fibre and particle size

Lee & Liu (1982) Eq. (38) — coefficients 1.6 and 0.6, no cross term — over Davies × 0.67,
α = 0.05, 1 cm/s, 20 °C. QF = ln PF / Δp in kPa⁻¹, split by mechanism. Impaction omitted:
St < 0.1 everywhere except the starred cell (0.36). Generated with
`cargo run --release -- qf --df_um 0.1,1,10,20` in `filtration_modelling`; rerun that,
don't hand-roll.

| d_f (µm) | d_p (µm) | Diffusion | Interception | Total |
|---:|---:|---:|---:|---:|
| 0.1 | 0.1 | 101 | 27 | 129 |
| 0.1 | 0.3 | 32 | 123 | 156 |
| 0.1 | 0.5 | 21 | 229 | 249 |
| 0.1 | 1.0 | 12 | 499 | 510\* |
| 1 | 0.1 | 219 | 5 | 224 |
| 1 | 0.3 | 70 | 38 | 108 |
| 1 | 0.5 | 45 | 91 | 136 |
| 1 | 1.0 | 26 | 274 | 300 |
| 10 | 0.1 | 471 | 1 | 472 |
| 10 | 0.3 | 150 | 5 | 155 |
| 10 | 0.5 | 96 | 13 | 109 |
| 10 | 1.0 | 55 | 50 | 105 |
| 20 | 0.1 | 594 | 0 | 594 |
| 20 | 0.3 | 190 | 2 | 192 |
| 20 | 0.5 | 121 | 7 | 128 |
| 20 | 1.0 | 70 | 26 | 96 |

Reading it:

- The 10 and 20 µm rows are inside Eq. (38)'s fitted range (R = 0.0045–0.12, St ≤ 0.22).
  The 0.1 µm row is not: R ≥ 1 there, and at α = 0.05 the mean fibre gap is ~0.4 µm, so a
  1 µm particle is sieved rather than intercepted. Single-fibre theory has nothing to say
  about that cell; a real medium's PF is then set by its largest pores, not the mean —
  the channelling result in the fibreglass derisking doc.
- The 0.1 µm column is also at Kn ≈ 1.3, where Davies (a continuum fit) overpredicts Δp,
  so those QFs are floors.
- Coarse fibres win on diffusion per pascal (the d_f^(1/3) row above) and, *in this table*,
  push the MPPS up to ~1 µm; fine fibres are already deep in interception at 0.5 µm.
  **The measured fabrics do not behave this way** — their PF rises monotonically from 0.3
  to 1 µm, so their MPPS is at or below 0.3 µm (`../testing/RESULTS.md`, "Particle size").
  Read the ~1 µm figure as a property of the monodisperse idealisation, not of blanket.
- Scaling to other velocities: diffusion ∝ v^(−5/3), interception ∝ v^(−1).

### 8.2 Fibre diameters in HEPA glass paper

**Measured sheets.** SEM image analysis of commercial HEPA ("THE") glass papers, count basis.
Every number read from the thesis page, not a summary.

| Medium | Source | Count median d₅₀ (µm) | GSD | Count mean (µm) | Sheet |
|---|---|---|---|---|---|
| Bernard Dumas D309 | [Pénicot-Baugé 1998](http://docnum.univ-lorraine.fr/public/INPL_T_1998_PENICOT_BAUGE_P.pdf), Tab. 5 | 0.70 | 1.44 | 0.86 | α 0.056 |
| Bernard Dumas D309, re-measured | [Mouret 2008](http://docnum.univ-lorraine.fr/public/INPL/2008_MOURET_G.pdf), Fig. A-19 (read from curve) | ≈ 0.9 | ≈ 1.9 (d₈₄/d₅₀) | — | α 0.078, 409 µm |
| Bernard Dumas D350 | Pénicot-Baugé 1998, Tab. 5 | 0.76 | 1.50 | 0.88 | α 0.059 |
| IRSN nuclear-grade THE | [Joubert 2009](http://docnum.univ-lorraine.fr/public/INPL/2009_JOUBERT_A.pdf), Tab. 2-11 (165 fibres) | 0.6 | 2.2 | 0.9 | α 0.071, 521 µm, 92 g/m² |
| Nuclear-grade THE | [Bourrous 2014](http://docnum.univ-lorraine.fr/public/DDOC_T_2014_0301_BOURROUS.pdf), Tab. 4 | — | — | 0.59–0.60 | α 0.078, 450 µm |
| Whatman THE | Pénicot-Baugé 1998, Tab. 5 | 0.33 | 1.63 | 0.36 | α 0.056 |

**Typical HEPA glass paper: count median 0.6–0.9 µm, GSD 1.4–2.2.** Whatman's lab paper is
the fine outlier at 0.33 µm.

**Recipes.** Patent worked examples, HEPA-grade by test. Diameters are the fibre maker's
nominal grade value, which Johns Manville defines as a BET (surface-area) diameter —
[code 106 = 0.65 µm, 110X = 2.70 µm](https://www.jm.com/content/dam/jm/global/en/engineered-products/EP-documents/Product_Data_Sheets/Fibers/Micro_Fibers/Americas/FINAL%20VERSION_EP_Microfibers_Sell_Sheet_LR.pdf) —
not a count median. [DOE-HDBK-1169-2003](https://www.energy.gov/sites/default/files/2026-05/DOE-HDBK-1169-2003_Chapter-3.pdf)
Table 3.1 gives the same codes as freeness-test ranges (106: 0.54–0.63 µm).

| Source | Fine grade | Coarse grade | Chopped strand | Sheet and result |
|---|---|---|---|---|
| [Hokuetsu US 6,939,386](https://patents.google.com/patent/US6939386B2/en), Ex. 1 | 60 wt% 0.65 µm | 35 wt% 2.70 µm | 5 wt% 6 µm | 70 g/m²; 280 Pa at 5.3 cm/s; 99.9936 % at 0.3–0.4 µm |
| [H&V US 8,709,120](https://patents.google.com/patent/US8709120B2/en), Ex. 1 | 61 wt% 0.6 µm | 30 wt% 3.0 µm | 9 wt% 6.5 µm | 70.8 g/m², 0.295 mm; 399 Pa at 5.3 cm/s; 0.0007 % pen. at 0.3 µm |
| [Hokuetsu US 8,951,324](https://patents.google.com/patent/US8951324B2/en), Ref. Ex. 1 | 90 wt% JM 106-475 (0.65 µm) | 10 wt% JM 110X-475 (2.70 µm) | none | 70 g/m²; 441 Pa at 5.3 cm/s; 99.9965 % at 0.1–0.15 µm |

**Unresolved:** a 0.65 µm-BET grade should have a count median below 0.65 µm, so these
recipes predict finer sheets than the European papers measured above. No measured
distribution exists for a US or Japanese recipe paper, so this could be a real product
difference or a plan-view SEM detection floor near 0.25 µm.

**Rejected — do not cite:**

- [Moelter & Fissan 1997](https://doi.org/10.1080/02786829708965484) (H13, polished cross-sections): their
  64-class histograms are mass-weighted and unreliable below 0.45 µm. Count mean 0.7–0.8 µm
  agrees with the table; the "2.7 µm median" is by mass and should not be compared with anything above.
- [Charvet et al. 2018](https://hal.science/hal-01828938v1): "mean fibre diameter 1.6 µm", ~300 fibres,
  weighting and method unstated.
- DOE-HDBK-1169-2003 §3.3.1 "0.2 to 0.5 µm": asserted from theory, contradicted by its own
  Table 3.1, deleted from the 2022 edition.
- Pui group "HE 1073 = 1.9 µm" (KONA 2013): derived from Δp, and the sheet is 87 % at 0.3 µm, not HEPA.
- Wikipedia "0.5 to 2.0 µm": cites a hospital-planning textbook.
- [WO 2021/072122](https://patents.google.com/patent/WO2021072122A1/en): electrospun nylon, not glass; its "1.52" is g/m².
- "0.64–1.52 µm fine / 2.03–4.57 µm coarse": a search-engine attribution that appears in no patent.

## 9. Masks as a filter bank: layers are cheaper than area

The IIR mask fit (`../testing/RESULTS.md`) has an interception floor C = 0.61 logs per
layer that costs no area, so for a fixed logs target stacking layers needs less mask than
spreading one layer wide — until pressure, k = 7.83 Pa/(cm/s) per layer, bites. For
170 L/min and 3 logs, masks 12.5 × 15 cm with 30% of the area lost to seams and edges
(131 cm² usable each):

| layers | v (cm/s) | masks | Δp (Pa) |
|---|---|---|---|
| 1 | 3.1\* | 6.9 | 25 |
| 2 | 13.8 | 3.1 | 217 |
| 3 | 48 | 1.3 | 1126 |
| 4 | 227\* | 0.4 | 7095 |

\* outside the 5.1–54 cm/s measured range.

Without a pressure limit the answer degenerates (five layers reach 3 logs on the floor
alone, at any velocity). At a **200 Pa budget** two layers is the optimum: 222 cm² effective
per layer, 3.4 masks. In whole masks, **4 masks as two layers of two** — 10.8 cm/s,
3.3 logs, 169 Pa.

## Caveats

- §§1–6 are the **uniform-velocity limit**. Real bundles sit a few percent below it; §2
  says how far, and §7 does the 1/r integral exactly. Use `testing/roll_model.py` for a specific
  geometry.
- **§§1–6 need face area free to grow.** Every result there depends on being able to trade
  layers for breadth. If the build caps frontal area, adding resistive material stops
  paying and the break-even q rises toward 1 — §7 is what that looks like.
- Coefficients come from single-material roll sweeps and have not predicted a
  two-material build to better than ~20% at the top of the flow range — see `../testing/RESULTS.md`.
- Δp is treated as linear in Q, and layers as independent of depth.
- Materials with an impaction term have a **worst velocity** rather than monotonically
  improving as flow drops — towel 3.8, duvet 2.8 cm/s. Slowing past that point still
  helps QF (pressure falls faster than protection) but stops helping PF.
