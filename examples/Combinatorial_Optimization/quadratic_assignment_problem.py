from feloopy import *

#Environment
m = feloopy('QAP', 'pyomo')

#Data
w = [[0, 3, 0, 2],
     [3, 0, 0, 1],  # Flow matrix (between assignees)
     [0, 0, 0, 4],
     [2, 1, 4, 0]]

d = [[0, 22, 53, 53],
     [22, 0, 40, 62],  # Distance matrix (between assignments)
     [53, 40, 0, 55],
     [53, 62, 55, 0]]

#Sets
I = range(len(w))  # Set of assignees
K = I

J = range(len(w[0]))  # Set of assignments
L = J

#Parameter
a = {(i, j, k, l): w[i][k]*d[j][l] for i, j, k, l in sets(I, J, K, L)}  # Relative cost matrix

#Variable
x = m.bvar('x', [I, J])

#Objective
m.obj(sum(a[i, j, k, l]*x[i, j]*x[k, l] for i, j, k, l in sets(I, J, K, L)))

#Constraints
for j in J:
    m.con(sum(x[i, j] for i in I) |e| 1)

for i in I:
    m.con(sum(x[i, j] for j in J) |e| 1)

#Solve
m.sol('min', 'bonmin_online', email='youremailforNEOS@email.com')

#Display
for i, j in sets(I, J):
    if m.get(x[i, j]) == 1:
        print(f"agent {i} assigned to job {j}")

'''

Output:

agent 0 assigned to job 2
agent 1 assigned to job 3
agent 2 assigned to job 0
agent 3 assigned to job 1

'''