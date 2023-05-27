### **Introduction**

| FelooPy                                            | [![version code](https://img.shields.io/badge/version-0.2.5-darkgreen.svg)](https://github.com/ktafakkori/feloopy/releases) [![number of users](https://static.pepy.tech/personalized-badge/feloopy?period=total&units=international_system&left_color=grey&right_color=darkgreen&left_text=users)](https://pepy.tech/project/feloopy) ![release date](https://img.shields.io/github/release-date/ktafakkori/feloopy?color=blue) [![monthly Downloads](https://static.pepy.tech/personalized-badge/feloopy?period=month&units=international_system&left_color=grey&right_color=blue&left_text=monthly%20downloads%20)](https://pepy.tech/project/feloopy) [![license type](https://img.shields.io/badge/license-MIT-darkred.svg)](https://opensource.org/licenses/MIT) |
| :------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Image description](miscellaneous/logo/logo1.png) | FelooPy (pronounced /fɛlupaɪ/) is a free and open-source Python library for automated operations research. It serves as both a hyper-optimization interface and an integrated optimization environment. The name comes from the idea of suggesting practical and applicable solutions for systems, industries, and supply chains. It also references the importance of loops in programming and algorithm development, and draws similarities to the name "Floppy" to highlight memory efficiency. FelooPy helps operations research scientists achieve their goals using various target, representor, and learner models, shifting their focus from coding to modeling and analytics.                                                                                 |
| News                                               | 🎉 _Version 0.2.5 is Out: New Feature Release!_ 🎉                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

### **Installation**

FelooPy can be installed on Linux-based distributions, Windows, or macOS. It has a few dependencies that should work on all these platforms.

<div align="center">

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
    
`pip install feloopy==0.2.5`
</td>
<td> Python >= 3.10 </td>
</tr>

<tr>
<td> Command </td>
<td>
    
`!pip install feloopy==0.2.5`
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

install('feloopy')

````
</td>
<td> Python >= 3.10 </td>
</tr>

<tr>
<td> Local </td>
<td>

1. Download the [feloopy-0.2.5.zip][c] file.
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
!pip install feloopy==0.2.5
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

FelooPy (v0.2.5) has a few optional dependencies that can be installed using the following commands:

* All solvers: `pip install feloopy[all_solvers]`
* Gurobi: `pip install feloopy[gurobi]`
* CPLEX: `pip install feloopy[cplex]`
* XPRESS: `pip install feloopy[xpress]`
* Linux: `pip install feloopy[linux]` (for multi-objective optimization)

For multi-objective optimization, you should use the linux command for installation. However, please note that the optional dependencies for Linux might not work on other operating systems. As a workaround, you can use a Conda-based Python 3.10 interpreter to ensure that optional dependencies for multi-objective optimization are installed correctly.

### **Features**

- Simplest universal optimization programming language based on Python for exact, heuristic, and constraint optimization.
- Supporting 17 exact, constraint, and heuristic optimization interfaces and solvers, just by changing two parameters, `<interface>` and `<solver>`, in the above examples. Please see the [appendix](#appendix).
- Supporting benchmarking with various interfaces and solvers.
- Supporting multi-parameter sensitivity analysis on a single objective.
- Supporting solve options such as logs, number of threads, time limit, absolute gap or releative gap.


### **Supporters**

If you find this project useful, please consider giving it a star on GitHub (https://github.com/ktafakkori/feloopy) and introducing it to your colleagues to show your appreciation and help us continue its development! Starring a project makes it easier for you to find it again later, and also helps other people discover it. For more ways to support this project, please visit [this page][support].

- Stars:

[![Stars](https://reporoster.com/stars/notext/ktafakkori/feloopy)](https://github.com/ktafakkori/feloopy/stargazers)

- Forks:

[![Forks](https://reporoster.com/forks/notext/ktafakkori/feloopy)](https://github.com/ktafakkori/feloopy/network/members)

### **Contributions**

We welcome your contributions to this project, such as reporting bugs, submitting pull requests, testing changes, providing examples, and so on. We will acknowledge your contributions in the contributors section.

### **Citation**

It is recommended to cite this GitHub repository or the Python library if you use its facilities in your work, as it helps others reproduce the results of your research. You may also provide the specific version of this Python library that you used in your research or project.

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