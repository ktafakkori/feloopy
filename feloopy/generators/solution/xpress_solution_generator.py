import xpress as xpress_interface
import timeit

xpress_solver_selector = {'xpress': 'xpress'}

def generate_solution(model_object, objectives_list, constraints_list, dir, labels, mode, solver_name, objective_number=0, algorithm_options=None, user_email=None):
    
    if solver_name not in xpress_solver_selector.keys():
        raise RuntimeError("Using solver '%s' is not supported by 'xpress'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))
    
    match mode:

        case False:

            for constraint in constraints_list[0]:
                model_object.addConstraint(constraint)

            match dir[objective_number]:

                case "min":
                    model_object.setObjective(objectives_list[objective_number], sense=xpress_interface.minimize)

                case "max":
                    model_object.setObjective(objectives_list[objective_number], sense=xpress_interface.maximize)

            time_solve_begin = timeit.default_timer()
            result = model_object.solve()
            time_solve_end = timeit.default_timer()
            generated_solution = [result, [time_solve_begin, time_solve_end]]

    return generated_solution