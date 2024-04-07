import feloopy as flp


def instance(X):

    # Define model instance
    m = flp.model(name="model_name", method="heuristic", interface="feloopy", agent=X)

    # Define variables for the model instance
    x = m.bvar(name="x")
    y = m.pvar(name="y", bound=[0, 1])

    # Define constraints for the model instance
    m.con(x + y | flp.l | 1, name="c1")
    m.con(x - y | flp.g | 1, name="c2")

    # Define an objective for the model instance
    m.obj((x - 1) ** 2 + (y - 1) ** 2)

    # Solve the model instance
    m.sol(directions=["max"], solver="ga", solver_options={"epoch": 1000, "pop_size": 100})

    return m[X]


# Make the main model
m = flp.make_model(instance)

# Solve the model
m.sol(penalty_coefficient=10)

# Report the results
m.clean_report()
