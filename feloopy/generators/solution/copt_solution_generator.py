# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


from coptpy import *
import timeit

copt_solver_selector = {'copt': 'copt'}


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

    if solver_name not in copt_solver_selector.keys():

        raise RuntimeError(
            "Using solver '%s' is not supported by 'copt'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))

    if time_limit != None:
        model_object.setParam(COPT.Param.TimeLimit, time_limit)

    if thread_count != None:
        model_object.setParam(COPT.Param.Threads, thread_count)

    if relative_gap != None:
        model_object.setParam(COPT.Param.MIPGap, relative_gap)

    if absolute_gap != None:
        model_object.setParam(COPT.Param.MIPGapAbs, absolute_gap)

    if log:
    
        ""
        
    else:

        model_object.setParam(COPT.Param.Logging, 0)
        model_object.setParam(COPT.Param.LogToConsole, 0)

    if save != False:
        model_object.setLogFile(f'{save}.log')

    if len(solver_options) != 0:

        for key in solver_options:
            model_object.setParam(key, solver_options[key])

    match debug:

        case False:

            match directions[objective_id]:
                case "min":
                    model_object.setObjective(
                        model_objectives[objective_id], COPT.MINIMIZE)
                case "max":
                    model_object.setObjective(
                        model_objectives[objective_id], COPT.MAXIMIZE)

            counter=0
            for constraint in model_constraints:
                model_object.addConstr(constraint, name = constraint_labels[counter])
                counter+=1

            if save_model != False:

                model_object.write(save_model)

            time_solve_begin = timeit.default_timer()
            result = model_object.solve()
            time_solve_end = timeit.default_timer()
            generated_solution = result, [time_solve_begin, time_solve_end]

    return generated_solution
