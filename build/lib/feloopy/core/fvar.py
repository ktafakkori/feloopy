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
from .age import *

# gekko


def add_gekko_fvar(modelobject, var_name, b, dim=0):
    if dim == 0:
        return modelobject.Var(lb=b[0], ub=b[1])
    else:
        if len(dim)==1: return {key: modelobject.Var(lb=b[0], ub=b[1]) for key in dim[0]}
        else:  return {key: modelobject.Var(lb=b[0], ub=b[1]) for key in it.product(*dim)}

# ortools


def add_ortools_fvar(modelobject, var_name, b, dim=0):
    if b[0]==None: b[0]=-modelobject.infinity()
    if b[1]==None: b[1]=modelobject.infinity()

    if dim == 0:
        return modelobject.NumVar(b[0], b[1], var_name)
    else:
        if len(dim)==1: return {key: modelobject.NumVar(b[0], b[1], f"{var_name}{key}") for key in dim[0]}
        else: return {key: modelobject.NumVar(b[0], b[1], f"{var_name}{key}") for key in it.product(*dim)}

# pulp


def add_pulp_fvar(modelobject, var_name, b, dim=0):
    if dim == 0:
        return pulp_interface.LpVariable(var_name, b[0], b[1], pulp_interface.LpContinuous)
    else:
        if len(dim)==1: return {key: pulp_interface.LpVariable(f"{var_name}{key}", b[0], b[1], pulp_interface.LpContinuous) for key in dim[0]}
        else: return {key: pulp_interface.LpVariable(f"{var_name}{key}", b[0], b[1], pulp_interface.LpContinuous) for key in it.product(*dim)}

# pyomo


def add_pyomo_fvar(modelobject, var_name, b, dim=0):
    if dim == 0:
        modelobject.add_component(
            var_name, pyomo_interface.Var(domain=pyomo_interface.Reals, bounds=(b[0],b[1])))
    else:
        modelobject.add_component(var_name, pyomo_interface.Var([i for i in it.product(*dim)], domain=pyomo_interface.Reals, bounds=(b[0],b[1])))
    return modelobject.component(var_name)

def add_ga_fvar(var_name, agent, VarLength, dim=0,  b=[0, 1], vectorized=False):
    if dim == 0:
        if vectorized:
            return b[0] + agent[:, VarLength[0]:VarLength[1]] * (b[1] - b[0])
        else:
            return b[0] + agent[VarLength[0]:VarLength[1]] * (b[1] - b[0])
    else:
        if vectorized:
            return multiagent(var_name, b[0] + agent[:, VarLength[0]:VarLength[1]] * (b[1] - b[0]), dim, 'fvar')
        else:
            return singleagent(var_name, b[0]+ agent[VarLength[0]:VarLength[1]] * (b[1] - b[0]), dim, 'fvar')



fvar_maker = {
    "gekko": add_gekko_fvar,
    "ortools": add_ortools_fvar,
    "pulp": add_pulp_fvar,
    "pyomo": add_pyomo_fvar,
    "ga": add_ga_fvar
}
