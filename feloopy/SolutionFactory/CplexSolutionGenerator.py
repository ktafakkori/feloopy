'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

from docplex.mp.model import Model as CPLEXMODEL
import docplex as cplex_interface
import timeit

cplex_solver_selector = {'cplex': 'cplex'}

def GenerateSolution(modelobject, objectiveslist, constraintslist, dir, solvername, objectivenumber=0, algoptions=None, email=None):
    
    if solvername not in cplex_solver_selector.keys():
        
        raise RuntimeError("Cplex does not support '%s' as a solver. Check the provided name or use another interface." % (solvername))
    
    if dir[objectivenumber] == "min":
        
        modelobject.set_objective('min', objectiveslist[objectivenumber])
    
    if dir[objectivenumber] == "max":
        
        modelobject.set_objective('max', objectiveslist[objectivenumber])
    
    for constraint in constraintslist:
        
        modelobject.add_constraint(constraint)
    
    time_solve_begin = timeit.default_timer()

    result = modelobject.solve()
    
    time_solve_end = timeit.default_timer()

    GeneratedSolution = [result, [time_solve_begin, time_solve_end]]
    return GeneratedSolution