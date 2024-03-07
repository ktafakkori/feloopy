import feloopy as flp
import numpy as np

# Generate data
np.random.seed(100)
J = 10
due_date = np.random.uniform(75, 200, size=[J])
priority_weights = np.random.random_integers(1, 5, size=[J])

# Define a model
m = flp.model("constraint", "model_name", "cplex_cp")

# Define variables
process_event = m.cevar(
    "job",
    range(J),
    {j: [np.random.random_integers(10, 40), None, None] for j in range(J)},
)

# Define constraints
m.con(m.cp_forbid_event_overlap([process_event[j] for j in range(J)]))

# Define an objective
m.obj(
    sum(
        (m.cp_get_event_end(process_event[j]) > due_date[j]) * priority_weights[j]
        for j in range(J)
    )
)

# Solve the model
m.sol(["min"], "cplex")

# Report the results
m.report()
