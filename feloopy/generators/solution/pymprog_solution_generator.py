'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.8)                               |
|  Modified: Wednesday, 27th September 2023 11:33:32 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''

import pymprog as pymprog_interface
import timeit

pymprog_solver_selector = {'glpk': 'glpk'}


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

        ""

    else:

        msg_lev = pymprog_interface.glpk.GLP_MSG_OFF

    if time_limit != None:
        tmlim = time_limit
    else:
        tmlim= None

    if solver_name not in pymprog_solver_selector.keys():
        raise RuntimeError(
            "Using solver '%s' is not supported by 'pymprog'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))

    match debug:

        case False:

            match directions[objective_id]:

                case "min":
                    pymprog_interface.minimize(
                        model_objectives[objective_id], 'objective')
                case "max":
                    pymprog_interface.maximize(
                        model_objectives[objective_id], 'objective')

            for constraint in model_constraints:
                constraint
            time_solve_begin = timeit.default_timer()
            result = pymprog_interface.solve(msg_lev=msg_lev, tmlim=tmlim)
            time_solve_end = timeit.default_timer()
            generated_solution = result, [time_solve_begin, time_solve_end]

    return generated_solution
