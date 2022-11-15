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
import os
import timeit
import numpy as np

gekko_solver_selector = {'apopt': 1,
                         'bpopt': 2,
                         'ipopt': 3}


def solve_gekko_model(modelobject, objectiveslist, constraintslist, dir, solvername, objectivenumber=0, email=None):
    if solvername not in gekko_solver_selector.keys():
        raise RuntimeError(
            "Gekko does not support '%s' as a solver. Check the provided name or use another interface." %(solvername))
    if dir == "min":
        modelobject.Minimize(objectiveslist[objectivenumber])
    if dir == "max":
        modelobject.Maximize(objectiveslist[objectivenumber])
    for constraint in constraintslist:
        modelobject.Equation(constraint)
    if 'online' not in solvername:
        modelobject.options.SOLVER = gekko_solver_selector[solvername]
        time_solve_begin = timeit.default_timer()
        result = modelobject.solve(disp=False)
        time_solve_end = timeit.default_timer()
    else:
        gekko_interface.GEKKO(remote=True)
        modelobject.options.SOLVER = gekko_solver_selector[solvername]

        time_solve_begin = timeit.default_timer()
        result = modelobject.solve(disp=False)
        time_solve_end = timeit.default_timer()
    return result, [time_solve_begin, time_solve_end]


ortools_solver_selector = {
    'clp': 'CLP_LINEAR_PROGRAMMING',
    'cbc': 'CBC_MIXED_INTEGER_PROGRAMMING',
    'scip' : 'SCIP_MIXED_INTEGER_PROGRAMMING',
    'glop': 'GLOP_LINEAR_PROGRAMMING',
    'bop': 'BOP_INTEGER_PROGRAMMING',
    'sat': 'SAT_INTEGER_PROGRAMMING',
    'gurobi_': 'GUROBI_LINEAR_PROGRAMMING',
    'gurobi': 'GUROBI_MIXED_INTEGER_PROGRAMMING',
    'cplex_': 'CPLEX_LINEAR_PROGRAMMING',
    'cplex': 'CPLEX_MIXED_INTEGER_PROGRAMMING',
    'xpress_': 'XPRESS_LINEAR_PROGRAMMING',
    'xpress': 'XPRESS_MIXED_INTEGER_PROGRAMMING',
    'glpk_': 'GLPK_LINEAR_PROGRAMMING',
    'glpk': 'GLPK_MIXED_INTEGER_PROGRAMMING'
}

def solve_ortools_model(modelobject, objectiveslist, constraintslist, dir, solvername, objectivenumber=0, email=None):
    if solvername not in ortools_solver_selector.keys():
        raise RuntimeError(
            "Ortools does not support '%s' as a solver. Check the provided name or use another interface." %(solvername))
    if dir == "min":
        modelobject.Minimize(objectiveslist[objectivenumber])
    if dir == "max":
        modelobject.Maximize(objectiveslist[objectivenumber])
    for constraint in constraintslist:
        modelobject.Add(constraint)
    modelobject.CreateSolver(ortools_solver_selector[solvername])
    time_solve_begin = timeit.default_timer()
    result = modelobject.Solve()
    time_solve_end = timeit.default_timer()
    return result, [time_solve_begin, time_solve_end]

pulp_solver_selector = {
    'glpk': pulp_interface.GLPK_CMD(),
    'pyglpk': pulp_interface.PYGLPK(),
    'cplex': pulp_interface.CPLEX_CMD(),
    'cplex_py': pulp_interface.CPLEX_PY(),
    'gurobi': pulp_interface.GUROBI(),
    'gurobi_cmd': pulp_interface.GUROBI_CMD(),
    'mosek': pulp_interface.MOSEK(),
    'xpress': pulp_interface.XPRESS(),
    'cbc': pulp_interface.PULP_CBC_CMD(),
    'coin': pulp_interface.COIN_CMD(),
    'coinmp_dll': pulp_interface.COINMP_DLL(),
    'choco': pulp_interface.CHOCO_CMD(),
    'mipcl': pulp_interface.MIPCL_CMD(),
    'scip': pulp_interface.SCIP_CMD()
    #,
#    'highs': pulp_interface.HiGHS_CMD(),
}


def solve_pulp_model(modelobject, objectiveslist, constraintslist, dir, solvername, objectivenumber=0, email=None):
    if solvername not in pulp_solver_selector.keys():
        raise RuntimeError(
            "Pulp does not support '%s' as a solver. Check the provided name or use another interface." %(solvername))
    if dir == "min":
        modelobject += objectiveslist[objectivenumber]
    if dir == "max":
        modelobject += -objectiveslist[objectivenumber]
    for constraint in constraintslist:
        modelobject+=constraint
    time_solve_begin = timeit.default_timer()
    result = modelobject.solve(solver=pulp_solver_selector[solvername])
    time_solve_end = timeit.default_timer()
    return result, [time_solve_begin, time_solve_end]


pyomo_offline_solver_selector = {
    'baron': 'baron',
    'cbc': 'cbc',
    'conopt': 'conopt',
    'cplex': 'cplex',
    'cplex_direct': 'cplex_direct',
    'cplex_persistent': 'cplex_persistent',
    'cyipopt': 'cyipopt',
    'gams': 'gams',
    'asl': 'asl',
    'gdpopt': 'gdpopt',
    'gdpopt.gloa': 'gdpopt.gloa',
    'gdpopt.lbb': 'gdpopt.lbb',
    'gdpopt.loa': 'gdpopt.loa',
    'gdpopt.ric': 'gdpopt.ric',
    'glpk': 'glpk',
    'gurobi': 'gurobi',
    'gurobi_direct': 'gurobi_direct',
    'gurobi_persistent': 'gurobi_prsistent',
    'ipopt': 'ipopt',
    'mindtpy': 'mindtpy',
    'mosek': 'mosek',
    'mosek_direct': 'mosek_direct',
    'mosek_persistent': 'mosek_persistent',
    'mpec_minlp': 'mpec_minlp',
    'mpec_nlp': 'mpec_nlp',
    'multistart': 'multistart',
    'path': 'path',
    'scip': 'scip',
    'trustregion': 'trustregion',
    'xpress': 'xpress',
    'xpress_direct': 'xpress_direct',
    'xpress_persistent': 'xpress_persistent'
}

pyomo_online_solver_selector = {
    'bonmin_online': 'bonmin',
    'cbc_online': 'cbc',
    'conopt_online': 'conopt',
    'couenne_online': 'couenne',
    'cplex_online': 'cplex',
    'filmint_online': 'filmint',
    'filter_online': 'filter',
    'ipopt_online': 'ipopt',
    'knitro_online': 'knitro',
    'l-bfgs-b_online': 'l-bfgs-b',
    'lancelot_online': 'lancelot',
    'lgo_online': 'lgo',
    'loqo_online': 'loqo',
    'minlp_online': 'minlp',
    'minos_online': 'minos',
    'minto_online': 'minto',
    'mosek_online': 'mosek',
    'octeract_online': 'octeract',
    'ooqp_online': 'ooqp',
    'path_online': 'path',
    'raposa_online': 'raposa',
    'snopt_online': 'snopt'
}

def solve_pyomo_model(modelobject, objectiveslist, constraintslist, dir, solvername, objectivenumber=0, email=None):
    if dir == "min":
        modelobject.OBJ = pyomo_interface.Objective(
            expr=objectiveslist[objectivenumber], sense=pyomo_interface.minimize)
    if dir == "max":
        modelobject.OBJ = pyomo_interface.Objective(
            expr=objectiveslist[objectivenumber], sense=pyomo_interface.maximize)    
    modelobject.constraint = pyomo_interface.ConstraintList()
    for element in constraintslist:
        modelobject.constraint.add(expr=element)
    if 'online' not in solvername:
        if solvername not in pyomo_offline_solver_selector.keys():
            raise RuntimeError(
                "Pyomo does not support '%s' as a solver. Check the provided name or use another interface." %(solvername))
        solver_manager = pyomo_interface.SolverFactory(
            pyomo_offline_solver_selector[solvername])
        time_solve_begin = timeit.default_timer()
        result = solver_manager.solve(modelobject)
        time_solve_end = timeit.default_timer()
    else:
        if solvername not in pyomo_online_solver_selector.keys():
            raise RuntimeError(
                "Neos does not support '%s' as a solver. Check the provided name or use another interface." %(solvername))
        os.environ['NEOS_EMAIL'] = email
        solver_manager = pyomo_interface.SolverManagerFactory('neos')
        time_solve_begin = timeit.default_timer()
        result = solver_manager.solve(
            modelobject, solver=pyomo_online_solver_selector[solvername])
        time_solve_end = timeit.default_timer()
    return result, [time_solve_begin, time_solve_end]

pymprog_solver_selector = {'glpk':'glpk'}

def solve_pymprog_model(modelobject, objectiveslist, constraintslist, dir, solvername, objectivenumber=0, email=None):
    if solvername not in pymprog_solver_selector.keys():
        raise RuntimeError(
            "Pymprog does not support '%s' as a solver. Check the provided name or use another interface." %(solvername))
    if dir == "min":
        pymprog_interface.minimize(objectiveslist[objectivenumber], 'objective')
    if dir == "max":
        pymprog_interface.maximize(objectiveslist[objectivenumber], 'objective')
    for constraint in constraintslist:
        constraint
    time_solve_begin = timeit.default_timer()
    result = pymprog_interface.solve()
    time_solve_end = timeit.default_timer()
    return result, [time_solve_begin, time_solve_end]

def solve_ga_model(objectiveslist, constraintslist, dir, objectivenumber=0):
    penalty = np.amax(np.array([0]+constraintslist, dtype=object))
    if dir == "min":
        return +objectiveslist[0] - (penalty-0)**2
    if dir == "max":
        return -objectiveslist[0] + (penalty-0)**2

def implement_ga_model(model,dir):
    time_solve_begin = timeit.default_timer()
    model.run()
    time_solve_end = timeit.default_timer()
    Chronometer = [time_solve_begin, time_solve_end]
    bestagent = model.best_variable
    bestallreward = - model.best_function if dir == 'max' else  model.best_function 
    result = [bestagent,bestallreward]
    return result, Chronometer


solver = {
    "gekko": solve_gekko_model,
    "ortools": solve_ortools_model,
    "pulp": solve_pulp_model,
    "pyomo": solve_pyomo_model,
    "pymprog": solve_pymprog_model,
    "ga": solve_ga_model
}

implementor = {
    "ga": implement_ga_model
}
def ava_solver(interface):
    if interface == "gekko":
        print()
        print("-------------------------")
        print("Available LOCAL\CLOUD:   ")
        print("-------------------------")
        print(gekko_solver_selector.keys())
        print()
    if interface == "ortools":
        print()
        print("-------------------------")
        print("Available LOCAL:   ")
        print("-------------------------")
        print(ortools_solver_selector.keys())
        print()
    if interface == "pulp":
        print()
        print("-------------------------")
        print("Available LOCAL:   ")
        print("-------------------------")
        print(pulp_solver_selector.keys())
        print()
    if interface == "pyomo":
        print()
        print("-------------------------")
        print("Available LOCAL:   ")
        print("-------------------------")
        print(pyomo_offline_solver_selector.keys())
        print()
        print()
        print("-------------------------")
        print("Available CLOUD:   ")
        print("-------------------------")
        print(pyomo_online_solver_selector.keys())
        print()
    if interface == "pymprog":
        print()
        print("-------------------------")
        print("Available LOCAL:   ")
        print("-------------------------")
        print(pymprog_solver_selector.keys())
        print()
    if interface == "ga":
        print()
        print("-------------------------")
        print("Available LOCAL:   ")
        print("-------------------------")
        print("geneticalgorithm")
        print()

ava_solver = {
    "gekko": ava_solver,
    "ortools": ava_solver,
    "pulp": ava_solver,
    "pymprog": ava_solver,
    "pyomo": ava_solver
}


