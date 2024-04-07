# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

from feloopy import *

#Environment
m = target_model('exact', 'price optimziation problem', 'gekko')

#Dataset
a = [1000, 800, 600]
b = [2   , 3  , 4  ]
cost = [2, 3, 5]

#Set
I = range(len(a))

#Variable
q = m.pvar('q', [I])

#Objective
m.obj(sum((q[i] - cost[i]) * (a[i] - b[i] * q[i]) for i in I))

#Solve
m.sol(['max'], 'apopt')

#Display
m.report()
