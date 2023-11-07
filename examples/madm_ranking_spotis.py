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

m = madm('spotis','spotis_model', 'pydecision')

m.add_dm([
        [10.5, -3.1,  1.7],  
        [-4.7,    0,  3.4],   
        [ 8.1,  0.3,  1.3],   
        [ 3.2,  7.3, -5.3]    
        ])

m.add_wv([0.2, 0.3, 0.5])
m.add_lbt([-5, -6, -8])
m.add_ubt([12, 10,  5])

m.sol(['max', 'min', 'max'], show_graph=False)

m.report(show_tensors=True)
