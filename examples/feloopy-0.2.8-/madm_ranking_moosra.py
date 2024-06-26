# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

# Example credit: https://github.com/Valdecy/pyDecision

from feloopy import *

m = madm('moosra','moosra_model', 'pydecision')

m.add_dm([
        [3.5, 6, 1256, 4, 16, 3, 17.3, 8, 2.82, 4100],   
        [3.1, 4, 1000, 2, 8,  1, 15.6, 5, 3.08, 3800],   
        [3.6, 6, 2000, 4, 16, 3, 17.3, 5, 2.9,  4000],   
        [3,   4, 1000, 2, 8,  2, 17.3, 5, 2.6,  3500],   
        [3.3, 6, 1008, 4, 12, 3, 15.6, 8, 2.3,  3800],  
        [3.6, 6, 1000, 2, 16, 3, 15.6, 5, 2.8,  4000],   
        [3.5, 6, 1256, 2, 16, 1, 15.6, 6, 2.9,  4000]    
        ])

m.add_wv([0.297, 0.025, 0.035, 0.076, 0.154, 0.053, 0.104, 0.017, 0.025, 0.214])

m.sol(['max', 'max', 'max', 'max', 'max', 'max', 'max', 'max', 'min', 'min'],show_graph=False)

m.report(show_tensors=False)