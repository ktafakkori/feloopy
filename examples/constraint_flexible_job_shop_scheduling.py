from feloopy import *

m = target_model('constraint', 'flexible_job_shop_scheduling', 'cplex_cp', key=1)

# Sets for jobs and machines
J = m.set(5)
K = m.set(3)

# Random job operations and task-machine pairs
J_O = m.uniformint(1,3,[J])
TJO = [(t, j, o) for j in J for o in range(J_O[j]) for t in [sum(J_O[:j]) + o]]
TM = [(triplet[0], k) for triplet in TJO for k in np.random.choice(K, np.random.random_integers(1, len(K)), replace=False)]

# Random intervals for each task-machine pair
interval = {i: [m.uniformint(20,34), None, None] for i in TM}

# Event variables for task-job-operation and task-machine
tjo = m.cevar('task_job_operation', TJO)
tm = m.cevar('task_machine', TM, interval, optional=True)

# Minimize the maximum completion time
m.obj(m.max([m.end_of(tm[t, k]) for t, k in TM]))

# Forbid overlapping tasks on the same machine
for k in K:
    m.con(m.forbid_overlap([tm[t,kk] for t, kk in TM if kk == k]))

# Define the precedence constraint for tasks within the same job
predecessor = {task2: task1[0] for task1, task2 in sets(TJO,TJO) if task1[1]==task2[1] and task1[2] + 1 == task2[2]}
for j in J:
    for task in TJO:
        if task[1] == j and task[2] >= 1:
            m.con(m.prec_end_before_start(tjo[(predecessor[task], task[1], task[2] - 1)], tjo[task]))

# Add alternative constraints to ensure each task is assigned to only one machine
for task in tjo:
    m.con(m.alternative(tjo[task], [tm[(o, m)] for (o, m) in tm if (o == task[0])], 1))

# Solve the model
m.solve(['min'], 'cplex')

# Display report
m.report()
