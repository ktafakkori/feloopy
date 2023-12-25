# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

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