By following this section, new FelooPy users can learn to use the core classes, methods, or functions that help them code, model, and solve various decision problems. Notably, by solution method, we mean the process used to make the final decision based on the given inputs and following the features of the search algorithm.

## Installing FelooPy

If you have already installed other optimization packages like `pyomo`, `pulp`, `ortools`, `gekko` or `docplex`, `gurobipy`, `xpress`, `coptpy` and `insideopt`, and want to upgrade the way you use them through FelooPy you may use the following installation command:

```terminal
pip install feloopy
```

Else, if you are new to optimization in Python or want a fresh install, you can start installation using the following command:

```terminal
pip install feloopy[stock]
```

## Exact solution methods

FelooPy supports solving target optimization models using exact solution methods. By target, we mean models directly structured by an expert based on assumed aspects in terms of mathematical relations.

These solution methods (e.g., simplex, dual simplex, revised simplex, branch & bound, or branch & cut) have already been coded and fine-tuned by free and open-source solvers like `cbc`, `highs`, `glpk`, and `ipopt` or by commercial solvers like `cplex`, `gurobi`, `copt`, `xpress`, and `seeker`. You can also use a basic solver like `cbc` and design problem-specific exact or decomposition-based solution methods.

An instance of a decision problem using exact solution methods is coded and solved as follows:

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./getting-started/exact-optimization.py"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./getting-started/exact-optimization.txt"
    ```

## Heuristic solution methods


FelooPy supports solving representor optimization models using heuristic solution methods. By representor, we mean models encoded and decoded using heuristics desired by an expert based on assumed aspects of mathematical logic.

These solution methods (e.g., genetic algorithm, particle swarm optimization, differential evolution, simulated annealing, or tabu search) have already been coded and fine-tuned by free and open-source interfaces like `mealpy` and `pygad`, or by `feloopy` itself. Note that you can modify the decoding process according to your needs or have several local search phases.

An instance of a decision problem using heuristic solution methods is coded and solved as follows:

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./getting-started/heuristic-optimization.py"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./getting-started/heuristic-optimization.txt"
    ```

## Convex solution methods


FelooPy supports using convex solution methods. The models solved via these solution methods should have a specific property: convexity.

An instance of a decision problem using convex solution methods is coded and solved as follows:

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./getting-started/convex-optimization.py"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./getting-started/convex-optimization.txt"
    ```

## Constraint solution methods

FelooPy supports using constraint programming-based solution methods. The models solved via these solution methods can be of any form. However, the focus is on satisfying constraints or finding feasible solutions. Sometimes, they can also find optimal solutions. Besides, they only accept binary and integer variables and event variables.

An instance of a decision problem using constraint solution methods is coded and solved as follows:

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./getting-started/constraint-optimization.py"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./getting-started/constraint-optimization.txt"
    ```


## Uncertain solution methods

FelooPy supports handling uncertainty of your (predicted/estimated) datasets using extra processes. An example of using these methods is provided as follows:


=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./getting-started/uncertain-optimization.py"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./getting-started/uncertain-optimization.txt"
    ```

## Multi-objective solution methods


FelooPy supports solving optimization problems that include multiple objective functions. An instance of a decision problem using these methods is coded and solved as follows:


=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./getting-started/multiobjective-optimization.py"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./getting-started/multiobjective-optimization.txt"
    ```

## Multi-attribute solution methods

FelooPy supports getting experts opinions regarding the performance of multiple alternatives regarding multiple criteria and then weight criteria, rank alternatives or do both simultanously. Some of these methods also enable classification of alternatives. Below, is an example solved using these methods:


=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./getting-started/multiattribute-decision.py"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./getting-started/multiattribute-decision.txt"
    ```