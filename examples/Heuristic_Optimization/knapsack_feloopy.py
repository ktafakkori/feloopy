from feloopy import *

# Sets
J = range(7)  # Set of the items

# Parameters
w = [40, 50, 30, 10, 10, 40, 30]  # Weight of the items
W = 100  # Capacity of the knapsack
p = [40, 60, 10, 10, 3, 20, 60]  # Value of the items

def instance(X):

    # Environment
    m = model('heuristic', 'kp', 'feloopy',AgentProperties=X)
    # Variables
    x = m.bvar('x', [J])

    # Objective
    m.obj(sum(p[j]*x(j) for j in J))

    # Constraints
    m.con(sum(w[j]*x(j) for j in J) |ll| W)

    # Solve
    m.sol(['max'], 'TS')

    return m[X]

m = implement(instance)

m.sol(PenaltyMultiplier=150,Times=1)
m.inf()
m.dis_obj()

# Display
for j in J:
    print(f"item {j} is {m.get(['x',(j,)])}")

'''
Output:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   FelooPy (Version 0.2.0) - Released: 11 December 2022
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


PROBLEM FEATURES 
 --------
| info      | detail    | variable   | count (cat,tot)   | other      | count (cat, tot)   |
|-----------|-----------|------------|-------------------|------------|--------------------|
| model     | kp        | positive   | [0, 0]            | objective  | [1, 1]             |
| interface | feloopy   | binary     | [1, 7]            | constraint | [1, 1]             |
| solver    | TS        | integer    | [0, 0]            |            |                    |
| direction | ['max']   | free       | [0, 0]            |            |                    |
| method    | heuristic | tot        | [1, 7]            |            |                    |
objective:  133.0
item 0 is 0.0
item 1 is 1.0
item 2 is 0.0
item 3 is 1.0
item 4 is 1.0
item 5 is 0.0
item 6 is 1.0


'''
