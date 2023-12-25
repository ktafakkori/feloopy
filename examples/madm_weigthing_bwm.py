# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

# Example credit: https://github.com/Valdecy/pyDecision

from feloopy import *

m = madm('bw','bw_model', 'pydecision')

m.add_bocv([1, 3, 4, 7])
m.add_owcv([7, 5, 5, 1])

m.sol()

m.report(show_tensors=False)