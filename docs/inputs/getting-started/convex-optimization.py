import feloopy as flp
import numpy as np

# Import useful tensor-based functions
from cvxpy import sum_squares

# Generate data
m = 20
n = 15
np.random.seed(1)
A = np.random.randn(m, n)
b = np.random.randn(m)

# Define a model
m = flp.model(name="model_name", method="convex",  interface="cvxpy")

# Define variables
x = m.ftvar(name="x", shape=[n])

# Define an objective
m.obj(sum_squares(A @ x - b))

# Solve the model
m.sol(["min"], "ecos")

# Report the results
m.clean_report()
