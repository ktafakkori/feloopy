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

def roll(n, d):
    l = [0, 1, 2, 3, 4, 5, 6]
    if n < d:
        x = l[:n+1] + l[n+(len(l)-d+1):]
    else:
        x = l[n-(d-1):n+1]
    return x

#Environment
m = target_model('exact', 'staffing problem', 'pulp', key=0)

#Dataset
Data = {
    'Mon': 17,
    'Tue': 13,
    'Wed': 15,
    'Thu': 19,
    'Fri': 14,
    'Sat': 16,
    'Sun': 11
}
RD = 5  # Rolling horizon

#Sets
I = range(7)  # Set of days

#Variables
x = m.ivar('x', [I])

#Objective
m.obj(sum(x[i] for i in I))

#Constraints
for i in I:
    m.con(sum(x[j] for j in roll(i, RD)) >= list(Data.values())[i])

#Solve
m.sol(['min'], 'cplex')

#Display
m.report()