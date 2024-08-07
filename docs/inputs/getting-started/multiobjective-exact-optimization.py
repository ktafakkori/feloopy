import feloopy as flp


def model_name():

    # Define a model
    m = flp.model(name="model_name", method="exact", interface="pulp")

    # Define variables
    x = m.pvar("x", [2])

    # Define objectives
    m.obj(x[0])
    m.obj(3 * x[0] + 4 * x[1])

    # Define constraints
    m.con(x[0] <= 20)
    m.con(5 * x[0] + 4 * x[1] <= 200)

    return m

payoff, conflict, pareto, variables = flp.sol_multi(
    model_name,
    ["max", "max"],
    "cplex",
    objective_id="ecm",
    approach_options={"payoff_method": "separated", "intervals": 100},
)

print("Payoff table")
print(payoff)

print("Conflict")
print(conflict)

print("Pareto front")
print(pareto)
