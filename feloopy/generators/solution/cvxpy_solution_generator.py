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

def generate_solution(model_object, objectives_list, constraints_list, dir, labels, mode, solver_name, objective_number=0, algortihm_options=None, user_email=None):

    if solver_name not in cvxpy_solver_selector.keys():
        raise RuntimeError("Using solver '%s' is not supported by 'cvxpy'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))

    match mode:

        case False:

            match dir[objective_number]:

                case 'min':
                    obj = cvxpy_interface.Minimize(objectives_list[objective_number])

                case 'max':
                    obj = cvxpy_interface.Maximize(objectives_list[objective_number])

            prob = cvxpy_interface.Problem(obj, constraints_list)
            time_solve_begin = timeit.default_timer()
            result = prob.solve(solver=cvxpy_solver_selector[solver_name])
            time_solve_end = timeit.default_timer()
            newresult = [prob, result]
            generated_solution = [newresult, [time_solve_begin, time_solve_end]]

    return generated_solution
