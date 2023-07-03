from feloopy import *

#Environment
m = target_model('exact', 'knaspack problem', 'pyomo', key=0)

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
    
#Solve (Using solvers with "_online" at the end)
m.sol(['max'], 'bonmin_online', email="youremail@domain.com")

# Display
m.report()