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

m = madm('borda','borda_model', 'pydecision')

m.add_dm([
        [7, 9, 9, 5],  
        [8, 7, 8, 7],   
        [9, 6, 8, 9],   
        [6, 7, 8, 6]    
        ])

m.sol(['max', 'max', 'max', 'min'],show_log=False)

m.report(show_tensors=False)