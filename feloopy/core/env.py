
'''
Name: Feloopy
Version: 0.1.11
Contributors: Keivan Tafakkori
Date: 20 November 2022
License: MIT. (For more details please refer to LICENSE.txt file).
Copyright (c) 2022 Keivan Tafakkori & FELOOP (https://ktafakkori.github.io/)
'''

import itertools as it
import numpy as np
from feloopy.heuristic import *

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

# gekko


def add_gekko_model():
    return gekko_interface.GEKKO(remote=False)


# ortools


def add_ortools_model():
    return ortools_interface.Solver.CreateSolver('SCIP')


# pulp


def add_pulp_model():
    return pulp_interface.LpProblem('None', pulp_interface.LpMinimize)


# pyomo


def add_pyomo_model():
    return pyomo_interface.ConcreteModel()


# pymprog


def add_pymprog_model():
    pymprog_interface.begin('None')


# picos


def add_picos_model():
    return picos_interface.Problem('None')

# cplex


def add_cplex_model():
    return CPLEXMODEL("None")


# gurobi


def add_gurobi_model():
    return gurobi_interface.Model("None")


# xpress


def add_xpress_model():
    return xpress_interface.problem("None")


# linopy


def add_linopy_model():
    return LINOPYMODEL()


# cvxpy


def add_cvxpy_model():
    "None"


# cylp


def add_cylp_model():
    return cylp_interface.py.modeling.CyLPModel()


# mip


def add_mip_model():
    return mip_interface.Model("None")


# ga


def add_ga_model(model, n_vars, algsetting):
    return ga(function=model, dimension=n_vars, variable_type='real', variable_boundaries=np.array([[0, 1]]*n_vars), progress_bar=False, convergence_curve=False, algorithm_parameters=algsetting)


model_maker = {
    "gekko": add_gekko_model,
    "ortools": add_ortools_model,
    "pulp": add_pulp_model,
    "pyomo": add_pyomo_model,
    "pymprog": add_pymprog_model,
    "picos": add_picos_model,
    "cplex": add_cplex_model,
    "gurobi": add_gurobi_model,
    "xpress": add_xpress_model,
    "linopy": add_linopy_model,
    "cvxpy": add_cvxpy_model,
    "cylp": add_cylp_model,
    "mip": add_mip_model,
    "ga": add_ga_model
}
