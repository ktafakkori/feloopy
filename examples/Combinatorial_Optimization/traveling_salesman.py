from feloopy import *

# Environment
m = feloopy('TSP', 'ortools')

# Sets
N = range(10)
U = range(1, len(N))

# Parameters
np.random.seed(0)

c = np.random.randint(1, 10, size=(len(N), len(N)))

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
m.sol('min', 'scip')

# Display
for i, j in sets(N, N):
    if m.get(x[i, j]) == 1:
        print(f"when the traveler is at {i} goes to {j}")

'''
Output:

when the traveler is at 0 goes to 9
when the traveler is at 1 goes to 4
when the traveler is at 2 goes to 6
when the traveler is at 3 goes to 0
when the traveler is at 4 goes to 3
when the traveler is at 5 goes to 2
when the traveler is at 6 goes to 1
when the traveler is at 7 goes to 8
when the traveler is at 8 goes to 5
when the traveler is at 9 goes to 7

'''