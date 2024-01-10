# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


import sys

import gurobipy as gurobi_interface
from ...helpers.formatter import *

gurobi_status_dict = {
    gurobi_interface.GRB.LOADED: 'loaded',
    gurobi_interface.GRB.OPTIMAL: 'optimal',
    gurobi_interface.GRB.INFEASIBLE: 'infeasible',
    gurobi_interface.GRB.INF_OR_UNBD: 'infeasible or unbounded',
    gurobi_interface.GRB.UNBOUNDED: 'unbounded',
    gurobi_interface.GRB.CUTOFF: 'cutoff',
    gurobi_interface.GRB.ITERATION_LIMIT: 'iteration limit',
    gurobi_interface.GRB.NODE_LIMIT: 'node limit',
    gurobi_interface.GRB.TIME_LIMIT: 'time limit',
    gurobi_interface.GRB.SOLUTION_LIMIT: 'solution limit',
    gurobi_interface.GRB.INTERRUPTED: 'interrupted',
    gurobi_interface.GRB.NUMERIC: 'numerical',
    gurobi_interface.GRB.SUBOPTIMAL: 'suboptimal',
    gurobi_interface.GRB.INPROGRESS: 'inprogress'
}


def Get(model_object, result, input1, input2=None):
    input1 = input1[0]

    match input1:
        case 'variable':
            return input2.X
        
        case 'status':
            return gurobi_status_dict[model_object.status]

        case 'objective':
            return model_object.ObjVal

        case 'time':
            return (result[1][1] - result[1][0])

        case 'dual':
            return model_object.getConstrByName(input2).Pi

        case 'slack':
            return model_object.getConstrByName(input2).Slack

        case 'rc':
            return input2.rc
         
        case 'iis':
            model_object.computeIIS()
            
            output = ''
            
            constrs = model_object.getConstrs()
            vars = model_object.getVars()

            for i, c in enumerate(constrs):
                if c.IISConstr:
                    output += left_align(f"con: {c.constrName}", rt=True)
                    if i != len(constrs) - 1 or i == 0:
                        output += "\n"

            for i, v in enumerate(vars):
                if v.IISLB > 0 or v.IISUB > 0:
                    output += left_align(f"var: {v.varName}", rt=True)
                    if i != len(vars) - 1 or i == 0:
                        output += "\n"

            return output