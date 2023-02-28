import pulp as pulp_interface

import timeit


def generate_solution(log, model_object, objectives_list, constraints_list, dir, labels, mode, solver_name, objective_number=0):

    pulp_solver_selector = {
        'cbc': pulp_interface.PULP_CBC_CMD(msg=log),
        'choco': pulp_interface.CHOCO_CMD(msg=log),
        'coin': pulp_interface.COIN_CMD(msg=log),
        'coinmp_dll': pulp_interface.COINMP_DLL(msg=log),
        'cplex_py': pulp_interface.CPLEX_PY(msg=log),
        'cplex': pulp_interface.CPLEX_CMD(msg=log),
        'glpk': pulp_interface.GLPK_CMD(msg=log),
        'gurobi_cmd': pulp_interface.GUROBI_CMD(msg=log),
        'gurobi': pulp_interface.GUROBI(msg=log),
        'highs': pulp_interface.HiGHS_CMD(msg=log),
        'mipcl': pulp_interface.MIPCL_CMD(msg=log),
        'mosek': pulp_interface.MOSEK(msg=log),
        'pyglpk': pulp_interface.PYGLPK(msg=log),
        'scip': pulp_interface.SCIP_CMD(msg=log),
        'xpress_py': pulp_interface.XPRESS_PY(msg=log),
        'xpress': pulp_interface.XPRESS(msg=log)
    }

    if solver_name not in pulp_solver_selector.keys():
        raise RuntimeError("Using solver '%s' is not supported by 'pulp'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))

    match mode:

        case False:

            match dir[objective_number]:

                case "min":
                    model_object += objectives_list[objective_number]

                case "max":
                    model_object += -objectives_list[objective_number]

            for constraint in constraints_list:
                model_object += constraint

            time_solve_begin = timeit.default_timer()
            result = model_object.solve(solver=pulp_solver_selector[solver_name])
            time_solve_end = timeit.default_timer()
            generated_solution = [result, [time_solve_begin, time_solve_end]]

    return generated_solution