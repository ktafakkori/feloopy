'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.8)                               |
|  Modified: Wednesday, 27th September 2023 08:50:18 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''

from feloopy import *

def instance(X):
    
    m = representor_model('heuristic','my_model','pymoo',X)
    
    x = m.pvar('x', [2], bound= [-1000,1000])
    
    m.obj(x[...,0]**2 + x[...,1]**2)
    
    m.obj((x[...,0]-2)**2 + (x[...,1]-2)**2)

    m.sol(['min','min'], 'ns-ga-ii', {'n_gen': 100}, obj_id='all')

    return m[X]

m = implement(instance)

m.solve(show_log=True)

m.report(sys_info=True, dec_info=True, all_metrics=True)