'''
Name: FelooPy
Version: 0.1.11
Contributors: Keivan Tafakkori
Date: 21 November 2022
License: MIT. (For more details please refer to LICENSE.txt file).
Copyright (c) 2022 Keivan Tafakkori & FELOOP (https://ktafakkori.github.io/)
'''


import itertools as it
from .age import *

import mip as mip_interface
import cylp as cylp_interface
from cylp.cy import CyClpSimplex
import cvxpy as cvxpy_interface
from linopy import Model
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


# gekko

def add_gekko_ivar(modelobject, var_name, b, dim=0):
    if dim == 0:
        return modelobject.Var(lb=b[0], ub=b[1], integer=True)
    else:
        if len(dim) == 1:
            return {key:  modelobject.Var(lb=b[0], ub=b[1], integer=True) for key in dim[0]}
        else:
            return {key:  modelobject.Var(lb=b[0], ub=b[1], integer=True) for key in it.product(*dim)}

# ortools


def add_ortools_ivar(modelobject, var_name, b, dim=0):
    if b[0] == 0:
        b[0] = 0
    if b[1] == None:
        b[1] = modelobject.infinity()

    if dim == 0:
        return modelobject.IntVar(b[0], b[1], var_name)
    else:
        if len(dim) == 1:
            return {key: modelobject.IntVar(b[0], b[1], f"{var_name}{key}") for key in dim[0]}
        else:
            return {key: modelobject.IntVar(b[0], b[1], f"{var_name}{key}") for key in it.product(*dim)}

# pulp


def add_pulp_ivar(modelobject, var_name, b, dim=0):
    if dim == 0:
        return pulp_interface.LpVariable(var_name, b[0], b[1], pulp_interface.LpInteger)
    else:
        if len(dim) == 1:
            return {key: pulp_interface.LpVariable(f"{var_name}{key}", b[0], b[1], pulp_interface.LpInteger) for key in dim[0]}
        else:
            return {key: pulp_interface.LpVariable(f"{var_name}{key}", b[0], b[1], pulp_interface.LpInteger) for key in it.product(*dim)}

# pyomo


def add_pyomo_ivar(modelobject, var_name, b, dim=0):
    if dim == 0:
        modelobject.add_component(
            var_name, pyomo_interface.Var(domain=pyomo_interface.NonNegativeIntegers, bounds=(b[0], b[1])))
    else:
        modelobject.add_component(var_name, pyomo_interface.Var(
            [i for i in it.product(*dim)], domain=pyomo_interface.NonNegativeIntegers, bounds=(b[0], b[1])))
    return modelobject.component(var_name)

# pymprog


def add_pymprog_ivar(modelobject, var_name, b, dim=0):
    if dim == 0:
        return pymprog_interface.var(var_name, bounds=(b[0], b[1]), kind=int)
    else:
        if len(dim) == 1:
            return {key: pymprog_interface.var(var_name, bounds=(b[0], b[1]), kind=int) for key in dim[0]}
        else:
            return {key: pymprog_interface.var(var_name, bounds=(b[0], b[1]), kind=int) for key in it.product(*dim)}

# picos


def add_picos_ivar(modelobject, var_name, b, dim=0):
    if dim == 0:
        return picos_interface.IntegerVariable(var_name, lower=b[0], upper=b[1])
    else:
        if len(dim) == 1:
            return {key: picos_interface.IntegerVariable(var_name, lower=b[0], upper=b[1]) for key in dim[0]}
        else:
            return {key: picos_interface.IntegerVariable(var_name, lower=b[0], upper=b[1]) for key in it.product(*dim)}


# cplex

def add_cplex_ivar(modelobject, var_name, b, dim=0):
    if dim == 0:
        return modelobject.integer_var(lb=b[0], ub=b[1])
    else:
        if len(dim) == 1:
            return {key: modelobject.integer_var(lb=b[0], ub=b[1]) for key in dim[0]}
        else:
            return {key: modelobject.integer_var(lb=b[0], ub=b[1]) for key in it.product(*dim)}

# gurobi


def add_gurobi_ivar(modelobject, var_name, b, dim=0):
    if dim == 0:
        return modelobject.addVar(vtype=gurobi_interface.GRB.INTEGER, lb=b[0], ub=b[1], name=var_name)
    else:
        if len(dim) == 1:
            return {key: modelobject.addVar(vtype=gurobi_interface.GRB.INTEGER, lb=b[0], ub=b[1], name=f"{var_name}{key}") for key in dim[0]}
        else:
            return {key: modelobject.addVar(vtype=gurobi_interface.GRB.INTEGER, lb=b[0], ub=b[1], name=f"{var_name}{key}") for key in it.product(*dim)}

# xpress

def add_xpress_ivar(modelobject, var_name, b, dim=0):
    if b[0] == None:
        b[0] = 0
    if b[1] == None:
        b[1] = xpress_interface.infinity
    if dim == 0:
        var = xpress_interface.var(vartype=xpress_interface.integer)
        modelobject.addVariable(var)
        return var
    else:
        if len(dim) == 1:
            var = {key: xpress_interface.var(vartype=xpress_interface.integer) for key in dim[0]}
            modelobject.addVariable(var)
            return var
        else:
            var = {key: xpress_interface.var(name= f"{var_name}{key}", lb=b[0],ub=b[1],vartype=xpress_interface.integer) for key in it.product(*dim)}
            modelobject.addVariable(var)
            return var



# linopy


def add_linopy_ivar(modelobject, var_name, b, dim=0):
    if dim == 0:
        return modelobject.add_variables(lower=b[0], upper=b[1], name=var_name, binary=True)
    else:
        return modelobject.add_variables(lower=b[0], upper=b[1], coords=[i for i in it.product(*dim)], name=var_name,  binary=True)

# cvxpy


def add_cvxpy_ivar(modelobject, var_name, b, dim=0):
    if dim == 0:
        return cvxpy_interface.Variable(1, integer=True)
    else:
        if len(dim) == 1:
            return {key: cvxpy_interface.Variable(1, integer=True) for key in dim[0]}
        else:
            return {key: cvxpy_interface.Variable(1, integer=True) for key in it.product(*dim)}

# cylp


def add_cylp_ivar(modelobject, var_name, b, dim=0):
    if dim == 0:
        return modelobject.addVariable(var_name, 1, isInt=True)
    else:
        if len(dim) == 1:
            return {key: modelobject.addVariable(f"{var_name}{key}", 1, isInt=True) for key in dim[0]}
        else:
            return {key: modelobject.addVariable(f"{var_name}{key}", 1, isInt=True) for key in it.product(*dim)}

# mip


def add_mip_ivar(modelobject, var_name, b, dim=0):
    if dim == 0:
        return modelobject.add_var(var_type=mip_interface.INTEGER)
    else:
        if len(dim) == 1:
            return {key: modelobject.add_var(var_type=mip_interface.INTEGER) for key in dim[0]}
        else:
            return {key: modelobject.add_var(var_type=mip_interface.INTEGER) for key in it.product(*dim)}

# ga


def add_ga_ivar(var_name, agent, VarLength, dim=0,  b=[0, 1], vectorized=False):
    if dim == 0:
        if vectorized:
            return np.round(b[0] + agent[:, VarLength[0]:VarLength[1]] * (b[1] - b[0]))
        else:
            return np.round(b[0] + agent[VarLength[0]:VarLength[1]] * (b[1] - b[0]))
    else:
        if vectorized:
            return multiagent(var_name, b[0] + agent[:, VarLength[0]:VarLength[1]] * (b[1] - b[0]), dim, 'ivar')
        else:
            return singleagent(var_name, b[0] + agent[VarLength[0]:VarLength[1]] * (b[1] - b[0]), dim, 'ivar')


ivar_maker = {
    "gekko": add_gekko_ivar,
    "ortools": add_ortools_ivar,
    "pulp": add_pulp_ivar,
    "pyomo": add_pyomo_ivar,
    "pymprog": add_pymprog_ivar,
    "picos": add_picos_ivar,
    "cplex": add_cplex_ivar,
    "gurobi": add_gurobi_ivar,
    "xpress": add_xpress_ivar,
    "linopy": add_linopy_ivar,
    "cvxpy": add_cvxpy_ivar,
    "cylp": add_cylp_ivar,
    "mip": add_mip_ivar,
    "ga": add_ga_ivar
}
