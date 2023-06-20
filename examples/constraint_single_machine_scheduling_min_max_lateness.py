from feloopy import *

m = target_model('constraint', 'single_machine_scheduling', 'cplex_cp', key=0)

J = m.set(10)

due_date = m.uniform(75, 200, [J])
release_time = m.uniform(1,50, [J])

process_interval = m.cevar('job', J, [[m.uniformint(10,40), None, None] for j in J])
max_lateness = m.ivar('lateness')

m.obj(max_lateness)

for j in J:
    m.con(m.start_of(process_interval[j])>=release_time[j])

for j in J:
    m.con(m.max([0,m.end_of(process_interval[j])-due_date[j]])<=max_lateness)

m.con(m.forbid_overlap([process_interval[j] for j in J]))
m.sol(['min'], 'cplex')

m.report()