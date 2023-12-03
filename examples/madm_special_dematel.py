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

m = madm('dematel','dematel_model', 'pydecision')

m.add_cim([
    [  0,  1,  2,  0  ],   
    [  3,  0,  4,  4  ],   
    [  3,  2,  0,  1  ],   
    [  4,  1,  2,  0  ]
    ])

m.sol(show_graph=False)

m.report(show_tensors=False)