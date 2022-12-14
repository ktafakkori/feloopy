from feloopy import *


def roll(n, d):
    l = [0, 1, 2, 3, 4, 5, 6]
    if n < d:
        x = l[:n+1] + l[n+(len(l)-d+1):]
    else:
        x = l[n-(d-1):n+1]
    return x


# Environemnt
m = model('exact', 'ws', 'pulp')

# Data
Data = {
    'Mon': 17,
    'Tue': 13,
    'Wed': 15,
    'Thu': 19,
    'Fri': 14,
    'Sat': 16,
    'Sun': 11
}

RD = 5  # Rolling horizon

# Sets
I = range(7)  # Set of days

# Variables
x = m.ivar('x', [I])

# Objective
m.obj(sum(x[i] for i in I))

# Constraint
for i in I:
    m.con(sum(x[j] for j in roll(i, RD)) | g | list(Data.values())[i])

# Solve
m.sol(['min'], 'cbc')
m.inf()
m.dis_model()
m.dis_obj()
m.dis_status()

# Display
for i in I:
    print(
        f"Number of employees who start working on {list(Data.keys())[i]}: {m.get(x[i])} ")

'''
Output:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   FelooPy (Version 0.2.0) - Released: 11 December 2022
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


PROBLEM FEATURES
 --------
| info      | detail   | variable   | count (cat,tot)   | other      | count (cat, tot)   |
|-----------|----------|------------|-------------------|------------|--------------------|
| model     | ws       | positive   | [0, 0]            | objective  | [1, 1]             |
| interface | pulp     | binary     | [0, 0]            | constraint | [7, 7]             |
| solver    | cbc      | integer    | [1, 7]            |            |                    |
| direction | ['min']  | free       | [0, 0]            |            |                    |
| method    | exact    | tot        | [1, 7]            |            |                    |
~~~~~~~~~~~~~~~~~~~~~~
model: ws
~~~~~~~~~~~~~~~~~~~~~~
min x0 + x1 + x2 + x3 + x4 + x5 + x6
s.t.
x0 + x3 + x4 + x5 + x6 >= 17
x0 + x1 + x4 + x5 + x6 >= 13
x0 + x1 + x2 + x5 + x6 >= 15
x0 + x1 + x2 + x3 + x6 >= 19
x0 + x1 + x2 + x3 + x4 >= 14
x1 + x2 + x3 + x4 + x5 >= 16
x2 + x3 + x4 + x5 + x6 >= 11
~~~~~~~~~~~~~~~~~~~~~~
objective:  23.0
status:  Optimal
Number of employees who start working on Mon: 2.0
Number of employees who start working on Tue: 6.0
Number of employees who start working on Wed: 0.0
Number of employees who start working on Thu: 7.0
Number of employees who start working on Fri: 0.0
Number of employees who start working on Sat: 3.0
Number of employees who start working on Sun: 5.0

'''
