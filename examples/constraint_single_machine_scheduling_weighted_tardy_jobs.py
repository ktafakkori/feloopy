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

J = 10
due_date = np.random.uniform(75, 200, size=[J])
priority_weights = np.random.random_integers(1,5, size=[J])
process_interval = m.cevar('job', range(J), {j: [np.random.random_integers(10,40), None, None] for j in range(J)})

m.obj(sum((m.end_of(process_interval[j]) > due_date[j])*priority_weights[j] for j in range(J)))
m.con(m.forbid_overlap([process_interval[j] for j in range(J)]))

m.sol(['min'], 'cplex')

m.report()