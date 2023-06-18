from feloopy import *

def instance(X):

    # Environment
    m = model('heuristic', 'knapsack_problem', 'mealpy', X)

    # Sets
    J = range(7)  # Set of the items

    # Parameters
    w = [40, 50, 30, 10, 10, 40, 30]  # Weight of the items
    W = 100  # Capacity of the knapsack
    p = [40, 60, 10, 10, 3, 20, 60]  # Value of the items

    # Variables
    x = m.bvar('x', [J])

    # Objective
    m.obj(sum(p[j]*x[j] for j in J))

    # Constraints
    m.con(sum(w[j]*x[j] for j in J) |l| W)

    # Solve
    m.sol(['max'], 'base-ga', {'epoch':10})

    return m[X]

m = make_model(instance)

m.sol(penalty_coefficient=0.1,show_log=True)

m.report()