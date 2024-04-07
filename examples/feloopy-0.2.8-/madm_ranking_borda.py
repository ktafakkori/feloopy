# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

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