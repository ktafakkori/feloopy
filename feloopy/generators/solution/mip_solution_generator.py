import mip as mip_interface
import timeit

mip_solver_selector = {'cbc': 'cbc'}

def generate_solution(model_object, model_objectives, model_constraints, directions, constraint_labels, debug, time_limit, absolute_gap, relative_gap, thread_count, solver_name, log, save, max_iterations, objective_id, solver_options, email):

    if solver_name not in mip_solver_selector.keys():
        raise RuntimeError("Using solver '%s' is not supported by 'mip'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))
    
    match debug:

        case False:

            for constraint in model_constraints:
                model_object += constraint

            match directions[objective_id]:
                case "min":
                    model_object.objective = mip_interface.minimize(model_objectives[objective_id]) 
                case "max":
                    model_object.objective = mip_interface.maximize(model_objectives[objective_id])
                
            time_solve_begin = timeit.default_timer()
            result = model_object.optimize()
            time_solve_end = timeit.default_timer()
            generated_solution = [ result, [time_solve_begin, time_solve_end]]
    
    return generated_solution