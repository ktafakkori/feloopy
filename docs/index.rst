Welcome to FelooPy's documentation!
=======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

##############################
**Introduction**
##############################

.. list-table::
   :header-rows: 1

   * - FelooPy
     - |image:: miscellaneous/logo/logo1.png
       | FelooPy (pronounced /fɛlupaɪ/) is a free and open-source Python library for automated operations research that serves as both a hyper-optimization interface and an integrated optimization environment. The name comes from the idea of suggesting practical and applicable solutions for systems, industries, and supply chains, and it also references the importance of loops in programming and algorithm development, and draws similarities to the name "Floppy" to highlight memory efficiency. FelooPy helps operations research scientists achieve their goals using various target, representor, and learner models. In simple words, FelooPy is a unified framework for optimization algorithms, decision-making methods, and modeling and analytical tools.
   * - News
     - 🎉 *Version 0.2.5 is out: Added new features!* 🎉

##############################
**Installation**
##############################

FelooPy can be installed on Linux-based distributions, Windows, or macOS. It has a few dependencies that should work on all these platforms.

.. list-table::
   :header-rows: 1

   * - Method
     - Description
     - Requirements
   * - Quick
     - ``pip install --upgrade feloopy``
     - Python >= 3.10
   * - PyPI
     - ``pip install feloopy==0.2.5``
     - Python >= 3.10

.. note::

   FelooPy requires Python 3.10 or later to be installed on your system. If you don't have Python installed, or if you have an older version, you can download it from the official website (https://www.python.org/downloads/) and follow the installation instructions. Alternatively, if you are using Anaconda, you can create a new environment with Python 3.10 or later and install FelooPy in that environment:

   .. code-block:: bash

      conda create --name feloopy python=3.10
      conda activate feloopy
      pip install feloopy

   FelooPy (v0.2.5) has a few optional dependencies that can be installed using the following commands:

   * All solvers: ``pip install feloopy[all_solvers]``
   * Gurobi: ``pip install feloopy[gurobi]``
   * Cplex: ``pip install feloopy[cplex]``
   * Xpress: ``pip install feloopy[xpress]``
   * Linux: ``pip install feloopy[linux]`` (better support for multi-objective optimization)

   For multi-objective optimization, you should use the linux command for installation. However, please note that the optional dependencies for Linux kernel might not work on some operating systems. As a workaround, you can use a Conda-based Python 3.10 interpreter to ensure that optional dependencies for multi-objective optimization are installed correctly.

##############################
**Features**
##############################

FelooPy offers the following key features:

* **Simplest optimization programming language**: Designed to be easy to use, even for those with little or no programming experience.
* **Modeling, solving and analyzing optimization problems**: Provides a complete suite of tools for modeling, solving and analyzing a wide range of optimization problems.

.. note::

   Please refer to https://feloopy.readthedocs.io/en/latest/ for the complete list of features.

##############################
**Documentation**
##############################

Please refer to https://feloopy.readthedocs.io/en/latest/.

##############################
**Contributions**
##############################

We welcome your contributions to this project, such as reporting bugs, submitting pull requests, testing changes, providing examples, and so on.

##############################
**Support FelooPy**
##############################

We are committed to continuing the development of FelooPy and would greatly appreciate your support. You can help us by:

* Starring the project on GitHub: Your stars motivate us to keep improving FelooPy. You can star the project here: https://github.com/ktafakkori/feloopy/stargazers

* Forking the project on GitHub: You can also contribute to FelooPy by forking the project here: https://github.com/ktafakkori/feloopy/network/members

* Making a donation: Your donations help to sustain and maintain the project and add new features. If you would like to support us, please visit our website at https://ktafakkori.github.io/support/.

##############################
**Citation**
##############################

If you use FelooPy in your research or project, please consider citing it as follows:

```bibtex
@software{ktafakkori2022Sep,
  author       = {Keivan Tafakkori},
  title        = {{FelooPy: An integrated optimization environment for AutoOR in Python}},
  year         = {2022},
  month        = sep,
  publisher    = {GitHub},
  url          = {https://github.com/ktafakkori/feloopy/}
}
```
This will help others discover and make use of FelooPy, and it will also give credit to its contributors and maintainers.

##############################
License
##############################

FelooPy is released under the MIT License. Read the LICENSE file for more information.