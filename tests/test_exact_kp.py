from feloopy import *
import plotly.express as px


success_list = []
error_list = []
time = []

size = 1000

for combination in exact_algorithms:

    print(combination)

    m = model('exact', 'kp', combination[0], key=0)

    J = range(size)  

    w = m.uniform(10,30,[J]) 
    W = 1000  
    p = m.uniform(10,30,[J])

    x = m.bvar('x', [J])

    m.obj(sum(p[j]*x[j] for j in J))

    m.con(sum(w[j]*x[j] for j in J) <= W)

    for j in J:

        m.con(x[j]<=1)

        m.con(x[j]>=0)

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