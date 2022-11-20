from setuptools import setup, find_packages

setup(
    name='feloopy',
    packages=find_packages(include=['feloopy','feloopy.*']),
    version='0.1.11',
    description='FelooPy: An Integrated Optimization Environment (IOE) for AutoOR in Python.',
    author='Keivan Tafakkori',
    author_email='k.tafakkori@gmail.com',
    url = 'https://github.com/ktafakkori/feloopy',
    keywords = ['optimization', 'machine_learning', 'simulation', 'operations_research', 'computer_science', 'data_science'],
    license='MIT',
    install_requires=[
    #dependencies
    'tabulate',
    'numpy',
    'matplotlib',
    'infix',
    'func-timeout',
    'pandas',
    'openpyxl',

    #Interfaces & solvers
    'gekko',
    'ortools',
    'pulp',
    'pyomo',
    'pymprog',
    'picos',
    'optlang',
    'cplex',
    'docplex',
    'gurobipy',
    'xpress',
    'linopy',
    'cvxpy',
    'cylp',
    'mip',
    'ga',
    ]
)

    