'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

from linopy import Model as LINOPYMODEL
import timeit

linopy_solver_selector = {'cbc': 'cbc', 'glpk': 'glpk', 'highs': 'highs',
                          'gurobi': 'gurobi', 'xpress': 'xpress', 'cplex': 'cplex'}


def GenerateSolution(modelobject, objectiveslist, constraintslist, dir, solvername, objectivenumber=0, algoptions=None, email=None):
    if solvername not in linopy_solver_selector.keys():
        raise RuntimeError(
            "Linopy does not support '%s' as a solver. Check the provided name or use another interface." % (solvername))
    if dir[objectivenumber] == "min":
        modelobject.add_objective(objectiveslist[objectivenumber])
    if dir[objectivenumber] == "max":
        modelobject.add_objective(-objectiveslist[objectivenumber])
    for constraint in constraintslist:
        modelobject.add_constraints(constraint)
    time_solve_begin = timeit.default_timer()
    result = modelobject.solve(solver_name=solvername)
    time_solve_end = timeit.default_timer()
    Solution = [result, [time_solve_begin, time_solve_end]]
    return Solution
