from feloopy import *


# Creating the environment
m = model('exact', 'bc', 'gekko')


# Classification function
def classify(w, b, a): 
    print(f"Input = {a} -> Output = {round((1+exponent(-(sum(w[i]*a[i] for i in U) + b)))**(-1))}")


# Training dataset

a = [[1,2,2],[2,3,3],[3,4,5],[4,5,6],[5,7,8]] #Features
b = [ 0     , 1     , 0     , 1     , 0     ] #Target

a=np.array(a)
b=np.array(b)

lam = 0 # Regularization factor

# Defining sets (based on input data):
U = range(3)  # Features
T = range(5)  # Observations

# Decision variables

x = m.fvar('x', [U])
z = m.fvar('z')
g = m.fvar('g', [T])

# Optimization model

m.obj(sum((g[t]-b[t])**2 for t in T) + lam*sum(x[i]**2 for i in U))

#m.obj(sum(b[t]*m.ModelObject.log(g[t])+(1-b[t])*m.ModelObject.log(1-g[t]) for t in T))

for t in T:
    m.con(g[t] == (1+m.exponent(-sum(a[t,i]*x[i] for i in U) + z))**(-1))

m.sol(['min'], 'ipopt')
m.inf()
m.dis_obj()
m.dis_status()

# Getting the results
w = []
for i in U:
    w.append(m.get(x[i]))
b = m.get(z)

# Test dataset
aa = [[1, 2.1, 2], [4, 3, 3], [10, 4, 5], [3, 5, 6], [9, 7, 8]]  # Features
bb = [0, 1, 1, 0, 0]  # Target

for item in aa:
    classify(w, b, item)


'''
~~~~~~~~~~~~
PROBLEM INFO
~~~~~~~~~~~~
| info      | detail   | variable   | count [cat,tot]   | other      | count [cat,tot]    |
|-----------|----------|------------|-------------------|------------|--------------------|
| model     | bc       | positive   | [0, 0]            | objective  | [1, 1]             |
| interface | gekko    | binary     | [0, 0]            | constraint | [1, 5]             |
| solver    | ipopt    | integer    | [0, 0]            |            |                    |
| direction | ['min']  | free       | [3, 9]            |            |                    |
| method    | exact    | tot        | [3, 9]            |            |                    |
~~~~~~~~~~~~

objective:  5.6118960513e-32
status:  optimal
Input = [1, 2.1, 2] -> Output = 0
Input = [4, 3, 3] -> Output = 1
Input = [10, 4, 5] -> Output = 1
Input = [3, 5, 6] -> Output = 0
Input = [9, 7, 8] -> Output = 1
'''