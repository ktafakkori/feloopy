from feloopy import *

#Environemnt
m = model('exact','ads', 'pulp')

#Data
c = [50, 100]

v = [28, 24]

p = np.array([[7,  2] , 
              [2, 12]])

#Sets
I = range(len(c)) #Set of ads
J = range(len(v)) #Set of viewer types

#Variables
x = m.ivar('x', [I])

#Objective
m.obj(sum(c[i]*x[i] for i in I))

#Constraint
for j in J:
    m.con(sum(p[i,j]*x[i] for i in I) |g| v[j])

#Solve
m.sol(['min'],'cbc')
m.inf()
m.dis_model()
m.dis_obj()
m.dis_status()

#Display
for i in I:
    print(f"Minutes of AD {i} purchased: {m.get(x[i])}")

'''
Output:

PROBLEM FEATURES
 --------
| info      | detail   | variable   | count (cat,tot)   | other      | count (cat, tot)   |
|-----------|----------|------------|-------------------|------------|--------------------|
| model     | sm       | positive   | [1, 4]            | objective  | [1, 1]             |
| interface | pulp     | binary     | [1, 16]           | constraint | [12, 12]           |
| solver    | cbc      | integer    | [0, 0]            |            |                    |
| direction | ['min']  | free       | [0, 0]            |            |                    |
| method    | exact    | tot        | [2, 20]           |            |                    |
objective:  18.25
status:  Optimal
| job  0  | position 2 | finish: 19.0 |
| job  1  | position 0 | finish: 8.0 |
| job  2  | position 3 | finish: 28.0 |
| job  3  | position 1 | finish: 12.0 |

'''