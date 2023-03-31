import xpress as xpress_interface
import timeit

xpress_solver_selector = {'xpress': 'xpress'}

def generate_solution(model_object, model_objectives, model_constraints, directions, constraint_labels, debug, time_limit, absolute_gap, relative_gap, thread_count, solver_name, log, save, max_iterations, objective_id, solver_options):
    
    if solver_name not in xpress_solver_selector.keys():
        raise RuntimeError("Using solver '%s' is not supported by 'xpress'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))
    
    match debug:

        case False:

            for constraint in model_constraints[0]:
                model_object.addConstraint(constraint)

            match directions[objective_id]:

                case "min":
                    model_object.setObjective(model_objectives[objective_id], sense=xpress_interface.minimize)

                case "max":
                    model_object.setObjective(model_objectives[objective_id], sense=xpress_interface.maximize)

            time_solve_begin = timeit.default_timer()
            result = model_object.solve()
            time_solve_end = timeit.default_timer()
            generated_solution = [result, [time_solve_begin, time_solve_end]]

    return generated_solution