from feloopy import *

# Environment
m = model('exact', 'tsp', 'ortools',Key=0)

# Sets
N = m.set(10)
U = m.set(9)

# Parameters
c = m.uniformint(1, 10, [N,N])

for i, j in sets(N, N):
    c[i][i] = 0
    c[i][j] = c[j][i]

# Variables
x = m.bvar('x', [N, N])
u = m.ivar('u', [N])

# Objective
m.obj(sum(c[i, j]*x[i, j] for i, j in sets(N, N)))

# Constraints
for j in N:
    m.con(sum(x[i, j] for i in N if i != j) |e| 1)

for i in N:
    m.con(sum(x[i, j] for j in N if j != i) |e| 1)

for i, j in sets(U, N):
    if i != j:
        m.con(u[i] - u[j] + x[i, j] * len(N) |l| len(N)-1)

# Solve
m.sol(['min'], 'scip')
m.inf()
m.dis_obj()
m.dis_status()

# Display
for i, j in sets(N, N):
    if m.get(x[i, j]) == 1:
        print(f"when the traveler is at {i} goes to {j}")

'''
Output:

PROBLEM FEATURES
 --------
| info      | detail   | variable   | count (cat,tot)   | other      | count (cat, tot)   |
|-----------|----------|------------|-------------------|------------|--------------------|
| model     | tsp      | positive   | [0, 0]            | objective  | [1, 1]             |
| interface | ortools  | binary     | [1, 100]          | constraint | [101, 101]         |
| solver    | scip     | integer    | [1, 10]           |            |                    |
| direction | ['min']  | free       | [0, 0]            |            |                    |
| method    | exact    | tot        | [2, 110]          |            |                    |
objective:  25.0
status:  optimal
when the traveler is at 0 goes to 2
when the traveler is at 1 goes to 5
when the traveler is at 2 goes to 8
when the traveler is at 3 goes to 4
when the traveler is at 4 goes to 1
when the traveler is at 5 goes to 6
when the traveler is at 6 goes to 9
when the traveler is at 7 goes to 0
when the traveler is at 8 goes to 3
when the traveler is at 9 goes to 7

'''
