# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


import cylp as cylp_interface
from cylp.cy import CyClpSimplex
import timeit

cylp_solver_selector = {'cbc': 'cbc', 'clp':'clp', 'cgl':'cgl'}


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

    if solver_name not in cylp_solver_selector.keys():
        raise RuntimeError(
            "Using solver '%s' is not supported by 'cylp'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))

    match debug:

        case False:

            match directions[objective_id]:
                case 'min':
                    model_object.objective = 1*(model_objectives[objective_id])
                case 'max':
                    model_object.objective = -1 * \
                        (model_objectives[objective_id])

            for constraint in model_constraints:
                model_object += constraint

            cbcModel = cylp_interface.cy.CyClpSimplex(
                model_object).getCbcModel()
            time_solve_begin = timeit.default_timer()
            result = cbcModel.solve()
            time_solve_end = timeit.default_timer()
            generated_solution = [result, [time_solve_begin, time_solve_end]]

    return generated_solution
