# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

# Example credit: https://github.com/Valdecy/pyDecision

from feloopy import *

m = madm('fuzzy_dematel','fuzzy_dematel_model', 'pydecision')

m.add_fcim([
    [  (  0,   0, 1/4),  (  0, 1/4, 1/2),  (1/4, 1/2, 3/4),  (  0,   0, 1/4)  ],   
    [  (1/2, 3/4,   1),  (  0,   0, 1/4),  (3/4,   1,   1),  (3/4,   1,   1)  ],   
    [  (1/2, 3/4,   1),  (1/4, 1/2, 3/4),  (  0,   0, 1/4),  (  0, 1/4, 1/2)  ],   
    [  (3/4,   1,   1),  (  0, 1/4, 1/2),  (1/4, 1/2, 3/4),  (  0,   0, 1/4)  ]    
    ])

m.sol(show_graph=False)

m.report(show_tensors=False)