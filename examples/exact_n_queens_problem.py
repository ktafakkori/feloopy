'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-06-21
 # @ Modified: 2023-07-06
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

from feloopy import *

# Credit: https://python-mip.readthedocs.io/en/latest/examples.html

m = target_model('exact', 'n_queens_problem', 'mip')

N = 30
x = m.bvar('x', [N,N])

for i in range(N):
    m.eq(sum(x[i,j] for j in range(N)) == 1)

for j in range(N):
    m.eq(sum(x[i,j] for i in range(N)) == 1)

for k in range(2 - N, N - 2 + 1):
    m.eq(sum(x[i,i-k] for i in range(N) if 0<= i-k< N) <=1)

m.sol('cplex')

m.report()