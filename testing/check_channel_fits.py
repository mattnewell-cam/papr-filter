"""Check channel selection, flat/radial predictions and saved 0.5 um fits."""
import csv
import json
import math
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from fit_materials import observations, flat_observations, prediction, fit

HERE = Path(__file__).resolve().parent
rows = list(csv.reader((HERE/'prototype_pf_q.csv').open(encoding='utf-8-sig')))
specs = json.loads((HERE/'fit_series.json').read_text())['materials']
fits = json.loads((HERE/'coefficients_0.5um.json').read_text())
assert not fits['_unresolved']
for name, m in fits.items():
    if name.startswith('_'):
        continue
    obs = flat_observations(HERE/'iir_mask.csv','0.5') if name == 'IIR mask' else observations(rows,specs[name],'0.5')
    theta = [m['D'],m['C'],m['alpha']] + ([m['B'],m['beta']] if m['impaction_selected'] else [])
    pred = prediction(theta,obs,m['t_layer'],m['impaction_selected'])
    residual = pred-np.array([o['y'] for o in obs])
    assert math.isclose(float(np.sqrt(np.mean(residual**2))),m['log_rmse'],abs_tol=1e-10)
    for o, p in zip(obs,pred):
        def capture(v):
            return m['D']*v**-m['alpha']+m['C']+m.get('B',0)*v**m.get('beta',1)
        independent = capture(o['midpoint_velocity']) if o.get('flat') else quad(lambda r:capture(o['K']/r)/m['t_layer'],o['ri'],o['ro'])[0]
        assert math.isclose(p,independent,rel_tol=1e-9)
        if not o.get('flat'):
            row = rows[o['row']-1]
            assert math.isclose(10**o['y'],float(row[20])/float(row[15]),rel_tol=1e-7)
    if name in specs:
        old = observations(rows,specs[name])
        assert all(o['y'] == float(rows[o['row']-1][6]) for o in old)
    print(f'{name}: channel, response and numerical prediction checks passed')
bad = [r[:] for r in rows]
bad[4][8] = '0'
try:
    observations(bad,specs['grey fuzzy'],'0.5')
except ValueError:
    pass
else:
    raise AssertionError('Zero PF must not become a fitted observation')

ignored = dict(specs['grey fuzzy'], series=[dict(rows=[91,96], description_prefix='Grey fuzzy only, halved', r_i=3)])
for channel in ('0.3','0.5'):
    try:
        observations(rows,ignored,channel)
    except ValueError as error:
        assert 'OLD / IGNORE' in str(error)
    else:
        raise AssertionError('Ignored measurements must never enter either fit')
published = json.loads((HERE/'coefficients.json').read_text())['grey fuzzy']
current = fit(observations(rows,specs['grey fuzzy']),published['t_layer'])
assert published['rows'] == [5,6,7,8,9]
for key in ('D','C','alpha','k_layer'):
    assert math.isclose(current[key],published[key],rel_tol=1e-8,abs_tol=1e-10), key
assert current['k_layer'] == fits['grey fuzzy']['k_layer']
print('Grey fuzzy: ignored rows rejected and both pressure coefficients agree')
