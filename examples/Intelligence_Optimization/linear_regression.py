from feloopy import *

#Prediction function
def predict(w,b,a): return print(f"Input = {a} -> Output = {sum(w[i]*a[i] for i in range(len(a))) + b}")

#Creating the environment
m = feloopy('LinearRegression','gekko')

#Training dataset
a = [[1,2,2],[2,3,3],[3,4,5],[4,5,6],[5,7,8]] #Features
b = [ 1     , 2     , 3     , 4     , 5     ] #Target

#Defining sets (based on input data):
U = range(len(a[0])) #Features
T = range(len(b)) #Observations

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

#Optimization model
m.obj((2*len(T))**(-1)*sum((g[t]-n_b[t])**2 for t in T))
for t in T: m.con(g[t] |e| sum(n_a[t,i]*x[i] for i in U) + z)

#Solve
m.sol('min', 'apopt')

#Getting the results
w = [] 
for i in U: w.append(m.get(x[i])[0])
b = m.get(z)[0]

#Test dataset
aa = [[6,8,9],[7,4,3],[8,3,5],[9,1,6],[10,9,3]] #Features
bb = [ 6     , 7     , 8     , 9     , 10     ] #Target

for item in aa:
    predict(w,b,item)

'''

Output:

Input = [6, 8, 9] -> Output = 6.000000000190427
Input = [7, 4, 3] -> Output = 6.999999999697222
Input = [8, 3, 5] -> Output = 7.999999999796734
Input = [9, 1, 6] -> Output = 8.999999999829779
Input = [10, 9, 3] -> Output = 9.999999999426267

'''