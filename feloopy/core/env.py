'''
FelooPy version 0.1.1
Release: 26 October 2022
'''

'''
MIT License

Copyright (c) 2022 Keivan Tafakkori & FELOOP (https://ktafakkori.github.io/)

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

   1. Redistributions of source code must retain the above copyright notice, this list of
      conditions and the following disclaimer.

   2. Redistributions in binary form must reproduce the above copyright notice, this list
      of conditions and the following disclaimer in the documentation and/or other materials
      provided with the distribution.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import itertools as it
import pulp as pulp_interface
import pyomo.environ as pyomo_interface
import gekko as gekko_interface
from ortools.linear_solver import pywraplp as ortools_interface
import pymprog as pymprog_interface
import numpy as np
from feloopy.heuristic import *

def add_gekko_model():
    modelobject = gekko_interface.GEKKO(remote=False)
    return modelobject

def add_ortools_model():
    modelobject = ortools_interface.Solver.CreateSolver('SCIP')
    return modelobject

def add_pulp_model():
    modelobject = pulp_interface.LpProblem('None',pulp_interface.LpMinimize)
    return modelobject

def add_pyomo_model():
    modelobject = pyomo_interface.ConcreteModel()
    return modelobject

def add_pymprog_model():
    pymprog_interface.begin('None')

def add_ga_model(model, n_vars, algsetting):
        varbound = np.array([[0, 1]]*n_vars)
        model = ga(function=model, dimension=n_vars, variable_type='real', variable_boundaries=varbound, progress_bar=False, convergence_curve=False, algorithm_parameters=algsetting)
        return model

model_maker = {
    "gekko": add_gekko_model,
    "ortools": add_ortools_model,
    "pulp": add_pulp_model,
    "pyomo": add_pyomo_model,
    "pymprog": add_pymprog_model,
    "ga": add_ga_model
}

