# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import xpress as xpress_interface
import timeit

xpress_solver_selector = {'xpress': 'xpress'}


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
        model_object.controls.outputlog = 0

    if solver_name not in xpress_solver_selector.keys():
        raise RuntimeError(
            "Using solver '%s' is not supported by 'xpress'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))

    match debug:

        case False:

            for constraint in model_constraints:
                model_object.addConstraint(constraint)

            match directions[objective_id]:

                case "min":
                    model_object.setObjective(
                        model_objectives[objective_id], sense=xpress_interface.minimize)

                case "max":
                    model_object.setObjective(
                        model_objectives[objective_id], sense=xpress_interface.maximize)

            time_solve_begin = timeit.default_timer()
            result = model_object.solve()
            time_solve_end = timeit.default_timer()
            generated_solution = [result, [time_solve_begin, time_solve_end]]

    return generated_solution
