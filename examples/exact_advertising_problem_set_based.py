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

# Data
c = [50, 100]
v = [28, 24]
p = np.array([[7,  2], [2, 12]])

# Sets
I = range(len(c))  # Set of ads
J = range(len(v))  # Set of viewer types

# Environment
m = target_model('exact', 'advertising problem', 'pulp', key=0)

# Variables
x = m.pvar('x', [I])

# Objective
m.obj(sum(c[i] * x[i] for i in I))

# Constraints
for j in J:
    m.con(sum(p[i, j] * x[i] for i in I) >= v[j])

# Solve
m.sol(['min'], 'glpk')

# Display
m.report()