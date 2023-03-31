import cylp as cylp_interface
from cylp.cy import CyClpSimplex
import timeit 

cylp_solver_selector = {'cbc': 'cbc'}

def generate_solution(model_object, model_objectives, model_constraints, directions, constraint_labels, debug, time_limit, absolute_gap, relative_gap, thread_count, solver_name, log, save, max_iterations, objective_id, solver_options,email):
    
    if solver_name not in cylp_solver_selector.keys():
        raise RuntimeError("Using solver '%s' is not supported by 'cylp'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))
    
    match debug:

        case False:
                
            match directions[objective_id]:
                case 'min':
                    model_object.objective = 1*(model_objectives[objective_id])
                case 'max': 
                    model_object.objective = -1*(model_objectives[objective_id])

            for constraint in model_constraints:
                model_object += constraint
            
            cbcModel = cylp_interface.cy.CyClpSimplex(model_object).getCbcModel()
            time_solve_begin = timeit.default_timer()
            result = cbcModel.solve()
            time_solve_end = timeit.default_timer() 
            generated_solution = [result, [time_solve_begin, time_solve_end]]
        
    return generated_solution

