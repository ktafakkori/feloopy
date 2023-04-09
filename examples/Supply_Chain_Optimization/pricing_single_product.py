from feloopy import *

#Environment
m = model('exact','lr_single','gekko') 

#Data
#     Monday   Tuesday    Wednesday   Thursday   Friday   Saturday   Sunday
a = [   [80],    [150],       [200],    [400],    [145],    [350],    [409]]    #Sales
b = [     20,       22,          18,       25,       55,       15,       21]    #Prices

#Sets
U = range(len(a[0]))  #Set of input features
T = range(len(b))     #Set of the training points

#Defining sets (based on input data):
U = range(len(a[0])) #Features
T = range(len(b)) #Observations

#Decision variables
x = m.fvar('x',[U])
z = m.fvar('z')
g = m.fvar('g', [T])

#Optimization model
m.obj((2*len(T))**(-1)*sum((g[t]-b[t])**2 for t in T))
for t in T: m.con(g[t] == sum(a[t][i]*x[i] for i in U) + z)

#Solve
m.sol(['min'], 'apopt')
m.inf()
m.dis_obj()
m.dis_status()


#Getting the results
w = [] 
for i in U: w.append(m.get(x[i]))
b = m.get(z)

x = w[0]
z = b

print(x,z)
m = model('exact','pricing','gekko')

q = m.pvar('q')

m.obj(z*q+x*(q**2))

m.sol(['max'],'bpopt')
m.inf()
m.dis_obj()
m.dis_status()


print("total revenue: ", z*m.get(q)+x*(m.get(q)**2), "$")
print("marginal revenue: ", z+2*x*m.get(q), "$")
print("optimal price (maximum willingness to pay): ", z+x*m.get(q), "$")
print("optimal sales (consumption level): ", m.get(q) , "units")

'''

~~~~~~~~~~~~
PROBLEM INFO
~~~~~~~~~~~~
| info      | detail   | variable   | count [cat,tot]   | other      | count [cat,tot]    |
|-----------|----------|------------|-------------------|------------|--------------------|
| model     | lr       | positive   | [0, 0]            | objective  | [1, 1]             |
| interface | gekko    | binary     | [0, 0]            | constraint | [1, 7]             |
| solver    | apopt    | integer    | [0, 0]            |            |                    |
| direction | ['min']  | free       | [3, 9]            |            |                    |
| method    | exact    | tot        | [3, 9]            |            |                    |
~~~~~~~~~~~~

objective:  71.498759054
status:  optimal
-0.02980603901 32.526238806
~~~~~~~~~~~~
PROBLEM INFO
~~~~~~~~~~~~
| info      | detail   | variable   | count [cat,tot]   | other      | count [cat,tot]    |
|-----------|----------|------------|-------------------|------------|--------------------|
| model     | pricing  | positive   | [1, 1]            | objective  | [1, 1]             |
| interface | gekko    | binary     | [0, 0]            | constraint | [0, 0]             |
| solver    | bpopt    | integer    | [0, 0]            |            |                    |
| direction | ['max']  | free       | [0, 0]            |            |                    |
| method    | exact    | tot        | [1, 1]            |            |                    |
~~~~~~~~~~~~

objective:  8873.6733059
status:  optimal
total revenue:  8873.673305852495 $
marginal revenue:  -5.7734276026621956e-08 $
optimal price (maximum willingness to pay):  16.263119374132863 $
optimal sales (consumption level):  545.63168982 units

'''