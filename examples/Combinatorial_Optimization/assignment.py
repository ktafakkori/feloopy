from feloopy import *

m = feloopy('Assignment','pulp')

I = range(3) #Set of agents
J = range(3) #Set of tasks
c = [[7, 3, 1],
     [2, 9, 5],  #Cost matrix for agent-task assignment
     [6, 8, 4]]

x = m.bvar('x',[I,J])

m.obj(sum(c[i][j]*x[i,j] for i,j in sets(I, J)))
for i in I: m.con(sum(x[i,j] for j in J) |e| 1)
for j in J: m.con(sum(x[i,j] for i in I) |e| 1)

m.sol('min','cbc')

for i,j in sets(I,J):
    if m.get(x[i,j])==1:
        print(f"agent {i} assigned to job {j}")