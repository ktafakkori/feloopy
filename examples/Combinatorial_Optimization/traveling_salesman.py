from feloopy import *

#Environment
m = feloopy('TSP','ortools')

#Sets
N = range(10)
U = range(1,len(N)) 

#Parameters
np.random.seed(0)

c = np.random.randint(1,10, size=(len(N),len(N))) 

for i,j in sets(N,N):
    c[i][i]=0                 #Cost (distance) matrix 
    c[i][j]=c[j][i]

#Variables
x = m.bvar('x',[N,N])
u = m.ivar('u',[N])

#Objective
m.obj(sum(c[i,j]*x[i,j]  for i,j in sets(N,N)))

#Constraints
for j in N: m.con(sum(x[i,j] for i in N if i!=j ) |e| 1)
for i in N: m.con(sum(x[i,j] for j in N if j!=i ) |e| 1)

for i,j in sets(U,N): 
    if i!=j: m.con(u[i] - u[j] + x[i,j] * len(N) <= len(N)-1)

m.sol('min','scip')

for i,j in sets(N,N):
    if m.get(x[i,j])==1:
        print(f"traveler goes from {i} to {j}")

'''
Output:

traveler goes from 0 to 9
traveler goes from 1 to 4
traveler goes from 2 to 6
traveler goes from 3 to 0
traveler goes from 4 to 3
traveler goes from 5 to 2
traveler goes from 6 to 1
traveler goes from 7 to 8
traveler goes from 8 to 5
traveler goes from 9 to 7

'''