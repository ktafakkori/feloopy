from linopy import Model as LINOPYMODEL
import timeit

linopy_solver_selector = {'cbc': 'cbc', 
                          'glpk': 'glpk', 
                          'highs': 'highs',
                          'gurobi': 'gurobi', 
                          'xpress': 'xpress', 
                          'cplex': 'cplex'}

def generate_solution(model_object, objectives_list, constraints_list, dir, labels, mode, solver_name, objective_number=0, algorithm_options=None, user_email=None):
    
    if solver_name not in linopy_solver_selector.keys():
        raise RuntimeError("Using solver '%s' is not supported by 'linopy'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))
    
    match mode:

        case False:

            match dir[objective_number]:
                case "min":
                    model_object.add_objective(objectives_list[objective_number])
                case "max":
                    model_object.add_objective(-objectives_list[objective_number])

            for constraint in constraints_list:
                model_object.add_constraints(constraint)
    
            time_solve_begin = timeit.default_timer()
            result = model_object.solve(solver_name=solver_name)
            time_solve_end = timeit.default_timer()
            generated_solution = [result, [time_solve_begin, time_solve_end]]
        
    return generated_solution