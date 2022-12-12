'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

import pyomo.environ as pyomo_interface
import timeit
import os

pyomo_offline_solver_selector = {
    'baron': 'baron',
    'cbc': 'cbc',
    'conopt': 'conopt',
    'cplex': 'cplex',
    'cplex_direct': 'cplex_direct',
    'cplex_persistent': 'cplex_persistent',
    'cyipopt': 'cyipopt',
    'gams': 'gams',
    'highs': 'highs',
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

def GenerateSolution(modelobject, objectiveslist, constraintslist, dir, solvername, objectivenumber=0, algoptions=None, email=None):
    
    if dir[objectivenumber] == "min":
        
        modelobject.OBJ = pyomo_interface.Objective(expr=objectiveslist[objectivenumber], sense=pyomo_interface.minimize)
    
    if dir[objectivenumber] == "max":
        
        modelobject.OBJ = pyomo_interface.Objective(expr=objectiveslist[objectivenumber], sense=pyomo_interface.maximize)

    modelobject.constraint = pyomo_interface.ConstraintList()

    for element in constraintslist:
        
        modelobject.constraint.add(expr=element)

    if 'online' not in solvername:
        
        if solvername not in pyomo_offline_solver_selector.keys():

            raise RuntimeError("Pyomo does not support '%s' as a solver. Check the provided name or use another interface." % (solvername))
        
        solver_manager = pyomo_interface.SolverFactory(pyomo_offline_solver_selector[solvername])

        if algoptions == None:

            time_solve_begin = timeit.default_timer()

            result = solver_manager.solve(modelobject)

            time_solve_end = timeit.default_timer()

        else:

            time_solve_begin = timeit.default_timer()

            result = solver_manager.solve(modelobject, options=algoptions)

            time_solve_end = timeit.default_timer()     

    else:
        
        if solvername not in pyomo_online_solver_selector.keys():
           
            raise RuntimeError("Neos does not support '%s' as a solver. Check the provided name or use another interface." % (solvername))
        
        os.environ['NEOS_EMAIL'] = email
        
        solver_manager = pyomo_interface.SolverManagerFactory('neos')
        
        time_solve_begin = timeit.default_timer()
        
        result = solver_manager.solve(modelobject, solver=pyomo_online_solver_selector[solvername])
        
        time_solve_end = timeit.default_timer()

    Solution = result, [time_solve_begin, time_solve_end]
    
    return Solution