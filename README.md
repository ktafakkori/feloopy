
[![GitHub release](https://img.shields.io/badge/version-0.2.0-orange.svg)](https://github.com/ktafakkori/feloopy/releases)
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
    />
</p>

# FelooPy: An integrated optimization environment for AutoOR in Python

FelooPy (/fɛlupaɪ/, an abbreviation for feasible, logical, optimal, and Python) is a hyper-optimization interface and an integrated optimization environment (IOE) that provides an all-in-one exact and heuristic optimization tool for AutoOR in Python. The motivation behind the development of FelooPy is to move the focus of operations research scientists from coding to modeling, and from modeling to analysis/analytics to automate time-consuming, iterative tasks of optimization model development, debugging, and implementation. FelooPy can currently give you access to more than 172 single-objective heuristic optimization solvers (thanks to `mealpy` interface) and 82 single-objective commercial and open-source exact optimization solvers  (thanks to `pyomo`,`pulp`,`ortools`, `gekko`, `cplex`, `gurobi`, `xpress`, `picos`, `pymprog`, `cvxpy`, `cylp`, `linopy`, and `mip` interfaces), all with the same coding syntax! This means that switching from one solver to the other one is not costly. Besides, FelooPy automates common tasks in the optimization process and analytics, by providing tools such as sensitivity analysis, automated encoding/decoding (representation method) for heuristic optimization, timers, and more, all in the Python programming language environment.


## Features

- **Free** and **Open-Source** integrated optimization environment developed under **MIT** license.
- **Straightforward** mathematical programming **workflow**.
- Using **single** optimization programming syntax for **14** **exact** and **heuristic** optimization interfaces in Python.
- Accessing **82** exact and **172+5** heuristic optimization solvers (total: **259** optimization algorithms).
- Supporting **scalable** optimization for **large-scale** real-world problems.
- Supporting **benchmarking** with various optimization solvers.
- Supporting **multi-parameter** sensitivity analysis on a single objective.
- Supporting **multi-criteria** and **multi-objective** optimization (coming soon).
- ...

## Installation

*Note 1*: Installation process requires `python==3.10.x`, `pip>=22.3.1` and a stable internet connection.

*Note 2:* Ensure to add Python to PATH during the installation process (usually the first menu).

- *Downloads*: [Python 3.10][py], ([Visual Studio Code][vs] or [Anaconda][sp])
- *Cloud*: [Google Colab][gc]

[py]: https://www.python.org/downloads/release/python-3100/
[vs]: https://code.visualstudio.com/
[sp]: https://www.anaconda.com/
[gc]: https://colab.research.google.com/

### Method 1: Terminal command (e.g., CMD or GC):

```text
pip install feloopy==0.2.0
```

### Method 2: IDE command (e.g., Spyder):

*Note*: After installation, this line of code should be deleted.

```text
!pip install feloopy==0.2.0
```

### Method 3: Inside your Python code

*Note*: After installation, this piece of code should be deleted.

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

1. Download the [feloopy-0.2.0.zip][c] file.
2. Extract it into a specific directory.
3. Open a terminal in that directory.
4. Type: `pip install .`

[a]: https://github.com/ktafakkori/feloopy/releases
[b]: https://git-scm.com/downloads
[c]: https://github.com/ktafakkori/feloopy/releases/download/0.2.0/feloopy-0.2.0.zip

### Method 5: From GitHub repository (insiders version)

1. Download and install [git][b].

2. Run this command inside a terminal:

```text
pip install -U git+https://github.com/ktafakkori/feloopy
```

## Documentation

* [Tutorial][01]
* [Examples][02]
* [Exact Solvers][03]
* [Heuristic Solvers][04]
* [Changelog][05]

[01]: https://github.com/ktafakkori/feloopy/blob/main/documentation/Tutorial.md
[02]: https://github.com/ktafakkori/feloopy/tree/main/examples
[03]: https://github.com/ktafakkori/feloopy/blob/main/documentation/Exact_List.md
[04]: https://github.com/ktafakkori/feloopy/blob/main/documentation/Heuristic_List.md
[05]: https://github.com/ktafakkori/feloopy/blob/main/documentation/Updates.md

## Citation

```text
@software{ktafakkori2022Dec,
  author       = {Keivan Tafakkori},
  title        = {{FelooPy: An integrated optimization environment for AutoOR in Python}},
  year         = {2022},
  month        = dec,
  publisher    = {GitHub},
  version      = {v0.2.0},
  url          = {https://github.com/ktafakkori/feloopy/}
}
```
