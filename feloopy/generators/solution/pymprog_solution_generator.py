import pymprog as pymprog_interface
import timeit

pymprog_solver_selector = {'glpk': 'glpk'}

def generate_solution(model_object, objectives_list, constraints_list, dir, labels, mode, solver_name, objective_number=0, algorithm_options=None, user_email=None):
    
    if solver_name not in pymprog_solver_selector.keys():
        raise RuntimeError("Using solver '%s' is not supported by 'pymprog'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))

    match mode:

        case False:

            match dir[objective_number]:

                case "min":
                    pymprog_interface.minimize(objectives_list[objective_number], 'objective')
                case "max":
                    pymprog_interface.maximize(objectives_list[objective_number], 'objective')

            for constraint in constraints_list:
                constraint
            time_solve_begin = timeit.default_timer()
            result = pymprog_interface.solve()
            time_solve_end = timeit.default_timer()
            generated_solution = result, [time_solve_begin, time_solve_end]
    
    return generated_solution