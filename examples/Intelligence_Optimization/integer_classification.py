from feloopy import *

def argmax(x): return max(range(len(x)), key=lambda i: x[i])

#Classification function
def classify(x,z,a): print(f"Input = {a} -> Output = {argmax([((1+2.73**(-(sum(a[i]*x[j][i] for i in range(len(a))) + z[j])))**(-1)) for j in range(len(x))])}")

#Training dataset
a = [[1,2,2],[2,3,3],[3,4,5],[4,5,6],[5,7,8]] #Features
b = [ 0     , 1     , 2     , 3     , 4     ] #Target
lam = 0 #Regularization factor

#Defining sets based on input data:
C = range(5) #Classes
U = range(len(a[0])) #Features
T = range(len(b)) #Observations

save_b = tuple(b)

#Defining classes
x_c=[None for j in C]
z_c=[None for j in C]
for j in C:
    for t in T:
        if b[t] == j:
            b[t] = 1
        else:
            b[t] = 0

    #Creating the environment
    m = feloopy('IntegerClassification', 'gekko') 

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
    weigth = []
    for i in U: weigth.append(m.get(x[i])[0])
    bias = m.get(z)[0]

    #Storing the results
    b = list(save_b)
    x_c[j]=weigth
    z_c[j]=bias

w = x_c
b = z_c

#Test dataset
aa = [[1,2.1,2],[1.9,3,3],[3.2,4,5],[4.1,5,6],[4.9,7,8]] #Features
bb = [ 0       , 1       , 2       , 3       , 4       ] #Target

for item in aa:
    classify(w,b,item)