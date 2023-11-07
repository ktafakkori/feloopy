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

# Credit: https://python-mip.readthedocs.io/en/latest/examples.html

m = target_model('exact', 'resource_constrained_project_scheduling', 'mip')

n = 10

p = [0, 3, 2, 5, 4, 2, 3, 4, 2, 4, 6, 0]

u = [[0, 0], [5, 1], [0, 4], [1, 4], [1, 3], [3, 2], [3, 1], [2, 4],
     [4, 0], [5, 2], [2, 5], [0, 0]]

c = [6, 8]

S = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 9], [2, 10], [3, 8], [4, 6],
     [4, 7], [5, 9], [5, 10], [6, 8], [6, 9], [7, 8], [8, 11], [9, 11], [10, 11]]

(R, J, T) = (range(len(c)), range(len(p)), range(sum(p)))

x = m.bvar('x', [J, T])

m.obj(sum(t * x[n + 1,t] for t in T))

for j in J:
    m.con(sum(x[j,t] for t in T) == 1)

for r, t in sets(R, T):
    m.con(sum(u[j][r] * x[j,t2] for j in J for t2 in range(max(0, t - p[j] + 1), t + 1))<= c[r])

for j, s in S:
    m.con(sum(t * x[s,t] - t * x[j,t] for t in T) >= p[j])

m.sol(['min'], 'cbc')
m.report()