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
m = learner_model('exact', 'demand learner', 'gekko', key=0)

#Dataset
a = [   [80],    [150],       [200],    [400],    [145],    [350],    [409]]    
b = [     20,       22,          18,       25,       55,       15,       21]

#Sets
U = range(len(a[0]))  
T = range(len(b))

#Variables
x = m.fvar('x',[U])
z = m.fvar('z')
g = m.fvar('g', [T])

#Objective
m.obj((2*len(T))**(-1)*sum((g[t]-b[t])**2 for t in T))

#Constraints
for t in T: 
    m.con(g[t] == sum(a[t][i]*x[i] for i in U) + z)

#Solve
m.sol(['min'], 'apopt')

#Report
m.report()

#Store
w = []
for i in U: w.append(m.get(x[i]))
b = m.get(z)

#Environment
m = target_model('exact', 'price optimization problem', 'gekko', key=0)

#Dataset
x = w[0]
z = b

#Variable
q = m.pvar('q')

#Objective
m.obj(z*q+x*(q**2))

#Solve
m.sol(['max'],'apopt')

m.report()