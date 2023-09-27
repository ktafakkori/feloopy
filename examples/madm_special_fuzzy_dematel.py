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

m = madm('fuzzy_dematel','fuzzy_dematel_model', 'pydecision')

m.add_fcim([
    #          g1              g2                g3                  g4
    [  (  0,   0, 1/4),  (  0, 1/4, 1/2),  (1/4, 1/2, 3/4),  (  0,   0, 1/4)  ],   #g1
    [  (1/2, 3/4,   1),  (  0,   0, 1/4),  (3/4,   1,   1),  (3/4,   1,   1)  ],   #g2
    [  (1/2, 3/4,   1),  (1/4, 1/2, 3/4),  (  0,   0, 1/4),  (  0, 1/4, 1/2)  ],   #g3
    [  (3/4,   1,   1),  (  0, 1/4, 1/2),  (1/4, 1/2, 3/4),  (  0,   0, 1/4)  ]    #g4
    ])

m.sol(show_graph=False)

m.report(show_tensors=False)