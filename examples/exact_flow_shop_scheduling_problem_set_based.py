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
w = [0.1, 0.4, 0.15, 0.35]  # Priority weight of each job
p = [[7, 3, 9, 4],
     [7, 3, 9, 4]]  # Processing time of each job on each machine
s = [5, 2]  # Setup times of the machines

# Sets
I = range(len(p[0]))  # Set of jobs
J = range(len(I))  # Set of positions
K = range(len(p))  # Set of machines

# Environment
m = target_model('exact', 'flow shop scheduling', 'pulp', key=0)

# Variables
x = m.bvar('x', [I, J])
c = m.pvar('c', [J, K])
d = m.pvar('d', [J, K])

# Objective
m.obj(sum(w[j] * c[j, 1] for j in J))

# Constraints
# Job assignment constraints
for i in I:
    m.con(sum(x[i, j] for j in J) == 1)

for j in J:
    m.con(sum(x[i, j] for i in I) == 1)

# Completion time constraints
for j in J:
    if j != 0:
        m.con(c[j, 1] >= sum(x[i, j] * p[1][i] for i in I) + d[j, 1])

m.con(c[0, 1] == s[1] + sum(x[i, 0] * p[1][i] for i in I) + c[0, 0])

for j in J:
    if j != 0:
        m.con(c[j, 0] >= c[j - 1, 0] + sum(x[i, j] * p[0][i] for i in I))

m.con(c[0, 0] == s[0] + sum(x[i, 0] * p[0][i] for i in I))

# Delay constraints
for j in J:
    if j != 0:
        m.con(d[j, 1] >= c[j - 1, 1])

for j in J:
    m.con(d[j, 1] >= c[j, 0])

# Solve
m.sol(['min'], 'cplex')

# Display
m.report(sys_info=True)
