'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.7)                               |
|  Modified: Wednesday, 27th September 2023 08:50:18 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''

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