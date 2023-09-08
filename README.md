### **Introduction**

| FelooPy | [![Version](https://img.shields.io/badge/version-0.2.6-darkgreen.svg)](https://github.com/ktafakkori/feloopy/releases) [![Release Date](https://img.shields.io/github/release-date/ktafakkori/feloopy?color=blue)](https://github.com/ktafakkori/feloopy/releases) [![Downloads](https://static.pepy.tech/badge/feloopy?&left_text=users)](https://pepy.tech/project/feloopy?&left_text=users) [![License](https://img.shields.io/badge/license-MIT-darkred.svg)](https://opensource.org/licenses/MIT) |
| :--- | :--- |
| ![FelooPy Logo](miscellaneous/logo/logo1.png) | **FelooPy** (pronounced /fɛlupaɪ/) is a free and open-source Python library for automated operations research. It serves as both a hyper-optimization interface and an integrated optimization environment. The name "FelooPy" reflects the idea of suggesting practical solutions for various systems, industries, and supply chains. It emphasizes the importance of loops in programming and algorithm development, drawing similarities to the name "Floppy" to highlight memory efficiency. FelooPy helps operations research scientists achieve their goals with a range of models and tools. In simple words, FelooPy is a unified framework for optimization algorithms, decision-making methods, modeling, and analysis. |
| **News** | 🎉 Version 0.2.6 is out: Robustness and Stability! 🎉 |




### **Installation**

FelooPy can be installed on Linux-based distributions, Windows, or macOS. It has a few dependencies that should work on all these platforms.

<div align="left">

<table>
<tr>
<td> Method </td> <td> Description </td> <td> Requirements </td>
</tr>

<tr>
<td> Quick </td>
<td>
    
`pip install --upgrade feloopy`
</td>
<td> Python >= 3.10 </td>
</tr>

<tr>
<td> PyPI </td>
<td>
    
`pip install feloopy==0.2.6`
</td>
<td> Python >= 3.10 </td>
</tr>

<tr>
<td> Command </td>
<td>
    
`!pip install feloopy==0.2.6`
</td>
<td> Python >= 3.10 </td>
</tr>

<tr>
<td> Script </td>
<td>
    
```python
import pip

def install(package):
  if hasattr(pip, 'main'):
    pip.main(['install','-U', package])
  else:
    pip._internal.main(['install','-U', package])

install('feloopy==0.2.6')

````
</td>
<td> Python >= 3.10 </td>
</tr>

<tr>
<td> Local </td>
<td>

1. Download the [feloopy-0.2.6.zip][c] file.
2. Extract it into a specific directory.
3. Open a terminal in that directory.
4. Type: `pip install .`

</td>

<td> Python >= 3.10 </td>

</tr>

<tr>
<td> Colab </td>
<td>

1. Run this cell and reload (CTRL + R) (using `"py310"` or `"py311"`):

```python
!wget https://github.com/korakot/kora/releases/download/v0.10/py310.sh
!bash ./py310.sh -b -f -p /usr/local
!python -m ipykernel install --name "py310" --user
````

2. Run this cell and reload (CTRL + R):

```python
!pip install feloopy==0.2.6
```

</td>

<td> Python >= 3.10 </td>

</tr>

<tr>
<td> Git </td>
<td>
    
`pip install -U git+https://github.com/ktafakkori/feloopy`
</td>

<td> Python >= 3.10 </td>

</tr>

</table>

</div>

FelooPy requires Python 3.10 or later to be installed on your system. If you don't have Python installed, or if you have an older version, you can download it from the official website (https://www.python.org/downloads/) and follow the installation instructions. Alternatively, if you are using Anaconda, you can create a new environment with Python 3.10 or later and install FelooPy in that environment:

```
conda create --name feloopy python=3.10
conda activate feloopy
pip install feloopy
```

FelooPy (v0.2.6) has a few optional dependencies that can be installed using the following commands:

* All solvers: `pip install feloopy[all_solvers]`
* Gurobi: `pip install feloopy[gurobi]`
* Cplex: `pip install feloopy[cplex]`
* Xpress: `pip install feloopy[xpress]`
* Linux: `pip install feloopy[linux]` (better support for multi-objective optimization)

For multi-objective optimization, you should use the linux command for installation. However, please note that the optional dependencies for Linux kernel might not work on some operating systems. As a workaround, you can use a Conda-based Python 3.10 interpreter to ensure that optional dependencies for multi-objective optimization are installed correctly.

### **Features**

FelooPy offers the following key features:

* **Simplest optimization programming language**: Designed to be easy to use, even for those with little or no programming experience.
* **Modeling, solving and analyzing optimization problems**: Provides a complete suite of tools for modeling, solving and analyzing a wide range of optimization problems.
* **Exact optimization algorithms**: Supports *107* exact optimization algorithms that guarantee the optimal solution to your problem.
* **Heuristic optimization algorithms**: Supports *197* heuristic optimization algorithms that can find best possible solutions to complex problems.
* **Convex optimization algorithms**: Supports *20* convex optimization algorithms that ease tensor- and matrix-form modeling, primarily for convex problems.
* **Constraint optimization algorithms**: Supports *2* constraint optimization algorithms that can handle a wide range of complex constraints for operational and time-dependent decisions.
* **Multi-objective optimization algorithms**: Supports *17* multi-objective optimization algorithms, in which objectives might be conflicting or with different numerical units.
* **Multi-critera decision-making methods**: Supports *41* MCDM algorithms to solve decision problems with expert-based inputs without mathematical modeling.
* **Solver configurations**: Lets you configure the solver to meet specific requirements.
* **Auto-encoders for general purpose programming**: Provides auto-encoders to simplify general-purpose programming tasks.
* **Auto-linearizers for linear programming conversions**: Provides auto-linearizers that can handle mixed-integer non-linear programming problems.
* **Auto-logic for modeling special constraints**: Provides auto-logic to help you model and solve problems with special constraints.
* **Auto-sensitivity for analyzing the impact of key parameters**: Provides auto-sensitivity tools to help you analyze the impact of key parameters on your optimization problem.

### **Documentation**

Please refer to https://feloopy.readthedocs.io/en/latest/.

### **Contributions**

We welcome your contributions to this project, such as reporting bugs, submitting pull requests, testing changes, providing examples, and so on.
### **Support FelooPy**

We are committed to continuing the development of FelooPy and would greatly appreciate your support. You can help us by:

* Starring the project on GitHub: Your stars motivate us to keep improving FelooPy. You can star the project here: https://github.com/ktafakkori/feloopy/stargazers

* Forking the project on GitHub: You can also contribute to FelooPy by forking the project here: https://github.com/ktafakkori/feloopy/network/members

* Making a donation: Your donations help to sustain and maintain the project and add new features. If you would like to support us, please visit our website at https://ktafakkori.github.io/support/.

### **Citation**

If you use the facilities of this GitHub repository or the Python library in your work, we recommend citing it to help others reproduce the results of your research. You may also provide the specific version of the Python library used in your research or project for accuracy and reproducibility. Thank you for your consideration.

- APA 7:

```text
Tafakkori, K. (2022). FelooPy: An integrated optimization environment for AutoOR in Python [Python Library]. https://github.com/ktafakkori/feloopy (Original work published September 2022)
```

- LaTeX:

```text
@software{ktafakkori2022Sep,
  author       = {Keivan Tafakkori},
  title        = {{FelooPy: An integrated optimization environment for AutoOR in Python}},
  year         = {2022},
  month        = sep,
  publisher    = {GitHub},
  url          = {https://github.com/ktafakkori/feloopy/}
}
```

[c]: https://github.com/ktafakkori/feloopy/releases
[support]: https://ktafakkori.github.io/support/

### **License**

FelooPy is completely free and open-source and licensed under the [MIT][08] license.

[08]: https://github.com/ktafakkori/feloopy/blob/main/LICENSE

