from setuptools import setup, find_packages

setup(

    name='feloopy',
    
    version='0.2.4',

    description='FelooPy: An Integrated Optimization Environment (IOE) for Automated operations research (AutoOR) in Python.',

    long_description=open('README.md', encoding="utf8").read(),

    long_description_content_type='text/markdown',

    keywords=['Optimization', 'Machine_Learning', 'Simulation', 'Operations_Research', 'Computer_Science', 'Data_Science'],

    author='Keivan Tafakkori',

    author_email='k.tafakkori@gmail.com',

    maintainer='Keivan Tafakkori',

    maintainer_email='k.tafakkori@gmail.com',

    url='https://github.com/ktafakkori/feloopy',

    download_url='https://github.com/ktafakkori/feloopy/releases',

    packages=find_packages(include=['feloopy', 'feloopy.*']),

    license='MIT',

    python_requires='>=3.10',

    install_requires=[
    
        'tabulate',

        'numpy',

        'matplotlib',

        'infix',

        'pandas',

        'openpyxl',

        'gekko',

        'ortools',

        'pulp',

        'pyomo',

        'pymprog',

        'plotly',

        'picos',

        'cplex',

        'docplex',

        'gurobipy',

        'xpress',

        'linopy',

        'cvxpy',

        'cylp',

        'mip',

        'mealpy',
    ],
)