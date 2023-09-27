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
from feloopy import *

# Credit: https://python-mip.readthedocs.io/en/latest/examples.html

m = target_model('exact', 'n_queens_problem', 'mip')

N = 30
x = m.bvar('x', [N,N])

for i in range(N):
    m.eq(sum(x[i,j] for j in range(N)) == 1)

for j in range(N):
    m.eq(sum(x[i,j] for i in range(N)) == 1)

for k in range(2 - N, N - 2 + 1):
    m.eq(sum(x[i,i-k] for i in range(N) if 0<= i-k< N) <=1)

m.sol('cplex')

m.report()