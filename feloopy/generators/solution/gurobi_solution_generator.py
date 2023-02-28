import gurobipy as gurobi_interface
import timeit

gurobi_solver_selector = {'gurobi': 'gurobi'}

def generate_solution(model_object, objectives_list, constraints_list, dir, labels, mode, solver_name, objective_number=0, algorithm_options=None, user_email=None):
    
    if solver_name not in gurobi_solver_selector.keys():

        raise RuntimeError("Using solver '%s' is not supported by 'gurobi'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))
    
    match mode:

        case False:

            match dir[objective_number]:
                case "min":
                    model_object.setObjective(objectives_list[objective_number], gurobi_interface.GRB.MINIMIZE)
                case "max":
                    model_object.setObjective(objectives_list[objective_number], gurobi_interface.GRB.MAXIMIZE)
                
            for constraint in constraints_list:
                model_object.addConstr(constraint)

            time_solve_begin = timeit.default_timer()
            result = model_object.optimize()
            time_solve_end = timeit.default_timer()
            generated_solution = result, [time_solve_begin, time_solve_end]

    return generated_solution