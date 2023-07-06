'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-06-22
 # @ Modified: 2023-07-06
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

from feloopy import *

#Environment
m = target_model('exact', 'knaspack problem', 'ortools', key=0)

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