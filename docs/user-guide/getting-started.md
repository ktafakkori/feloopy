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

## `exact` optimization methods

`feloopy` supports solving target optimization models using `exact` solution methods. By target, we mean models directly structured by an expert based on assumed aspects in terms of mathematical relations. 

These solution methods (e.g., simplex, dual simplex, revised simplex, branch & bound or branch & cut) have already been coded and fine-tuned by free and open-source solvers like `cbc`, `highs`, `glpk`, and `ipopt` or by commercial solvers like `cplex`, `gurobi`, `copt`, `xpress`, and `seeker`. Note that you can also use a basic solver like `cbc` and design problem-specific exact or decomposition-based solution methods. 

An instance of a decision problem using `exact` solution methods is coded and solved as follows:

=== ":fontawesome-brands-python: Python"

    ```py
    import feloopy as flp

    # Define a model
    m = flp.model("exact", "model_name", "pymprog")

    # Define variables
    x = m.bvar(name="x")
    y = m.pvar(name="y", bound=[0, 1])

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
=== ":material-console: Console"

    ```console
    ╭─ FelooPy v0.0.0 ───────────────────────────────────────────────────────────────╮
    │                                                                                │
    │ Date: 0000-00-00                                                Time: 00:00:00 │
    │ Interface: pymprog                                                Solver: glpk │
    │                                                                                │
    ╰────────────────────────────────────────────────────────────────────────────────╯
    ╭─ Model ────────────────────────────────────────────────────────────────────────╮
    │                                                                                │
    │ Name: target_model_name                                                        │
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
    │ CPT (microseconds)                                                     1899.50 │
    │ CPT (hour:min:sec)                                                    00:00:00 │
    │                                                                                │
    ╰────────────────────────────────────────────────────────────────────────────────╯
    ╭─ Decision ─────────────────────────────────────────────────────────────────────╮
    │                                                                                │
    │ x = 1.0                                                                        │
    │                                                                                │
    ╰────────────────────────────────────────────────────────────────────────────────╯
    ```

## `heuristic` optimization methods


`feloopy` supports solving representor optimization models using `heuristic` solution methods. By representor, we mean models that are encoded and decoded using heuristics desired by an expert based on assumed aspects in terms of mathematical logic.

These solution methods (e.g., genetic algorithm, particle swarm optimization, differential evolution, simulated annealing or tabu search) have already been coded and fine-tuned by free and open-source interfaces like `mealpy` and `pygad`, or by `feloopy` itself. Note that you can also modify the decoding process according to your needs or have seeral local search phases.

An instance of a decision problem using `heuristic` solution methods is coded and solved as follows:

=== ":fontawesome-brands-python: Python"

    ```py
    import feloopy as flp


    def instance(X):

        # Define model instance
        m = flp.model("heuristic", "model_name", "feloopy", X)

        # Define variables for the model instance
        x = m.bvar(name="x")
        y = m.pvar(name="y", bound=[0, 1])

        # Define constraints for the model instance
        m.con(x + y | flp.l | 1, name="c1")
        m.con(x - y | flp.g | 1, name="c2")

        # Define an objective for the model instance
        m.obj((x - 1) ** 2 + (y - 1) ** 2)

        # Solve the model instance
        m.sol(["max"], "ga", {"epoch": 1000, "pop_size": 100})

        return m[X]


    # Make the main model
    m = flp.make_model(instance)

    # Solve the model
    m.sol(penalty_coefficient=10)

    # Report the results
    m.report()
    ```
=== ":material-console: Console"

    ```console
    ╭─ FelooPy v0.0.0 ───────────────────────────────────────────────────────────────╮
    │                                                                                │
    │ Date: 0000-00-00                                                Time: 00:00:00 │
    │ Interface: feloopy                                                  Solver: ga │
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
    │ Method: heuristic                                              Objective value │
    │ Status:                                                                    max │
    │ feasible (constrained)                                                    1.00 │
    │                                                                                │
    ╰────────────────────────────────────────────────────────────────────────────────╯
    ╭─ Metric ───────────────────────────────────────────────────────────────────────╮
    │                                                                                │
    │ CPT (microseconds)                                                    2.01e+06 │
    │ CPT (hour:min:sec)                                                    00:00:02 │
    │                                                                                │
    ╰────────────────────────────────────────────────────────────────────────────────╯
    ╭─ Decision ─────────────────────────────────────────────────────────────────────╮
    │                                                                                │
    │ x = [1.]                                                                       │
    │                                                                                │
    ╰────────────────────────────────────────────────────────────────────────────────╯
    ```

## `heuristic` optimization methods


`feloopy` supports solving convex optimization models using `convex` solution methods. The models that are solved via these solution methods should have a specific convexity property.

An instance of a decision problem using `convex` solution methods is coded and solved as follows:

=== ":fontawesome-brands-python: Python"

    ```py
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
    ```

=== ":material-console: Console"

    ``` console
    ╭─ FelooPy v0.0.0 ───────────────────────────────────────────────────────────────╮
    │                                                                                │
    │ Date: 0000-00-00                                                Time: 00:00:00 │
    │ Interface: cvxpy                                                  Solver: ecos │
    │                                                                                │
    ╰────────────────────────────────────────────────────────────────────────────────╯
    ╭─ Model ────────────────────────────────────────────────────────────────────────╮
    │                                                                                │
    │ Name: convex_model_name                                                        │
    │ Feature:                                Class:                        Total:   │
    │ Free variable                           1                             1        │
    │ Total variables                         1                             1        │
    │ Objective                               -                             1        │
    │ Constraint                              2                             2        │
    │                                                                                │
    ╰────────────────────────────────────────────────────────────────────────────────╯
    ╭─ Solve ────────────────────────────────────────────────────────────────────────╮
    │                                                                                │
    │ Method: convex                                                 Objective value │
    │ Status:                                                                    min │
    │ optimal                                                                   9.00 │
    │                                                                                │
    ╰────────────────────────────────────────────────────────────────────────────────╯
    ╭─ Metric ───────────────────────────────────────────────────────────────────────╮
    │                                                                                │
    │ CPT (microseconds)                                                    1.16e+04 │
    │ CPT (hour:min:sec)                                                    00:00:00 │
    │                                                                                │
    ╰────────────────────────────────────────────────────────────────────────────────╯
    ╭─ Decision ─────────────────────────────────────────────────────────────────────╮
    │                                                                                │
    │ x = 1.000000005186514                                                          │
    │                                                                                │
    ╰────────────────────────────────────────────────────────────────────────────────╯
    ```

```python exec="on" result="utf8" session="reading"
--8<-- "reading.py"
```