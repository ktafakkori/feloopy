from feloopy import *

# Environment
m = model('exact', 'tsp', 'ortools',key=0)

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
~~~~~~~~~~~~
PROBLEM INFO
~~~~~~~~~~~~
| info      | detail   | variable   | count [cat,tot]   | other      | count [cat,tot]    |
|-----------|----------|------------|-------------------|------------|--------------------|
| model     | tsp      | positive   | [0, 0]            | objective  | [1, 1]             |
| interface | ortools  | binary     | [1, 100]          | constraint | [1, 101]           |
| solver    | scip     | integer    | [1, 10]           |            |                    |
| direction | ['min']  | free       | [0, 0]            |            |                    |
| method    | exact    | tot        | [2, 110]          |            |                    |
~~~~~~~~~~~~

objective:  25.0
status:  optimal
when the traveler is at 0 goes to 7
when the traveler is at 1 goes to 4
when the traveler is at 2 goes to 0
when the traveler is at 3 goes to 8
when the traveler is at 4 goes to 3
when the traveler is at 5 goes to 1
when the traveler is at 6 goes to 5
when the traveler is at 7 goes to 9
when the traveler is at 8 goes to 2
when the traveler is at 9 goes to 6

'''



def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = [
        [0, 2451, 713, 1018, 1631, 1374, 2408, 213, 2571, 875, 1420, 2145, 1972],
        [2451, 0, 1745, 1524, 831, 1240, 959, 2596, 403, 1589, 1374, 357, 579],
        [713, 1745, 0, 355, 920, 803, 1737, 851, 1858, 262, 940, 1453, 1260],
        [1018, 1524, 355, 0, 700, 862, 1395, 1123, 1584, 466, 1056, 1280, 987],
        [1631, 831, 920, 700, 0, 663, 1021, 1769, 949, 796, 879, 586, 371],
        [1374, 1240, 803, 862, 663, 0, 1681, 1551, 1765, 547, 225, 887, 999],
        [2408, 959, 1737, 1395, 1021, 1681, 0, 2493, 678, 1724, 1891, 1114, 701],
        [213, 2596, 851, 1123, 1769, 1551, 2493, 0, 2699, 1038, 1605, 2300, 2099],
        [2571, 403, 1858, 1584, 949, 1765, 678, 2699, 0, 1744, 1645, 653, 600],
        [875, 1589, 262, 466, 796, 547, 1724, 1038, 1744, 0, 679, 1272, 1162],
        [1420, 1374, 940, 1056, 879, 225, 1891, 1605, 1645, 679, 0, 1017, 1200],
        [2145, 357, 1453, 1280, 586, 887, 1114, 2300, 653, 1272, 1017, 0, 504],
        [1972, 579, 1260, 987, 371, 999, 701, 2099, 600, 1162, 1200, 504, 0],
    ]  # yapf: disable
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data