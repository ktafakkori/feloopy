import gekko as gekko_interface
import timeit 

gekko_solver_selector = {'apopt': 1,
                         'bpopt': 2,
                         'ipopt': 3}

def generate_solution(model_object, model_objectives, model_constraints, directions, constraint_labels, debug, time_limit, absolute_gap, relative_gap, thread_count, solver_name, log, save, max_iterations, objective_id, solver_options,email):
    
    if solver_name not in gekko_solver_selector.keys():
        raise RuntimeError("Using solver '%s' is not supported by 'gekko'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))
    
    match debug:

        case False:

            match directions[objective_id]: 
                case "min":
                    model_object.Minimize(model_objectives[objective_id])
                case "max":
                    model_object.Maximize(model_objectives[objective_id])

            for constraint in model_constraints:
                model_object.Equation(constraint)

            if 'online' not in solver_name:
                model_object.options.SOLVER = gekko_solver_selector[solver_name]
                time_solve_begin = timeit.default_timer()
                result = model_object.solve(disp=False)
                time_solve_end = timeit.default_timer()

            else:
                
                gekko_interface.GEKKO(remote=True)
                model_object.options.SOLVER = gekko_solver_selector[solver_name]
                time_solve_begin = timeit.default_timer()
                result = model_object.solve(disp=False)
                time_solve_end = timeit.default_timer()
                
            generated_solution = [result, [time_solve_begin, time_solve_end]]
            
    return generated_solution