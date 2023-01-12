from feloopy import *

#Classification function
def classify(dataset,x,z,alpha,a): 
   if sum(sum(alpha[t]*dataset[1][t]*dataset[0][t][i] for t in T)*a[i] for i in U) + z > 0:   
    return print(f"Input = {a} -> Output = {1}")
   else:
    return print(f"Input = {a} -> Output = {-1}")

#Training dataset
a = [[1,2,2],[2,3,3],[3,4,5],[4,5,6],[5,7,8]] #Features  
b = [ -1     , 1     , -1     , 1     , -1  ] #Target

U = range(len(a[0]))  #Features
T = range(len(b)) #Observations

#Creating the environment
m = model('exact','svm','gekko')

#Decision variable
alpha = m.pvar('alpha',[T])

#Optimization model
m.obj(sum(alpha[t] for t in T) - sum(alpha[t]*alpha[tt] * b[t]*b[tt] * sum(a[t][i]*a[tt][i] for i in U) for t,tt in sets(T,T)))
m.con(sum(alpha[t]*b[t] for t in T) |e| 0)

#Solve
m.sol(['max'],'apopt')
m.inf()
m.dis_obj()
m.dis_status()

#Getting the results
for t in T: alpha[t] = m.get(alpha[t])
weight = [None for i in U]
for i in U:
    weight[i]=sum(alpha[t]*b[t]*a[t][i] for t in T)
for t in T:
    if alpha[t]>0:
        bias=b[t] - sum(weight[i]*a[t][i] for i in U)
        break

#Test dataset
aa = [[1,2.1,2],[1.9,3,3],[3.2,4,5],[4.1,5,6],[4.9,7,8]] #Features
bb = [ -1      , 1       , -1      , 1       , -1      ] #Target

for item in aa:
    classify([a,b],weight,bias,alpha,item)

'''

Output:

PROBLEM FEATURES
 --------
| info      | detail   | variable   | count (cat,tot)   | other      | count (cat, tot)   |
|-----------|----------|------------|-------------------|------------|--------------------|
| model     | svm      | positive   | [1, 5]            | objective  | [1, 1]             |
| interface | gekko    | binary     | [0, 0]            | constraint | [1, 1]             |
| solver    | apopt    | integer    | [0, 0]            |            |                    |
| direction | ['max']  | free       | [0, 0]            |            |                    |
| method    | exact    | tot        | [1, 5]            |            |                    |
objective:  -13.0
status:  optimal
Input = [1, 2.1, 2] -> Output = -1
Input = [1.9, 3, 3] -> Output = -1
Input = [3.2, 4, 5] -> Output = -1
Input = [4.1, 5, 6] -> Output = 1
Input = [4.9, 7, 8] -> Output = -1

'''