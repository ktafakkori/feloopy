# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import timeit

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
    obj_operators = features['obj_operators']

    if log:
        display=True
    else:
        display=False

    if solver_name =='scipy':
        from rsome import lpg_solver
        solver = lpg_solver
    
    elif solver_name == 'cylp':
        from rsome import clp_solver
        solver = clp_solver
    
    elif solver_name == 'ortools':
        from rsome import ort_solver
        solver = ort_solver
    
    elif solver_name == 'ecos':
        from rsome import eco_solver
        solver = eco_solver

    elif solver_name == 'gurobi':
        from rsome import grb_solver
        solver = grb_solver
    
    elif solver_name == 'cplex':
        from rsome import cpx_solver
        solver = cpx_solver
    
    elif solver_name == 'mosek':
        from rsome import msk_solver
        solver = msk_solver
    
    elif solver_name =='copt':
        from rsome import cpt_solver
        solver = cpt_solver

    elif solver_name =='cvxpy':
        from rsome import cvx_solver
        solver = cvx_solver

    else:
        raise RuntimeError(
            "Using solver '%s' is not supported by 'rsome_dro'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))

    match debug:

        case False:

            match directions[objective_id]:

                case "min":
                    if len(obj_operators)==0:                    
                        model_object.min(model_objectives[objective_id])
                    elif obj_operators[objective_id] == 'sup':
                        model_object.minsup(*model_objectives[objective_id])
                case "max":
                    if len(obj_operators)==0:
                        model_object.max(model_objectives[objective_id])
                    elif obj_operators[objective_id] == 'inf':
                        model_object.maxinf(*model_objectives[objective_id])

            for constraint in model_constraints:
                model_object.st(constraint)

            time_solve_begin = timeit.default_timer()
            result = model_object.solve(solver,display,solver_options)
            time_solve_end = timeit.default_timer()
            generated_solution = [result, [time_solve_begin, time_solve_end]]

    return generated_solution

