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
m = target_model('exact', 'production planning problem', 'pyomo', key=0)

#Sets
I  = range(10)
R  = range(3) 

#Dataset
p = load_from_excel('data_exact_production_planning_problem.xlsx', [I], [1], ['i'], 'profit') 
a = load_from_excel('data_exact_production_planning_problem.xlsx', [I,R], [1,1], ['i','r'], 'usage') 
b = load_from_excel('data_exact_production_planning_problem.xlsx', [R], [1], ['r'], 'resource')

#Variables
x = m.pvar('production', [I])

#Objective
m.obj(sum(p[i]*x[i] for i in I))

#Constraints
for r in R:
    m.con(sum(a[i,r]*x[i] for i in I) <= b[r])

#Solve
m.sol(['max'],'cbc')

# Display
m.report()
