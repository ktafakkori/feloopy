# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

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