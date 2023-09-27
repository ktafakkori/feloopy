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

m = madm('saw','saw_model', 'pydecision')

m.add_dm([
    [  25,   67,   7,  20],   
    [  21,   78,   6,  24],   
    [  19,   53,   5,  33],    
    [  22,   25,   2,  31]    
    ])

m.add_wv([0.25, 0.25, 0.25, 0.25])

m.sol( ['max', 'max', 'min', 'max'], show_graph=False)

m.report(show_tensors=True)
