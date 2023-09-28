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

m = madm('entropy','entropy_model', 'pydecision')

m.add_dm([
        [0.22, 0.28, 0.24],
        [0.33, 0.32, 0.33],
        [0.44, 0.40, 0.43]
        ])

m.sol(['min', 'min', 'min'])

m.report(show_tensors=False)