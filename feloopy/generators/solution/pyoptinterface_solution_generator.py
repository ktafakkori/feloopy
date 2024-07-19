# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import pyoptinterface as poi

poi_solver_selector = {'highs': 'highs'}

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

    if solver_name not in poi_solver_selector.keys():
        raise RuntimeError("Using solver '%s' is not supported by 'pyoptinterface'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))

    if log:
        model_object.set_model_attribute(poi.ModelAttribute.Silent, False)
    else:
        model_object.set_model_attribute(poi.ModelAttribute.Silent, True)
        
    match debug:

        case False:

            counter=0

            for constraint in model_constraints:
  
                if constraint[1] in ['<=', 'le', 'leq', '=l=']:
                    if constraint_labels[counter]:
                        model_object.add_linear_constraint(constraint[0], poi.Leq, constraint[2], name=constraint_labels[counter])
                    else:
                        model_object.add_linear_constraint(constraint[0], poi.Leq, constraint[2])
                        
                if constraint[1] in ['>=', 'ge', 'geq', '=g=']:

                    if constraint_labels[counter]:
                        model_object.add_linear_constraint(constraint[0], poi.Geq, constraint[2], name=constraint_labels[counter])
                    else:
                        model_object.add_linear_constraint(constraint[0], poi.Geq, constraint[2])
                        
                if constraint[1] in ['==', 'eq', '=e=']:
                    if constraint_labels[counter]:
                        model_object.add_linear_constraint(constraint[0], poi.Eq, constraint[2], name=constraint_labels[counter])
                    else:
                        model_object.add_linear_constraint(constraint[0], poi.Eq, constraint[2])
                counter+=1

            match directions[objective_id]:

                case 'min':
                    model_object.set_objective(model_objectives[objective_id], poi.ObjectiveSense.Minimize)
                    
                case 'max':
                    model_object.set_objective(model_objectives[objective_id], poi.ObjectiveSense.Maximize)
                
            time_solve_begin = timeit.default_timer()
            model_object.optimize()
            time_solve_end = timeit.default_timer()

            generated_solution = [None, [time_solve_begin, time_solve_end]]

    return generated_solution
