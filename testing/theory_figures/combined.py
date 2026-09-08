from pathlib import Path
import json, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

m = json.load(open(Path(__file__).resolve().parents[1]/'coefficients.json'))["grey fuzzy"]
tl = m["t_layer"]
a, c, k = m["D"]/tl, m["C"]/tl, m["k_layer"]/tl
al, Q = 0.5, 3000.0

g  = lambda v: a*v**-al + c
A  = np.linspace(800, 8000, 3000); gv = g(Q/A)
Lp = lambda P: (P/(k*Q))*A*gv
Lv = lambda V: (V/A)*gv
star = lambda P, V: (np.sqrt(k*Q*V/P), (V/np.sqrt(k*Q*V/P))*g(Q/np.sqrt(k*Q*V/P)))

BLUE, ORANGE = "#2a78d6", "#eb6834"
G_DARK, G_MID, G_LIGHT = "#5dcaa5", "#9fe1cb", "#e1f5ee"
DASH = (0, (2, 2.5))

fig, ax = plt.subplots(figsize=(9.0, 4.8), dpi=220)

ax.fill_between(A, 0, np.minimum(Lp(300), Lv(30000)), color=G_LIGHT, lw=0, zorder=0)
for P, V in ((300, 20000), (200, 30000)):
    ax.fill_between(A, 0, np.minimum(Lp(P), Lv(V)), color=G_MID, lw=0, zorder=1)
ax.fill_between(A, 0, np.minimum(Lp(200), Lv(20000)), color=G_DARK, lw=0, zorder=2)

for P, V, lab in ((200, 20000, "Default"),
                  (300, 20000, "Increase pressure budget"),
                  (200, 30000, "Increase material budget"),
                  (300, 30000, "Increase both")):
    As, Ls = star(P, V)
    ax.hlines(Ls, 800, As, colors="#000000", ls=(0, (5, 3)), lw=1.3, zorder=5)
    ax.text(880, Ls + 0.08, lab, fontsize=5.4, color="#000000",
            ha="left", va="bottom", zorder=6)

ax.plot(A, Lp(200), color=BLUE,   lw=2.2, zorder=4)
ax.plot(A, Lp(300), color=BLUE,   lw=2.2, ls=DASH, zorder=4)
ax.plot(A, Lv(20000), color=ORANGE, lw=2.2, zorder=4)
ax.plot(A, Lv(30000), color=ORANGE, lw=2.2, ls=DASH, zorder=4)

ax.set_xlim(800, 8000); ax.set_ylim(0, 9)
ax.set_xlabel("face area A (cm²)", fontsize=10, color="#898781")
ax.set_ylabel(r"log$_{10}$ PF", fontsize=10, color="#898781")
ax.grid(axis="y", color="#e1e0d9", lw=1); ax.set_axisbelow(True)
for s in ("top", "right"): ax.spines[s].set_visible(False)
for s in ("left", "bottom"): ax.spines[s].set_color("#c3c2b7")
ax.tick_params(labelsize=9.5, colors="#898781")
ax.xaxis.set_major_formatter(matplotlib.ticker.StrMethodFormatter("{x:,.0f}"))
ax.legend(handles=[
    Line2D([], [], color=BLUE,   lw=2.2,            label=r"$\Delta p$ = 200 Pa"),
    Line2D([], [], color=BLUE,   lw=2.2, ls=DASH,   label=r"$\Delta p$ = 300 Pa"),
    Line2D([], [], color=ORANGE, lw=2.2,            label=r"$V$ = 20 L"),
    Line2D([], [], color=ORANGE, lw=2.2, ls=DASH,   label=r"$V$ = 30 L")],
    ncol=4, frameon=False, fontsize=9.5, labelcolor="#52514e",
    loc="lower left", bbox_to_anchor=(0.0, 1.01), handlelength=2.4, columnspacing=2.2)
fig.tight_layout()
out = str(Path(__file__).resolve().parents[1]/'plots'/ 'slab_budget_grid.png')
fig.savefig(out, facecolor="white"); print(out)
