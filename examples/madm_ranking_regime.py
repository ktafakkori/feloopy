# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

# Example credit: https://github.com/Valdecy/pyDecision

from feloopy import *

m = madm('regime','regime_model', 'pydecision')

m.add_dm([
        [250,  16,  12,  5],
        [200,  16,  8 ,  3],
        [300,  32,  16,  4],
        [275,  32,  8 ,  4],
        [225,  16,  16,  2]
        ])

m.add_wv([0.1, 0.4, 0.2, 0.4])

m.sol( ['min', 'max', 'max', 'max'], show_graph=False)

m.report(show_tensors=True)
