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

# Example credit: https://github.com/Valdecy/pyDecision

from feloopy import *

m = madm('promethee_iii','promethee_iii_model', 'pydecision')

m.add_dm([
        [8.840, 8.790, 6.430, 6.950],  
        [8.570, 8.510, 5.470, 6.910], 
        [7.760, 7.750, 5.340, 8.760],  
        [7.970, 9.120, 5.930, 8.090],  
        [9.030, 8.970, 8.190, 8.100],  
        [7.410, 7.870, 6.770, 7.230]  
        ])

m.add_qt([ 0.3,  0.3,  0.3,  0.3])
m.add_st([ 0.4,  0.4,  0.4,  0.4])
m.add_pt([ 0.5,  0.5,  0.5,  0.5])
m.add_wv([9.00, 8.24, 5.98, 8.48])
m.add_uf(['t5', 't5', 't5', 't5'])

m.sol(show_graph=False)

m.report(show_tensors=False)