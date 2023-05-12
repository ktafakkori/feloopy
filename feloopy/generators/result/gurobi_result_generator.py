'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

import gurobipy as gurobi_interface

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

            return (result[1][1]-result[1][0])
