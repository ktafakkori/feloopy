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

m = madm('mabac','mabac_model', 'pydecision')

m.add_dm([
        [75.5, 420,	 74.2, 2.8,	 21.4,	0.37,	 0.16],   
        [95,   91,	 70,	 2.68, 22.1,	0.33,	 0.16],   
        [770,  1365, 189,	 7.9,	 16.9,	0.04,	 0.08],   
        [187,  1120, 210,	 7.9,	 14.4,	0.03,	 0.08],   
        [179,  875,	 112,	 4.43,	9.4,	0.016, 0.09],   
        [239,  1190, 217,	 8.51,	11.5,	0.31,	 0.07],   
        [273,  200,	 112,	 8.53,	19.9,	0.29,	 0.06]    
        ])

m.sol(['max', 'max', 'max', 'min', 'min', 'min', 'min'],show_graph=False)

m.report(show_tensors=False)