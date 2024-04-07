import feloopy as flp
import numpy as np

# Define a model
m = flp.model(name="mean_varience_portfolio", method="uncertain", interface="rsome_ro")

# Define parameters
n = 150
i = np.arange(1, n + 1)
p = 1.15 + i * 0.05 / 150
sigma = 0.05 / 450 * (2 * i * n * (n + 1)) ** 0.5
phi = 5
Q = np.diag(sigma**2)

# Define variables
x = m.ptvar("x", [n])

# Define an objective
m.obj(p @ x - phi * m.quad(x, Q))

# Define constraints
m.con(x.sum() == 1)

# Solve the model
m.sol(["max"], "ecos")

# Report the results
m.clean_report()
