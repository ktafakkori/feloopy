import feloopy as flp

# Define a model
m = flp.model(name="model_name", method="exact", interface="pymprog")

# Define variables
x = m.bvar(name="x")
y = m.pvar(name="y", bound=[0, 1])

# Define constraints
m.con(x + y <= 1, name="c1")
m.con(x - y >= 1, name="c2")

# Define an objective
m.obj(x + y)

# Solve the model
m.sol(["max"], "glpk")

# Report the results
m.clean_report()
