# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

from feloopy import *

#Environment
m = learner_model('exact', 'demand learner', 'gekko')

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
m = target_model('exact', 'price optimization problem', 'gekko')

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