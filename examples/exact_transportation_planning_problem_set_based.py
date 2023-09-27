'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.7)                               |
|  Modified: Wednesday, 27th September 2023 08:50:18 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''
from feloopy import *

#Environment
m = target_model('exact', 'transportation planning problem', 'pymprog', key=0)

#Sets
I = m.set(5) # set of loactions
L = m.set(2) # set of capacity levels

#Dataset
dc = load_from_excel('data_exact_transportation_planning_problem.xlsx', [I,I], [1,1], ['i', 'j'], 'driver_cost') # pairwise driver cost
fc = load_from_excel('data_exact_transportation_planning_problem.xlsx', [I,I], [1,1], ['i', 'j'], 'freight_cost') # pairwise freight cost
vc = fc/1000 + dc # pairwise variable cost
ec = load_from_excel('data_exact_transportation_planning_problem.xlsx', [I,L], [1,1], ['i', 'j'], 'fixed_cost') # establishment cost per capacity level
ca = load_from_excel('data_exact_transportation_planning_problem.xlsx', [I,L], [1,1], ['i', 'j'], 'capacity') # capacity
d = load_from_excel('data_exact_transportation_planning_problem.xlsx', [I], [1], ['i'], 'demand') # demand

#Variables
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
m.sol(['min'], 'glpk',show_log=False)

m.report()