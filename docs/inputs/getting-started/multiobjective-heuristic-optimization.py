import feloopy as flp


def instance(X):

    # Define model instance
    m = flp.model(name="model_name", method="heuristic",  interface="pymoo", X)

    # Define variables for the model instance
    x = m.pvar(name="x", dim=[2], bound=[-1000, 1000])

    # Define objectives for the model instance
    m.obj(x[..., 0] ** 2 + x[..., 1] ** 2)
    m.obj((x[..., 0] - 2) ** 2 + (x[..., 1] - 2) ** 2)

    # Solve the model instance
    m.sol(["min", "min"], "ns-ga-ii", {"n_gen": 100}, obj_id="all")

    return m[X]


# Make the main model
m = flp.make_model(instance)

# Solve the model
m.sol()

# Report the results
m.clean_report()
