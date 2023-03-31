import pulp as pulp_interface

import timeit


def generate_solution(model_object, model_objectives, model_constraints, directions, constraint_labels, debug, time_limit, absolute_gap, relative_gap, thread_count, solver_name, log, save, max_iterations, objective_id, solver_options, email):

    if time_limit != None:
        solver_options['timeLimit'] = time_limit

    if thread_count != None:
        solver_options['threads'] = thread_count

    if relative_gap != None:
        solver_options['gapRel'] = relative_gap

    if absolute_gap != None:
        solver_options['gapAbs'] = absolute_gap

    if log:
        solver_options['msg'] = 1
    else:
        solver_options['msg'] = 0

    if max_iterations != None:
        "None"

    pulp_solver_selector = {
        'cbc': pulp_interface.PULP_CBC_CMD(**solver_options),
        'choco': pulp_interface.CHOCO_CMD(**solver_options),
        'coin': pulp_interface.COIN_CMD(**solver_options),
        'coinmp_dll': pulp_interface.COINMP_DLL(**solver_options),
        'cplex_py': pulp_interface.CPLEX_PY(**solver_options),
        'cplex': pulp_interface.CPLEX_CMD(**solver_options),
        'glpk': pulp_interface.GLPK_CMD(**solver_options),
        'gurobi_cmd': pulp_interface.GUROBI_CMD(**solver_options),
        'gurobi': pulp_interface.GUROBI(**solver_options),
        'highs': pulp_interface.HiGHS_CMD(**solver_options),
        'mipcl': pulp_interface.MIPCL_CMD(**solver_options),
        'mosek': pulp_interface.MOSEK(**solver_options),
        'pyglpk': pulp_interface.PYGLPK(**solver_options),
        'scip': pulp_interface.SCIP_CMD(**solver_options),
        'xpress_py': pulp_interface.XPRESS_PY(**solver_options),
        'xpress': pulp_interface.XPRESS(**solver_options)
    }

    if solver_name not in pulp_solver_selector.keys():
        raise RuntimeError("Using solver '%s' is not supported by 'pulp'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))

    match debug:

        case False:

            match directions[objective_id]:

                case "min":
                    model_object += model_objectives[objective_id]

                case "max":
                    model_object += -model_objectives[objective_id]

            for constraint in model_constraints:
                model_object += constraint

            time_solve_begin = timeit.default_timer()
            result = model_object.solve(solver=pulp_solver_selector[solver_name])
            time_solve_end = timeit.default_timer()
            generated_solution = [result, [time_solve_begin, time_solve_end]]

    return generated_solution