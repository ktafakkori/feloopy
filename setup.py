# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

from setuptools import setup, find_packages

# Common packages for all versions of FelooPy

common = [
    'gputil',
    'infix', 
    'matplotlib', 
    'numba', 
    'numpy', 
    'openpyxl', 
    'pandas', 
    'plotly', 
    'psutil', 
    'py-cpuinfo', 
    'tabulate', 
    'win-unicode-console', 
    'scikit-learn',
    'polars',
    'xlsxwriter', 
]

# Interfaces for optimization solvers or algorithms

pico = [

]

nano = pico + [
    'pymprog'
]

micro = nano + [
    'gekko',
    'mealpy'
]

mini = micro + [
    'ortools',
    'cvxpy'
]

full = mini + [
    'pymoo',
    'pydecision'
]

stock = full + [
    'pulp',
    'pyomo',
    'picos',
    'linopy',
    'mip',
    'rsome',
    'niapy',
    'pygad'
]

# Solvers for optimization problems or algorithms

plus_gurobi = [
    'gurobipy'
]

plus_cplex = [
    'cplex',
    'docplex'
]

plus_xpress = [
    'xpress'
]

plus_copt = [
    'coptpy'
]

hyper = stock + plus_gurobi + plus_cplex + plus_xpress + plus_copt

# Might have some os-dependent issues

only_cylp = [
    'cylp'
]

only_linux = [
    'pymultiobjective'
]

mega = hyper + only_cylp + only_linux

extra_dict = {
    'pico': pico,
    'nano': nano,
    'micro': micro, 
    'mini': mini, 
    'full': full, 
    'stock': stock,
    'hyper': hyper,
    'plus_gurobi': plus_gurobi,
    'plus_cplex': plus_cplex,
    'plus_xpress': plus_xpress,
    'plus_copt': plus_copt,
    'only_cylp': only_cylp,
    'only_linux': only_linux,
    'mega': mega}

keywords_list = [
    'optimization',
    'machine learning', 
    'simulation', 
    'operations research', 
    'computer science',
    'data science', 
    'management science', 
    'industrial engineering', 
    'supply chain', 
    'operations management',
    'mathematical modeling',
    'decision making'
    ]

def install_feloopy():
    """
    -> Installs the Feloopy package and returns None. 
    """
    setup(
        name = 'feloopy',
        version = '0.2.8',
        description = 'FelooPy: An integrated optimization environment (IOE) for automated operations research (AutoOR) in Python.',
        packages = find_packages(include=['feloopy', 'feloopy.*']),
        long_description = open('./docs/README.md', encoding="utf8").read(),
        long_description_content_type = 'text/markdown',
        keywords = keywords_list,
        author='Keivan Tafakkori',
        author_email='k.tafakkori@gmail.com',
        maintainer='Keivan Tafakkori',
        maintainer_email='k.tafakkori@gmail.com',
        url='https://github.com/ktafakkori/feloopy',
        download_url='https://github.com/ktafakkori/feloopy/releases',
        license='MIT',
        python_requires='>=3.10',
        extras_require=extra_dict,
        install_requires=[common],
    )

if __name__ == '__main__':

    install_feloopy()
