'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

import cvxpy as cvxpy_interface
import timeit

cvxpy_solver_selector = {
    'qsqp': cvxpy_interface.OSQP,
    'ecos': cvxpy_interface.ECOS,
    'cvxopt': cvxpy_interface.CVXOPT,
    'scs': cvxpy_interface.SCS,
    'highs': [cvxpy_interface.SCIPY, {"method": "highs"}],
    'glop': cvxpy_interface.GLOP,
    'glpk': cvxpy_interface.GLPK,
    'glpk_mi': cvxpy_interface.GLPK_MI,
    'gurobi': cvxpy_interface.GUROBI,
    'mosek': cvxpy_interface.MOSEK,
    'cbc': cvxpy_interface.CBC,
    'cplex': cvxpy_interface.CPLEX,
    'nag': cvxpy_interface.NAG,
    'pdlp': cvxpy_interface.PDLP,
    'scip': cvxpy_interface.SCIP,
    'xpress': cvxpy_interface.XPRESS}


def GenerateSolution(modelobject, objectiveslist, constraintslist, dir, solvername, objectivenumber=0, algoptions=None, email=None):
    if solvername not in cvxpy_solver_selector.keys():
        raise RuntimeError(
            "Cvxpy does not support '%s' as a solver. Check the provided name or use another interface." % (solvername))
    if dir[objectivenumber] == "min":
        obj = cvxpy_interface.Minimize(objectiveslist[objectivenumber])
    if dir[objectivenumber] == "max":
        obj = cvxpy_interface.Maximize(objectiveslist[objectivenumber])
    prob = cvxpy_interface.Problem(obj, constraintslist)
    time_solve_begin = timeit.default_timer()
    result = prob.solve(solver=cvxpy_solver_selector[solvername])
    time_solve_end = timeit.default_timer()
    return result, [time_solve_begin, time_solve_end]
