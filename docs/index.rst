Welcome to FelooPy's Documentation
==================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   exact
   heuristic
   convex
   constraint
   multiobjective
   multicriteria
   uncertain

Introduction
============

FelooPy
-------

Welcome to FelooPy (pronounced /fɛlupaɪ/), a free and open-source Python library designed for automated operations research. FelooPy serves as a comprehensive hyper-optimization interface and a fully integrated optimization environment.

The name 'FelooPy' encapsulates our mission: to provide practical and applicable solutions for systems, industries, and supply chains. It echoes the importance of 'loops' in programming and algorithm development, drawing a playful parallel with the word 'Floppy' to highlight memory efficiency.

FelooPy is a powerful tool for operations research scientists. It combines various target, representor, and learner models with a unified framework of optimization algorithms, decision-making methods, and modeling and analytical tools. Simply put, FelooPy is your one-stop solution for all things optimization.

Latest News
===========

🎉 *Exciting Update: FelooPy Version 0.2.6 is now available!* 🎉

We are thrilled to announce the release of FelooPy Version 0.2.6. This update brings stability and robustness!

Features
========

FelooPy offers the following key features:

* 📘 Simplest optimization programming language: Designed for easy use.
* 🔧 Comprehensive toolkit: For modeling, solving, and analyzing optimization problems.
* 🎯 Extensive support for optimization algorithms: Including exact (107), heuristic (198), convex (20), constraint (2), and multi-objective (17).
* 🧮 Multi-criteria decision-making methods: Supporting 41 MCDM algorithms.
* ⚙️ Customizable solver configurations: For specific requirements.
* 🔄 General-purpose programming made easy: With auto-encoders.
* 📐 Handles mixed-integer non-linear programming problems: With auto-linearizers.
* 📏 Special constraints modeling: Supported by auto-logic.
* 📊 Key parameters impact analysis: Provided by auto-sensitivity.

Installation
============

FelooPy is compatible with Linux-based distributions, Windows, and macOS.

Quick Installation
------------------

Install the latest version with pip:

.. code-block:: bash

   pip install --upgrade feloopy

Specific Version Installation
-----------------------------

Install a specific version from PyPI:

.. code-block:: bash

   pip install feloopy==0.2.6

Script Installation
-------------------

Use a Python script for installation:

.. code-block:: python

   import pip

   def install(package):
     if hasattr(pip, 'main'):
       pip.main(['install','-U', package])
     else:
       pip._internal.main(['install','-U', package])

   install('feloopy==0.2.6')

Local Installation
------------------

Install from a local zip file:

1. Download the `feloopy-0.2.6.zip`_.
2. Extract to a directory.
3. Install from terminal in that directory:

.. code-block:: bash

   pip install .

Colab Installation
------------------

Install in a Colab environment:

1. Prepare the environment:

.. code-block:: bash

   !wget https://github.com/korakot/kora/releases/download/v0.10/py310.sh
   !bash ./py310.sh -b -f -p /usr/local
   !python -m ipykernel install --name "py310" --user

2. Install FelooPy:

.. code-block:: bash

   !pip install feloopy==0.2.6

Git Installation
----------------

Install directly from GitHub:

.. code-block:: bash

   pip install -U git+https://github.com/ktafakkori/feloopy

.. _feloopy-0.2.6.zip: https://example.com/feloopy-0.2.6.zip

Contributions
=============

Your contributions are welcome! This includes bug reporting, pull requests submission, changes testing, and examples providing.

Support FelooPy
===============

Support us in the following ways:

* ⭐ Give us a star on `GitHub <https://github.com/ktafakkori/feloopy/stargazers>`_.
* 🍴 Fork the project on `GitHub <https://github.com/ktafakkori/feloopy/network/members>`_.
* 💰 Make a donation on our `support page <https://ktafakkori.github.io/support/>`_.

Citation
========

Please cite FelooPy in your research or project:

.. code-block:: bibtex

   @software{ktafakkori2022Sep,
     author       = {Keivan Tafakkori},
     title        = {{FelooPy: An integrated optimization environment for AutoOR in Python}},
     year         = {2022},
     month        = sep,
     publisher    = {GitHub},
     url          = {https://github.com/ktafakkori/feloopy/}
   }

License
=======

FelooPy is released under the [MIT License](https://github.com/ktafakkori/feloopy/blob/main/LICENSE).




