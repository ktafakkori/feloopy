from feloopy import *

m = feloopy('FlowShop', 'pulp')

w = [0.1, 0.4, 0.15, 0.35] #Priority weight of each job
p = [[  7,   3,    9,    4],
     [  7,   3,    9,    4]] #Processing time of each job on each machine
s = [5, 2] #Setup times of the machines

I = range(len(p[0])) #Set of jobs
J = range(len(I)) #Set of positions
K = range(len(p)) #Set of machines

x = m.bvar('x', [I,J])
c = m.pvar('c', [J,K])
d = m.pvar('d', [J,K])

m.obj(sum(w[j]*c[j,1] for j in J))

for i in I: 
    m.con(sum(x[i,j] for j in J) |e| 1)

for j in J: 
    m.con(sum(x[i,j] for i in I) |e| 1)

for j in J: 
    if j!=0: 
        m.con(c[j,1] |g| sum(x[i,j]*p[1][i] for i in I) + d[j,1])

m.con(c[0,1] |e| s[1] + sum(x[i,0]*p[1][i] for i in I) + c[0,0])

for j in J: 
    if j!=0: 
        m.con(c[j,0] |g| c[j-1,0] + sum(x[i,j]*p[0][i] for i in I))

m.con(c[0,0] |e| s[0] + sum(x[i,0]*p[0][i] for i in I))

for j in J: 
    if j!=0: 
        m.con(d[j,1] |g| c[j-1,1])

for j in J: 
    m.con(d[j,1] |g| c[j,0])

m.sol('min','cbc')

for i,j in sets(I,J):
    if m.get(x[i,j])!=0:
        print(f"x{i}{j} = {m.get(x[i,j])}")

for j,k in sets(J,K):
    if m.get(c[j,k])!=0:
        print(f"c{j}{k} = {m.get(c[j,k])}")

for j,k in sets(J,K):
    if m.get(d[j,k]):
        print(f"d{j}{k} = {m.get(d[j,k])}")

'''

Output:

x02 = 1.0
x10 = 1.0
x23 = 1.0
x31 = 1.0
c00 = 8.0
c01 = 13.0
c10 = 12.0
c11 = 17.0
c20 = 19.0
c21 = 26.0
c30 = 28.0
c31 = 37.0
d01 = 8.0
d11 = 13.0
d21 = 19.0
d31 = 28.0

'''