'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

import pulp as pulp_interface

import timeit

pulp_solver_selector = {

    'cbc': pulp_interface.PULP_CBC_CMD(),

    'choco': pulp_interface.CHOCO_CMD(),

    'coin': pulp_interface.COIN_CMD(),

    'coinmp_dll': pulp_interface.COINMP_DLL(),

    'cplex_py': pulp_interface.CPLEX_PY(),

    'cplex': pulp_interface.CPLEX_CMD(),

    'glpk': pulp_interface.GLPK_CMD(),

    'gurobi_cmd': pulp_interface.GUROBI_CMD(),

    'gurobi': pulp_interface.GUROBI(),

    'highs': pulp_interface.HiGHS_CMD(),

    'mipcl': pulp_interface.MIPCL_CMD(),

    'mosek': pulp_interface.MOSEK(),

    'pyglpk': pulp_interface.PYGLPK(),

    'scip': pulp_interface.SCIP_CMD(),

    'xpress_py': pulp_interface.XPRESS_PY(),

    'xpress': pulp_interface.XPRESS()
}


def GenerateSolution(modelobject, objectiveslist, constraintslist, dir, solvername, objectivenumber=0, algoptions=None, email=None):

    if solvername not in pulp_solver_selector.keys():

        raise RuntimeError(
            "Pulp does not support '%s' as a solver. Check the provided name or use another interface." % (solvername))

    if dir[objectivenumber] == "min":

        modelobject += objectiveslist[objectivenumber]

    if dir[objectivenumber] == "max":

        modelobject += -objectiveslist[objectivenumber]

    for constraint in constraintslist:

        modelobject += constraint

    time_solve_begin = timeit.default_timer()

    result = modelobject.solve(solver=pulp_solver_selector[solvername])

    time_solve_end = timeit.default_timer()

    Solution = [result, [time_solve_begin, time_solve_end]]

    return Solution