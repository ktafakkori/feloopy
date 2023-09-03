'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-06-18
 # @ Modified: 2023-07-06
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

from feloopy import *

#Environment
m = target_model('exact', 'production planning problem', 'pyomo', key=0)

#Sets
I  = m.set(10)
R  = m.set(3) 

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
m.sol(['max'],'glpk')

# Display
m.report()
