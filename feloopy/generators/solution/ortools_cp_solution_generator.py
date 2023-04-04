from ortools.sat.python import cp_model
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

def generate_solution(model_object, model_objectives, model_constraints, directions, constraint_labels, debug, time_limit, absolute_gap, relative_gap, thread_count, solver_name, log, save, max_iterations, objective_id, solver_options, email):


    match debug:

        case False:

            if len(directions)!=0:

                match directions[objective_id]:

                    case "min":
                        model_object.Minimize(model_objectives[objective_id])

                    case "max":
                        model_object.Maximize(model_objectives[objective_id])

            for constraint in model_constraints:
                model_object.Add(constraint)

            solver = cp_model.CpSolver()

            if time_limit != None:
                solver.parameters.max_time_in_seconds = time_limit

            time_solve_begin = timeit.default_timer()
            result = solver.Solve(model_object)
            time_solve_end = timeit.default_timer()
            generated_solution = [[result,solver], [time_solve_begin, time_solve_end]]


            if log:

                    print('\nStatistics')
                    print(f'  conflicts      : {solver.NumConflicts()}')
                    print(f'  branches       : {solver.NumBranches()}')
                    print(f'  wall time      : {solver.WallTime()} s')

                    
    return generated_solution
