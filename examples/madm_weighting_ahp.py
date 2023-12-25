# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

# Example credit: https://github.com/Valdecy/pyDecision

from feloopy import *

m = madm('ahp','ahp_model', 'pydecision')

m.add_cpcm([
  [1  ,   1/3,   1/5,   1  ,   1/4,   1/2,   3  ],   
  [3  ,   1  ,   1/2,   2  ,   1/3,   3  ,   3  ],  
  [5  ,   2  ,   1  ,   4  ,   5  ,   6  ,   5  ],   
  [1  ,   1/2,   1/4,   1  ,   1/4,   1  ,   2  ],   
  [4  ,   3  ,   1/5,   4  ,   1  ,   3  ,   2  ],   
  [2  ,   1/3,   1/6,   1  ,   1/3,   1  ,   1/3],   
  [1/3,   1/3,   1/5,   1/2,   1/2,   3  ,   1  ]   
])

m.sol()

m.report(show_tensors=True)