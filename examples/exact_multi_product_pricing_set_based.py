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
m = target_model('exact', 'price optimziation problem', 'gekko', key=0)

#Dataset
a = [1000, 800, 600]
b = [2   , 3  , 4  ]
cost = [2, 3, 5]

#Set
I = m.set(len(a))

#Variable
q = m.pvar('q', [I])

#Objective
m.obj(sum((q[i] - cost[i]) * (a[i] - b[i] * q[i]) for i in I))

#Solve
m.sol(['max'], 'apopt')

#Display
m.report()
