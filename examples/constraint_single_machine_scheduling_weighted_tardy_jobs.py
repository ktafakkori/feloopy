from feloopy import *

# Credit: https://github.com/ErayCakici/Scheduling-DOCPLEX-Examples_CP

m = target_model('constraint', 'single_machine_scheduling', 'cplex_cp', key=0)

J = m.set(10)
due_date = m.uniform(75, 200, [J])
priority_weights = m.uniformint(1,5, [J])
process_interval = m.cevar('job', J, {j: [m.uniformint(10,40), None, None] for j in J})

m.obj(sum((m.end_of(process_interval[j]) > due_date[j])*priority_weights[j] for j in J))
m.con(m.forbid_overlap([process_interval[j] for j in J]))

m.sol(['min'], 'cplex')

m.report()