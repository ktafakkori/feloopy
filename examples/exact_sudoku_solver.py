'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-06-20
 # @ Modified: 2023-07-06
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

from feloopy import *

m = target_model('exact', 'sudoku solver', 'gurobi')

puzzle = np.array([[5, 3, 0, 0, 7, 0, 0, 0, 2],
                   [6, 0, 0, 1, 9, 5, 0, 0, 0],
                   [0, 9, 8, 0, 0, 0, 0, 6, 0],
                   [8, 0, 0, 0, 6, 0, 0, 0, 3],
                   [4, 0, 0, 8, 0, 3, 0, 0, 1],
                   [7, 0, 0, 0, 2, 0, 0, 0, 6],
                   [0, 6, 0, 0, 0, 0, 2, 8, 0],
                   [0, 0, 0, 4, 1, 9, 0, 0, 5],
                   [0, 0, 0, 0, 8, 0, 0, 7, 9]])

x = m.btvar('x', [9, 9, 9])

m.obj(0)

for i in range(3):
    m.con(x.sum(axis=i) == 1)

i, j = np.where(puzzle)
m.con(x[i, j, puzzle[i, j]-1] == 1)

for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        m.con(x[i: i+3, j: j+3, :].sum(axis=(0, 1)) == 1)

m.sol(['max'], 'gurobi')

m.report()