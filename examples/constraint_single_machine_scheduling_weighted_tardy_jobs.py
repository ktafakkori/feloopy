# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

# Example Credit: https://github.com/ErayCakici/Scheduling-DOCPLEX-Examples_CP

from feloopy import *

m = target_model('constraint', 'single_machine_scheduling', 'cplex_cp')

J = 10
due_date = np.random.uniform(75, 200, size=[J])
priority_weights = np.random.random_integers(1,5, size=[J])
process_interval = m.cevar('job', range(J), {j: [np.random.random_integers(10,40), None, None] for j in range(J)})

m.obj(sum((m.cp_get_event_end(process_interval[j]) > due_date[j])*priority_weights[j] for j in range(J)))
m.con(m.cp_forbid_event_overlap([process_interval[j] for j in range(J)]))

m.sol(['min'], 'cplex')

m.report()