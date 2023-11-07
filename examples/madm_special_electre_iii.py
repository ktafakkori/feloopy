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

m = madm('electre_iii','electre_iii_model', 'pydecision')

m.add_dm([
        [8.84, 8.79, 6.43, 6.95],   
        [8.57, 8.51, 5.47, 6.91],   
        [7.76, 7.75, 5.34, 8.76],  
        [7.97, 9.12, 5.93, 8.09],
        [9.03, 8.97, 8.19, 8.10],
        [7.41, 7.87, 6.77, 7.23]  
        ])

m.add_qt([0.30, 0.30, 0.30, 0.30])
m.add_pt([0.50, 0.50, 0.50, 0.50])
m.add_vt([0.70, 0.70, 0.70, 0.70])
m.add_wv([9.00, 8.24, 5.98, 8.48])

m.sol(show_graph=False)

m.report(show_tensors=True)