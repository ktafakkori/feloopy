import feloopy as flp

dt = flp.data_toolkit(key=0)

I = dt.set(name="I", bound=[0, 9])
J = dt.set(name="J", bound=[0, 9])

m = flp.model(name="model", method="convex", interface="cvxpy")


# --8<-- [start:multidimensional]
y = m.bvar(name="y")
y = m.bvar(name="y", dim=[I, J])
w = m.ivar(name="w")
w = m.ivar(name="w", dim=[I, J])
x = m.pvar(name="x")
x = m.pvar(name="x", dim=[I, J])
z = m.fvar(name="z")
z = m.fvar(name="z", dim=[I, J])
p = m.svar(name="p", length=10)
c = m.evar(name="c", dim=[I], event=[10, None, None])
c = m.evar(name="c", dim=[I, J], event=[10, None, None])
epsilon = m.rvar(name="epsilon", dim=[I])
epsilon = m.rvar(name="epsilon", dim=[I, J])
# --8<-- [end:multidimensional]

# --8<-- [start:tensor]
y = m.btvar(name="y", shape=[I])
y = m.btvar(name="y", shape=[I, J])
w = m.itvar(name="w", shape=[I])
w = m.itvar(name="w", shape=[I, J])
x = m.ptvar(name="x", shape=[I])
x = m.ptvar(name="x", shape=[I, J])
z = m.ftvar(name="z", shape=[I])
z = m.ftvar(name="z", shape=[I, J])
epsilon = m.rtvar(name="epsilon", shape=[I])
epsilon = m.rtvar(name="epsilon", shape=[I, J])
# --8<-- [end:tensor]


# --8<-- [start:multidimensionalcoll]
y = m.cbvar(name="y", indices={0, 1}, dim={0: [I, J], 1: [J]}, bound={0: [0, 1], 1: [0, 1]})
w = m.civar(name="w", indices={0, 1}, dim={0: [I, J], 1: [J]}, bound={0: [0, 1], 1: [0, 1]})
x = m.cpvar(name="x", indices={0, 1}, dim={0: [I, J], 1: [J]}, bound={0: [0, 1], 1: [0, 1]})
z = m.cfvar(name="z", indices={0, 1}, dim={0: [I, J], 1: [J]}, bound={0: [0, 1], 1: [0, 1]})
p = m.csvar(name="p", indices={0, 1}, length={0: 10, 1: 10})
# --8<-- [end:multidimensionalcoll]


# --8<-- [start:tensorcoll]
y = m.cbtvar(name="y", indices={0, 1}, shape={0: [I, J], 1: [J]}, bound={0: [0, 1], 1: [0, 1]})
w = m.citvar(name="w", indices={0, 1}, shape={0: [I, J], 1: [J]}, bound={0: [0, 1], 1: [0, 1]})
x = m.cptvar(name="x", indices={0, 1}, shape={0: [I, J], 1: [J]}, bound={0: [0, 1], 1: [0, 1]})
z = m.cftvar(name="z", indices={0, 1}, shape={0: [I, J], 1: [J]})
epsilon = m.crtvar(name="z", indices={0, 1}, shape={0: [I, J], 1: [J]})
# --8<-- [end:tensorcoll]
