from feloopy import *

#Environment
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
x = m.pvar('x', [I])

#Objective
m.obj(sum(c[i]*x[i] for i in I))

#Constraint
for j in J:
    m.con(sum(p[i,j]*x[i] for i in I) >= v[j])

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
~~~~~~~~~~~~
PROBLEM INFO
~~~~~~~~~~~~
| info      | detail   | variable   | count [cat,tot]   | other      | count [cat,tot]    |
|-----------|----------|------------|-------------------|------------|--------------------|
| model     | ads      | positive   | [1, 2]            | objective  | [1, 1]             |
| interface | pulp     | binary     | [0, 0]            | constraint | [1, 2]             |
| solver    | cbc      | integer    | [0, 0]            |            |                    |
| direction | ['min']  | free       | [0, 0]            |            |                    |
| method    | exact    | tot        | [1, 2]            |            |                    |
~~~~~~~~~~~~

~~~~~~~~~~
MODEL INFO
~~~~~~~~~~
name: ads
objective: min 50*x0 + 100*x1
subject to:
constraint 0: 7*x0 + 2*x1 >= 28
constraint 1: 2*x0 + 12*x1 >= 24
~~~~~~~~~~

objective:  320.0
status:  Optimal
Minutes of AD 0 purchased: 3.6
Minutes of AD 1 purchased: 1.4
'''