By following this section, new FelooPy users can learn to use the core classes, methods, or functions that help them code, model, and solve various decision problems.

## Installing `feloopy`

If you have already installed other optimization packages like `pyomo`, `pulp`, `ortools`, `gekko` or `docplex`, `gurobipy`, `xpress`, `coptpy` and `insideopt`, and want to upgrade the way you use them through `feloopy` you may use the following installation command:

```terminal
pip install feloopy
```

Else, if you are new to optimization in Python or want a fresh install, you can start installation using the following command:


```terminal
pip install feloopy[stock]
```

## Using `exact` solution methods

`feloopy` supports solving target optimization models using `exact` solution methods. By target, we mean models directly structured by an expert based on assumed aspects in terms of mathematical relations. 

These solution methods, e.g., simplex, dual simplex, revised simplex, branch & bound, branch & cut, have already been coded and fine-tuned by free and open-source solvers like `cbc`, `highs`, `glpk`, and `ipopt` or by commercial solvers like `cplex`, `gurobi`, `copt`, `xpress`, and `seeker`. You may also use a basic solver like `cbc` and design problem-specific exact or decomposition-based solution methods. 

An instance of a decision problem using `exact` solution methods is coded and solved as follows:

```py
from feloopy import *

# Define a model
m = model("exact", "model_name", "pymprog")

# Define variables
x = m.bvar(name="x", dim=0)
y = m.pvar(name="y", dim=0, bound=[0, 1])

# Define constraints
m.con(x + y <= 1, name="c1")
m.con(x - y >= 1, name="c2")

# Define an objective
m.obj(x + y)

# Solve the model
m.sol(["max"], "glpk")

# Report the results
m.report()
```

```console
╭─ FelooPy v0.0.0 ───────────────────────────────────────────────────────────────╮
│                                                                                │
│ Date: 0000-00-00                                                Time: 00:00:00 │
│ Interface: pymprog                                                Solver: glpk │
│                                                                                │
╰────────────────────────────────────────────────────────────────────────────────╯
╭─ Model ────────────────────────────────────────────────────────────────────────╮
│                                                                                │
│ Name: model_name                                                               │
│ Feature:                                Class:                        Total:   │
│ Positive variable                       1                             1        │
│ Binary variable                         1                             1        │
│ Total variables                         2                             2        │
│ Objective                               -                             1        │
│ Constraint                              2                             2        │
│                                                                                │
╰────────────────────────────────────────────────────────────────────────────────╯
╭─ Solve ────────────────────────────────────────────────────────────────────────╮
│                                                                                │
│ Method: exact                                                  Objective value │
│ Status:                                                                    max │
│ optimal                                                                   1.00 │
│                                                                                │
╰────────────────────────────────────────────────────────────────────────────────╯
╭─ Metric ───────────────────────────────────────────────────────────────────────╮
│                                                                                │
│ CPT (microseconds)                                                     1591.90 │
│ CPT (hour:min:sec)                                                    00:00:00 │
│                                                                                │
╰────────────────────────────────────────────────────────────────────────────────╯
╭─ Decision ─────────────────────────────────────────────────────────────────────╮
│                                                                                │
│ x = 1.0                                                                        │
│                                                                                │
╰────────────────────────────────────────────────────────────────────────────────╯
```