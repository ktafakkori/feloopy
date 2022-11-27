'''
Name: FelooPy
Version: 0.1.11
Contributors: Keivan Tafakkori
Date: 21 November 2022
License: MIT. (For more details please refer to LICENSE.txt file).
Copyright (c) 2022 Keivan Tafakkori & FELOOP (https://ktafakkori.github.io/)
'''

import itertools as it

import mip as mip_interface
import cylp as cylp_interface
from cylp.cy import CyClpSimplex
import cvxpy as cvxpy_interface
from linopy import Model as LINOPYMODEL
import xpress as xpress_interface
import gurobipy as gurobi_interface
from docplex.mp.model import Model as CPLEXMODEL
import docplex as cplex_interface
import picos as picos_interface
import pymprog as pymprog_interface
import pyomo.environ as pyomo_interface
import pulp as pulp_interface
from ortools.linear_solver import pywraplp as ortools_interface
import gekko as gekko_interface


#gekko

gekko_status_dict = {0: "not_optimal", 1: "optimal"}

def show_gekko_get(modelobject,input):
    return input.value

def show_gekko_getstat(modelobject, result):
    return gekko_status_dict.get(modelobject.options.SOLVESTATUS)

def show_gekko_getobj(modelobject, result):
    return -modelobject.options.objfcnval

#ortools

def show_ortools_get(modelobject,input):
    return input.solution_value()

ortools_status_dict = {0: "optimal", 1: "feasible", 2: "infeasible",
                            3: "unbounded", 4: "abnormal", 5: "model_invalid", 6: "not_solved"}

def show_ortools_getstat(modelobject, result):
    return ortools_status_dict.get(result, "unknown")

def show_ortools_getobj(modelobject, result):
    return modelobject.Objective().Value()

#pulp

def show_pulp_get(modelobject,input):
    return input.varValue

def show_pulp_getstat(modelobject, result):
    return pulp_interface.LpStatus[result]

def show_pulp_getobj(modelobject, result):
    return pulp_interface.value(modelobject.objective)

#pyomo

def show_pyomo_get(modelobject,input):
    return pyomo_interface.value(input)

def show_pyomo_getstat(modelobject, result):
    return result.solver.termination_condition

def show_pyomo_getobj(modelobject, result):
    return pyomo_interface.value(modelobject.OBJ)

#pymprog

def show_pymprog_get(modelobject,input):
    return input.primal

def show_pymprog_getstat(modelobject, result):
    return pymprog_interface.status()

def show_pymprog_getobj(modelobject, result):
    return pymprog_interface.vobj()

#picos

def show_picos_get(modelobject,input):
    return input.value

def show_picos_getstat(modelobject, result):
    return result.claimedStatus

def show_picos_getobj(modelobject, result):
    return modelobject.obj_value()

#cplex

def show_cplex_get(modelobject,input):
    return input.solution_value

def show_cplex_getstat(modelobject, result):
    return modelobject.solve_details.status

def show_cplex_getobj(modelobject, result):
    return modelobject.objective_value

#gurobi

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

def show_gurobi_get(modelobject,input):
    return input.X

def show_gurobi_getstat(modelobject, result):
    return gurobi_status_dict[modelobject.status]

def show_gurobi_getobj(modelobject, result):
    return modelobject.ObjVal

# linopy

def show_linopy_get(modelobject,input):
    return input.solution

def show_linopy_getstat(modelobject, result):
    return result[1]

def show_linopy_getobj(modelobject, result):
    return "None"

# cvxpy

def show_cvxpy_get(modelobject,input):
    return input.value

def show_cvxpy_getstat(modelobject, result):
    return modelobject.status

def show_cvxpy_getobj(modelobject, result):
    return modelobject.value

# cylp

def show_cylp_get(modelobject, input):
    return modelobject.primalVariableSolution[input]

def show_cylp_getstat(modelobject, result):
    return result.status

def show_cylp_getobj(modelobject, result):
    return -modelobject.objectiveValue


#xpress

def show_xpress_get(modelobject,input):
    return modelobject.getSolution(input)

def show_xpress_getstat(modelobject, result):
    return result

def show_xpress_getobj(modelobject, result):
    return modelobject.getSolution(result)

# mip

def show_mip_get(modelobject, input):
    return input.x

def show_mip_getstat(modelobject, result):
    return result

def show_mip_getobj(modelobject, result):
    return modelobject.objective_value

variable_getter = {
    "gekko": show_gekko_get,
    "ortools": show_ortools_get,
    "pulp": show_pulp_get,
    "pyomo": show_pyomo_get,
    "pymprog": show_pymprog_get,
    "picos": show_picos_get,
    "cplex": show_cplex_get,
    "gurobi": show_gurobi_get,
    "xpress": show_xpress_get,
    "linopy": show_linopy_get,
    "cvxpy": show_cvxpy_get,
    "cylp": show_cylp_get,
    "mip": show_mip_get
}

objective_getter = {
    "gekko": show_gekko_getobj,
    "ortools": show_ortools_getobj,
    "pulp": show_pulp_getobj,
    "pyomo": show_pyomo_getobj,
    "pymprog": show_pymprog_getobj,
    "picos": show_picos_getobj,
    "cplex": show_cplex_getobj,
    "gurobi": show_gurobi_getobj,
    "xpress": show_xpress_getobj,
    "linopy": show_linopy_getobj,
    "cvxpy": show_cvxpy_getobj,
    "cylp": show_cylp_getobj,
    "mip": show_mip_getobj
}

status_getter = {
    "gekko": show_gekko_getstat,
    "ortools": show_ortools_getstat,
    "pulp": show_pulp_getstat,
    "pyomo": show_pyomo_getstat,
    "pymprog": show_pymprog_getstat,
    "picos": show_picos_getstat,
    "cplex": show_cplex_getstat,
    "gurobi": show_gurobi_getstat,
    "xpress": show_xpress_getstat,
    "linopy": show_linopy_getstat,
    "cvxpy": show_cvxpy_getstat,
    "cylp": show_cylp_getstat,
    "mip": show_mip_getstat
}


