'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.8)                               |
|  Modified: Wednesday, 27th September 2023 08:50:18 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''

from feloopy import *

#Environment
m = target_model('exact', 'price optimziation problem', 'gekko', key=0)

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
