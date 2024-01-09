# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


import cplex
from docplex.mp.model import Model as CPLEXMODEL
import docplex as cplex_interface
import timeit
from docplex.util.environment import get_environment
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

    if solver_name not in cplex_solver_selector.keys():
        raise RuntimeError(
            "Using solver '%s' is not supported by 'cplex'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))

    if time_limit != None:
        model_object.parameters.timelimit.set(time_limit)

    if thread_count != None:
        model_object.parameters.threads = thread_count

    if relative_gap != None:
        model_object.parameters.mip.tolerances.mipgap = relative_gap

    if absolute_gap != None:
        model_object.parameters.mip.tolerances.absmipgap = absolute_gap

    if log:
        model_object.context.solver.log_output = True
        model_object.context.solver.verbose = 5

    if max_iterations != None:
        "None"

    if len(solver_options) != 0:
        try:
            for key in solver_options:
                try:
                    model_object.parameters.mip.__setattr__(
                        key, solver_options[key])
                except:
                    model_object.parameters.__setattr__(
                        key, solver_options[key])
        except:
            with cplex.Cplex() as solver:
                for key in solver_options:
                    solver.parameters.__setattr__(key, solver_options[key])
        try:
            model_object.context.solver.__setattr__(key, solver_options[key])
        except:
            "None"

    match debug:

        case False:

            match directions[objective_id]:

                case 'min':
                    model_object.set_objective(
                        'min', model_objectives[objective_id])

                case 'max':
                    model_object.set_objective(
                        'max', model_objectives[objective_id])
            
            model_object.add_constraints(model_constraints, names=constraint_labels)
            
            """
            counter=0
            for constraint in model_constraints:
                model_object.add_constraint(constraint, ctname=constraint_labels[counter])
                counter+=1
            """

            if save_model != False:

                if '.lp' in save_model:
                    model_object.export_as_lp(path=save_model)
                if '.mps' in save_model:
                    model_object.export_as_mps(path=save_model)
                else:
                    model_object.export_as_lp(path=save_model)

            time_solve_begin = timeit.default_timer()
            result = model_object.solve()
            time_solve_end = timeit.default_timer()
            generated_solution = [result, [time_solve_begin, time_solve_end]]

    if save != False:
        f = open(save, "w+")

        with cplex.Cplex() as cpx, open(save, "w+") as cplexlog:
            cpx.set_results_stream(cplexlog)
            cpx.set_warning_stream(cplexlog)
            cpx.set_error_stream(cplexlog)
            cpx.set_log_stream(cplexlog)
        with open(f"{save}.log", "w+") as solfile:

            solfile.write(model_object.solution.to_string())

    return generated_solution
