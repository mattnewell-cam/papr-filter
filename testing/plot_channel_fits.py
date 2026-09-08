"""Plot the saved 0.5 um fits and measured log10PF; no refitting."""
import csv
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, FuncFormatter, NullFormatter
from fit_materials import observations, flat_observations, prediction

HERE = Path(__file__).resolve().parent
rows = list(csv.reader((HERE/'prototype_pf_q.csv').open(encoding='utf-8-sig')))
specs = json.loads((HERE/'fit_series.json').read_text())['materials']
fits = json.loads((HERE/'coefficients_0.5um.json').read_text())
fig, axes = plt.subplots(4,2,figsize=(10,13),layout='constrained')
for ax, (name,m) in zip(axes.flat,((n,m) for n,m in fits.items() if not n.startswith('_'))):
    obs = flat_observations(HERE/'iir_mask.csv','0.5') if name == 'IIR mask' else observations(rows,specs[name],'0.5')
    theta = [m['D'],m['C'],m['alpha']] + ([m['B'],m['beta']] if m['impaction_selected'] else [])
    ax.scatter([o['midpoint_velocity'] for o in obs],[o['y'] for o in obs],color='#222222',label='Measured',zorder=3)
    reference = obs[0]
    grid = []
    for v in np.geomspace(m['midpoint_v_lo'],m['midpoint_v_hi'],150):
        o = dict(reference,midpoint_velocity=v)
        if not o.get('flat'):
            o['K'] = v*(o['ri']+o['ro'])/2
        grid.append(o)
    ax.plot([o['midpoint_velocity'] for o in grid],prediction(theta,grid,m['t_layer'],m['impaction_selected']),color='#2465a8',label='Fit')
    ax.set(xscale='log',title=f"{name} (RMSE {m['log_rmse']:.3f} logs)",xlabel='Face velocity (cm/s)' if name=='IIR mask' else 'Mid-wall velocity (cm/s)',ylabel='Whole-test log₁₀ PF')
    ax.xaxis.set_major_locator(LogLocator(base=10,subs=(1,2,5)))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x,pos:f'{x:g}'))
    ax.xaxis.set_minor_formatter(NullFormatter())
    ax.grid(alpha=.2)
axes[0,0].legend()
fig.suptitle('0.5 µm count-based filtration fits',fontsize=16)
fig.savefig(HERE/'plots'/'fits_0.5um.png',dpi=150)
