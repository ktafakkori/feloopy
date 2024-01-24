# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

from feloopy import *

# Environment
m = target_model('exact', 'distribution_planning_problem', 'pyomo')

dt = data_toolkit()
# Data
I = range(2)  # Number of suppliers
J = range(2)  # Number of warehouses
K = range(3)  # Number of customers
P = range(3)  # Type of products
T = range(4)  # Time periods

# Dataset
dk = dt.uniformint('dk', [K, P, T], [10, 20])      # Customer demand
cap = dt.uniformint('cap', [I, P, T], [60, 90])     # Supplier capacity
c = dt.uniformint('c', [I, J, P, T], [1, 4])      # Cost of sending each unit of goods from the supplier to the warehouse
cp = dt.uniformint('cp', [J, K, P, T], [1, 4])     # Cost of sending each item from the warehouse to the customer
cpp = dt.uniformint('cpp', [I, K, P, T], [2, 8])    # Cost of sending each unit of goods from the supplier to the customer

# Variables
x = m.ivar('x', [I, J, P, T])  # Transfer rate of products from the supplier to the warehouse
y = m.ivar('y', [J, K, P, T])  # Transfer rate of products from the warehouse to the customer
z = m.ivar('z', [I, K, P, T])  # Amount of direct transfer of products from the supplier to the customer

# Objective
m.obj(sum(x[i, j, p, t] * c[i, j, p, t] for i, j, p, t in sets(I, J, P, T)) + sum(y[j, k, p, t] * cp[j, k, p, t] for j, k, p, t in sets(J, K, P, T)) + sum(z[i, k, p, t] * cpp[i, k, p, t] for i, k, p, t in sets(I, K, P, T)))

# Constraints
# Supplier capacity constraint
for i, p, t in sets(I, P, T):
    m.con(sum(x[i, j, p, t] for j in J) + sum(z[i, k, p, t] for k in K) <= cap[i, p, t])

# Warehouse flow constraint
for j, p, t in sets(J, P, T):
    m.con(sum(x[i, j, p, t] for i in I) >= sum(y[j, k, p, t] for k in K))

# Customer demand constraint
for k, p, t in sets(K, P, T):
    m.con(sum(y[j, k, p, t] for j in J) + sum(z[i, k, p, t] for i in I) >= dk[k, p, t])

# Solve
m.sol(['min'], 'cbc')

# Display
m.report()
