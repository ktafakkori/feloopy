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

m = madm('critic','critic_model', 'pydecision')

m.add_dm([
            [250,  16,  12,  5],
            [200,  16,  8 ,  3],
            [300,  32,  16,  4],
            [275,  32,  8 ,  4],
            [225,  16,  16,  2]
            ])

m.sol(['min', 'max', 'max', 'max'])

m.report(show_tensors=False)