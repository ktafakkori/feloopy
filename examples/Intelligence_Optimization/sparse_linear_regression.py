from feloopy import *

#Prediction function
def predict(w,b,a): return print(f"Input = {a} -> Output = {sum(w[i]*a[i] for i in range(len(a))) + b}")

#Creating the environment
m = model('exact','slr','gekko')

#Training dataset
a = [[1,2,2],[2,3,3],[3,4,5],[4,5,6],[5,7,8]] #Features
b = [ 1     , 2     , 3     , 4     , 5     ] #Target

#Defining sets (based on input data):
U = range(len(a[0])) #Features
T = range(len(b)) #Observations

k = 2 #Features to select
BigM = 100 #A large number

#Normalizing input data:
ran_a = {i: max(a[t][i] for t in T) - min(a[t][i] for t in T) for i in U}
ave_a = {i: sum(a[t][i] for t in T)/len(T) for i in U}
n_a = {(t,i): (a[t][i]-ave_a[i])/ran_a[i] for t,i in sets(T,U)}
ran_b = max(b[t] for t in T) - min(b[t] for t in T)
ave_b = sum(b[t] for t in T)/len(T)
n_b = {t: (b[t]-ave_b)/ran_b for t in T}

#Decision variables
x = m.fvar('x',[U])
z = m.fvar('z')
g = m.fvar('g', [T])
s = m.bvar('s', [U])

#Optimization model
m.obj((2*len(T))**(-1)*sum((g[t]-n_b[t])**2 for t in T))
for t in T: m.con(g[t] == sum(n_a[t,i]*x[i] for i in U) + z)
for i in U: m.con(x[i] >= -BigM*s[i])
for i in U: m.con(x[i] <= BigM*s[i])
m.con(sum(s[i] for i in U) <= k)

#Solve
m.sol(['min'], 'apopt')

m.inf()
m.dis_obj()
m.dis_status()

#Getting the results
w = [] 
for i in U: 
    w.append(m.get(x[i]))

b = m.get(z)

x = w
z = b

#Test dataset
aa = [[6,8,9],[7,4,3],[8,3,5],[9,1,6],[10,9,3]] #Features
bb = [ 6     , 7     , 8     , 9     , 10     ] #Target

for item in aa:
    predict(w,b,item)


'''

Output:

PROBLEM FEATURES
 --------
| info      | detail   | variable   | count (cat,tot)   | other      | count (cat, tot)   |       
|-----------|----------|------------|-------------------|------------|--------------------|       
| model     | slr      | positive   | [0, 0]            | objective  | [1, 1]             |       
| interface | gekko    | binary     | [1, 3]            | constraint | [12, 12]           |       
| solver    | apopt    | integer    | [0, 0]            |            |                    |       
| direction | ['min']  | free       | [3, 9]            |            |                    |       
| method    | exact    | tot        | [4, 12]           |            |                    |       
objective:  2.4208334274e-20
status:  optimal
Input = [6, 8, 9] -> Output = 5.999999991152457
Input = [7, 4, 3] -> Output = 7.00000001037623
Input = [8, 3, 5] -> Output = 8.000000017957174
Input = [9, 1, 6] -> Output = 9.00000002941906
Input = [10, 9, 3] -> Output = 10.000000002071515
'''