[![GitHub release](https://img.shields.io/badge/version-0.2.3-orange.svg)](https://github.com/ktafakkori/feloopy/releases)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-310/)
![Package Size](https://img.shields.io/github/languages/code-size/ktafakkori/feloopy)
![Supporters](https://img.shields.io/github/stars/ktafakkori/feloopy)
![Downloads](https://img.shields.io/pypi/dm/feloopy.svg)
[![Total Downloads](https://static.pepy.tech/personalized-badge/feloopy?period=total&units=international_system&left_color=grey&right_color=blue&left_text=downloads)](https://pepy.tech/project/feloopy)
![Release Date](https://img.shields.io/github/release-date/ktafakkori/feloopy.svg)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/ktafakkori/feloopy.svg)](http://isitmaintained.com/project/ktafakkori/feloopy "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/ktafakkori/feloopy.svg)](http://isitmaintained.com/project/ktafakkori/feloopy "Percentage of issues still open")
![GitHub contributors](https://img.shields.io/github/contributors/ktafakkori/feloopy.svg)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

<p align="center">
  <img src="logo/feloopy.gif" 
  width=“80” height=“80”
    />
</p>

# FelooPy: An integrated optimization environment for AutoOR in Python

<div align="center">

_Optimization in Python for **Operations Research** has never been this easy_!

<div align="left">

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisits](#prerequisits)
- [Installation](#installation)
- [Documentation](#documentation)
- [Benchmarks](#benchmarks)
- [How to get started?](https://github.com/ktafakkori/feloopy/blob/main/documentation/Tutorial.md)
- [Examples](https://github.com/ktafakkori/feloopy/tree/main/examples)
- [Contributions](#contributions)
- [Support](#support)
- [Citation](#citation)
- [License](#license)

#

<div align="center">

<div align="left">

## News

🎉 _Version 0.2.3 is out: More stable than ever!_ 🎉

🎉 _The next version would focus on solve facilities_ 🎉

💻 _Quick install_: `pip install --upgrade feloopy`

#

## Introduction

FelooPy (/fɛlupaɪ/, an acronym for feasible, logical, optimal, and Python), is both a hyper-optimization interface and an integrated optimization environment for automated operations research in Python. The name comes from the idea of proposing practical and applicable solutions. The name also emphasizes on feasibility and logicality before optimality. In another view, it emphasizes on the importance of "loops" in programming and algorithm development. Finally, it refers to the memory efficiency, by being similar to the name Floppy, in which the available memory is too low.

Using FelooPy, operations research scientists can: provide their target, representor, or learner model to get results; move focus from coding to modeling, and from modeling to analytics; automate time-consuming, iterative tasks of optimization model development, debugging, and implementation; access to 263 single-objective heuristic and exact optimization algorithms; switch between optimization interfaces and algorithms with no need of code changes; and use tools such as sensitivity analysis, automated encoding and decoding for heuristic optimization, timers, etc.

## Features

Are you tired of wasting time and energy on debugging codes provided by chatbots for optimization in Python? Do you wish there was a better way to create reliable and efficient codes without hassle? Well, now there is! Introducing this new optimization package that does all the hard work for you! You don’t need to learn any new packages or debug any faulty codes. You can just focus on the creative aspects of modeling and analytics!

But wait, there’s more! This optimization package also offers you these amazing features:

- **Free** and **Open-Source** integrated optimization environment developed under **MIT** license.
- **Straightforward** mathematical programming **workflow**.

```python
from feloopy import *
m = model('exact', 'simple_problem', 'cplex')
x = m.pvar('x')
y = m.ivar('y')
m.obj(2*x+5*y)
m.con(5*x+3*y <= 10)
m.con(2*x+7*y <= 9)
m.sol(['max'], 'cplex')
m.report()
m.dis_variable(x,y)
```

- Using **single** optimization programming syntax (simple as above!) for **15** **exact** and **heuristic** optimization interfaces in Python.

<div align="center">

| Solution method | Available interfaces                                                                                                   |
| :-------------- | :--------------------------------------------------------------------------------------------------------------------- |
| exact           | `cplex`, `cvxpy`, `cylp`, `gekko`, `gurobi`, `linopy`, `mip`, `ortools`, `picos`, `pulp`, `pymprog`, `pyomo`, `xpress` |
| heuristic       | `feloopy`, `mealpy`                                                                                                    |
| constraint      | `cplex_cp`, `ortools_cp`                                                                                               |

<div align="left">

- Accessing **86** exact and **177** heuristic optimization algorithms (total: **263**) (see [solvers and interfaces][03]).
- Supporting **scalable** optimization for **large-scale** real-world problems.
- Supporting **benchmarking** with various optimization solvers.
- Supporting **multi-parameter** sensitivity analysis on a single objective.
- Supporting specific **solver options** such as **logs**, **number of threads**, **time limit**, **absolute gap** or **releative gap**.

Try this optimization package today and see its capabilities for yourself!

## Prerequisits

- Knowledge of what interfaces and solvers are (see [interfaces and solvers for optimization in Python][10])
- Knowledge of what operations research can do for you and your business (see [use cases][09]).
- Basic knowledge of optimization techniques.
- Python version `3.10.x`
- Linux-based distributions, Windows or macOS.

[09]: https://ktafakkori.github.io/use-cases-of-operations-research-list/
[10]: https://ktafakkori.github.io/optimization-packages-in-python-list/

## Installation

_Optional downloads_: [Python 3.10][py] | [Visual Studio Code][vs] | [Anaconda][sp]

_Note 1_: Installation process requires `python==3.10.x`, `pip>=22.3.1` and a stable internet connection.

_Note 2:_ Ensure to add Python to PATH during the installation process (usually the first menu).

_Note 3:_ To use FelooPy inside [Google Colab][gc] environment, please first run the following code to configure Python version. Note that this code requires you to choose the desired version during implementation.

```python
!sudo apt-get update -y
!sudo apt-get install python3.10
!sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
!sudo update-alternatives --config python3
!sudo apt install python3-pip
!sudo apt-get install python3.10-distutils
!curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
```

[py]: https://www.python.org/downloads/release/python-3100/
[vs]: https://code.visualstudio.com/
[sp]: https://www.anaconda.com/
[gc]: https://colab.research.google.com/

### Method 1: Terminal command (e.g., CMD or GC):

```text
pip install feloopy==0.2.3
```

### Method 2: IDE command (e.g., Spyder):

_Note_: After installation, this line of code should be deleted.

```text
!pip install feloopy==0.2.3
```

### Method 3: Inside your Python code

_Note_: After installation, this piece of code should be deleted.

```text
import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install','-U', package])
    else:
        pip._internal.main(['install','-U', package])

install('feloopy')
```

### Method 4: From GitHub [Releases][a] section

1. Download the [feloopy-0.2.3.zip][c] file.
2. Extract it into a specific directory.
3. Open a terminal in that directory.
4. Type: `pip install .`

[a]: https://github.com/ktafakkori/feloopy/releases
[b]: https://git-scm.com/downloads
[c]: https://github.com/ktafakkori/feloopy/releases/download/0.2.3/feloopy-0.2.3.zip

### Method 5: From GitHub repository (insiders version)

1. Download and install [git][b].

2. Run this command inside a terminal:

```text
pip install -U git+https://github.com/ktafakkori/feloopy
```

## Documentation

- [Tutorial][01]
- [Syntax][06]
- [Examples][02]
- [Solvers and Interfaces][03]
- [Changelog][05]

[01]: https://github.com/ktafakkori/feloopy/blob/main/documentation/Tutorial.md
[02]: https://github.com/ktafakkori/feloopy/tree/main/examples
[03]: https://github.com/ktafakkori/feloopy/blob/main/documentation/Solvers.md
[05]: https://github.com/ktafakkori/feloopy/blob/main/documentation/Updates.md
[06]: https://github.com/ktafakkori/feloopy/blob/main/documentation/Syntax.md

## Benchmarks

1| Knapsack Problem | Benchmark results for 34 exact optimization interfaces and solvers: Using FelooPy (v0.2.3x) for a 0/1 Knapsack Problem with 1000 items, the following results can be obtained. It is interesting to see that almost all of the interfaces and solvers can handle this optimization problem in less than 1 second. It should be noted that in this case, the knapsack constraint itself is speeding up the solution process! (Why?)

<p align="center">
  <img src="images/benchmark-kp1000.png"
    />
</p>

2| Traveling Salesperson Problem | Benchmark results for 16 exact optimization interfaces and solvers: I used FelooPy (v0.2.3x) to solve the Traveling Salesperson Problem with 50 cities in under a second, using the Miller-Tucker-Zemlin formulation. It seems that the solution time also depends on the interface, not just the solver.

<p align="center">
  <img src="images/benchmark-tsp50.png"
    />
</p>

## Contributions

We welcome your contributions to this project, such as reporting bugs, submitting pull requests, testing changes, and so on. We will acknowledge your contributions in the contributors section.

## Support

If you find this project useful, please consider giving it a star on GitHub (https://github.com/ktafakkori/feloopy) and introducing it to your colleagues to show your appreciation and help us continue its development! Starring a project makes it easier for you to find it again later, and also helps other people discover it. For more ways to support this project, please visit [this page][07].

[07]: https://ktafakkori.github.io/support/

## Citation

It is recommended to cite this GitHub repository or the Python library if you use its facilities in your work:

- APA 7:

```text
Tafakkori, K. (2023). FelooPy: An integrated optimization environment for AutoOR in Python (0.2.3) [Python Library]. https://github.com/ktafakkori/feloopy (Original work published 2023)
```

- LaTeX:

```text
@software{ktafakkori2023Feb,
  author       = {Keivan Tafakkori},
  title        = {{FelooPy: An integrated optimization environment for AutoOR in Python}},
  year         = {2023},
  month        = feb,
  publisher    = {GitHub},
  version      = {v0.2.3},
  url          = {https://github.com/ktafakkori/feloopy/}
}
```

## License

FelooPy is completely free and open-source and licensed under the [MIT][08] license.

[08]: https://github.com/ktafakkori/feloopy/blob/main/LICENSE
