

# FelooPy v0.2.3 Coding Syntax

## **Environment definition**

* `Model(solution_method, model_name, interface_name, agent=None, key=None)`

    * Used to define a target, representor, or learner `model_object`.

    * Arguments:
        * _solution_method_
            * Which type of optimization algorithms is this mathematical model going to be solved with? 
            * Answer= '`exact`' or `'heuristic'`.
            * Required.
        * _model_name_
            * What is the name of this mathematical model?
            * Answer= An optional string. Examples: `'knapsack'`, `'tsp'`, `'supply_chain'`, `'neural_network'`, etc.
            * Required.
        * _interface_name_
            * What is the desired optimization interface?
            * Answer= A predefined string. Examples: `feloopy` or `mealpy` (for heuristic optimization), `cplex`, `pyomo`, `'ortools'`, or `gekko` (for exact optimization). (See [Exact Interfaces][03] or [Heuristic Interfaces][04])
            * Required
        * _agent_
            * What is the algorithm agent?
            * Answer= An input argument from a higher level function. Example: `X`, which has been previously defined as a function argument `def model(X):`. 
            * Optional. Only if _solution_method_ is set to `heuristic`.
        * _key_
            * What is the key (seed) for random number generator?
            * Answer= An optional value. Examples: `0`, `19038`, etc.
            * Optional. If you are using FelooPy's specific random number generators and want to keep the results reproducible.

    * Example: `model_object = model(solution_method, model_name, interface_name, agent=None, key=None)`

    * Alternatives: `add_model` | `create_environment` | `env` | `feloopy` | `model`

    * Required, if you need to optimize something.

## **Set definition**

* `model_object.set(size)`

    * Used to add a set to the `model_object`.

    * Arguments:

        * _size_
            * What is the size of this set? 
            * Answer= An integer. Examples: `{0,1,2,...}`
            * Required.

    * Example: `I = model_object.set(10)`

    * Alternatives: None.

    * Optional. `range(size)` can be used instead.

* `model_object.card(set)`

    * Used to get the size of a set from the `model_object`.

    * Arguments:

        * _set_
            * What is the target set? 
            * Answer= A set. Examples: `I, J, K`
            * Required.

    * Example: `size = model_object.card(I)`

    * Alternatives: None.

    * Optional. `len(set)` can be used instead.

## **Variable definition**

* `model_object.bvar(name, dim=0, b=[0, 1])`

    * Used to add a binary variable, i.e., a variable that takes a value from the set `{0,1}` to the `model_object`.

    * Arguments:
        * _name_
            * What is the name of this variable? 
            * Answer= An optional string. Examples: `'x'`, `'y'`, `'select'`, `'route'`, etc.
            * Required.
        * _dim_
            * What is the dimension of this variable?
            * Answer= An optional list, which contains sets. Examples: `[I]` for a binary variable like $x_i$, `[I,J,K]` for $x_{ijk}$, etc. Leave empty for $x$ without indices.
            * Optional.
        * _b_
            * What are the bounds of this variable?
            * Answer= An optional list, which contains two numbers. Examples: `[0,1]`. 
            * Optional. But, you might not change it for a binary variable!

    * Example: `x = model_object.bvar('select', [I])`

    * Alternatives: `binary_variable` | `add_binary_variable` 

    * Optional. If your mathematical model does contain, needs to be represented using binary decision values.


* `model_object.ivar(name, dim=0, b=[0, None])`

    * Used to add an integer variable, i.e., a variable that takes a value from the set `{0,1,...}` to the `model_object`.

    * Arguments:
        * _name_
            * What is the name of this variable? 
            * Answer= An optional string. Examples: `'x'`, `'y'`, `'quantity'`, `'count'`, etc.
            * Required.
        * _dim_
            * What is the dimension of this variable?
            * Answer= An optional list, which contains sets. Examples: `[I]` for an integer variable like $x_i$, `[I,J,K]` for $x_{ijk}$, etc. Leave empty for $x$ without indices.
            * Optional.
        * _b_
            * What are the bounds of this variable?
            * Answer= An optional list, which contains two numbers. Examples: `[0,10]`. 
            * Optional for exact optimization algorithms. Required for heuristic optimization algorithms.

    * Example: `x = model_object.ivar('count', [I])`

    * Alternatives: `integer_variable` | `add_integer_variable`

    * Optional. If your mathematical model does contain, needs to be represented using integer decision values.

* `model_object.pvar(name, dim=0, b=[0, None])`

    * Used to add a positive variable, i.e., a variable that takes a value from the range `[0,+inf]` to the `model_object`.

    * Arguments:
        * _name_
            * What is the name of this variable? 
            * Answer= An optional string. Examples: `'x'`, `'y'`, `'value'`, `'level'`, etc.
            * Required.
        * _dim_
            * What is the dimension of this variable?
            * Answer= An optional list, which contains sets. Examples: `[I]` for a positive variable like $x_i$, `[I,J,K]` for $x_{ijk}$, etc. Leave empty for $x$ without indices.
            * Optional.
        * _b_
            * What are the bounds of this variable?
            * Answer= An optional list, which contains two numbers. Examples: `[0,1000]`. 
            * Optional for exact optimization algorithms. Required for heuristic optimization algorithms.

    * Example: `x = model_object.pvar('level', [I])`

    * Alternatives: `positive_variable` | `add_positive_variable`

    * Optional. If your mathematical model does contain, needs to be represented using positive decision values.

* `model_object.fvar(name, dim=0, b=[None, None])`

    * Used to add a free variable, i.e., a variable that takes a value from the range `[-inf,+inf]` to the `model_object`.

    * Arguments:
        * _name_
            * What is the name of this variable? 
            * Answer= An optional string. Examples: `'x'`, `'y'`, `'rate'`, `'utility'`, etc.
            * Required.
        * _dim_
            * What is the dimension of this variable?
            * Answer= An optional list, which contains sets. Examples: `[I]` for a free variable like $x_i$, `[I,J,K]` for $x_{ijk}$, etc. Leave empty for $x$ without indices.
            * Optional.
        * _b_
            * What are the bounds of this variable?
            * Answer= An optional list, which contains two numbers. Examples: `[-1000,1000]`. 
            * Optional for exact optimization algorithms. Required for heuristic optimization algorithms.

    * Example: `x = model_object.fvar('rate', [I])`

    * Alternatives: `free_variable` | `add_free_variable`

    * Optional. If your mathematical model does contain, needs to be represented using free (real or float point) decision values.

## **Objective definition**

* `model_object.obj(expression, direction=None, label=None)`

    * Used to add an objective function, i.e., a function that guides the target, representor, or learner models to the `model_object`.

    * Arguments:
        * _expression_
            * What is the mathematical formula of this objective function?
            * Answer= A required mathematical formula. Examples `2*x+y`, `(x-2)**3`, `sum(x[i,j] for i,j in sets(I,J))`, etc.
            * Required.
        * _direction_
            * The lower the value the better, or the higher the value the better?
            * Answer= An optinal string `'max'`, or `'min'`. It is better to be provided later!
            * Optional.
        * _label_
            * What is the name of this objective function?
            * Answer= An optional string. Examples: `'obj0'`, `'profit'`, etc.
            * Optional
        
    * Example: `model_object.obj(x**2+y**2)`

    * Alternatives: `objective` | `add_objective`

    * Required. 

## **Constraint definition**

* `model_object.con(expression, label=None)`

    * Used to add a constraint (equality or inequality) to logically limit the target, representor, or learner models for making feasible decisions, to the `model_object`.

    * Arguments:
        * _expression_
            * What it the mathematical expression of this constraint?
            * Answer= A required mathematical expression. 
                * Examples for exact optimization algorithms: `2*x+y <= 10`, `2*x+y |l| 10`, `2*x+y >= 10`, `2*x+y |g| 10`, `2*x+y == 10`, or `2*x+y |e| 10` etc.
                * Examples for heuristic optimization algorithms: `2*x+y |ll| 10` or `2*x+y |gg| 10`.
            * Required.
        * _label_
            * What is the name of this constraint?
            * Answer= An optional string. Examples: `'c0'`, `'demand'`, etc.
            * Optional
        
    * Example: `model_object.con(x-y>=10)`

    * Alternatives: `constraint` | `equation` | `add_constraint` | `add_equation`

    * Optional. 

## **Solve definition**

* `model_object.sol(directions=None, solver_name=None, solver_options=dict(), objective_id=0, email=None, time_limit=28800, cpu_threads=None, absolute_gap=None, relative_gap=None, log=False)`

* Used to find the best possible/optimal solution, region, or policy, for a target, representor, or learner `model_object`.
    * Arguments:
        * _directions_
            * What is the direction of the optimization?
            * Answer= An optinal list containing the string `'max'`, or `'min'`. Example: `['max']` or `['min']`.
            * Required.
        * _solver_name_
            * What is the name of the desired solver? Please note that this should match the interface defined for the environment.
            * Answer= A predefined string. Examples: `cplex` or `highs` (for exact optimization), `GA`, `DE`, `BaseGA`, or `OriginalSSpiderA` (for heuristic optimization). (See [Exact Solvers][03] or [Heuristic Solvers][04])
            * Required.
        * _solver_options_
            * How is the solver configured? (Currently available for heuristic optimization only).
            * Answer= A dictionary. Example: `{'epoch': 10, 'pop_size': 100, 'mutation_rate': 0.1, 'crossover_rate':0.8}`
            * Optional for exact optimization algorithms. Required for heuristic optimization algorithms.
        * _objective_id_
            * What is the id of the objective being optimized?
            * Answer= An optional integer. Defaults to 0.
            * Optional
        * _email_
            * What is your email address? This would be used by the cloud-powered optimization server 'NEOS' to send you the results after a specific amount of time. The interface should be set to `'pyomo'` and the solver name should end with `_online`.
            * Answer= An string defining your email address. Example: `you@example.com`
            * Optional.
        * _time_limit_
            * What is the maximum allowable time for the solution process?
            * Answer= An integer determining a value in seconds.
            * Optional. Currently only supported by `cplex` as the interface and `cplex` as the solver.
        * _cpu_threads_
            * How many CPU threads can be used in the solution process?
            * Answer= An integer defining the number of CPU threads. 
            * Optional. Currently only supported by `cplex` as the interface and `cplex` as the solver.
        * _absolute_gap_
            * What is the absolute gap for optimization?
            * Answer= A value as an absolute gap. 
            * Optional. Currently only supported by `cplex` as the interface and `cplex` as the solver.
        * _absolute_gap_
            * What is the relative gap for optimization?
            * Answer= A ratio as a relative gap. 
            * Optional. Currently only supported by `cplex` as the interface and `cplex` as the solver.
        * _log_
            * Do you need to see the solver log?
            * Answer= `True` or `False`.
            * Optional.

[01]: https://github.com/ktafakkori/feloopy/blob/main/documentation/Tutorial.md
[02]: https://github.com/ktafakkori/feloopy/tree/main/examples
[03]: https://github.com/ktafakkori/feloopy/blob/main/documentation/Exact_List.md
[04]: https://github.com/ktafakkori/feloopy/blob/main/documentation/Heuristic_List.md
[05]: https://github.com/ktafakkori/feloopy/blob/main/documentation/Updates.md