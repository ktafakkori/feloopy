from feloopy import *

#Classification function
def classify(w,b,a): return print(f"Input = {a} -> Output = {round((1+2.73**(-(sum(w[i]*a[i] for i in U) + b)))**(-1))}")

#Creating the environment
m = feloopy('BinaryClassification', 'gekko')

#Training dataset
a = [[1,2,2],[2,3,3],[3,4,5],[4,5,6],[5,7,8]] #Features
b = [ 0     , 1     , 0     , 1     , 0     ] #Target
lam = 0 #Regularization factor

#Defining sets (based on input data):
U = range(len(a[0])) #Features
T = range(len(b)) #Observations

#Decision variables
x = m.fvar('x',[U])
z = m.fvar('z')
g = m.fvar('g', [T])

#Optimization model
m.obj(sum((g[t]-b[t])**2 for t in T) + lam*sum(x[i]**2 for i in U))
for t in T: m.con(g[t] |e| (1+2.73**(-(sum(a[t][i]*x[i] for i in U) + z)))**(-1))

#Solve
m.sol('min', 'ipopt')

#Getting the results
w = []
for i in U: w.append(m.get(x[i])[0])
b = m.get(z)[0]

#Test dataset
aa = [[1,2.1,2],[1.9,3,3],[3.2,4,5],[4.1,5,6],[4.9,7,8]] #Features
bb = [ 0       , 1       , 0       , 1       , 0       ] #Target

for item in aa:
    classify(w,b,item)