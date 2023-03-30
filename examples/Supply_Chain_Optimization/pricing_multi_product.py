from feloopy import *

m = model('exact','lr_multi','gekko')

a = [1000, 800, 600]
b = [2, 3, 4]

cost = [2, 3, 5]

I = m.set(len(a))

price = m.pvar('price', [I])

m.obj(sum((price[i] - cost[i]) * (a[i] - b[i] * price[i]) for i in I))

m.sol(['max'], 'apopt')

for i in I:
    print(f"Optimal price of product {i+1}: {m.get(price[i])}")