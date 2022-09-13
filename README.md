![](https://img.shields.io/github/stars/ktafakkori/feloopy?style=social)
![](https://img.shields.io/github/languages/code-size/ktafakkori/feloopy?style=social)
![](https://hitcounter.pythonanywhere.com/count/tag.svg?url=https://github.com/ktafakkori/feloopy/)

# FelooPy

![](images/feloopy.png)

An integrated optimization environment (IOE) for AutoOR!

## 🐍Introduction

Feloopy (FEasible, LOgical & OPtimal + Python) is a hyper-optimization interface that allows operations research scientists to build, develop, and test optimization models with almost all open-source and commercial solvers available for optimization in Python. With FelooPy, the users would be able to benchmark the solvers to see if they meet the requirements.

Motivated by the AutoML era, which is "the process of automating the time-consuming, iterative tasks of machine learning model development," FelooPy is the first package that is going to provide an AutoOR tool for automating the time-consuming tasks of modeling, implementing, and analyzing an optimization model by providing an integrated (exact and heuristic) optimization environment in Python. Accordingly, FelooPy would also support multiple features such as sensitivity analysis, visualization, and more!

⚠️ Please note that the FelooPy project is in its infancy. Therefore, the package is not very stable. However, the interested users can still use the popular optimization interfaces such as `ortools,` `pulp,` `pyomo` and `gekko` through it!

License: MIT

## 🔝 Advantages:

- An integrated optimization environment.
- Automating operation research model development workflow.
- Straightforward syntax for optimization modeling.
- Using only one syntax for coding.
- Having access to multiple optimization interfaces all at once.
- Using almost all solvers available.
- Getting execution time of your optimization model.
- (Upcoming) possibility for sensitivity analysis.
- (Upcoming) possibility for benchmarking all optimizers for your_model.
- (Scope) possibility for heuristic optimization with the same syntax.
- ...

## ⬇️ Installation

There are multiple ways to install this Python package:

- Using the command `pip install feloopy` in a terminal.
- Using the command `!pip install feloopy` at the top of your code and implementing it for once.
- Using the following piece of code:

```python
import os
os.system("pip install feloopy")
```

- Using the following function:

```python
import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

install('feloopy')
```

## 📄 Documentation

Still, no documentation is provided.

## 👤 Usage

Some examples are provided as follows:

### Solving a simple MILP with FelooPy by Pyomo:

```python
import feloopy.interfaces.pyomo_int as pyomo

m = pyomo.iterface(direction="max")
x = m.pvar('x')
y = m.ivar('y')

m.obj(2*x+5*y)
m.con(5*x+3*y <= 10)
m.con(2*x+7*y <= 9)

m.solve('glpk')
m.display(x, y)
```

Results:

```
Pyomo solved 'your_model' with glpk solver | CPT= 411416.3999984157 (μs) 00:00:00 (h:m:s)
x: 1.0
y: 1.0
obj: 7.0
```

### Solving a simple MILP with FelooPy by Gekko:

```python
import feloopy.interfaces.gekko_int as gekko

m = gekko.interface(direction="max")
x = m.pvar('x')
y = m.ivar('y')

m.obj(2*x+5*y)
m.con(5*x+3*y <= 10)
m.con(2*x+7*y <= 9)

m.solve('apopt')
m.display(x, y)
```

Results:

```
Gekko solved 'your_model' with apopt solver | CPT= 505112.3000012012 (μs) 00:00:00 (h:m:s)
v1: [1.0]
int_v2: [1.0]
obj: 7.0
```

### Solving a simple MILP with FelooPy by Ortools:

```python
import feloopy.interfaces.ortools_int as ortools

m = ortools.interface(direction="max")
x = m.pvar('x')
y = m.ivar('y')

m.obj(2*x+5*y)
m.con(5*x+3*y <= 10)
m.con(2*x+7*y <= 9)

m.solve('glpk')
m.display(x, y)
```

Results:

```
ORTOOLs solved 'your_model' with glpk solver | CPT= 3619.700000854209 (μs) 00:00:00 (h:m:s)
x: 1.0
y: 1.0
obj: 7.0
```

### Solving a simple MILP with FelooPy by PuLP:

```python
import feloopy.feloopy.interfaces.pulp_int as pulp

m = pulp.interface(direction="max")
x = m.pvar('x')
y = m.ivar('y')

m.obj(2*x+5*y)
m.con(5*x+3*y <= 10)
m.con(2*x+7*y <= 9)

m.solve('glpk')
m.display(x, y)
```

Results:

```
PuLP solved 'your_model' with <pulp.apis.glpk_api.GLPK_CMD object at 0x000001DDC0021750> solver | CPT= 1706935.9999986773 (μs) 00:00:01 (h:m:s)
x: 1.0
y: 1
obj: 7.0
```

## 🆘 Contributions

Are welcome :)

## 🎛️ Current contributors

![Contributors](https://contrib.rocks/image?repo=ktafakkori/feloopy)

## ⚡Support

This repository will be more and more complete over time.

Hence, it is kindly requested to support this work by giving a ⭐ to the repository to make it available for a broad range of audiences who are interested in using heuristic optimization techniques in the Python programming language.

## 💫 Supporters

[![Stars given](https://reporoster.com/stars/dark/ktafakkori/feloopy)](https://github.com/ktafakkori/feloopy/stargazers)

## ❤️ Sponsorship

Contact me on [Twitter][1], or on [Linkedin][2].

[1]: https://twitter.com/ktafakkori
[2]: https://www.linkedin.com/in/keivan-tafakkori/
