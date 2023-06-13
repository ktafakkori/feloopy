'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

from setuptools import setup, find_packages

common = ['tabulate', 'numpy', 'matplotlib',
          'infix', 'pandas', 'openpyxl', 'numba', 'plotly']
interfaces = ['gekko', 'ortools', 'pulp', 'pyomo', 'pymprog',
              'picos', 'linopy', 'cvxpy', 'cylp<=0.91.5', 'mip', 'mealpy', 'pyDecision','rsome', 'pymoo']
solvers = ['cplex', 'docplex', 'xpress', 'gurobipy']

setup(
    name='feloopy',
    version='0.2.6',
    description='FelooPy: An integrated optimization environment for automated operations research in Python.',
    packages=find_packages(include=['feloopy', 'feloopy.*']),
    long_description=open('README.md', encoding="utf8").read(),
    long_description_content_type='text/markdown',
    keywords=['optimization', 'machine learning', 'simulation', 'operations research', 'computer science',
              'data science', 'management science', 'industrial engineering', 'supply chain', 'operations management'],
    author='Keivan Tafakkori',
    author_email='k.tafakkori@gmail.com',
    maintainer='Keivan Tafakkori',
    maintainer_email='k.tafakkori@gmail.com',
    url='https://github.com/ktafakkori/feloopy',
    download_url='https://github.com/ktafakkori/feloopy/releases',
    license='MIT',
    python_requires='>=3.10',
    extras_require={'all_solvers': solvers,
                     'gurobi': [solvers[3]],
                    'cplex': [solvers[0], solvers[1]],
                    'xpress': [solvers[2]],
                    'linux': ['pymultiobjective']},
    install_requires=[common+interfaces],
)
