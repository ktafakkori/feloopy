# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

seeker_solver_selector = {'seeker': 'seeker'}
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
    max_iterations = features['max_iterations']
    solver_options = features['solver_options']

    if solver_name not in seeker_solver_selector.keys():
        raise RuntimeError("Using solver '%s' is not supported by 'seeker'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))

    if time_limit != None:
        timeLimit = time_limit
    else:
        timeLimit = 1e9
        
    if "lb" in solver_options.keys():
        lowerBound = solver_options['lb']
    else:
        lowerBound = -1e20

    if "ub" in solver_options.keys():
        upperBound = solver_options['ub']
    else:
        upperBound = 1e20
        
    match debug:

        case False:

            counter=0

            for constraint in model_constraints:
  
                if constraint[1] in ['<=', 'le', 'leq', '=l=']:
                    model_object.enforce_leq(constraint[0], constraint[2])
                            
                if constraint[1] in ['>=', 'ge', 'geq', '=g=']:
                    model_object.enforce_geq(constraint[0], constraint[2])

                if constraint[1] in ['==', 'eq', '=e=']:
                    model_object.enforce_eq(constraint[0], constraint[2])

                if constraint[1] in ['<', 'lt']:
                    model_object.enforce_lt(constraint[0], constraint[2])
                    
                if constraint[1] in ['>', 'gt']:
                    model_object.enforce_gt(constraint[0], constraint[2])
                                      
                if constraint[1] in ['!=', 'neq']:
                    model_object.enforce_neq(constraint[0], constraint[2])

                counter+=1

            match directions[objective_id]:

                case 'min':
                    time_solve_begin = timeit.default_timer()
                    model_object.minimize(model_objectives[objective_id], lowerBound=lowerBound, timeLimit=timeLimit)
                    time_solve_end = timeit.default_timer()
                    objective = model_objectives[objective_id]
                    
                case 'max':
                    time_solve_begin = timeit.default_timer()
                    model_object.maximize(model_objectives[objective_id], upperBound=upperBound, timeLimit=timeLimit)
                    time_solve_end = timeit.default_timer()
                    objective = model_objectives[objective_id]
                    

            generated_solution = [objective, [time_solve_begin, time_solve_end]]

    return generated_solution
