from feloopy import *

m = feloopy('TravelingSalesman','pulp')

np.random.seed(0) #Fixing the seed for random number generator

N = range(5) #Set of cities (nodes)
U = range(1,len(N)) #Set of dummy variables for sub-tour elimination constraint
c = np.random.randint(1,10, size=(len(N),len(N))) 
for (i,j) in it.product(N,N):
    c[i][i]=0                 #Cost (distance) matrix 
    c[i][j]=c[j][i]

x = m.bvar('x',[N,N])
u = m.ivar('u',[N], [0,len(N)-1])

m.obj(sum(c[i][j]*x[(i,j)]  for i,j in it.product(N,N)))

for j in N: m.con(sum(x[i,j] for i in N if i!=j ) == 1)
for i in N: m.con(sum(x[i,j] for j in N if j!=i ) == 1)
for i,j in sets(U,N): 
    if i!=j: m.con(u[i] - u[j] + x[(i,j)] * len(N) <= len(N)-1)

m.sol('min','cbc')

for i,j in sets(N,N):
    if m.get(x[i,j])==1:
        print(f"arc {i}-{j}")