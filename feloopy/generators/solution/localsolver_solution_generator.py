'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.8)                               |
|  Modified: Wednesday, 27th September 2023 11:32:45 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''

import localsolver as ls
import time

def generate_solution(features):

    model_object = features['model_object_before_solve']
    directions = features['directions']
    objective_id = features['objective_being_optimized']
    time_limit = features['time_limit']
    thread_count = features['thread_count']
    save_model = features['write_model_file']

    ls_env = ls.LocalSolver()

    if time_limit != None:
        ls_env.param.time_limit = time_limit

    if thread_count != None:
        ls_env.param.nb_threads = thread_count

    match directions[objective_id]:
        case 'min':
            model_object.minimize(model_object[objective_id])
        case 'max':
            model_object.maximize(model_object[objective_id])

    time_solve_begin = time.time()
    ls_env.solve()
    time_solve_end = time.time()
    
    generated_solution = [ls_env.solution, [time_solve_begin, time_solve_end]]

    if save_model != False:
        model_object.write_model(save_model)

    return generated_solution
