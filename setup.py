from setuptools import setup, find_packages

setup(
    name='feloopy',
    packages=find_packages(include=['feloopy','feloopy.*']),
    version='0.1',
    description='FelooPy: An Integrated Optimization Environment',
    author='Keivan Tafakkori',
    author_email='k.tafakkori@gmail.com',
    url = 'https://github.com/ktafakkori/feloopy',
    keywords = ['optimization', 'machine_learning', 'simulation'],
    license='MIT',
    install_requires=['pyomo','pulp','gekko','ortools'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)