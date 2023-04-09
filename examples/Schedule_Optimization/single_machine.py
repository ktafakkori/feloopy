from feloopy import *

#Environment
m = model('exact','sm', 'pulp')

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
    m.con(sum(x[i,j] for j in J) == 1)

for j in J: 
    m.con(sum(x[i,j] for i in I) == 1)

m.con(c[0] == s + sum(x[i,0]*p[i] for i in I))

for j in J:
    if j!=0: m.con(c[j] >= c[j-1] + sum(x[i,j]*p[i] for i in I))

#Solve
m.sol(['min'],'cbc')
m.inf()
m.dis_obj()
m.dis_status()

#Display
for i,j in sets(I,J):
    if m.get(x[i,j])==1:
        print(f"| job  {i}  | position {j} | finish: {m.get(c[j])} | ")
        
'''

~~~~~~~~~~~~
PROBLEM INFO
~~~~~~~~~~~~
| info      | detail   | variable   | count [cat,tot]   | other      | count [cat,tot]    |
|-----------|----------|------------|-------------------|------------|--------------------|
| model     | sm       | positive   | [1, 4]            | objective  | [1, 1]             |
| interface | pulp     | binary     | [1, 16]           | constraint | [1, 12]            |
| solver    | cbc      | integer    | [0, 0]            |            |                    |
| direction | ['min']  | free       | [0, 0]            |            |                    |
| method    | exact    | tot        | [2, 20]           |            |                    |
~~~~~~~~~~~~

objective:  18.25
status:  Optimal
| job  0  | position 2 | finish: 19.0 | 
| job  1  | position 0 | finish: 8.0 | 
| job  2  | position 3 | finish: 28.0 | 
| job  3  | position 1 | finish: 12.0 | 

'''