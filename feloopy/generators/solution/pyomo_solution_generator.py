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

def generate_solution(model_object, objectives_list, constraints_list, dir, labels, mode, solver_name, objective_number=0, algorithm_options=None, user_email=None):

    match mode:

        case False:

            match dir[objective_number]:

                case "min":
                    model_object.OBJ = pyomo_interface.Objective(expr=objectives_list[objective_number], sense=pyomo_interface.minimize)
                
                case "max":
                    model_object.OBJ = pyomo_interface.Objective(expr=objectives_list[objective_number], sense=pyomo_interface.maximize)

            model_object.constraint = pyomo_interface.ConstraintList()

            for element in constraints_list:

                model_object.constraint.add(expr=element)

            if 'online' not in solver_name:
                
                if solver_name not in pyomo_offline_solver_selector.keys():

                     raise RuntimeError("Using solver '%s' is not supported by 'pyomo'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))
                
                solver_manager = pyomo_interface.SolverFactory(pyomo_offline_solver_selector[solver_name])

                if algorithm_options == None:

                    time_solve_begin = timeit.default_timer()
                    result = solver_manager.solve(model_object)
                    time_solve_end = timeit.default_timer()

                else:

                    time_solve_begin = timeit.default_timer()
                    result = solver_manager.solve(model_object, options=algorithm_options)
                    time_solve_end = timeit.default_timer()     

            else:
                
                if solver_name not in pyomo_online_solver_selector.keys():

                    raise RuntimeError("Using solver '%s' is not supported by 'pyomo'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))
                
                os.environ['NEOS_EMAIL'] = user_email
                solver_manager = pyomo_interface.SolverManagerFactory('neos')
                time_solve_begin = timeit.default_timer()
                result = solver_manager.solve(model_object, solver=pyomo_online_solver_selector[solver_name])
                time_solve_end = timeit.default_timer()

            generated_solution = result, [time_solve_begin, time_solve_end]
        
    return generated_solution