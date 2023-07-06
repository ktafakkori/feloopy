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
m = target_model('exact', 'quadratic_assignment_problem', 'gekko', key=0)

#Dataset
w = [[0, 3, 0, 2],
     [3, 0, 0, 1],  # Flow matrix (between assignees)
     [0, 0, 0, 4],
     [2, 1, 4, 0]]

w = np.array(w)

d = [[0, 22, 53, 53],
     [22, 0, 40, 62],  # Distance matrix (between assignments)
     [53, 40, 0, 55],
     [53, 62, 55, 0]]

d = np.array(d)

#Sets
I = m.set(m.card(w))  # Set of assignees
K = I

J = m.set(m.card(w[0]))  # Set of assignments
L = J

a = {(i, j, k, l): w[i, k]*d[j, l] for i, j, k, l in sets(I, J, K, L)}  # Relative cost matrix

#Variables
x = m.bvar('x', [I, J])

#Objective
m.obj(sum(a[i, j, k, l]*x[i, j]*x[k, l] for i, j, k, l in sets(I, J, K, L)))

#Constraints
for j in J:
    m.con(sum(x[i, j] for i in I if i !=j) == 1)

for i in I:
    m.con(sum(x[i, j] for j in J if j!=i) == 1)

#Solve
m.sol(['min'], 'apopt')

#Display
m.report()