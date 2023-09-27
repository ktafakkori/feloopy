'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.7)                               |
|  Modified: Wednesday, 27th September 2023 08:50:18 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''

# Example credit: https://github.com/Valdecy/pyDecision

from feloopy import *

m = madm('electre_i_s','electre_i_model', 'pydecision')

m.add_dm([
        [1, 2, 1, 5, 2, 2, 4],   
        [3, 5, 3, 5, 3, 3, 3],   
        [3, 5, 3, 5, 3, 2, 2],   
        [1, 2, 2, 5, 1, 1, 1],   
        [1, 1, 3, 5, 4, 1, 5]    
        ])

m.add_wv([0.0780, 0.1180, 0.1570, 0.3140, 0.2350, 0.0390, 0.0590])

m.sol(show_graph=False)

m.report(show_tensors=False)