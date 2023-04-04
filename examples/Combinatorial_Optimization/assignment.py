from feloopy import *

# Environment
m = model('exact', 'ap', 'gurobi')

# Sets
I = m.set(3)  # Agents
J = m.set(3)  # Tasks

c = [[7, 3, 1],
     [2, 9, 5],  # Cost matrix for agent-task assignment
     [6, 8, 4]]

c = np.array(c)

# Variable
x = m.bvar('x', [I, J])

# Objective
m.obj(sum(c[i, j]*x[i, j] for i, j in sets(I, J)))

# Constraints
for i in I:
    m.con(sum(x[i, j] for j in J) == 1)

for j in J:
    m.con(sum(x[i, j] for i in I) == 1)

m.sol(['min'], 'gurobi', log=True)
m.inf()
m.dis_obj()
m.dis_status()

# Display
for i, j in sets(I, J):
    if m.get(x[i, j]) == 1:
        print(f"agent {i} is assigned to job {j}")

'''
~~~~~~~~~~~~
PROBLEM INFO
~~~~~~~~~~~~
| info      | detail   | variable   | count [cat,tot]   | other      | count [cat,tot]    |
|-----------|----------|------------|-------------------|------------|--------------------|
| model     | ap       | positive   | [0, 0]            | objective  | [1, 1]             |
| interface | cplex    | binary     | [1, 9]            | constraint | [1, 6]             |
| solver    | cplex    | integer    | [0, 0]            |            |                    |
| direction | ['min']  | free       | [0, 0]            |            |                    |
| method    | exact    | tot        | [1, 9]            |            |                    |
~~~~~~~~~~~~

objective:  9.0
status:  integer optimal solution
agent 0 is assigned to job 1
agent 1 is assigned to job 0
agent 2 is assigned to job 2
'''
