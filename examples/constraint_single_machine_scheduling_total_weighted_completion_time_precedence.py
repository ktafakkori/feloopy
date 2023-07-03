from feloopy import *

# Credit: https://github.com/ErayCakici/Scheduling-DOCPLEX-Examples_CP

m = target_model('constraint', 'single_machine_scheduling', 'cplex_cp', key=0)

J = m.set(10)

due_date = m.uniform(75, 200, [J])
release_time = m.uniform(1,50, [J])
priority_weights = m.uniformint(1,5, [J])
precedences = list()
for j in J:
    if j>=len(J)/2:
        precedences.append((m.uniformint(0,len(J)/2-1), j))

process_interval = m.cevar('job', J, {j: [m.uniformint(10,40), None, None] for j in J})

m.obj(sum([m.end_of(process_interval[j])*priority_weights[j] for j in J])) 

m.con(m.forbid_overlap([process_interval[j] for j in J]))

m.con([m.prec_end_before_start(process_interval[i],process_interval[j]) for [i,j] in precedences])

m.sol(['min'], 'cplex')

m.report()