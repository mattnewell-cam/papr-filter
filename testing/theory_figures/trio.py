from pathlib import Path
import json, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from scipy.optimize import brentq

m = json.load(open(Path(__file__).resolve().parents[1]/'coefficients.json'))["grey fuzzy"]
tl = m["t_layer"]
a, c, k = m["D"]/tl, m["C"]/tl, m["k_layer"]/tl
al, Q, V, P = 0.5, 3000.0, 20000.0, 200.0
Ab = np.sqrt(k*Q*V/P); Lb = (V/Ab)*(a*(Q/Ab)**-al + c)
RHS = 2*V*P/(k*Q)
def solve(ri):
    ro = brentq(lambda r: np.log(r/ri)*(r*r-ri*ri) - RHS, ri*(1+1e-12), ri+500)
    H = V/(np.pi*(ro**2-ri**2)); K = Q/(2*np.pi*H)
    return ro, H, (2/3)*a*K**-0.5*(ro**1.5-ri**1.5) + c*(ro-ri)

RIS = [3.0, 10.0, 30.0]
G = [(ri, *solve(ri)) for ri in RIS]
xs, cur = [], 0.0
for ri, ro, H, L in G:
    xs.append(cur + ro); cur += 2*ro + 16
W = cur - 16
CEN = np.array([W/2 - G[0][1], 0.0, 22.0])
EL, D = np.radians(19.0), 2600.0
CAM = CEN + D*np.array([0.0, -np.cos(EL), np.sin(EL)]); F = D*7.4
n = lambda v: v/np.linalg.norm(v)
fwd = n(CEN-CAM); right = n(np.cross(fwd, [0,0,1.0])); up = np.cross(right, fwd)
def proj(p):
    d = np.asarray(p, float)-CAM; z = d @ fwd
    return np.array([F*(d @ right)/z, F*(d @ up)/z])
dist = lambda p: np.linalg.norm(np.asarray(p, float)-CAM)

N = 120; PH = np.linspace(0, 2*np.pi, N, endpoint=False)
def band(x0, r0, r1, z0, z1):
    o = []
    for i in range(N):
        A_, B_ = PH[i], PH[(i+1) % N]
        o.append([(x0+r0*np.cos(A_), r0*np.sin(A_), z0), (x0+r0*np.cos(B_), r0*np.sin(B_), z0),
                  (x0+r1*np.cos(B_), r1*np.sin(B_), z1), (x0+r1*np.cos(A_), r1*np.sin(A_), z1)])
    return o
ring = lambda x0, r, z: [(x0+r*np.cos(A_), r*np.sin(A_), z) for A_ in PH]

FILL, EDGE, INK = "#dedbd2", "#4a4945", "#2c2c2a"
fig, ax = plt.subplots(figsize=(11.6, 5.6), dpi=220)
polys = []
for (ri, ro, H, L), x0 in zip(G, xs):
    polys += band(x0, ro, ro, 0, H) + band(x0, ri, ri, 0, H)
    polys += band(x0, ri, ro, H, H) + band(x0, ri, ro, 0, 0)
polys.sort(key=lambda q: -dist(np.mean(q, 0)))
mid = np.median([dist(np.mean(q, 0)) for q in polys])
for q in polys:
    ax.add_patch(Polygon([proj(p) for p in q], closed=True, facecolor=FILL,
                         alpha=0.30 if dist(np.mean(q,0)) > mid else 0.55, lw=0, zorder=1))
for (ri, ro, H, L), x0 in zip(G, xs):
    for r, z in ((ro, H), (ri, H), (ro, 0), (ri, 0)):
        p = np.array([proj(q) for q in ring(x0, r, z) + [ring(x0, r, z)[0]]])
        ax.plot(p[:,0], p[:,1], color=EDGE, lw=1.1, zorder=3)
    for A_ in (0.0, np.pi):
        ax.plot(*zip(proj((x0+ro*np.cos(A_), ro*np.sin(A_), 0)),
                     proj((x0+ro*np.cos(A_), ro*np.sin(A_), H))), color=EDGE, lw=1.1, zorder=3)

    # H, on a dimension line clear of the left flank
    xh = proj((x0-ro, 0, 0))[0] - 16
    yb, yt = proj((x0-ro, 0, 0))[1], proj((x0-ro, 0, H))[1]
    ax.annotate("", xy=(xh, yt), xytext=(xh, yb), zorder=4,
                arrowprops=dict(arrowstyle="<|-|>", color=EDGE, lw=1.0, mutation_scale=11,
                                shrinkA=0, shrinkB=0))
    ax.text(xh-7, (yt+yb)/2, f"$H$ = {H:.0f} cm", fontsize=9, color=INK,
            rotation=90, ha="right", va="center", zorder=4)
    # t, bracketed off the rim where it reads widest
    pin, pout = proj((x0+ri, 0, H)), proj((x0+ro, 0, H))
    off = np.array([26.0, 26.0])
    ax.plot(*zip(pin+off, pout+off), color=EDGE, lw=1.0, zorder=4)
    for p in (pin, pout):
        ax.plot(*zip(p+off+[0,4], p+off-[0,4]), color=EDGE, lw=1.0, zorder=4)
        ax.plot(*zip(p, p+off), color=EDGE, lw=0.6, ls=(0,(2,2)), zorder=4)
    ax.text(*((pin+pout)/2+off+[0,7]), f"$t$ = {ro-ri:.1f} cm", fontsize=9, color=INK,
            ha="center", va="bottom", zorder=4)

ylo = min(proj((x0+r*np.cos(A_), r*np.sin(A_), 0))[1]
          for (ri, ro, H, L), x0 in zip(G, xs) for r in (ro,) for A_ in PH)
for (ri, ro, H, L), x0 in zip(G, xs):
    xc = proj((x0, 0, 0))[0]
    ax.text(xc, ylo-34, f"−{100*(1-L/Lb):.1f}%", fontsize=16, color=INK,
            ha="center", va="top", zorder=4)
    ax.text(xc, ylo-64, f"$r_i$ = {ri:.0f} cm", fontsize=10.5, color=INK,
            ha="center", va="top", zorder=4)

ax.set_aspect("equal"); ax.axis("off")
ax.relim(); ax.autoscale_view(); ax.margins(0.05, 0.10)
fig.tight_layout(pad=0.3)
out = str(Path(__file__).resolve().parents[1]/'plots'/ 'annulus_trio.png')
fig.savefig(out, facecolor="white")
for (ri, ro, H, L) in G:
    print(f"ri={ri:4.0f} ro={ro:6.2f} t={ro-ri:5.2f} H={H:6.2f} logPF={L:.4f} "
          f"dlog={L-Lb:+.3f}  PF {100*(10**(L-Lb)-1):+.1f}%")
print(out)
