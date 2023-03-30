from feloopy import *

m = model('exact', 'cvrp', 'pulp')

demand = [0, 10, 15, 12, 18, 20, 11, 13, 16]

distance = [
    [0, 10, 15, 20, 25, 30, 35, 40, 45],
    [10, 0, 5, 10, 15, 20, 25, 30, 35],
    [15, 5, 0, 5, 10, 15, 20, 25, 30],
    [20, 10, 5, 0 ,5 ,10 ,15 ,20 ,25],
    [25 ,15 ,10 ,5 ,0 ,5 ,10 ,15 ,20],
    [30 ,20 ,15 ,10 ,5 ,0 ,5 ,10 ,15],
    [35 ,25 ,20 ,15 ,10 ,5 ,0 ,5 ,10],
    [40 ,30 ,25 ,20 ,15 ,10 ,5 ,0 ,5],
    [45 ,35 ,30 ,25 ,20 ,15 ,10 ,5 ,0]
]

N = m.set(len(demand))
V = m.set(4)

capacity = [50 for v in V]

x = m.bvar('x', [N,N])
y = m.pvar('y', [N,N])

m.obj(sum(distance[i][j] * x[i,j] for i,j in sets(N,N)))

for j in N:
    m.con(sum(x[i,j] for i in N if i!=0 and i!=j) == 1)

for v in V:
    m.con(sum(x[0,j] for j in N if j!=0) == m.card(V))
    m.con(sum(x[i,0] for i in N if i!=0) == m.card(V))
    
for i,j,v in sets(N,N,V):
        if i !=0 and j !=0 and i !=j:
                m.con(y[i,j] >= y[0,i] + demand[j] - capacity[v] * (1 - x[i,j]))
                m.con(y[i,j] <= capacity[v])

m.sol(['min'], 'cbc')

m.dis_obj()
for i,j in sets(N,N):
    m.dis_variable(x[i,j])