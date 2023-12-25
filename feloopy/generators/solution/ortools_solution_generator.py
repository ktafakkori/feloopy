# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.



from ortools.linear_solver import pywraplp as ortools_interface
import timeit

ortools_solver_selector = {
    'clp': 'CLP_LINEAR_PROGRAMMING',
    'cbc': 'CBC_MIXED_INTEGER_PROGRAMMING',
    'scip': 'SCIP_MIXED_INTEGER_PROGRAMMING',
    'glop': 'GLOP_LINEAR_PROGRAMMING',
    'bop': 'BOP_INTEGER_PROGRAMMING',
    'sat': 'SAT_INTEGER_PROGRAMMING',
    'gurobi_': 'GUROBI_LINEAR_PROGRAMMING',
    'gurobi': 'GUROBI_MIXED_INTEGER_PROGRAMMING',
    'cplex_': 'CPLEX_LINEAR_PROGRAMMING',
    'cplex': 'CPLEX_MIXED_INTEGER_PROGRAMMING',
    'xpress_': 'XPRESS_LINEAR_PROGRAMMING',
    'xpress': 'XPRESS_MIXED_INTEGER_PROGRAMMING',
    'glpk_': 'GLPK_LINEAR_PROGRAMMING',
    'glpk': 'GLPK_MIXED_INTEGER_PROGRAMMING'
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

    if solver_name not in ortools_solver_selector.keys():
        raise RuntimeError(
            "Using solver '%s' is not supported by 'ortools'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))

    match debug:

        case False:

            match directions[objective_id]:

                case "min":
                    model_object.Minimize(model_objectives[objective_id])

                case "max":
                    model_object.Maximize(model_objectives[objective_id])

            if len(model_constraints)!=0:
                counter=0
                for constraint in model_constraints:
                    if constraint_labels[counter]==None:
                        constraint_labels[counter]=f"con[{counter}]"
                    model_object.Add(constraint, name=constraint_labels[counter])
                    counter+=1

            model_object.CreateSolver(ortools_solver_selector[solver_name])
            solverParams = ortools_interface.MPSolverParameters()

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
            result = model_object.Solve()
            time_solve_end = timeit.default_timer()
            generated_solution = [result, [time_solve_begin, time_solve_end]]

    return generated_solution
