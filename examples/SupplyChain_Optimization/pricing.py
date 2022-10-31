from feloopy import *


#     Monday   Tuesday    Wednesday   Thursday   Friday   Saturday   Sunday
a = [   [80],    [150],       [200],    [400],    [145],    [350],    [409]]    #Sales
b = [     20,       22,          18,       25,       55,       15,       21]    #Prices
U = range(len(a[0]))  #Set of input features
T = range(len(b))     #Set of the training points


m = feloopy('LinearRegression','gekko') 

#Defining sets (based on input data):
U = range(len(a[0])) #Features
T = range(len(b)) #Observations

#Decision variables
x = m.fvar('x',[U])
z = m.fvar('z')
g = m.fvar('g', [T])

#Optimization model
m.obj((2*len(T))**(-1)*sum((g[t]-b[t])**2 for t in T))
for t in T: m.con(g[t] |e| sum(a[t][i]*x[i] for i in U) + z)

#Solve
m.sol('min', 'apopt')

#Getting the results
w = [] 
for i in U: w.append(m.get(x[i])[0])
b = m.get(z)[0]

x = w[0]
z = b

print(x,z)
m = feloopy('Pricing','gekko')

q = m.pvar('q')

m.obj(z*q+x*(q**2))

m.sol('max','bpopt')

print("total revenue: ", z*m.get(q)[0]+x*(m.get(q)[0]**2), "$")
print("marginal revenue: ", z+2*x*m.get(q)[0], "$")
print("optimal price (maximum willingness to pay): ", z+x*m.get(q)[0], "$")
print("optimal sales (consumption level): ", m.get(q)[0] , "units")

'''

Output:

-0.02980603901 32.526238806
total revenue:  8873.673305852495 $
marginal revenue:  -5.7734276026621956e-08 $
optimal price (maximum willingness to pay):  16.263119374132863 $
optimal sales (consumption level):  545.63168982 units

'''