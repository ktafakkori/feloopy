# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

from feloopy import *

#Environment
m = model(method='exact', name='traveling salesperson problem', interface='ortools')

dt = data_toolkit(key=0)

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

print(m.features)