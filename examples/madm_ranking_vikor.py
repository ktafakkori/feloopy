# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

# Example credit: https://github.com/Valdecy/pyDecision

from feloopy import *

m = madm('vikor','vikor_model', 'pydecision')

m.add_dm([
            [250, 16, 12, 5],   #a1
            [200, 16, 8 , 3],   #a2
            [300, 32, 16, 4],   #a3
            [275, 32, 8 , 4],   #a4
            [225, 16, 16, 2]    #a5
            ])

m.add_wv([0.35, 0.30, 0.20, 0.15])

m.sol(['min', 'max', 'max', 'max'],show_graph=False)

m.report(show_tensors=False)
