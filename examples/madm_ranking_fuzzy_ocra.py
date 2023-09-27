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

m = madm('fuzzy_ocra','fuzzy_ocra_model', 'pydecision')

m.add_fdm([
    [ (  3,   6,   9), (  5,   8,   9), (  5,   7,   9) ],  
    [ (  5,   7,   9), (  3,   7,   9), (  3,   5,   7) ],   
    [ (  5,   8,   9), (  3,   5,   7), (  1,   2,   3) ],   
    [ (  1,   2,   4), (  1,   4,   7), (  1,   2,   5) ]    
    ])

m.add_fwv([[ (  0.1,   0.2,   0.3), (  0.7,   0.8,   0.9), (  0.3,   0.5,   0.8) ]])

m.sol(['max', 'max', 'min'])

m.report(show_tensors=False)