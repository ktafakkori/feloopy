'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.7)                               |
|  Modified: Wednesday, 27th September 2023 11:36:32 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''


def get(input, model_object, model_solution, Thing, variable_name_with_index):

    InterfaceName = input['interface_name']

    indicator = [Thing,
                 input['directions'],
                 input['objective_being_optimized']]

    if indicator[0] == 'variable' or indicator[0] == 'dual' or indicator[0] == 'slack' or indicator[0] == 'rc' or indicator[0] == 'iis':

        match InterfaceName:

            case 'pulp':

                from .result import pulp_result_generator
                return pulp_result_generator.Get(model_object, model_solution, indicator, variable_name_with_index)

            case 'pyomo':

                from .result import pyomo_result_generator
                return pyomo_result_generator.Get(model_object, model_solution, indicator, variable_name_with_index)

            case 'ortools':

                from .result import ortools_result_generator
                return ortools_result_generator.Get(model_object, model_solution, indicator, variable_name_with_index)

            case 'ortools_cp':

                from .result import ortools_cp_result_generator
                return ortools_cp_result_generator.Get(model_object, model_solution, indicator, variable_name_with_index)

            case 'gekko':

                from .result import gekko_result_generator
                return gekko_result_generator.Get(model_object, model_solution, indicator, variable_name_with_index)

            case 'picos':

                from .result import picos_result_generator
                return picos_result_generator.Get(model_object, model_solution, indicator, variable_name_with_index)

            case 'cvxpy':

                from .result import cvxpy_result_generator
                return cvxpy_result_generator.Get(model_object, model_solution, indicator, variable_name_with_index)

            case 'cylp':

                from .result import cylp_result_generator
                return cylp_result_generator.Get(model_object, model_solution, indicator, variable_name_with_index)

            case 'pymprog':

                from .result import pymprog_result_generator
                return pymprog_result_generator.Get(model_object, model_solution, indicator, variable_name_with_index)

            case 'localsolver':

                from .result import localsolver_result_generator
                return localsolver_result_generator.Get(model_object, model_solution, indicator, variable_name_with_index)

            case 'cplex':

                from .result import cplex_result_generator
                return cplex_result_generator.Get(model_object, model_solution, indicator, variable_name_with_index)

            case 'cplex_cp':

                from .result import cplex_cp_result_generator
                return cplex_cp_result_generator.Get(model_object, model_solution, indicator, variable_name_with_index)

            case 'gurobi':

                from .result import gurobi_result_generator
                return gurobi_result_generator.Get(model_object, model_solution, indicator, variable_name_with_index)

            case 'copt':

                from .result import copt_result_generator
                return copt_result_generator.Get(model_object, model_solution, indicator, variable_name_with_index)

            case 'xpress':

                from .result import xpress_result_generator
                return xpress_result_generator.Get(model_object, model_solution, indicator, variable_name_with_index)

            case 'mip':

                from .result import mip_result_generator
                return mip_result_generator.Get(model_object, model_solution, indicator, variable_name_with_index)

            case 'linopy':

                from .result import linopy_result_generator
                return linopy_result_generator.Get(model_object, model_solution, indicator, variable_name_with_index)

            case 'rsome_ro':

                from .result import rsome_ro_result_generator
                return rsome_ro_result_generator.Get(model_object, model_solution, indicator, variable_name_with_index)

            case 'rsome_dro':

                from .result import rsome_dro_result_generator
                return rsome_dro_result_generator.Get(model_object, model_solution, indicator, variable_name_with_index)

    elif indicator[0] == 'objective' or indicator[0] == 'status' or indicator[0] == 'time':

        match InterfaceName:

            case 'pulp':

                from .result import pulp_result_generator
                return pulp_result_generator.Get(model_object, model_solution, indicator)

            case 'pyomo':

                from .result import pyomo_result_generator
                return pyomo_result_generator.Get(model_object, model_solution, indicator)

            case 'ortools':

                from .result import ortools_result_generator
                return ortools_result_generator.Get(model_object, model_solution, indicator)

            case 'localsolver':

                from .result import localsolver_result_generator
                return localsolver_result_generator.Get(model_object, model_solution, indicator)
            
            case 'ortools_cp':

                from .result import ortools_cp_result_generator
                return ortools_cp_result_generator.Get(model_object, model_solution, indicator)

            case 'gekko':

                from .result import gekko_result_generator
                return gekko_result_generator.Get(model_object, model_solution, indicator)

            case 'picos':

                from .result import picos_result_generator
                return picos_result_generator.Get(model_object, model_solution, indicator)

            case 'cvxpy':

                from .result import cvxpy_result_generator
                return cvxpy_result_generator.Get(model_object, model_solution, indicator)

            case 'cylp':

                from .result import cylp_result_generator
                return cylp_result_generator.Get(model_object, model_solution, indicator)

            case 'pymprog':

                from .result import pymprog_result_generator
                return pymprog_result_generator.Get(model_object, model_solution, indicator)

            case 'cplex':

                from .result import cplex_result_generator
                return cplex_result_generator.Get(model_object, model_solution, indicator)

            case 'cplex_cp':

                from .result import cplex_cp_result_generator
                return cplex_cp_result_generator.Get(model_object, model_solution, indicator)

            case 'gurobi':

                from .result import gurobi_result_generator
                return gurobi_result_generator.Get(model_object, model_solution, indicator)

            case 'copt':

                from .result import copt_result_generator
                return copt_result_generator.Get(model_object, model_solution, indicator)
            
            case 'xpress':

                from .result import xpress_result_generator
                return xpress_result_generator.Get(model_object, model_solution, indicator)

            case 'mip':

                from .result import mip_result_generator
                return mip_result_generator.Get(model_object, model_solution, indicator)

            case 'linopy':

                from .result import linopy_result_generator
                return linopy_result_generator.Get(model_object, model_solution, indicator)
            
            case 'rsome_ro':
                    
                from .result import rsome_ro_result_generator
                return rsome_ro_result_generator.Get(model_object, model_solution, indicator)

            case 'rsome_dro':

                from .result import rsome_dro_result_generator
                return rsome_dro_result_generator.Get(model_object, model_solution, indicator)

