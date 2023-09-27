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

# Example credit: https://xiongpengnus.github.io/rsome/

from feloopy import *

m = target_model('exact', 'mean_varience_portfolio', 'rsome_ro')

n = 150                                     
i = np.arange(1, n+1)                       
p = 1.15 + i*0.05/150                       
sigma = 0.05/450 * (2*i*n*(n+1))**0.5      
phi = 5                                    
Q = np.diag(sigma**2)                       

x = m.ptvar('x', [n])                       

m.obj(p@x - phi*m.quad(x, Q))   
m.con(x.sum() == 1)             

m.sol(['max'], 'ecos')
m.report()