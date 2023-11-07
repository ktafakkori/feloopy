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

m = madm('topsis','topsis_model', 'pydecision')

m.add_dm([
        [6, 8, 4, 7],   
        [9, 3, 4, 6],   
        [4, 9, 7, 3],  
        [8, 2, 5, 8],  
        [4, 9, 2, 3],  
        [7, 5, 9, 9],   
        [9, 6, 3, 1],  
        [3, 5, 7, 6],   
        [5, 3, 8, 5],   
        [4, 6, 3, 8],   
        ])

m.add_wv([0.25, 0.25, 0.25, 0.25])

m.sol(['max', 'max', 'max', 'max'],show_graph=False, show_log=False)

m.report(show_tensors=False)