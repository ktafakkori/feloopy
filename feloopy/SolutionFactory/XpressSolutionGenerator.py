'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

import xpress as xpress_interface
import timeit

xpress_solver_selector = {'xpress': 'xpress'}

def GenerateSolution(modelobject, objectiveslist, constraintslist, dir, solvername, objectivenumber=0, algoptions=None, email=None):
    if solvername not in xpress_solver_selector.keys():
        raise RuntimeError(
            "Xpress does not support '%s' as a solver. Check the provided name or use another interface." % (solvername))
    for constraint in constraintslist:
        modelobject.addConstraint(constraint)
    if dir[objectivenumber] == "min":
        modelobject.setObjective(
            objectiveslist[objectivenumber], sense=xpress_interface.minimize)
    if dir[objectivenumber] == "max":
        modelobject.setObjective(
            objectiveslist[objectivenumber], sense=xpress_interface.maximize)
    time_solve_begin = timeit.default_timer()
    result = modelobject.solve()
    time_solve_end = timeit.default_timer()

    Solution = [result, [time_solve_begin, time_solve_end]]

    return Solution