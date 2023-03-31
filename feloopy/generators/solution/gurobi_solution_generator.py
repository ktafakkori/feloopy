import gurobipy as gurobi_interface
import timeit

gurobi_solver_selector = {'gurobi': 'gurobi'}

def generate_solution(model_object, model_objectives, model_constraints, directions, constraint_labels, debug, time_limit, absolute_gap, relative_gap, thread_count, solver_name, log, save, max_iterations, objective_id, solver_options,email):
    
    if solver_name not in gurobi_solver_selector.keys():

        raise RuntimeError("Using solver '%s' is not supported by 'gurobi'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))

    if time_limit != None:
        model_object.setParam('TimeLimit', time_limit)

    if thread_count != None:
        model_object.setParam('Threads', thread_count) 

    if relative_gap != None:
        model_object.setParam('MIPGap', relative_gap)

    if absolute_gap != None:
        model_object.setParam('MIPGapAbs', absolute_gap)

    if log:
        model_object.setParam('OutputFlag', 1)
    else:
        model_object.setParam('OutputFlag', 0)

    
    if save!=False:
        model_object.setParam('LogFile', f'{save}.log')

    if len(solver_options) !=0:

        for key in solver_options:
            model_object.setParam(key, solver_options[key])

    match debug:

        case False:

            match directions[objective_id]:
                case "min":
                    model_object.setObjective(model_objectives[objective_id], gurobi_interface.GRB.MINIMIZE)
                case "max":
                    model_object.setObjective(model_objectives[objective_id], gurobi_interface.GRB.MAXIMIZE)
                
            for constraint in model_constraints:
                model_object.addConstr(constraint)

            time_solve_begin = timeit.default_timer()
            result = model_object.optimize()
            time_solve_end = timeit.default_timer()
            generated_solution = result, [time_solve_begin, time_solve_end]

    return generated_solution