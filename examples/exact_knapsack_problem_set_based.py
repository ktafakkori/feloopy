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
m = target_model('exact', 'knapsack problem', 'ortools')

#Sets
J = range(7)  # Set of the items

#Dataset
w = [40, 50, 30, 10, 10, 40, 30]  # Weight of the items
W = 100  # Capacity of the knapsack
p = [40, 60, 10, 10, 3, 20, 60]  # Value of the items

#Variables
x = m.bvar('x', [J])

# Objective
m.obj(sum(p[j]*x[j] for j in J))

# Constraints
m.con(sum(w[j]*x[j] for j in J) <= W)
    
#Solve
m.sol(['max'], 'scip')

# Display
m.report()