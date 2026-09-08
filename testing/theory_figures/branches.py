from pathlib import Path
import json, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

m = json.load(open(Path(__file__).resolve().parents[1]/'coefficients.json'))["grey fuzzy"]
tl = m["t_layer"]
a, c, k = m["D"]/tl, m["C"]/tl, m["k_layer"]/tl
al = 0.5
Q, P, V = 3000.0, 200.0, 20000.0

g  = lambda v: a*v**-al + c
A  = np.linspace(800, 8000, 1500); gv = g(Q/A)
Lv = lambda vol: (vol/A)*gv                 # volume-limited,   t = V/A
Lp = lambda pr:  (pr/(k*Q))*A*gv            # pressure-limited, t = AP/kQ

def draw(out, colour, curves, labels):
    fig, ax = plt.subplots(figsize=(9.0, 4.3), dpi=220)
    ax.plot(A, curves[0], color=colour, lw=2.2)
    ax.plot(A, curves[1], color=colour, lw=2.2, ls=(0, (2, 3)), alpha=0.55)
    ax.set_xlim(800, 8000); ax.set_ylim(0, 12)
    ax.set_xlabel("face area A (cm²)", fontsize=10, color="#898781")
    ax.set_ylabel(r"log$_{10}$ PF", fontsize=10, color="#898781")
    ax.grid(axis="y", color="#e1e0d9", lw=1); ax.set_axisbelow(True)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    for s in ("left", "bottom"): ax.spines[s].set_color("#c3c2b7")
    ax.tick_params(labelsize=9.5, colors="#898781")
    ax.xaxis.set_major_formatter(matplotlib.ticker.StrMethodFormatter("{x:,.0f}"))
    ax.legend(handles=[Line2D([], [], color=colour, lw=2.2, label=labels[0]),
                       Line2D([], [], color=colour, lw=2.2, ls=(0, (2, 3)), alpha=0.55, label=labels[1])],
              ncol=2, frameon=False, fontsize=9.5, labelcolor="#52514e",
              loc="lower left", bbox_to_anchor=(0.0, 1.01), handlelength=2.0, columnspacing=1.8)
    fig.tight_layout(); fig.savefig(out, facecolor="white"); plt.close(fig)
    return out

base = Path(__file__).resolve().parents[1]/'plots'
print(draw(base/'slab_volume_branch.png', "#eb6834", [Lv(20000), Lv(30000)],
           [r"Volume-limited, $V$ = 20 L", r"$V$ = 30 L"]))
print(draw(base/'slab_pressure_branch.png', "#2a78d6", [Lp(200), Lp(300)],
           [r"Pressure-limited, $\Delta p$ = 200 Pa", r"$\Delta p$ = 300 Pa"]))
