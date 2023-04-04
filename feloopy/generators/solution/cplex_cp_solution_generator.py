import cplex
from docplex.mp.model import Model as CPLEXMODEL
import docplex as cplex_interface
import timeit
from docplex.util.environment import get_environment
env = get_environment()

from docplex.cp.config import context

cplex_solver_selector = {'cplex': 'cplex'}

def generate_solution(model_object, model_objectives, model_constraints, directions, constraint_labels, debug, time_limit, absolute_gap, relative_gap, thread_count, solver_name, log, save, max_iterations, objective_id, solver_options, email):

    if solver_name==None:
        solver_name='cplex'
    
    if log:
        context.solver.trace_cpo = True
        context.solver.trace_log = True
        context.params.LogPeriod = 5000

    else:
        context.solver.trace_cpo = False
        context.solver.trace_log = False
        context.params.LogPeriod = 1

    if solver_name not in cplex_solver_selector.keys():
        raise RuntimeError("Using solver '%s' is not supported by 'cplex'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))
    match debug:

        case False:

            if len(directions)!=0:

                match directions[objective_id]:

                    case 'min': 
                        model_object.minimize(model_objectives[objective_id])

                    case 'max': 
                        model_object.maximize(model_objectives[objective_id])

            for constraint in model_constraints:
                model_object.add_constraint(constraint)

            time_solve_begin = timeit.default_timer()
            result = model_object.solve(TimeLimit=time_limit)
            time_solve_end = timeit.default_timer()
            generated_solution = [result, [time_solve_begin, time_solve_end]]

    return generated_solution