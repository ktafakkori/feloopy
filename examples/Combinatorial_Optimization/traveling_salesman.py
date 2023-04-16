from feloopy import *

# Environment
m = model('exact', 'tsp', 'pyomo',key=0)

# Sets
N = m.set(90)
U = m.set(89)

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
    m.con(sum(x[i, j] for i in N if i != j) == 1)

for i in N:
    m.con(sum(x[i, j] for j in N if j != i) == 1)

for i, j in sets(U, N):
    if i != j:
        m.con(u[i] - u[j] + x[i, j] * len(N) <= len(N)-1)

# Solve
begin_timer()
m.sol(['min'], 'cplex')
end_timer(True)
m.inf()
m.dis_obj()
m.dis_status()

# Display
for i, j in sets(N, N):
    if i!=j:
        if m.get(x[i, j]) == 1:
            print(f"when the traveler is at {i} goes to {j}")

m.report()
