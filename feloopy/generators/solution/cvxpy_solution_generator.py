import cvxpy as cvxpy_interface
import timeit

cvxpy_solver_selector = {
    'qsqp': cvxpy_interface.OSQP,
    'ecos': cvxpy_interface.ECOS,
    'cvxopt': cvxpy_interface.CVXOPT,
    'scs': cvxpy_interface.SCS,
    'highs': [cvxpy_interface.SCIPY, {"method": "highs"}],
    'glop': cvxpy_interface.GLOP,
    'glpk': cvxpy_interface.GLPK,
    'glpk_mi': cvxpy_interface.GLPK_MI,
    'gurobi': cvxpy_interface.GUROBI,
    'mosek': cvxpy_interface.MOSEK,
    'cbc': cvxpy_interface.CBC,
    'cplex': cvxpy_interface.CPLEX,
    'nag': cvxpy_interface.NAG,
    'pdlp': cvxpy_interface.PDLP,
    'scip': cvxpy_interface.SCIP,
    'xpress': cvxpy_interface.XPRESS}

def generate_solution(features):

    model_object = features['model_object_before_solve']
    model_objectives = features['objectives']
    model_constraints = features['constraints']
    directions = features['directions']
    constraint_labels= features['constraint_labels']
    debug = features['debug_mode']
    time_limit = features['time_limit']
    absolute_gap = features['absolute_gap']
    relative_gap = features['relative_gap']
    thread_count = features['thread_count']
    solver_name = features['solver_name']
    objective_id = features['objective_being_optimized']
    log = features['log']
    save = features['save_solver_log']
    save_model = features['write_model_file']
    email = features['email_address']
    max_iterations= features['max_iterations']
    solver_options= features['solver_options']

    if solver_name not in cvxpy_solver_selector.keys():
        raise RuntimeError("Using solver '%s' is not supported by 'cvxpy'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))

    match debug:

        case False:

            match directions[objective_id]:

                case 'min':
                    obj = cvxpy_interface.Minimize(model_objectives[objective_id])

                case 'max':
                    obj = cvxpy_interface.Maximize(model_objectives[objective_id])

            prob = cvxpy_interface.Problem(obj, model_constraints)
            time_solve_begin = timeit.default_timer()
            result = prob.solve(solver=cvxpy_solver_selector[solver_name])
            time_solve_end = timeit.default_timer()
            newresult = [prob, result]
            generated_solution = [newresult, [time_solve_begin, time_solve_end]]

    return generated_solution
