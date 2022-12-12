from setuptools import setup, find_packages

setup(

    name='feloopy',

    version='0.2.0',

    description='FelooPy: An Integrated Optimization Environment (IOE) for AutoOR in Python.',

    long_description =open('README.md', encoding="utf8").read(),

    long_description_content_type='text/markdown',

    keywords = ['Optimization', 'Machine_Learning', 'Simulation', 'Operations_Research', 'Computer_Science', 'Data_Science'],

    author='Keivan Tafakkori',

    author_email='k.tafakkori@gmail.com',

    maintainer='Keivan Tafakkori',

    maintainer_email='k.tafakkori@gmail.com',

    url = 'https://github.com/ktafakkori/feloopy',

    download_url= 'https://github.com/ktafakkori/feloopy/releases',

    packages=find_packages(include=['feloopy','feloopy.*']),

    license='MIT',

    python_requires = '>=3.9',
    
    install_requires=[

    'tabulate',

    'numpy',

    'matplotlib',

    'infix',

    'pandas',

    'openpyxl', 

    'gekko>=1.0.5',

    'ortools>=9.4.1874',

    'pulp>=2.7.0',

    'pyomo>=6.4.4',

    'pymprog>=1.1.2',

    'picos>=2.4.11',

    'cplex>=22.1.0.0',

    'docplex>=2.23.222',

    'gurobipy>=10.0.0',

    'xpress>=8.14.2',

    'linopy>=0.0.14',

    'cvxpy>=1.2.1',

    'cylp>=0.91.5',

    'mip>=1.14.1',

    'mealpy>=2.5.1',
    ],
)

    