# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

from feloopy import *

#Environment
m = target_model('exact', 'production planning problem', 'pyomo')

dt = data_toolkit()

#Sets
I  = range(10)
R  = range(3) 

#Dataset
p = dt.load_from_excel('data_exact_production_planning_problem.xlsx', [I], [1], ['i'], 'profit') 
a = dt.load_from_excel('data_exact_production_planning_problem.xlsx', [I,R], [1,1], ['i','r'], 'usage') 
b = dt.load_from_excel('data_exact_production_planning_problem.xlsx', [R], [1], ['r'], 'resource')

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
