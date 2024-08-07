This section equips new FelooPy users with the fundamental elements (classes and their core methods and core functions) necessary to code, model, and solve almost all kinds of decision problems common in operations research and decision science.

## Installing FelooPy

Suppose you have already installed other optimization packages like `pyomo`, `pulp`, `ortools`, `gekko` or `docplex`, `gurobipy`, `xpress`, `coptpy`, `insideopt` and `gamspy`, and want to upgrade the way you use them through FelooPy. In that case, you may use the following installation command:

```terminal
pip install feloopy
```

Otherwise, if you are new to optimization in Python or want a fresh install, you can start installation using the following command:

```terminal
pip install feloopy[stock]
```

## Optimization algorithms

### *Exact optimization algorithms*

FelooPy supports solving mathematical models using exact optimization algorithms. These algorithms are heuristics guaranteed to find optimal solutions to a decision problem translated as a mathematical model in a not necessarily polynomial time. Simplex, dual simplex, revised simplex, branch & bound, or branch & cut are examples of such algorithms. Free and open-source solvers like `cbc`, `highs`, `glpk`, and `ipopt` or commercial solvers like `cplex`, `gurobi`, `copt`, `xpress`, and `seeker` have already coded and fine-tuned such algorithms for direct use. However, one can also leverage these solvers and design problem-specific or improved exact optimization algorithms. A mathematical model solved by an exact optimization algorithm is programmed as follows:

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./getting-started/exact-optimization.py"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./getting-started/exact-optimization.txt"
    ```

### *Heuristic optimization algorithms*

FelooPy supports solving a representation of mathematical models using heuristic optimization algorithms. These algorithms are heuristics that are not guaranteed to find optimal solutions to a decision problem translated by the representation of a mathematical model in a possibly polynomial time. Such algorithms include genetic algorithm, differential evolution, particle swarm optimization, grey wolf optimizer, simulated annealing, and tabu search. Free and open-source interfaces and solvers like `mealpy`, `niapy`, `pymoo`, `pygad` or `feloopy` (itself) have already coded and fine-tuned such algorithms for direct use. However, one can leverage these solvers and design problem-specific or improved heuristic optimization algorithms. A mathematical model solved by a heuristic optimization algorithm is programmed as follows:

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./getting-started/heuristic-optimization.py"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./getting-started/heuristic-optimization.txt"
    ```

## Programming facilitators

### *Convex programming methods*

FelooPy supports solving mathematical models that have convexity properties using convex programming methods. These programming methods facilitate using scalars, vectors, matrices, or tensors in programming a mathematical model, enabling the consideration of statistical metrics in machine learning, control, finance, and more. Most of these algorithms are guaranteed to find optimal solutions to a decision problem translated by the representation of a mathematical model in a not necessarily polynomial time.
Free and open-source interfaces like `cvxpy` and `gekko` or commercial ones like `gurobi` have already coded and fine-tuned such programming methods for direct use. A mathematical model solved by a convex programming method is coded as follows:

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./getting-started/convex-optimization.py"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./getting-started/convex-optimization.txt"
    ```

### *Constraint programming methods*

FelooPy empowers users to tackle complex decision problems through constraint programming. Unlike exact or heuristic optimization algorithms, which are targeted at finding "optimal" or "best possible" solutions in a huge feasible space, or unlike convex programming methods that primarily enable the use of the unique structure of variables, constraint programming allows the use of unique programming methods that specify logic for finding a reduced set of feasible solutions (satisfying your constraints) and only allows the use of binary or integer variables. Free and open-source interfaces like `ortools_cp` or commercial ones like `cplex_cp` have already coded and fine-tuned such programming methods for direct use. A mathematical model solved by a constraint programming method is coded as follows:

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./getting-started/constraint-optimization.py"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./getting-started/constraint-optimization.txt"
    ```

## Complexity handlers

### *Uncertainty handling methods*

FelooPy supports handling the uncertainty of your (predicted/estimated) datasets solved by exact optimization algorithms using special methods and functions. Free and open-source interfaces like `rsome_ro` or `rsome_dro` have already coded and fine-tuned stochastic, robust, or distributionally robust uncertainty handling methods for direct use. A mathematical model solved by an exact optimization algorithm using uncertainty handling methods is coded as follows:

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./getting-started/uncertain-optimization.py"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./getting-started/uncertain-optimization.txt"
    ```

### *Multi-objectivity handling methods*

FelooPy-specific methods support handling multi-objectivity of your decision problems being solved by either exact or heuristic optimization algorithms. 

A multi-objective mathematical model solved by an exact optimization algorithm is coded as follows:

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./getting-started/multiobjective-exact-optimization.py"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./getting-started/multiobjective-exact-optimization.txt"
    ```

A multi-objective mathematical model solved by a heuristic optimization algorithm is coded as follows:

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./getting-started/multiobjective-heuristic-optimization.py"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./getting-started/multiobjective-heuristic-optimization.txt"
    ```


### *Opinion handling methods*

FelooPy supports decision problems that involve getting experts' opinions regarding the performance of multiple alternatives regarding multiple criteria/attributes and then weighting criteria/attributes, ranking or selecting alternatives, or doing both simultaneously. These methods enable solving decision problems without mathematical models and using expert-based data. Some of these methods also allow the classification of alternatives. Below is an example solved using these methods:

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./getting-started/multiattribute-decision.py"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./getting-started/multiattribute-decision.txt"
    ```

