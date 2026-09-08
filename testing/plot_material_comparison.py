"""Plot capture curves scaled to 100 Pa at 1 cm/s, from the 0.3 um catalogue."""
import json, math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
catalogue=json.loads((HERE/'coefficients.json').read_text())
v=np.geomspace(.3,100,600)
fig,ax=plt.subplots(figsize=(10.5,5.7))
for name,m in catalogue.items():
    if name.startswith('_'):
        continue
    y=100/m['k_layer']*(m['D']*v**-m['alpha']+m['C']+m.get('B',0)*v**m.get('beta',1))
    valid=(v>=m['v_lo'])&(v<=m['v_hi'])
    line,=ax.plot(v,y,'--',alpha=.5,lw=1)
    qf=1000*math.log(10)*(m['D']+m['C']+m.get('B',0))/m['k_layer']
    ax.plot(v,np.where(valid,y,np.nan),color=line.get_color(),lw=1.7,label=f'{name}: QF@1 = {qf:.1f} kPa⁻¹')
ax.set(xscale='log',yscale='log',xlabel='Face velocity (cm/s)',ylabel='log₁₀ PF, thickness chosen for 100 Pa at 1 cm/s')
ax.set_title('0.3 µm fits — solid: measured velocity range; dashed: extrapolation')
ax.grid(True,which='both',alpha=.18)
ax.legend(fontsize=8,ncol=2)
fig.tight_layout()
fig.savefig(HERE/'plots/material_comparison.png',dpi=200)
