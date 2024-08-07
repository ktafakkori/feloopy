# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

from ortools.math_opt.python import mathopt
import timeit

mathopt_solver_selector = {
    'cp-sat': mathopt.SolverType.CP_SAT,
    'cpsat': mathopt.SolverType.CP_SAT,
    'ecos': mathopt.SolverType.ECOS,
    'glop': mathopt.SolverType.GLOP,
    'gscip': mathopt.SolverType.GSCIP,
    'gurobi': mathopt.SolverType.GUROBI,
    'pdlp': mathopt.SolverType.PDLP,
    'glpk': mathopt.SolverType.GLPK,
    'osqp': mathopt.SolverType.OSQP,
    'scs': mathopt.SolverType.SCS,
    'highs': mathopt.SolverType.HIGHS,
    'santorini': mathopt.SolverType.SANTORINI
}

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

    if solver_name not in mathopt_solver_selector.keys():
        raise RuntimeError(
            "Using solver '%s' is not supported by 'mathopt'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))

    match debug:

        case False:

            match directions[objective_id]:

                case "min":
                    model_object.minimize(model_objectives[objective_id])

                case "max":
                    model_object.maximize(model_objectives[objective_id])

            if len(model_constraints)!=0:
                counter=0
                for constraint in model_constraints:
                    if constraint_labels[counter]==None:
                        constraint_labels[counter]=f"con[{counter}]"
                    model_object.add_linear_constraint(constraint, name=constraint_labels[counter])
                    counter+=1



            if time_limit != None:
                model_object.set_time_limit(time_limit)

            if thread_count != None:
                model_object.SetNumThreads(thread_count)

            if relative_gap != None:
                solverParams.SetDoubleParam(
                    solverParams.RELATIVE_MIP_GAP, relative_gap)

            if absolute_gap != None:
                "None"

            if log:

                "None"

            time_solve_begin = timeit.default_timer()
            result = mathopt.solve(model_object, solver_type=mathopt_solver_selector[solver_name],params=solver_options)
            time_solve_end = timeit.default_timer()
            
            try:
                dual_values = {constraint_labels[counter]: result.dual_values()[model_constraints[counter]] for counter in range(len(model_constraints))} 
                generated_solution = [result, [time_solve_begin, time_solve_end], dual_values]
            except:
                generated_solution = [result, [time_solve_begin, time_solve_end]]
                pass

    return generated_solution
