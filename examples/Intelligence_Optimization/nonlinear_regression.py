from feloopy import *

#Prediction function
def predict(w,b,a): return print(f"Input = {a} -> Output = {sum(w[i]*a[i] for i in range(len(a))) + b}")

#Creating the environment
m = model('exact','lr','gekko')

#Training dataset
a = [-5,-3,-1,5,3,1] #Features
b = [ 127,151,379,421,460,426] #Target

#Defining sets (based on input data):
U = range(2) #Coefficients
T = range(6) #Observations

#Decision variables
x = m.fvar('x',[U])
z = m.fvar('z')
g = m.fvar('g', [T])

#Optimization model
m.obj((2*len(T))**(-1)*sum((g[t]-b[t])**2 for t in T))
for t in T: m.con(g[t] |e| x[0]*(2.73)**(a[t]*x[1])  + z)

#Solve
m.sol(['min'], 'ipopt')
m.inf()
m.dis_obj()
m.dis_status()

print('Coefficient[0]:',m.get(x[0]))
print('Coefficient[1]:',m.get(x[1]))
print('Coefficient[2]:',m.get(z))

'''
Output:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   FelooPy (Version 0.2.0) - Released: 11 December 2022
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROBLEM FEATURES
 --------
| info      | detail   | variable   | count (cat,tot)   | other      | count (cat, tot)   |
|-----------|----------|------------|-------------------|------------|--------------------|
| model     | lr       | positive   | [0, 0]            | objective  | [1, 1]             |
| interface | gekko    | binary     | [0, 0]            | constraint | [6, 6]             |
| solver    | ipopt    | integer    | [0, 0]            |            |                    |
| direction | ['min']  | free       | [3, 9]            |            |                    |
| method    | exact    | tot        | [3, 14]           |            |                    |
objective:  1173.7616541
status:  optimal
Coefficient[0]: -149.3518937
Coefficient[1]: -0.20575767885
Coefficient[2]: 516.65117417

'''