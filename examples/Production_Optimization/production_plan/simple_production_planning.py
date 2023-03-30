
from feloopy import *

m = model('exact','production_plan','cplex')

I  = m.set(10) #Set of items in product portfolio
R  = m.set(3) #Set of resources

p = load_from_excel('data.xlsx', [I], [1], ['i'], 'profit') # profit per item
a = load_from_excel('data.xlsx', [I,R], [1,1], ['i','r'], 'usage') # resource usage per item
b = load_from_excel('data.xlsx', [R], [1], ['r'], 'resource') # available resources

x = m.pvar('production', [I])

m.obj(sum(p[i]*x[i] for i in I))

for r in R:
    m.con(sum(a[i,r]*x[i] for i in I) <= b[r])

m.sol(['max'],'cplex')

m.dis_obj()

for i in I:
    if m.get(x[i])>0:
        print(f" produce {m.get(x[i])} units of item {i} and earn {p[i]*m.get(x[i])} dollars")

for r in R:
    if m.get(sum(a[i,r]*x[i] for i in I))>0:

        print(f" utilization rate of resource {r}: {sum(a[i,r]*m.get(x[i]) for i in I)/b[r]*100}%")