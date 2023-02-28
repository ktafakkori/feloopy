import picos as picos_interface
import timeit

picos_solver_selector = {'cplex': 'cplex',
                         'cvxopt': 'cvxopt',
                         'ecos': 'ecos',
                         'glpk': 'glpk',
                         'gurobi': 'gurobi',
                         'mosek': 'mosek',
                         'mskfsn': 'mskfsn',
                         'osqp': 'osqp',
                         'scip': 'scip',
                         'smcp': 'smcp'}

def generate_solution(model_object, objectives_list, constraints_list, dir, labels, mode, solver_name, objective_number=0, algorithm_options=None, user_email=None):

    if solver_name not in picos_solver_selector.keys():
        raise RuntimeError("Using solver '%s' is not supported by 'picos'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))

    match mode:

        case False:

            match dir[objective_number]:
                case "min":
                    model_object.set_objective('min', objectives_list[objective_number])
                case "max":
                    model_object.set_objective('max', objectives_list[objective_number])

            for constraint in constraints_list:
                model_object += constraint
        
            time_solve_begin = timeit.default_timer()
            result = model_object.solve(solver=solver_name)
            time_solve_end = timeit.default_timer()
            generated_solution = [result, [time_solve_begin, time_solve_end]]

    return generated_solution
