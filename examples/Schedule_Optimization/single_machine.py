from feloopy import *

#Environemnt
m = feloopy('SingleMachine', 'pulp')

#Data
w = [0.1, 0.4, 0.15, 0.35] #Priority weight of each job
p = [  7,   3,    9,    4] #Processing time of each job
s = 5 #Setup time of the machine

#Sets
I = range(len(p)) #Set of jobs
J = range(len(I)) #Set of positions

#Variables
x = m.bvar('x', [I,J])
c = m.pvar('c', [J])

#Objective
m.obj(sum(w[j]*c[j] for j in J))

#Constraint
for i in I: 
    m.con(sum(x[i,j] for j in J) |e| 1)

for j in J: 
    m.con(sum(x[i,j] for i in I) |e| 1)

m.con(c[0] |e| s + sum(x[i,0]*p[i] for i in I))

for j in J:
    if j!=0: m.con(c[j] |g| c[j-1] + sum(x[i,j]*p[i] for i in I))

#Solve
m.sol('min','cbc')

#Display
for i,j in sets(I,J):
    if m.get(x[i,j])==1:
        print(f"| job  {i}  | position {j} | finish: {m.get(c[j])} | ")
        
'''

Output:

| job  0  | position 2 | finish: 19.0 | 
| job  1  | position 0 | finish: 8.0 | 
| job  2  | position 3 | finish: 28.0 | 
| job  3  | position 1 | finish: 12.0 | 

'''