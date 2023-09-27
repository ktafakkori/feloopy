'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.7)                               |
|  Modified: Wednesday, 27th September 2023 08:50:18 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''

# Example Credit: https://github.com/ErayCakici/Scheduling-DOCPLEX-Examples_CP

from feloopy import *

m = target_model('constraint', 'single_machine_scheduling', 'cplex_cp', key=0)

J = range(10)

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