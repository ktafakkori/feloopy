import gekko as gekko_interface
import timeit 

gekko_solver_selector = {'apopt': 1,
                         'bpopt': 2,
                         'ipopt': 3}

def generate_solution(model_object, objectives_list, constraints_list, dir, labels, mode, solver_name, objective_number=0, algorithm_options=None, user_email=None):
    
    if solver_name not in gekko_solver_selector.keys():
        raise RuntimeError("Using solver '%s' is not supported by 'gekko'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))
    
    match mode:

        case False:

            match dir[objective_number]: 
                case "min":
                    model_object.Minimize(objectives_list[objective_number])
                case "max":
                    model_object.Maximize(objectives_list[objective_number])

            for constraint in constraints_list:
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