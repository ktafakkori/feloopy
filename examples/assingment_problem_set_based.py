from feloopy import *

#Environment
m = target_model('exact', 'assignment_problem', 'pulp', key=0)

#Dataset
c = [[7, 3, 1],
     [2, 9, 5],  # Cost matrix for agent-task assignment
     [6, 8, 4]]
c = np.array(c)

#Sets
I = m.set(3)  # Agents
J = m.set(3)  # Tasks

#Variables
x = m.bvar('x', [I, J])

#Objective
m.obj(sum(c[i, j]*x[i, j] for i, j in sets(I, J)))

#Constraints
for i in I:
    m.con(sum(x[i, j] for j in J) == 1)

for j in J:
    m.con(sum(x[i, j] for i in I) == 1)
    
#Solve
m.sol(['min'], 'highs')

#Display
m.report()