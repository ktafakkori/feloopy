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

m = madm('waspas','waspas_model', 'pydecision')

m.add_cim([
        [250, 16, 12, 5],   
        [200, 16, 8 , 3],  
        [300, 32, 16, 4],   
        [275, 32, 8 , 4], 
        [225, 16, 16, 2]    
        ])

m.add_wv([0.35, 0.30, 0.20, 0.15])

m.sol( ['min', 'max', 'max', 'max'], show_graph=False, show_log=False)

m.report(show_tensors=False)