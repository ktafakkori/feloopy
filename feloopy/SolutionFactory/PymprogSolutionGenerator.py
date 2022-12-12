'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

import pymprog as pymprog_interface
import timeit

pymprog_solver_selector = {'glpk': 'glpk'}

def GenerateSolution(modelobject, objectiveslist, constraintslist, dir, solvername, objectivenumber=0, algoptions=None, email=None):
    if solvername not in pymprog_solver_selector.keys():
        raise RuntimeError(
            "Pymprog does not support '%s' as a solver. Check the provided name or use another interface." % (solvername))
    if dir[objectivenumber] == "min":
        pymprog_interface.minimize(
            objectiveslist[objectivenumber], 'objective')
    if dir[objectivenumber] == "max":
        pymprog_interface.maximize(
            objectiveslist[objectivenumber], 'objective')
    for constraint in constraintslist:
        constraint
    time_solve_begin = timeit.default_timer()
    result = pymprog_interface.solve()
    time_solve_end = timeit.default_timer()
    Solution = result, [time_solve_begin, time_solve_end]
    return Solution