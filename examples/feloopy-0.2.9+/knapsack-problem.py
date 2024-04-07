# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import feloopy as flp

dt = flp.data_toolkit(key=0)

J = dt.set(name="J", bound=[0,6])
w = dt.store(name="w", value= [40, 50, 30, 10, 10, 40, 30] )
W = dt.store(name="W", value=100)
p = dt.store(name="p", value=[40, 60, 10, 10, 3, 20, 60])

def kp(m):
    c = dt.store("c",0)
    x = m.bvar('x', [J])
    m.obj(sum(p[j]*x[j] for j in J))
    m.con(sum(w[j]*x[j] for j in J) <= W)
    return m

m = flp.search(name="kp",environment=kp, directions=["max"])

print(dt.data)
m.report()
