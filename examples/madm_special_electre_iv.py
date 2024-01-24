# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

# Example credit: https://github.com/Valdecy/pyDecision

from feloopy import *

m = madm('electre_iv','electre_iv_model', 'pydecision')

m.add_dm([
        [15, 80, 60, 30, 60, 50, 60,  70],   
        [25,  0, 40, 30, 40, 40, 50, 140],   
        [25,  0, 50, 30, 40, 40, 50, 140],   
        [25,  0, 50, 30, 50, 40, 70, 140],   
        [25,  0, 50, 30, 50, 40, 50, 140],   
        [15, 20, 50, 30, 50, 60, 60, 100],  
        [15, 80, 50, 50, 40, 90, 60, 100],   
        ])

m.add_qt([ 10,  10,  10,  10,  10,  10,  10,  10])
m.add_pt([ 20,  20,  20,  20,  20,  20,  20,  20])
m.add_vt([100, 100, 100, 100, 100, 100, 100, 100])

m.sol(show_graph=False)

m.report(show_tensors=True)