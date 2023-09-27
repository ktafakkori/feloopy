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

m = madm('smart','smart_model', 'pydecision')

m.add_dm([
        [25000, 153, 15.3, 250],   
        [33000, 177, 12.3, 380],   
        [40000, 199, 11.1, 480]  
        ])

m.add_grades([9, 5, 7, 6])
m.add_ubt([40000, 220, 20, 2000])
m.add_lbt([20300, 140, 8.2, 230])

m.sol(['min', 'max', 'min', 'max'], show_graph=False)

m.report(show_tensors=True)
