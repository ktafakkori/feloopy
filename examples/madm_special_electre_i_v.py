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

m = madm('electre_i_v','electre_i_v_model', 'pydecision')

m.add_dm([
            [15,  9, 6, 10],   
            [10,  5, 7,  8],   
            [22, 12, 1, 14],   
            [31, 10, 6, 18],  
            [ 8,  9, 0,  9]   
            ])

m.add_vt([2, 2, 2, 2])
m.add_wv([7, 3, 5, 6])

m.sol(show_graph=False)

m.report(show_tensors=False)
