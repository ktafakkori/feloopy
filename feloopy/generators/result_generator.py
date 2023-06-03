'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''


def get(input, model_object, model_solution, Thing, variable_name_with_index):

    InterfaceName = input['interface_name']

    indicator = [Thing,
                 input['directions'],
                 input['objective_being_optimized']]

    if indicator[0] == 'variable' or indicator[0] == 'dual' or indicator[0] == 'slack':

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

            case 'cplex':

                from .result import cplex_result_generator
                return cplex_result_generator.Get(model_object, model_solution, indicator, variable_name_with_index)

            case 'cplex_cp':

                from .result import cplex_cp_result_generator
                return cplex_cp_result_generator.Get(model_object, model_solution, indicator, variable_name_with_index)

            case 'gurobi':

                from .result import gurobi_result_generator
                return gurobi_result_generator.Get(model_object, model_solution, indicator, variable_name_with_index)

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

