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
import pymprog as pymprog_interface
from ortools.linear_solver import pywraplp as ortools_interface

gekko_status_dict = {0: "not_optimal", 1: "optimal"}

def show_gekko_get(input):
    return input.value

def show_gekko_getstat(modelobject, result):
    return gekko_status_dict.get(modelobject.options.SOLVESTATUS)

def show_gekko_getobj(modelobject, result):
    return -modelobject.options.objfcnval

def show_ortools_get(input):
    return input.solution_value()

ortools_status_dict = {0: "optimal", 1: "feasible", 2: "infeasible",
                            3: "unbounded", 4: "abnormal", 5: "model_invalid", 6: "not_solved"}

def show_ortools_getstat(modelobject, result):
    return ortools_status_dict.get(result, "unknown")

def show_ortools_getobj(modelobject, result):
    return modelobject.Objective().Value()

def show_pulp_get(input):
    return input.varValue

def show_pulp_getstat(modelobject, result):
    return pulp_interface.LpStatus[result]

def show_pulp_getobj(modelobject, result):
    return pulp_interface.value(modelobject.objective)

def show_pyomo_get(input):
    return pyomo_interface.value(input)

def show_pyomo_getstat(modelobject, result):
    return result.solver.termination_condition

def show_pyomo_getobj(modelobject, result):
    return pyomo_interface.value(modelobject.OBJ)

def show_pymprog_get(input):
    return input.primal

def show_pymprog_getstat(modelobject, result):
    return pymprog_interface.status()

def show_pymprog_getobj(modelobject, result):
    return pymprog_interface.vobj()

variable_getter = {
    "gekko": show_gekko_get,
    "ortools": show_ortools_get,
    "pulp": show_pulp_get,
    "pyomo": show_pyomo_get,
    "pymprog": show_pymprog_get
}

objective_getter = {
    "gekko": show_gekko_getobj,
    "ortools": show_ortools_getobj,
    "pulp": show_pulp_getobj,
    "pyomo": show_pyomo_getobj,
    "pymprog": show_pymprog_getobj
}

status_getter = {
    "gekko": show_gekko_getstat,
    "ortools": show_ortools_getstat,
    "pulp": show_pulp_getstat,
    "pyomo": show_pyomo_getstat,
    "pymprog": show_pymprog_getstat
}


