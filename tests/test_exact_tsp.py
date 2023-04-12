from feloopy import *
import plotly.express as px

success_list = []
error_list = []
time = []

size = 50

for combination in exact_algorithms:

    print(combination)

    m = model('exact', 'tsp', combination[0],key=0)

    N = m.set(size)
    U = m.set(size-1)

    c = m.uniformint(1, 10, [N,N])

    for i, j in sets(N, N):

        c[i][i] = 0
        c[i][j] = c[j][i]

    x = m.bvar('x', [N, N])
    u = m.ivar('u', [N])

    m.obj(sum(c[i, j]*x[i, j] for i, j in sets(N, N)))

    for j in N:
        m.con(sum(x[i, j] for i in N if i != j) == 1)

    for i in N:
        m.con(sum(x[i, j] for j in N if j != i) == 1)

    for i, j in sets(U, N):
        if i != j:
            m.con(u[i] - u[j] + x[i, j] * len(N) <= len(N)-1)

    try:

        m.sol(['max'], combination[1])
        success_list.append(combination)
        time.append(m.get_time())

    except:

        print(f"combination {combination} has errors")
        error_list.append(combination)

        pass

print('success: ', success_list)
print('error: ', error_list)
print(len(time))
print(len(success_list))

for i in range(len(success_list)):
    success_list[i]=str(success_list[i])

fig = px.bar(x=success_list, y=time)
fig.show()