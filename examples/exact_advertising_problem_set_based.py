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