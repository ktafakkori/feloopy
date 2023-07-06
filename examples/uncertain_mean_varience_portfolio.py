'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-06-20
 # @ Modified: 2023-07-06
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

from feloopy import *

# Credit: https://xiongpengnus.github.io/rsome/

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