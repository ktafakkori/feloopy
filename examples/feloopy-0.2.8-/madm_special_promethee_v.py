# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

from feloopy import madm
m = madm("promethee_v", "promethee_v_model", "pydecision")
m.add_dm(
    [
        [8.840, 8.790, 6.430, 6.950],
        [8.570, 8.510, 5.470, 6.910],
        [7.760, 7.750, 5.340, 8.760],
        [7.970, 9.120, 5.930, 8.090],
        [9.030, 8.970, 8.190, 8.100],
        [7.410, 7.870, 6.770, 7.230],
    ]
)
m.add_qt([0.3, 0.3, 0.3, 0.3])
m.add_st([0.4, 0.4, 0.4, 0.4])
m.add_pt([0.5, 0.5, 0.5, 0.5])
m.add_wv([9.00, 8.24, 5.98, 8.48])
m.add_uf(["t5", "t5", "t5", "t5"])

m.add_con_max_criteria(4)
m.add_con_cost_budget([10, 10, 15, 10, 10, 15], 50)
m.add_con_forbid_selection([["a1", "a4"], ["a1", "a5"]])

m.sol(show_graph=True)
m.report(show_tensors=True)