N.B. this file is mainly for agents - it's dense and hard to parse. See PAPR Filtration gdoc for human-written, human-readable explanation of the theory and some testing results. 

# Bundle allocation theory — how to spend a fixed pressure budget

What to do with a given pile of blankets, given a flow rate you need and a pressure you
can afford. Derived from the per-layer model in `testing/RESULTS.md`; `testing/roll_model.py` computes
the general (non-uniform) case numerically.

These are model predictions. Constructed multi-material builds often achieve only
about half the PF predicted from single-material fits; see `testing/RESULTS.md`. This is not a universal correction.

Worked examples in §§1–6 use the current `testing/coefficients.json` (SHA256
`5514fecdc1e618ab52f42123988a51a33f94e86af8ea1b5666438d920512c566`).
Regenerate the numbers with `python testing/theory_examples.py`. §7 intentionally uses α=0.5.
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
impaction upturn — see `testing/RESULTS.md` for which, and the rule. The sections below are
written with the two-term form for readability; the impaction term changes none of the
conclusions, since it is small at the velocities a real bundle runs at.

Per centimetre of wall, dividing by t:

```
a(v) = (D*v^-alpha + C + B*v^beta)/t   logs per cm
Delta p = k*v per cm                   k in Pa per (cm/s) per cm
QF = 1000*ln(10)*a/(k*v)               (kPa^-1, thickness-independent)
```

`testing/coefficients.json` stores the per-layer fit as `D`, `C`, `B`, `alpha`, `beta`, `k_layer` (= k·t)
and `t_layer`; `testing/RESULTS.md` uses the same symbols as here.

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

`testing/roll_surface.py` draws the surface and solves this:
`python testing/roll_surface.py out.png --ro 15 --h 50`, or with no caps for the bare ridge.

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

The single-fibre theory the project runs on — Lee & Liu (1982) for capture, Davies for
pressure, both as implemented in `../../filtration_modelling/src/physics.rs` — gives d_f a
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
`../../filtration_modelling/CLAUDE.md`. The other two rows put it in context: in the
diffusion regime **finer fibres are slightly worse per pascal**, because drag grows as
d_f^(−2) while capture only grows as d_f^(−5/3); in interception finer fibres win outright.
The MPPS independence is not a coincidence — it is the crossover between the two, which is
what "most penetrating" means.

**This does not make fibre diameter irrelevant.** A finer medium moves its MPPS down —
meltblown filter media sit at 100–300 nm against ~600 nm for household cloth — so for a
fixed particle size of interest a fine-fibre medium can be operating on the interception
side of its own MPPS, where QF ∝ d_f^(−1). If the sizes we care about landed there, the
d_f^(1/3) verdict would flip in favour of fine fibres.

**Our mask data does not show that happening.** Interception is velocity-independent, so a
medium in interception territory would show log PF flat against v. The IIR mask sweep
(`IIR mask` tab of the testing sheet; 1–3 µm meltblown; PF at 0.3 µm over 5.1–54 cm/s)
fits D·v^−α + C with α pinned at the 2/3 cap — the full diffusion exponent — and an
interception floor of only C = 0.61 logs. At 0.3 µm the mask is still diffusion-dominated,
so its MPPS has not moved far enough below that size to put it in interception territory.
For now, at that particle size, the d_f^(1/3) regime is the one the data is in.

Davies is a continuum fit. At meltblown sizes (Kn = 2λ/d_f ≈ 0.04–0.13 for 1–3 µm) slip flow
softens the d_f^(−2) drag, so fine fibres recover a little QF relative to these exponents.

## Caveats

- §§1–6 are the **uniform-velocity limit**. Real bundles sit a few percent below it; §2
  says how far, and §7 does the 1/r integral exactly. Use `testing/roll_model.py` for a specific
  geometry.
- **§§1–6 need face area free to grow.** Every result there depends on being able to trade
  layers for breadth. If the build caps frontal area, adding resistive material stops
  paying and the break-even q rises toward 1 — §7 is what that looks like.
- Coefficients come from single-material roll sweeps and have not predicted a
  two-material build to better than ~20% at the top of the flow range — see `testing/RESULTS.md`.
- Δp is treated as linear in Q, and layers as independent of depth.
- Materials with an impaction term have a **worst velocity** rather than monotonically
  improving as flow drops — towel 3.8, duvet 2.8 cm/s. Slowing past that point still
  helps QF (pressure falls faster than protection) but stops helping PF.
