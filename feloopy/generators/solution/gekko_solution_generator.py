# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


import gekko as gekko_interface
import timeit

gekko_solver_selector = {'apopt': 1,
                         'bpopt': 2,
                         'ipopt': 3}

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

    if solver_name not in gekko_solver_selector.keys():
        raise RuntimeError(
            "Using solver '%s' is not supported by 'gekko'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))

    if len(solver_options) != 0:

        model_object.solver_options = [
            f'{key} {solver_options[key]}' for key in solver_options]

    if log:
        disp = True

    else:
        disp = False

    if max_iterations != None:
        model_object.options.MAX_ITER = max_iterations

    match debug:

        case False:

            match directions[objective_id]:
                case "min":
                    model_object.Minimize(model_objectives[objective_id])
                case "max":
                    model_object.Maximize(model_objectives[objective_id])

            for constraint in model_constraints:
                model_object.Equation(constraint)

            if 'online' not in solver_name:
                model_object.options.SOLVER = gekko_solver_selector[solver_name]
                time_solve_begin = timeit.default_timer()
                result = model_object.solve(disp=disp)
                time_solve_end = timeit.default_timer()

            else:

                gekko_interface.GEKKO(remote=True)
                model_object.options.SOLVER = gekko_solver_selector[solver_name]
                time_solve_begin = timeit.default_timer()
                result = model_object.solve(disp=disp)
                time_solve_end = timeit.default_timer()

            generated_solution = [result, [time_solve_begin, time_solve_end]]

    return generated_solution
