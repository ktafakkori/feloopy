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
cost_matrix = [
    [7, 3, 1],
    [2, 9, 5],  # Cost matrix for agent-task assignment
    [6, 8, 4]
]
c = np.array(cost_matrix)

# Environment
m = target_model('exact', 'assignment_problem', 'pulp', key=0)

# Sets
I = m.set(3)  # Agents
J = m.set(3)  # Tasks

# Variables
x = m.bvar('x', [I, J])

# Objective
m.obj(sum(c[i, j] * x[i, j] for i, j in sets(I, J)))

# Constraints

# Each agent is assigned to exactly one task.
for i in I:
    m.con(sum(x[i, j] for j in J) == 1)

# Each task is assigned to exactly one agent.
for j in J:
    m.con(sum(x[i, j] for i in I) == 1)

# Solve
m.sol(['min'], 'highs')

# Display
m.report()
