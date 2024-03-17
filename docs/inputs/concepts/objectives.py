import feloopy as flp

dt = flp.data_toolkit(key=0)

I = dt.set(name="I", bound=[0, 9])
J = dt.set(name="J", bound=[0, 9])
v = dt.uniform(name="d", dim=[J], bound=[2,10])
c = dt.uniform(name="c", dim=[I], bound=[2,10])
p = dt.uniform(name="p", dim=[I,J], bound=[4,12])

m = flp.model(name="model", method="exact", interface="pulp")

x = m.pvar(name="x", dim=[I])

for j in J: m.con(name=f'c_{j}', expression=sum(p[i,j] * x[i] for i in I) >= v[j])

m.obj(expression=sum(c[i]*x[i] for i in I))
