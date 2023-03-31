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
    'l-bfgs-b_online': 'l-bfgs-variable_bound',
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

def generate_solution(model_object, model_objectives, model_constraints, directions, constraint_labels, debug, time_limit, absolute_gap, relative_gap, thread_count, solver_name, log, save, max_iterations, objective_id, solver_options, email):

    if log:
        tee = True
    else:
        tee = False

    if max_iterations != None:
        "None"

    match debug:

        case False:

            match directions[objective_id]:

                case "min":
                    model_object.OBJ = pyomo_interface.Objective(expr=model_objectives[objective_id], sense=pyomo_interface.minimize)
                
                case "max":
                    model_object.OBJ = pyomo_interface.Objective(expr=model_objectives[objective_id], sense=pyomo_interface.maximize)

            model_object.constraint = pyomo_interface.ConstraintList()

            for element in model_constraints:

                model_object.constraint.add(expr=element)

            if 'online' not in solver_name:
                
                if solver_name not in pyomo_offline_solver_selector.keys():

                     raise RuntimeError("Using solver '%s' is not supported by 'pyomo'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))
                
                solver_manager = pyomo_interface.SolverFactory(pyomo_offline_solver_selector[solver_name])

                if thread_count != None:
                
                    solver_manager.options['threads'] = thread_count

                if time_limit != None:

                    solver_manager.options['timelimit'] = time_limit 

                if relative_gap != None:

                    solver_manager.options['mipgap'] = relative_gap
                
                if len(solver_options) == 0:
                    time_solve_begin = timeit.default_timer()
                    result = solver_manager.solve(model_object, tee=tee)
                    time_solve_end = timeit.default_timer()

                else:

                    time_solve_begin = timeit.default_timer()
                    result = solver_manager.solve(model_object, tee=tee, options=solver_options)
                    time_solve_end = timeit.default_timer()     

            else:
                
                if solver_name not in pyomo_online_solver_selector.keys():

                    raise RuntimeError("Using solver '%s' is not supported by 'pyomo'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))
                
                os.environ['NEOS_EMAIL'] = email
                solver_manager = pyomo_interface.SolverManagerFactory('neos')
                time_solve_begin = timeit.default_timer()
                result = solver_manager.solve(model_object, solver=pyomo_online_solver_selector[solver_name], tee=tee)
                time_solve_end = timeit.default_timer()

            generated_solution = result, [time_solve_begin, time_solve_end]
        
    return generated_solution