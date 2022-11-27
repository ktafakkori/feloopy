'''
Name: FelooPy
Version: 0.1.11
Contributors: Keivan Tafakkori
Date: 21 November 2022
License: MIT. (For more details please refer to LICENSE.txt file).
Copyright (c) 2022 Keivan Tafakkori & FELOOP (https://ktafakkori.github.io/)
'''


import itertools as it
import pulp as pulp_interface
import pyomo.environ as pyomo_interface
import gekko as gekko_interface
from ortools.linear_solver import pywraplp as ortools_interface
from .age import *

gekko_status_dict = {0: "not_optimal", 1: "optimal"}


def show_gekko_display(*args, modelobject, result, showstatus=True, showobj=True):
    print("------------------")
    if showstatus:
        print("status:", gekko_status_dict.get(
            modelobject.options.SOLVESTATUS, "unknown"))
    if showobj:
        print("obj:", -modelobject.options.objfcnval)
    print("------------------")
    for arg in args:
        print(str(arg)+":", arg.value)


ortools_status_dict = {0: "optimal", 1: "feasible", 2: "infeasible",
                       3: "unbounded", 4: "abnormal", 5: "model_invalid", 6: "not_solved"}


def show_ortools_display(*args, modelobject, result, showstatus=True, showobj=True):
    print("------------------")
    if showstatus:
        print("status:", ortools_status_dict.get(result, "unknown"))
    if showobj:
        print("obj:", modelobject.Objective().Value())
    print("------------------")
    for arg in args:
        print(str(arg)+":", arg.solution_value())


def show_pulp_display(*args, modelobject, result, showstatus=True, showobj=True):
    print("------------------")
    if showstatus:
        print("status:", pulp_interface.LpStatus[result])
    if showobj:
        print("obj:", pulp_interface.value(modelobject.objective))
    print("------------------")
    for arg in args:
        print(str(arg)+":", arg.varValue)


def show_pyomo_display(*args, modelobject, result, showstatus=True, showobj=True):
    print("------------------")
    if showstatus:
        print("status: ", result.solver.termination_condition)
    if showobj:
        print("obj:", pyomo_interface.value(modelobject.OBJ))
    print("------------------")
    for arg in args:
        print(str(arg)+":", pyomo_interface.value(arg))


def show_ga_display(*args, data):

    BestAgent = data[0]
    BestObj = data[1]
    Direction = data[2]
    VarBound = data[3]
    VarDim = data[4]
    showstatus = data[5]
    showobj = data[6]
    VarLength = data[7]
    VarType = data[8]

    print("------------------")
    if showstatus:
        print("status: ", "near optimal")
    if showobj:
        if Direction == 'max':
            print("obj:", BestObj)
        else:
            print("obj:", BestObj)
    print("------------------")

    for i in args:
        if len(i) == 2:
            encodedvalue = BestAgent[VarLength.get(
                i[0])[0]:VarLength.get(i[0])[1]]
            if VarType.get(i[0]) == "pvar":
                variable = singleagent(i[0], VarBound.get(i[0])[0] + encodedvalue * (
                    VarBound.get(i[0])[1] - VarBound.get(i[0])[0]), [VarDim.get(i[0])], type='pvar')
                print(i[0]+str(i[1])+': ', variable(*i[1]))
            if VarType.get(i[0]) == "ivar":
                variable = singleagent(i[0], VarBound.get(i[0])[0] + encodedvalue * (
                    VarBound.get(i[0])[1] - VarBound.get(i[0])[0]), [VarDim.get(i[0])], type='ivar')
                print(i[0]+str(i[1])+': ', variable(*i[1]))
        else:
            encodedvalue = BestAgent[VarLength.get(i)[0]:VarLength.get(i)[1]]
            if VarType.get(i) == "pvar":
                variable = singleagent(i, VarBound.get(i)[0] + encodedvalue * (
                    VarBound.get(i)[1] - VarBound.get(i)[0]), [VarDim.get(i)], type='pvar')
                print(i+': ', variable[0])
            if VarType.get(i) == "ivar":
                variable = singleagent(i, VarBound.get(i)[0] + encodedvalue * (
                    VarBound.get(i)[1] - VarBound.get(i)[0]), [VarDim.get(i)], type='ivar')
                print(i+': ', variable[0])


show = {
    "gekko": show_gekko_display,
    "ortools": show_ortools_display,
    "pulp": show_pulp_display,
    "pyomo": show_pyomo_display,
    "ga": show_ga_display
}
