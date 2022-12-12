'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

import mip as mip_interface
import timeit

mip_solver_selector = {'cbc': 'cbc'}


def GenerateSolution(modelobject, objectiveslist, constraintslist, dir, solvername, objectivenumber=0, algoptions=None, email=None):
    if solvername not in mip_solver_selector.keys():
        raise RuntimeError(
            "Mip does not support '%s' as a solver. Check the provided name or use another interface." % (solvername))
    for constraint in constraintslist:
        modelobject += constraint
    if dir[objectivenumber] == "min":
        modelobject.objective = mip_interface.minimize(
            objectiveslist[objectivenumber])
    if dir[objectivenumber] == "max":
        modelobject.objective = mip_interface.maximize(
            objectiveslist[objectivenumber])
    time_solve_begin = timeit.default_timer()
    result = modelobject.optimize()
    time_solve_end = timeit.default_timer()
    Solution = [ result, [time_solve_begin, time_solve_end]]
    return Solution
