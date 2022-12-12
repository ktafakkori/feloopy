'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

import gekko as gekko_interface
import timeit 

gekko_solver_selector = {'apopt': 1,
                         'bpopt': 2,
                         'ipopt': 3}

def GenerateSolution(modelobject, objectiveslist, constraintslist, dir, solvername, objectivenumber=0, algoptions=None, email=None):
    if solvername not in gekko_solver_selector.keys():
        raise RuntimeError("Gekko does not support '%s' as a solver. Check the provided name or use another interface." % (solvername))
    
    if dir[objectivenumber] == "min":
        modelobject.Minimize(objectiveslist[objectivenumber])

    if dir[objectivenumber] == "max":
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
        
    Solution = [result, [time_solve_begin, time_solve_end]]
    
    return Solution
