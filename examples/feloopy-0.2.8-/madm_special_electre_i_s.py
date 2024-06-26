# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

# Example credit: https://github.com/Valdecy/pyDecision

from feloopy import *

m = madm('electre_i_s','electre_i_s_model', 'pydecision')

m.add_dm([
            [16000, 201, 8, 40, 5, 378, 31.3],  
            [18000, 199, 8, 35, 5, 474, 33.0],  
            [16000, 195, 8, 36, 1, 480, 33.9],  
            [18000, 199, 8, 35, 5, 430, 33.1],   
            [17000, 191, 8, 34, 1, 430, 34.4],   
            [17000, 199, 8, 35, 4, 494, 32.0],   
            [15000, 194, 8, 37, 3, 452, 33.8],   
            [18000, 200, 8, 36, 6, 475, 33.8],   
            [17000, 209, 7, 37, 3, 440, 30.9]    
            ])

m.add_qt([2000,   2,   1,   1,   1,  50, 0.1])
m.add_pt([3000,   5,   2,   3,   2,  82, 0.2])
m.add_vt([3500,   7,   3,   5,   6,  90, 0.5])
m.add_wv([0.3 , 0.1, 0.3, 0.1, 0.2, 0.2, 0.1])

m.sol(show_graph=False)

m.report(show_tensors=False)