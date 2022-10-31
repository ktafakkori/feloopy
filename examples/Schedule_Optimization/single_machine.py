from feloopy import *

m = feloopy('SingleMachine', 'pulp')

w = [0.1, 0.4, 0.15, 0.35] #Priority weight of each job
p = [  7,   3,    9,    4] #Processing time of each job
s = 5 #Setup time of the machine
I = range(len(p)) #Set of jobs
J = range(len(I)) #Set of positions

x = m.bvar('x', [I,J])
c = m.pvar('c', [J])

m.obj(sum(w[j]*c[j] for j in J))

for i in I: m.con(sum(x[i,j] for j in J) == 1)
for j in J: m.con(sum(x[i,j] for i in I) == 1)
m.con(c[0] == s + sum(x[(i,0)]*p[i] for i in I))
for j in J:
    if j!=0: m.con(c[j] >= c[j-1] + sum(x[(i,j)]*p[i] for i in I))

m.sol('min','cbc')

for i,j in sets(I,J):
    if m.get(x[i,j])==1:
        print(f"| job  {i}  | position {j} | finish: {m.get(c[j])} | ") 

