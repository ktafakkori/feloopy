import pymprog as pymprog_interface
import timeit

pymprog_solver_selector = {'glpk': 'glpk'}

def generate_solution(model_object, model_objectives, model_constraints, directions, constraint_labels, debug, time_limit, absolute_gap, relative_gap, thread_count, solver_name, log, save, max_iterations, objective_id, solver_options, email):
    
    if solver_name not in pymprog_solver_selector.keys():
        raise RuntimeError("Using solver '%s' is not supported by 'pymprog'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))

    match debug:

        case False:

            match directions[objective_id]:

                case "min":
                    pymprog_interface.minimize(model_objectives[objective_id], 'objective')
                case "max":
                    pymprog_interface.maximize(model_objectives[objective_id], 'objective')

            for constraint in model_constraints:
                constraint
            time_solve_begin = timeit.default_timer()
            result = pymprog_interface.solve()
            time_solve_end = timeit.default_timer()
            generated_solution = result, [time_solve_begin, time_solve_end]
    
    return generated_solution