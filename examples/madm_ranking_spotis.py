# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

# Example credit: https://github.com/Valdecy/pyDecision

from feloopy import *

m = madm('spotis','spotis_model', 'pydecision')

m.add_dm([
        [10.5, -3.1,  1.7],  
        [-4.7,    0,  3.4],   
        [ 8.1,  0.3,  1.3],   
        [ 3.2,  7.3, -5.3]    
        ])

m.add_wv([0.2, 0.3, 0.5])
m.add_lbt([-5, -6, -8])
m.add_ubt([12, 10,  5])

m.sol(['max', 'min', 'max'], show_graph=False)

m.report(show_tensors=True)
