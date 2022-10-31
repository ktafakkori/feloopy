from feloopy import *

m = feloopy('QuadraticAssignment', 'pyomo')

w = [[0,3,0,2], 
     [3,0,0,1], #Flow matrix (between assignees)
     [0,0,0,4],
     [2,1,4,0]]

d = [[0,22,53,53],
     [22,0,40,62], #Distance matrix (between assignments)
     [53,40,0,55],
     [53,62,55,0]]

I = range(len(w)) #Set of assignees
K = I

J = range(len(w[0])) #Set of assignments
L = J

a ={(i,j,k,l): w[i][k]*d[j][l] for i,j,k,l in it.product(I,J,K,L)} #Relative cost matrix

x = m.bvar('x', [I,J])

m.obj(sum(a[i,j,k,l]*x[i,j]*x[k,l] for i,j,k,l in sets(I,J,K,L)))

for j in J: m.con(sum(x[i,j] for i in I) == 1)
for i in I: m.con(sum(x[i,j] for j in J) == 1)

m.sol('min','bonmin_online',email='youremail@email.com')

for i,j in sets(I,J):
    if m.get(x[i,j])==1:
        print(f"agent {i} assigned to job {j}")

