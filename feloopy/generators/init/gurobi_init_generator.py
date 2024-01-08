# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

from gurobipy import GRB

def set_init_value(features, variable, value, fix):
    if fix:
        variable.lb = value
        variable.ub = value
    else:
        variable.Start = value
     