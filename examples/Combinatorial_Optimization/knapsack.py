from feloopy import *

m = feloopy('Knapsack', 'pulp')

J = range(7) #Set of the items
w = [40,50,30,10,10,40,30] #Weight of the items
W = 100 #Capacity of the knapsack
p = [40,60,10,10,3 ,20,60] #Value of the items

x = m.bvar('x', [J])

m.obj(sum(p[j]*x[j] for j in J))

m.con(sum(w[j]*x[j] for j in J) |l| W)

m.sol('max', 'cbc')

for j in J:
    print(f"item {j} is {m.get(x[j])}")

print("obj:", -m.get_obj())