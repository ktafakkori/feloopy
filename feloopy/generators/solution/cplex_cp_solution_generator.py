# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


from docplex.cp.config import context
from docplex.cp.model import *
from docplex.util.environment import get_environment
import timeit

env = get_environment()
cplex_solver_selector = {'cplex': 'cplex'}

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

    if solver_name is None:
        solver_name = 'cplex'

    if solver_name not in cplex_solver_selector.keys():
        raise RuntimeError(f"Using solver '{solver_name}' is not supported by 'cplex_cp'! \nPossible fixes: \n1) Check the solver name. \n2) Use anotherinterface.")

    if not debug:
        if directions:
            if directions[objective_id] == 'min':
                model_object.add(model_object.minimize(model_objectives[objective_id]))
            elif directions[objective_id] == 'max':
                model_object.add(model_object.maximize(model_objectives[objective_id]))

        for constraint in model_constraints:
            model_object.add(constraint)

        time_solve_begin = timeit.default_timer()
        result = model_object.solve(TimeLimit=time_limit)
        time_solve_end = timeit.default_timer()

        generated_solution = [result, [time_solve_begin, time_solve_end]]

    return generated_solution