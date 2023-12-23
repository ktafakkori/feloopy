'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.8)                               |
|  Modified: Wednesday, 27th September 2023 08:50:18 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''

# Example Credit: https://github.com/ErayCakici/Scheduling-DOCPLEX-Examples_CP

from feloopy import *

m = target_model('constraint', 'single_machine_scheduling', 'cplex_cp')

dt = data_toolkit()

J = range(10)

due_date = dt.uniform('dd', [J], [75, 200])
release_time = dt.uniform('rt', [J],  [1,50])
priority_weights = dt.uniformint('pw', [J],  [1,5])
precedences = list()
for j in J:
    if j>=len(J)/2:
        precedences.append((dt.uniformint(f'pc[{j}]', bound=[0,len(J)/2-1]), j))

process_interval = m.cevar('job', J, {j: [dt.uniformint(f'pi[{j}]',bound=[10,40]), None, None] for j in J})

m.obj(sum([m.cp_get_event_end(process_interval[j])*priority_weights[j] for j in J])) 

m.con(m.cp_forbid_event_overlap([process_interval[j] for j in J]))

m.con([m.cp_event_end_before_start(process_interval[i],process_interval[j]) for [i,j] in precedences])

m.sol(['min'], 'cplex')

m.report()