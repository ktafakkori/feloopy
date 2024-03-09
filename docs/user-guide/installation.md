
## Recommended setup

- Operating system:

    Windows, MacOS, or Linux-based distros (e.g., Ubuntu or Manjaro).

- Python interpreter:

    CPython 3.10.x interpreters, which are downloadable from [here](https://www.python.org/downloads/), come with the `pip` package manager by default.

- Integrated development environment/Code editor:

    [Spyder](https://www.spyder-ide.org/#section-download), [Visual Studio Code](https://code.visualstudio.com/download), [Google Colab](https://colab.research.google.com/), or [JupyterLab](https://jupyter.org/install).

- Insiders/developer version access:

    [Git](https://git-scm.com/downloads).

## Quick installation

For a quick installation of FelooPy with the generous support of interfaces and solvers, you may use the pip package manager as follows:


=== ":material-console: System-wide"

    ``` console
    pip install -U "feloopy[stock]==0.2.8"
    ```

=== ":material-console: User-specific"

    ``` console
    pip install -U "feloopy[stock]==0.2.8" --user
    ```

=== ":material-console: Virtual environment"

    - Create a virtual environment (if you desire a new one):

    ``` console
    python -m venv {path/to/env}

    ```

    - Activate the desired virtual environment

    === ":material-console: Windows"


        ``` console
        {path\to\env}\Scripts\activate
        ```

    === ":material-console: Unix/MacOS"

        ``` console
        source {path/to/env}/bin/activate
        ```


    - Install the package when the environment is active
   

    ``` console
    pip install -U "feloopy[stock]==0.2.8"
    ```

    === ":material-console: Admin"

        ``` console
        pip install -U "feloopy[stock]==0.2.8"
        ```

    === ":material-console: User"

        ``` console
        pip install -U "feloopy[stock]==0.2.8" --user
        ```

=== ":material-console: ipykernel"

    ipykernel is a Python kernel for Jupyter notebooks and is used in Jupyter, Google Colab, and Spyder:

    ``` console
    !pip install -U "feloopy[stock]==0.2.8"
    ```



As some users might prefer a dedicated version, the following lists the available variants of FelooPy:

## Core variant

This variant installs the base package without any additional features. It installs FelooPy with typical data handling, visualization, and scientific computing dependencies. Besides, it comes with original developments of FelooPy (e.g., some heuristic optimization algorithms and problem-handling methods). Therefore, you can solve almost any decision problem using `feloopy` (itself) as the interface and algorithms like `ga`, `de`, `gwo`, `ts`, and `sa`.

=== ":material-console: System-wide"

    ``` console
    pip install -U "feloopy==0.2.8"
    ```

=== ":material-console: User-specific"

    ``` console
    pip install -U "feloopy==0.2.8" --user
    ```

=== ":material-console: Virtual environment"

    - Create a virtual environment (if you desire a new one):

    ``` console
    python -m venv {path/to/env}

    ```

    - Activate the desired virtual environment

    === ":material-console: Windows"


        ``` console
        {path\to\env}\Scripts\activate
        ```

    === ":material-console: Unix/MacOS"

        ``` console
        source {path/to/env}/bin/activate
        ```


    - Install the package when the environment is active
   

    ``` console
    pip install -U "feloopy==0.2.8"
    ```

    === ":material-console: Admin"

        ``` console
        pip install -U "feloopy==0.2.8"
        ```

    === ":material-console: User"

        ``` console
        pip install -U "feloopy==0.2.8" --user
        ```

=== ":material-console: ipykernel"

    ipykernel is a Python kernel for Jupyter notebooks and is used in Jupyter, Google Colab, and Spyder:

    ``` console
    !pip install -U "feloopy==0.2.8"
    ```

## Free variants

### `pico`

Same as the core variant.

=== ":material-console: System-wide"

    ``` console
    pip install -U "feloopy[pico]==0.2.8"
    ```

=== ":material-console: User-specific"

    ``` console
    pip install -U "feloopy[pico]==0.2.8" --user
    ```

=== ":material-console: Virtual environment"

    - Create a virtual environment (if you desire a new one):

    ``` console
    python -m venv {path/to/env}

    ```

    - Activate the desired virtual environment

    === ":material-console: Windows"


        ``` console
        {path\to\env}\Scripts\activate
        ```

    === ":material-console: Unix/MacOS"

        ``` console
        source {path/to/env}/bin/activate
        ```


    - Install the package when the environment is active
   

    ``` console
    pip install -U "feloopy[pico]==0.2.8"
    ```

    === ":material-console: Admin"

        ``` console
        pip install -U "feloopy[pico]==0.2.8"
        ```

    === ":material-console: User"

        ``` console
        pip install -U "feloopy[pico]==0.2.8" --user
        ```

=== ":material-console: ipykernel"

    ipykernel is a Python kernel for Jupyter notebooks and is used in Jupyter, Google Colab, and Spyder:

    ``` console
    !pip install -U "feloopy[pico]==0.2.8"
    ```

### `nano`

This variant allows you to get started with linear programming, integer programming and mixed-integer linear programming, thanks to the `pymprog` interface that comes with the free and open-source `glpk` solver.

=== ":material-console: System-wide"

    ``` console
    pip install -U "feloopy[nano]==0.2.8"
    ```

=== ":material-console: User-specific"

    ``` console
    pip install -U "feloopy[nano]==0.2.8" --user
    ```

=== ":material-console: Virtual environment"

    - Create a virtual environment (if you desire a new one):

    ``` console
    python -m venv {path/to/env}

    ```

    - Activate the desired virtual environment

    === ":material-console: Windows"


        ``` console
        {path\to\env}\Scripts\activate
        ```

    === ":material-console: Unix/MacOS"

        ``` console
        source {path/to/env}/bin/activate
        ```


    - Install the package when the environment is active
   

    ``` console
    pip install -U "feloopy[nano]==0.2.8"
    ```

    === ":material-console: Admin"

        ``` console
        pip install -U "feloopy[nano]==0.2.8"
        ```

    === ":material-console: User"

        ``` console
        pip install -U "feloopy[nano]==0.2.8" --user
        ```

=== ":material-console: ipykernel"

    ipykernel is a Python kernel for Jupyter notebooks and is used in Jupyter, Google Colab, and Spyder:

    ``` console
    !pip install -U "feloopy[nano]==0.2.8"
    ```

### `micro`

This variant extends the capabilities of the `nano` variant to enable nonlinear and general-purpose programming, thanks to the `gekko` and `mealpy` interfaces. `gekko` comes with three solvers: `ipopt,` `adopt,` and `boost`. `ipopt` solves nonlinear programming problems with a large number of variables without requiring a warm-start, `bpopt` acts almost the same, and `apopt` allows warm-starting from a given solution or with problems with less than 2000 variables and is the only nonlinear programming solver by `gekko` that is also suitable for mixed integer linear programming and mixed integer linear nonlinear programming. `mealpy` comes with more than 200 heuristic optimization algorithms (e.g., `base-ga` which is a basic variant of genetic algorithm, `base-gwo` which is a basic ariant of grey wolf optimizer and so on). 

=== ":material-console: System-wide"

    ``` console
    pip install -U "feloopy[micro]==0.2.8"
    ```

=== ":material-console: User-specific"

    ``` console
    pip install -U "feloopy[micro]==0.2.8" --user
    ```

=== ":material-console: Virtual environment"

    - Create a virtual environment (if you desire a new one):

    ``` console
    python -m venv {path/to/env}

    ```

    - Activate the desired virtual environment

    === ":material-console: Windows"


        ``` console
        {path\to\env}\Scripts\activate
        ```

    === ":material-console: Unix/MacOS"

        ``` console
        source {path/to/env}/bin/activate
        ```


    - Install the package when the environment is active
   

    ``` console
    pip install -U "feloopy[micro]==0.2.8"
    ```

    === ":material-console: Admin"

        ``` console
        pip install -U "feloopy[micro]==0.2.8"
        ```

    === ":material-console: User"

        ``` console
        pip install -U "feloopy[micro]==0.2.8" --user
        ```

=== ":material-console: ipykernel"

    ipykernel is a Python kernel for Jupyter notebooks and is used in Jupyter, Google Colab, and Spyder:

    ``` console
    !pip install -U "feloopy[micro]==0.2.8"
    ```

### `mini`

This variant extends the capabilities of the `micro` variant to enable convex and constraint programming, thanks to the `cvxpy` and `ortools_cp` interfaces. Users can also use some specific exact optimization algorithms for linear, integer, and mixed integer linear programming provided by `ortools`.

=== ":material-console: System-wide"

    ``` console
    pip install -U "feloopy[mini]==0.2.8"
    ```

=== ":material-console: User-specific"

    ``` console
    pip install -U "feloopy[mini]==0.2.8" --user
    ```

=== ":material-console: Virtual environment"

    - Create a virtual environment (if you desire a new one):

    ``` console
    python -m venv {path/to/env}

    ```

    - Activate the desired virtual environment

    === ":material-console: Windows"


        ``` console
        {path\to\env}\Scripts\activate
        ```

    === ":material-console: Unix/MacOS"

        ``` console
        source {path/to/env}/bin/activate
        ```


    - Install the package when the environment is active
   

    ``` console
    pip install -U "feloopy[mini]==0.2.8"
    ```

    === ":material-console: Admin"

        ``` console
        pip install -U "feloopy[mini]==0.2.8"
        ```

    === ":material-console: User"

        ``` console
        pip install -U "feloopy[mini]==0.2.8" --user
        ```

=== ":material-console: ipykernel"

    ipykernel is a Python kernel for Jupyter notebooks and is used in Jupyter, Google Colab, and Spyder:

    ``` console
    !pip install -U "feloopy[mini]==0.2.8"
    ```

### `full`

This variant extends the capabilities of the `mini` variant to enable multi-objectivity handling, uncertainty-handling and opinion handling. It comes with `pymoo`, `pydecision`, and `rsome` packages.

=== ":material-console: System-wide"

    ``` console
    pip install -U "feloopy[full]==0.2.8"
    ```

=== ":material-console: User-specific"

    ``` console
    pip install -U "feloopy[full]==0.2.8" --user
    ```

=== ":material-console: Virtual environment"

    - Create a virtual environment (if you desire a new one):

    ``` console
    python -m venv {path/to/env}

    ```

    - Activate the desired virtual environment

    === ":material-console: Windows"


        ``` console
        {path\to\env}\Scripts\activate
        ```

    === ":material-console: Unix/MacOS"

        ``` console
        source {path/to/env}/bin/activate
        ```


    - Install the package when the environment is active
   

    ``` console
    pip install -U "feloopy[full]==0.2.8"
    ```

    === ":material-console: Admin"

        ``` console
        pip install -U "feloopy[full]==0.2.8"
        ```

    === ":material-console: User"

        ``` console
        pip install -U "feloopy[full]==0.2.8" --user
        ```

=== ":material-console: ipykernel"

    ipykernel is a Python kernel for Jupyter notebooks and is used in Jupyter, Google Colab, and Spyder:

    ``` console
    !pip install -U "feloopy[full]==0.2.8"
    ```

### `stock`

For enabling the switch among multiple different optimization algorithms, programming facilitators, and complexity handling, this variant provides additional alternatives or linear programming, integer programming, mixed-integer linear programming, mixed-integer nonlinear programming, and general purpose programming like `pulp`, `pyomo`, `picos`, `linopy`, `mip`, `niapy`, and `pygad` packages.

=== ":material-console: System-wide"

    ``` console
    pip install -U "feloopy[stock]==0.2.8"
    ```

=== ":material-console: User-specific"

    ``` console
    pip install -U "feloopy[stock]==0.2.8" --user
    ```

=== ":material-console: Virtual environment"

    - Create a virtual environment (if you desire a new one):

    ``` console
    python -m venv {path/to/env}

    ```

    - Activate the desired virtual environment

    === ":material-console: Windows"


        ``` console
        {path\to\env}\Scripts\activate
        ```

    === ":material-console: Unix/MacOS"

        ``` console
        source {path/to/env}/bin/activate
        ```


    - Install the package when the environment is active
   

    ``` console
    pip install -U "feloopy[stock]==0.2.8"
    ```

    === ":material-console: Admin"

        ``` console
        pip install -U "feloopy[stock]==0.2.8"
        ```

    === ":material-console: User"

        ``` console
        pip install -U "feloopy[stock]==0.2.8" --user
        ```

=== ":material-console: ipykernel"

    ipykernel is a Python kernel for Jupyter notebooks and is used in Jupyter, Google Colab, and Spyder:

    ``` console
    !pip install -U "feloopy[stock]==0.2.8"
    ```

## Commercial variants

### `plus_gurobi`

This variant includes the Gurobi solver. It requires a valid Gurobi license. Refer to the [Gurobi website](https://www.gurobi.com/) for more information.

=== ":material-console: System-wide"

    ``` console
    pip install -U "feloopy[plus_gurobi]==0.2.8"
    ```

=== ":material-console: User-specific"

    ``` console
    pip install -U "feloopy[plus_gurobi]==0.2.8" --user
    ```

=== ":material-console: Virtual environment"

    - Create a virtual environment (if you desire a new one):

    ``` console
    python -m venv {path/to/env}

    ```

    - Activate the desired virtual environment

    === ":material-console: Windows"


        ``` console
        {path\to\env}\Scripts\activate
        ```

    === ":material-console: Unix/MacOS"

        ``` console
        source {path/to/env}/bin/activate
        ```


    - Install the package when the environment is active
   

    ``` console
    pip install -U "feloopy[plus_gurobi]==0.2.8"
    ```

    === ":material-console: Admin"

        ``` console
        pip install -U "feloopy[plus_gurobi]==0.2.8"
        ```

    === ":material-console: User"

        ``` console
        pip install -U "feloopy[plus_gurobi]==0.2.8" --user
        ```

=== ":material-console: ipykernel"

    ipykernel is a Python kernel for Jupyter notebooks and is used in Jupyter, Google Colab, and Spyder:

    ``` console
    !pip install -U "feloopy[plus_gurobi]==0.2.8"
    ```

### `plus_cplex`

This variant includes the CPLEX solver. It requires a valid CPLEX license. Refer to the [CPLEX website](https://www.ibm.com/analytics/cplex-optimizer) for more information.

=== ":material-console: System-wide"

    ``` console
    pip install -U "feloopy[plus_cplex]==0.2.8"
    ```

=== ":material-console: User-specific"

    ``` console
    pip install -U "feloopy[plus_cplex]==0.2.8" --user
    ```

=== ":material-console: Virtual environment"

    - Create a virtual environment (if you desire a new one):

    ``` console
    python -m venv {path/to/env}

    ```

    - Activate the desired virtual environment

    === ":material-console: Windows"


        ``` console
        {path\to\env}\Scripts\activate
        ```

    === ":material-console: Unix/MacOS"

        ``` console
        source {path/to/env}/bin/activate
        ```


    - Install the package when the environment is active
   

    ``` console
    pip install -U "feloopy[plus_cplex]==0.2.8"
    ```

    === ":material-console: Admin"

        ``` console
        pip install -U "feloopy[plus_cplex]==0.2.8"
        ```

    === ":material-console: User"

        ``` console
        pip install -U "feloopy[plus_cplex]==0.2.8" --user
        ```

=== ":material-console: ipykernel"

    ipykernel is a Python kernel for Jupyter notebooks and is used in Jupyter, Google Colab, and Spyder:

    ``` console
    !pip install -U "feloopy[plus_cplex]==0.2.8"
    ```

### `plus_xpress`

This variant includes the Xpress solver. It requires a valid Xpress license. Refer to the [Xpress website](https://www.fico.com/en/products/fico-xpress-optimization) for more information.


=== ":material-console: System-wide"

    ``` console
    pip install -U "feloopy[plus_xpress]==0.2.8"
    ```

=== ":material-console: User-specific"

    ``` console
    pip install -U "feloopy[plus_xpress]==0.2.8" --user
    ```

=== ":material-console: Virtual environment"

    - Create a virtual environment (if you desire a new one):

    ``` console
    python -m venv {path/to/env}

    ```

    - Activate the desired virtual environment

    === ":material-console: Windows"


        ``` console
        {path\to\env}\Scripts\activate
        ```

    === ":material-console: Unix/MacOS"

        ``` console
        source {path/to/env}/bin/activate
        ```


    - Install the package when the environment is active
   

    ``` console
    pip install -U "feloopy[plus_xpress]==0.2.8"
    ```

    === ":material-console: Admin"

        ``` console
        pip install -U "feloopy[plus_xpress]==0.2.8"
        ```

    === ":material-console: User"

        ``` console
        pip install -U "feloopy[plus_xpress]==0.2.8" --user
        ```

=== ":material-console: ipykernel"

    ipykernel is a Python kernel for Jupyter notebooks and is used in Jupyter, Google Colab, and Spyder:

    ``` console
    !pip install -U "feloopy[plus_xpress]==0.2.8"
    ```

### `plus_copt`

This variant includes the COPT solver. It requires a valid COPT license. Refer to the [COPT website](https://shanshu.ai/copt) for more information.

=== ":material-console: System-wide"

    ``` console
    pip install -U "feloopy[plus_copt]==0.2.8"
    ```

=== ":material-console: User-specific"

    ``` console
    pip install -U "feloopy[plus_copt]==0.2.8" --user
    ```

=== ":material-console: Virtual environment"

    - Create a virtual environment (if you desire a new one):

    ``` console
    python -m venv {path/to/env}

    ```

    - Activate the desired virtual environment

    === ":material-console: Windows"


        ``` console
        {path\to\env}\Scripts\activate
        ```

    === ":material-console: Unix/MacOS"

        ``` console
        source {path/to/env}/bin/activate
        ```


    - Install the package when the environment is active
   

    ``` console
    pip install -U "feloopy[plus_copt]==0.2.8"
    ```

    === ":material-console: Admin"

        ``` console
        pip install -U "feloopy[plus_copt]==0.2.8"
        ```

    === ":material-console: User"

        ``` console
        pip install -U "feloopy[plus_copt]==0.2.8" --user
        ```

=== ":material-console: ipykernel"

    ipykernel is a Python kernel for Jupyter notebooks and is used in Jupyter, Google Colab, and Spyder:

    ``` console
    !pip install -U "feloopy[plus_copt]==0.2.8"
    ```

### `plus_gams`

This variant includes the GAMS (General Algebraic Modeling System) interface. It requires a valid GAMS license. Refer to the [GAMS website](https://www.gams.com/) for more information.


=== ":material-console: System-wide"

    ``` console
    pip install -U "feloopy[plus_gams]==0.2.8"
    ```

=== ":material-console: User-specific"

    ``` console
    pip install -U "feloopy[plus_gams]==0.2.8" --user
    ```

=== ":material-console: Virtual environment"

    - Create a virtual environment (if you desire a new one):

    ``` console
    python -m venv {path/to/env}

    ```

    - Activate the desired virtual environment

    === ":material-console: Windows"


        ``` console
        {path\to\env}\Scripts\activate
        ```

    === ":material-console: Unix/MacOS"

        ``` console
        source {path/to/env}/bin/activate
        ```


    - Install the package when the environment is active
   

    ``` console
    pip install -U "feloopy[plus_gams]==0.2.8"
    ```

    === ":material-console: Admin"

        ``` console
        pip install -U "feloopy[plus_gams]==0.2.8"
        ```

    === ":material-console: User"

        ``` console
        pip install -U "feloopy[plus_gams]==0.2.8" --user
        ```

=== ":material-console: ipykernel"

    ipykernel is a Python kernel for Jupyter notebooks and is used in Jupyter, Google Colab, and Spyder:

    ``` console
    !pip install -U "feloopy[plus_gams]==0.2.8"
    ```

### `plus_insideopt`

This variant includes the Seeker(TM) solver. It requires a valid Seeker license. Refer to the [InsideOpt website](https://insideopt.com/pages/install-insideopt-seeker) for more information. You may use `plus_insideoptdemo` to test the demo version.




=== ":material-console: System-wide"

    ``` console
    pip install -U "feloopy[plus_insideopt]==0.2.8"
    ```

=== ":material-console: User-specific"

    ``` console
    pip install -U "feloopy[plus_insideopt]==0.2.8" --user
    ```

=== ":material-console: Virtual environment"

    - Create a virtual environment (if you desire a new one):

    ``` console
    python -m venv {path/to/env}

    ```

    - Activate the desired virtual environment

    === ":material-console: Windows"


        ``` console
        {path\to\env}\Scripts\activate
        ```

    === ":material-console: Unix/MacOS"

        ``` console
        source {path/to/env}/bin/activate
        ```


    - Install the package when the environment is active
   

    ``` console
    pip install -U "feloopy[plus_insideopt]==0.2.8"
    ```

    === ":material-console: Admin"

        ``` console
        pip install -U "feloopy[plus_insideopt]==0.2.8"
        ```

    === ":material-console: User"

        ``` console
        pip install -U "feloopy[plus_insideopt]==0.2.8" --user
        ```

=== ":material-console: ipykernel"

    ipykernel is a Python kernel for Jupyter notebooks and is used in Jupyter, Google Colab, and Spyder:

    ``` console
    !pip install -U "feloopy[plus_insideopt]==0.2.8"
    ```


## Incompatible variants

### `only_cylp`

This variant includes the CyLP solver. It requires a valid CyLP installation. Refer to this [link](https://github.com/coin-or/CyLP) for more information.


=== ":material-console: System-wide"

    ``` console
    pip install -U "feloopy[only_cylp]==0.2.8"
    ```

=== ":material-console: User-specific"

    ``` console
    pip install -U "feloopy[only_cylp]==0.2.8" --user
    ```

=== ":material-console: Virtual environment"

    - Create a virtual environment (if you desire a new one):

    ``` console
    python -m venv {path/to/env}

    ```

    - Activate the desired virtual environment

    === ":material-console: Windows"


        ``` console
        {path\to\env}\Scripts\activate
        ```

    === ":material-console: Unix/MacOS"

        ``` console
        source {path/to/env}/bin/activate
        ```


    - Install the package when the environment is active
   

    ``` console
    pip install -U "feloopy[only_cylp]==0.2.8"
    ```

    === ":material-console: Admin"

        ``` console
        pip install -U "feloopy[only_cylp]==0.2.8"
        ```

    === ":material-console: User"

        ``` console
        pip install -U "feloopy[only_cylp]==0.2.8" --user
        ```

=== ":material-console: ipykernel"

    ipykernel is a Python kernel for Jupyter notebooks and is used in Jupyter, Google Colab, and Spyder:

    ``` console
    !pip install -U "feloopy[only_cylp]==0.2.8"
    ```

### `only_linux`


This variant includes additional features for Linux-based distros. It installs FelooPy with its common dependencies and the `pymultiobjective` package.


=== ":material-console: System-wide"

    ``` console
    pip install -U "feloopy[only_linux]==0.2.8"
    ```

=== ":material-console: User-specific"

    ``` console
    pip install -U "feloopy[only_linux]==0.2.8" --user
    ```

=== ":material-console: Virtual environment"

    - Create a virtual environment (if you desire a new one):

    ``` console
    python -m venv {path/to/env}

    ```

    - Activate the desired virtual environment

    === ":material-console: Windows"


        ``` console
        {path\to\env}\Scripts\activate
        ```

    === ":material-console: Unix/MacOS"

        ``` console
        source {path/to/env}/bin/activate
        ```


    - Install the package when the environment is active
   

    ``` console
    pip install -U "feloopy[only_linux]==0.2.8"
    ```

    === ":material-console: Admin"

        ``` console
        pip install -U "feloopy[only_linux]==0.2.8"
        ```

    === ":material-console: User"

        ``` console
        pip install -U "feloopy[only_linux]==0.2.8" --user
        ```

=== ":material-console: ipykernel"

    ipykernel is a Python kernel for Jupyter notebooks and is used in Jupyter, Google Colab, and Spyder:

    ``` console
    !pip install -U "feloopy[only_linux]==0.2.8"
    ```


## Complete variants

### `hyper`

This variant includes all packages of free and commercial variants.

=== ":material-console: System-wide"

    ``` console
    pip install -U "feloopy[hyper]==0.2.8"
    ```

=== ":material-console: User-specific"

    ``` console
    pip install -U "feloopy[hyper]==0.2.8" --user
    ```

=== ":material-console: Virtual environment"

    - Create a virtual environment (if you desire a new one):

    ``` console
    python -m venv {path/to/env}

    ```

    - Activate the desired virtual environment

    === ":material-console: Windows"


        ``` console
        {path\to\env}\Scripts\activate
        ```

    === ":material-console: Unix/MacOS"

        ``` console
        source {path/to/env}/bin/activate
        ```


    - Install the package when the environment is active
   

    ``` console
    pip install -U "feloopy[hyper]==0.2.8"
    ```

    === ":material-console: Admin"

        ``` console
        pip install -U "feloopy[hyper]==0.2.8"
        ```

    === ":material-console: User"

        ``` console
        pip install -U "feloopy[hyper]==0.2.8" --user
        ```

=== ":material-console: ipykernel"

    ipykernel is a Python kernel for Jupyter notebooks and is used in Jupyter, Google Colab, and Spyder:

    ``` console
    !pip install -U "feloopy[onlhypery_linux]==0.2.8"
    ```


### `mega`

This variant includes all packages of free and commercial variants as well as incompatible variants.

=== ":material-console: System-wide"

    ``` console
    pip install -U "feloopy[mega]==0.2.8"
    ```

=== ":material-console: User-specific"

    ``` console
    pip install -U "feloopy[mega]==0.2.8" --user
    ```

=== ":material-console: Virtual environment"

    - Create a virtual environment (if you desire a new one):

    ``` console
    python -m venv {path/to/env}

    ```

    - Activate the desired virtual environment

    === ":material-console: Windows"


        ``` console
        {path\to\env}\Scripts\activate
        ```

    === ":material-console: Unix/MacOS"

        ``` console
        source {path/to/env}/bin/activate
        ```


    - Install the package when the environment is active
   

    ``` console
    pip install -U "feloopy[mega]==0.2.8"
    ```

    === ":material-console: Admin"

        ``` console
        pip install -U "feloopy[mega]==0.2.8"
        ```

    === ":material-console: User"

        ``` console
        pip install -U "feloopy[mega]==0.2.8" --user
        ```

=== ":material-console: ipykernel"

    ipykernel is a Python kernel for Jupyter notebooks and is used in Jupyter, Google Colab, and Spyder:

    ``` console
    !pip install -U "feloopy[mega]==0.2.8"
    ```


## Insider/developer variants

To contribute to the project, support the developer with pull requests, and get the latest updates, you can install a development variant as follows:

```bash
pip install -U git+https://github.com/ktafakkori/feloopy.git#egg=feloopy[variant_name]
```

or

```bash
git clone https://github.com/ktafakkori/feloopy.git
cd feloopy
pip install .[variant_name]

```

or

```bash
!git clone https://github.com/ktafakkori/feloopy.git
%cd feloopy
!pip install .[variant_name]
```

where variant_name is one of the above variants.
