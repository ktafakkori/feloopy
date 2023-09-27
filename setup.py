'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.7)                               |
|  Modified: Wednesday, 27th September 2023 08:05:25 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''

from setuptools import setup, find_packages

common = ['tabulate', 'numpy', 'matplotlib', 'infix', 'pandas', 'openpyxl', 'numba', 'plotly', 'psutil', 'py-cpuinfo', 'win-unicode-console', 'xlsxwriter', 'gputil']
interfaces = ['gekko', 'ortools', 'pulp', 'pyomo', 'pymprog', 'picos', 'linopy', 'cvxpy', 'mip', 'mealpy', 'pydecision','rsome', 'pymoo']
solvers = ['cplex', 'docplex', 'xpress', 'gurobipy','cylp', 'coptpy']

setup(
    name='feloopy',
    version='0.2.7',
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
                    'copt': [solvers[5]],
                    'cylp': [solvers[4]],
                    'linux': ['pymultiobjective']},
    install_requires=[common+interfaces],
)