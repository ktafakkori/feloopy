from docplex.mp.model import Model as CPLEXMODEL
import docplex as cplex_interface
import timeit

cplex_solver_selector = {'cplex': 'cplex'}

def generate_solution(model_object, objectives_list, constraints_list, dir, labels, mode, time_limit, absolute_gap, relative_gap, threads, solver_name, objective_number=0, algorithm_options=None, user_email=None):

    if solver_name not in cplex_solver_selector.keys():
        raise RuntimeError("Using solver '%s' is not supported by 'cplex'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))
    
    if time_limit != None:
        model_object.parameters.timelimit = time_limit

    if threads != None:
        model_object.parameters.threads = threads

    if relative_gap != None:
        model_object.parameters.mip.tolerances.mipgap = relative_gap

    if absolute_gap != None:
        model_object.parameters.mip.tolerances.absmipgap = absolute_gap

    match mode:

        case False:

            match dir[objective_number]:

                case 'min': 
                    model_object.set_objective('min', objectives_list[objective_number])

                case 'max': 
                    model_object.set_objective('max', objectives_list[objective_number])

            for constraint in constraints_list:
                model_object.add_constraint(constraint)

            time_solve_begin = timeit.default_timer()
            result = model_object.solve()
            time_solve_end = timeit.default_timer()
            generated_solution = [result, [time_solve_begin, time_solve_end]]

    return generated_solution
