'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-06-18
 # @ Modified: 2023-07-06
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

from feloopy import *

#Environment
m = target_model('exact', 'traveling salesperson problem', 'ortools', key=0)

#Sets
N = m.set(10)
U = m.set(9)

#Dataset
c = m.uniformint(1, 10, [N,N])
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