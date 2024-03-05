import feloopy as flp

# Define a model
m = flp.model("convex", "convex_model_name", "cvxpy")

# Define variables
x = m.ftvar(name="x")

# Define constraints
m.con(x <= 1, name="c1")
m.con(x >= 1, name="c2")

# Define an objective
m.obj((x - 4) ** 2)

# Solve the model
m.sol(["min"], "ecos")

# Report the results
m.report()
