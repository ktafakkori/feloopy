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

from feloopy import *

#Environment
m = target_model('exact', 'traveling salesperson problem', 'ortools')

dt = data_toolkit()

#Sets
N = range(10)
U = range(9)

#Dataset
c = dt.uniformint('c', dim= [N,N], bound=[1, 11])
for i, j in sets(N, N):
    c[i][i] = 0
    c[i][j] = c[j][i]

#Variables
x = m.bvar('x', [N, N])
u = m.ivar('u', [N])

#Objective
m.obj(sum(c[i, j]*x[i, j] for i, j in sets(N, N)))

#Constraints
for j in N:
    m.con(sum(x[i, j] for i in N if i != j) == 1)

for i in N:
    m.con(sum(x[i, j] for j in N if j != i) == 1)

for i, j in sets(U, N):
    if i != j:
        m.con(u[i] - u[j] + x[i, j] * len(N) <= len(N)-1)

#Solve
m.sol(['min'], 'glop', show_log=False)

m.report(show_tensors=True)