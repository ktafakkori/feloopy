from feloopy import *
m = model('exact', 'knapsack problem', 'pulp')
J = range(7) 
w = [40, 50, 30, 10, 10, 40, 30] 
W = 100 
p = [40, 60, 10, 10, 3, 20, 60]
x = m.bvar('x', [J])
m.obj(sum(p[j]*x[j] for j in J))
m.con(sum(w[j]*x[j] for j in J) <= W)
m.sol(['max'], 'cbc')
m.report()