import feloopy as flp

# Define a model
m = flp.model("constraint", "model_name", "ortools_cp")

# Define variables
x = m.bvar(name="x", dim=0)
y = m.ivar(name="y", dim=0, bound=[0, 1])

# Define constraints
m.con(x + y <= 1, name="c1")
m.con(x - y >= 1, name="c2")

# Define an objective
m.obj(x + y)

# Solve the model
m.sol(["max"], "ortools")

# Report the results
m.report()
