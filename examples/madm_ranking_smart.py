# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

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
