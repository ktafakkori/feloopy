from feloopy import *

#Environment
m = model('exact','transportation','ortools')

#Sets
I = m.set(5) # set of loactions
L = m.set(2) # set of capacity levels

#Data
dc = load_from_excel('data.xlsx', [I,I], [1,1], ['i', 'j'], 'driver_cost') # pairwise driver cost
fc = load_from_excel('data.xlsx', [I,I], [1,1], ['i', 'j'], 'freight_cost') # pairwise freight cost
vc = fc/1000 + dc # pairwise variable cost
ec = load_from_excel('data.xlsx', [I,L], [1,1], ['i', 'j'], 'fixed_cost') # establishment cost per capacity level
ca = load_from_excel('data.xlsx', [I,L], [1,1], ['i', 'j'], 'capacity') # capacity
d = load_from_excel('data.xlsx', [I], [1], ['i'], 'demand') # demand

#Decision Variables
x = m.pvar('flow',[I,I])
y = m.bvar('establish',[I,L])

#Objective

m.obj(sum(ec[i,lv]*y[i,lv] for i,lv in sets(I,L)) + sum(vc[i,j] * x[i,j] for i,j in sets(I,I)))

#Constraints
for j in I: 
    m.con(sum(x[i,j] for i in I if i!=j) == d[j])

for i in I:
    m.con(sum(x[i,j] for j in I if j !=i) <= sum(ca[i,lv]*y[i,lv]*1000 for lv in L))

#Solve
m.sol(['min'],'scip')

#Report

m.dis_obj()
for i,j in sets(I,I):
    if m.get(x[i,j])>0:
        print(f" transporting {m.get(x[i,j])} units from location {i} to {j} is necessary to meet demand.")

for i,lv in sets(I,L):
    if m.get(y[i,lv])>0:
        print(f"establishing facility of level {lv} at location {i} is necessary to meet demand.")



