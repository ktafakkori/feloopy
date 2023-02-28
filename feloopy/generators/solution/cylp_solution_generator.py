import cylp as cylp_interface
from cylp.cy import CyClpSimplex
import timeit 

cylp_solver_selector = {'cbc': 'cbc'}

def generate_solution(model_object, objectives_list, constraints_list, dir, labels, mode, solver_name, objective_number=0, algorithm_options=None, user_email=None):
    
    if solver_name not in cylp_solver_selector.keys():
        raise RuntimeError("Using solver '%s' is not supported by 'cylp'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))
    
    match mode:

        case False:
                
            match dir[objective_number]:
                case 'min':
                    model_object.objective = 1*(objectives_list[objective_number])
                case 'max': 
                    model_object.objective = -1*(objectives_list[objective_number])

            for constraint in constraints_list:
                model_object += constraint
            
            cbcModel = cylp_interface.cy.CyClpSimplex(model_object).getCbcModel()
            time_solve_begin = timeit.default_timer()
            result = cbcModel.solve()
            time_solve_end = timeit.default_timer() 
            generated_solution = [result, [time_solve_begin, time_solve_end]]
        
    return generated_solution

