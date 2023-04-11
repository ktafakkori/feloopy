from feloopy import *

# Environment
m = model('exact', 'kp', 'cvxpy')

# Sets
J = range(7)  # Set of the items

# Parameters
w = [40, 50, 30, 10, 10, 40, 30]  # Weight of the items
W = 100  # Capacity of the knapsack
p = [40, 60, 10, 10, 3, 20, 60]  # Value of the items

# Variables
x = m.bvar('x', [J])

# Objective
m.obj(sum(p[j]*x[j] for j in J))

# Constraints
m.con(sum(w[j]*x[j] for j in J) <= W)

for j in J:
    m.con(x[j]<=1)
    m.con(x[j]>=0)

# Solve
m.sol(['max'], 'gurobi',show_log=True)
m.inf()
m.dis_obj()
m.dis_status()

# Display
for j in J:
    print(f"item {j} is {m.get(x[j])}")

m.report()

'''
~~~~~~~~~~~~
PROBLEM INFO
~~~~~~~~~~~~
| info      | detail   | variable   | count [cat,tot]   | other      | count [cat,tot]    |
|-----------|----------|------------|-------------------|------------|--------------------|
| model     | kp       | positive   | [0, 0]            | objective  | [1, 1]             |
| interface | ortools  | binary     | [1, 7]            | constraint | [1, 1]             |
| solver    | scip     | integer    | [0, 0]            |            |                    |
| direction | ['max']  | free       | [0, 0]            |            |                    |
| method    | exact    | tot        | [1, 7]            |            |                    |
~~~~~~~~~~~~

objective:  133.0
status:  optimal
item 0 is 0.0
item 1 is 1.0
item 2 is 0.0
item 3 is 1.0
item 4 is 1.0
item 5 is 0.0
item 6 is 1.0

'''