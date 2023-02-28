
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
    />
</p>

# FelooPy: An integrated optimization environment for AutoOR in Python

*Version 0.2.3 is out! More stable than ever*!

FelooPy (/fɛlupaɪ/, an acronym for feasible, logical, optimal, and Python), is both a hyper-optimization interface and an integrated optimization environment for automated operations research in Python. 

Using FelooPy, operations research scientists can: provide their target, representor, or learner model to get results; move focus from coding to modeling, and from modeling to analytics; automate time-consuming, iterative tasks of optimization model development, debugging, and implementation; access to 259 single-objective heuristic and exact optimization algorithms; switch between optimization interfaces and algorithms with no need of code changes; and use tools such as sensitivity analysis, automated encoding and decoding for heuristic optimization, timers, etc.

## Specific features

- **Free** and **Open-Source** integrated optimization environment developed under **MIT** license.
- **Straightforward** mathematical programming **workflow**.
- Using **single** optimization programming syntax for **15** **exact** and **heuristic** optimization interfaces in Python.
- Accessing **82** exact and **177** heuristic optimization algorithms (total: **259**).
- Supporting **scalable** optimization for **large-scale** real-world problems.
- Supporting **benchmarking** with various optimization solvers.
- Supporting **multi-parameter** sensitivity analysis on a single objective.
- Supporting specific **solver options** such as **logging**, **number of threads**, **absolute gap** or **releative gap**.

## Supported optimization interfaces

### Exact optimization:

- cplex
- cvxpy
- cylp
- gekko
- gurobi
- linopy
- mip
- ortools
- picos
- pulp
- pymprog
- pyomo
- xpress
  
### Heuristic optimization:

- feloopy
- mealpy

## Installation

*Optional downloads*: [Python 3.10][py], ([Visual Studio Code][vs] or [Anaconda][sp])

*Note 1*: Installation process requires `python==3.10.x`, `pip>=22.3.1` and a stable internet connection.

*Note 2:* Ensure to add Python to PATH during the installation process (usually the first menu).

*Note 3:* To use FelooPy inside [Google Colab][gc] environment, please first run the following code to configure Python version. Note that this code requires you to choose the desired version during implementation.

```python
!sudo apt-get update -y
!sudo apt-get install python3.10
!sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
!sudo update-alternatives --config python3
!sudo apt install python3-pip
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

*Note*: After installation, this line of code should be deleted.

```text
!pip install feloopy==0.2.3
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

* APA 7:

```text
Tafakkori, K. (2023). Feloopy: An integrated optimization environment for AutoOR in Python (0.2.3) [Python]. https://github.com/ktafakkori/feloopy (Original work published 2023)
```
  
* LaTeX:
  
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
