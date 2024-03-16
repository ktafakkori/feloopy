import feloopy as flp

dt = flp.data_toolkit(key=0)

I = dt.set(name="I", bound=[0, 9])
J = dt.set(name="J", bound=[0, 9])
v = dt.uniform(name="d", dim=[J], bound=[2,10])
p = dt.uniform(name="p", dim=[I,J], bound=[4,12])

m = flp.model(name="model", method="exact", interface="pulp")

x = m.pvar(name="x", dim=[I])

# --8<-- [start:constraintdefintion]
# Method 1
for j in J: m.con(name=f'c_{j}', expression=sum(p[i,j] * x[i] for i in I) >= v[j])

# Method 2
for j in J: m.con(name=f'c_{j}', expression=[sum(p[i,j] * x[i] for i in I), '>=', v[j]])

# Method 3
for j in J: m.enforce_geq(name=f'c_{j}', lhs=sum(p[i,j] * x[i] for i in I), rhs=v[j])

# Method 4a
m.con(name='c_', expression=[[sum(p[i,j] * x[i] for i in I), '>=', v[j]] for j in J])

# Method 4b
m.con(name=[f'c_{j}' for j in J], expression=[[sum(p[i,j] * x[i] for i in I), '>=', v[j]] for j in J])

# Method 5a 
m.con(name='c_', expression=[sum(p[i,j] * x[i] for i in I) >= v[j] for j in J])

# Method 5b
m.con(name=[f'c_{j}' for j in J], expression=[sum(p[i,j] * x[i] for i in I) >= v[j] for j in J])

# Method 6
m.con(expression={f'c_{j}': sum(p[i,j] * x[i] for i in I) >= v[j] for j in J})

# Method 7
m.con(expression={f'c_{j}': [sum(p[i,j] * x[i] for i in I), '>=', v[j]] for j in J})
# --8<-- [end:constraintdefintion]