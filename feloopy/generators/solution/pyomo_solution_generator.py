# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


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


def generate_solution(features):

    model_object = features['model_object_before_solve']
    model_objectives = features['objectives']
    model_constraints = features['constraints']
    directions = features['directions']
    constraint_labels = features['constraint_labels']
    debug = features['debug_mode']
    time_limit = features['time_limit']
    absolute_gap = features['absolute_gap']
    relative_gap = features['relative_gap']
    thread_count = features['thread_count']
    solver_name = features['solver_name']
    objective_id = features['objective_being_optimized']
    log = features['log']
    save = features['save_solver_log']
    save_model = features['write_model_file']
    email = features['email_address']
    max_iterations = features['max_iterations']
    solver_options = features['solver_options']

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
                    model_object.OBJ = pyomo_interface.Objective(
                        expr=model_objectives[objective_id], sense=pyomo_interface.minimize)

                case "max":
                    model_object.OBJ = pyomo_interface.Objective(
                        expr=model_objectives[objective_id], sense=pyomo_interface.maximize)

            if len(model_constraints)!=0:
                if constraint_labels[0]==None:
                    model_object.constraint = pyomo_interface.ConstraintList()
                    for element in model_constraints:
                        model_object.constraint.add(expr=element)
                else:         
                    model_object.dual = pyomo_interface.Suffix(direction=pyomo_interface.Suffix.IMPORT)
                    model_object.c = pyomo_interface.Constraint(pyomo_interface.Any)
                    counter=0
                    for element in model_constraints:
                        model_object.c[constraint_labels[counter]] = element
                        counter+=1

            if 'online' not in solver_name:

                if solver_name not in pyomo_offline_solver_selector.keys():

                    raise RuntimeError(
                        "Using solver '%s' is not supported by 'pyomo'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))

                solver_manager = pyomo_interface.SolverFactory(
                    pyomo_offline_solver_selector[solver_name])

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
                    result = solver_manager.solve(
                        model_object, tee=tee, options=solver_options)
                    time_solve_end = timeit.default_timer()

            else:

                if solver_name not in pyomo_online_solver_selector.keys():

                    raise RuntimeError(
                        "Using solver '%s' is not supported by 'pyomo'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))

                os.environ['NEOS_EMAIL'] = email
                solver_manager = pyomo_interface.SolverManagerFactory('neos')
                time_solve_begin = timeit.default_timer()
                result = solver_manager.solve(
                    model_object, solver=pyomo_online_solver_selector[solver_name], tee=tee)
                time_solve_end = timeit.default_timer()

            generated_solution = result, [time_solve_begin, time_solve_end]

    return generated_solution
