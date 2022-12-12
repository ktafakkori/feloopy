'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

import gurobipy as gurobi_interface
import timeit


gurobi_solver_selector = {'gurobi': 'gurobi'}

def GenerateSolution(modelobject, objectiveslist, constraintslist, dir, solvername, objectivenumber=0, algoptions=None, email=None):
    if solvername not in gurobi_solver_selector.keys():
        raise RuntimeError(
            "Gurobi does not support '%s' as a solver. Check the provided name or use another interface." % (solvername))
    if dir[objectivenumber] == "min":
        modelobject.setObjective(
            objectiveslist[objectivenumber], gurobi_interface.GRB.MINIMIZE)
    if dir[objectivenumber] == "max":
        modelobject.setObjective(
            objectiveslist[objectivenumber], gurobi_interface.GRB.MAXIMIZE)
    for constraint in constraintslist:
        modelobject.addConstr(constraint)
    time_solve_begin = timeit.default_timer()
    result = modelobject.optimize()
    time_solve_end = timeit.default_timer()
    GeneratedSolution = result, [time_solve_begin, time_solve_end]

    return GeneratedSolution
