'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.8)                               |
|  Modified: Wednesday, 27th September 2023 08:50:18 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''

# Example credit: https://github.com/Valdecy/pyDecision

from feloopy import *

m = madm('fuzzy_bw','fuzzy_bw_model', 'pydecision')

m.add_fbocv([ (2/3, 1, 3/2), ( 1, 1, 1), (3/2, 2, 5/2 ), (2/3, 1, 3/2), (7/2, 4, 9/2) ])
m.add_fowcv([ (3/2, 2, 5/2), (7/2, 4, 9/2), (3/2, 2, 5/2) , (2/3, 1, 3/2), ( 1, 1, 1) ])

m.sol()

m.report(show_tensors=False)