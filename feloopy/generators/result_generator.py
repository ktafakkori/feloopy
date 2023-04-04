
def get(input, ModelObject, ModelSolution, Thing, VariableNameWithIndex):

    InterfaceName = input['interface_name']
    indicator = [Thing, input['directions'], input['objective_being_optimized']]

    if indicator[0] == 'variable':

        match InterfaceName:
            case 'pulp':

                from .result import pulp_result_generator
                return pulp_result_generator.Get(ModelObject, ModelSolution, indicator, VariableNameWithIndex)

            case 'pyomo':

                from .result import pyomo_result_generator
                return pyomo_result_generator.Get(ModelObject, ModelSolution, indicator, VariableNameWithIndex)

            case 'ortools':

                from .result import ortools_result_generator
                return ortools_result_generator.Get(ModelObject, ModelSolution, indicator, VariableNameWithIndex)

            case 'ortools_cp':

                from .result import ortools_cp_result_generator
                return ortools_cp_result_generator.Get(ModelObject, ModelSolution, indicator, VariableNameWithIndex)


            case 'gekko':

                from .result import gekko_result_generator
                return gekko_result_generator.Get(ModelObject, ModelSolution, indicator, VariableNameWithIndex)

            case 'picos':

                from .result import picos_result_generator
                return picos_result_generator.Get(ModelObject, ModelSolution, indicator, VariableNameWithIndex)

            case 'cvxpy':

                from .result import cvxpy_result_generator
                return cvxpy_result_generator.Get(ModelObject, ModelSolution, indicator, VariableNameWithIndex)

            case 'cylp':

                from .result import cylp_result_generator
                return cylp_result_generator.Get(ModelObject, ModelSolution, indicator, VariableNameWithIndex)

            case 'pymprog':

                from .result import pymprog_result_generator
                return pymprog_result_generator.Get(ModelObject, ModelSolution, indicator, VariableNameWithIndex)

            case 'cplex':

                from .result import cplex_result_generator
                return cplex_result_generator.Get(ModelObject, ModelSolution, indicator, VariableNameWithIndex)

            case 'cplex_cp':

                from .result import cplex_cp_result_generator
                return cplex_cp_result_generator.Get(ModelObject, ModelSolution, indicator, VariableNameWithIndex)

            case 'gurobi':

                from .result import gurobi_result_generator
                return gurobi_result_generator.Get(ModelObject, ModelSolution, indicator, VariableNameWithIndex)

            case 'xpress':

                from .result import xpress_result_generator
                return xpress_result_generator.Get(ModelObject, ModelSolution, indicator, VariableNameWithIndex)

            case 'mip':

                from .result import mip_result_generator
                return mip_result_generator.Get(ModelObject, ModelSolution, indicator, VariableNameWithIndex)

            case 'linopy':

                from .result import linopy_result_generator
                return linopy_result_generator.Get(ModelObject, ModelSolution, indicator, VariableNameWithIndex)

    elif indicator[0] == 'objective' or indicator[0] == 'status' or indicator[0] == 'time':
        
        match InterfaceName:

            case 'pulp':

                from .result import pulp_result_generator
                return pulp_result_generator.Get(ModelObject, ModelSolution, indicator)

            case 'pyomo':

                from .result import pyomo_result_generator
                return pyomo_result_generator.Get(ModelObject, ModelSolution, indicator)

            case 'ortools':

                from .result import ortools_result_generator
                return ortools_result_generator.Get(ModelObject, ModelSolution, indicator)

            case 'ortools_cp':

                from .result import ortools_cp_result_generator
                return ortools_cp_result_generator.Get(ModelObject, ModelSolution, indicator)

            case 'gekko':

                from .result import gekko_result_generator
                return gekko_result_generator.Get(ModelObject, ModelSolution, indicator)

            case 'picos':

                from .result import picos_result_generator
                return picos_result_generator.Get(ModelObject, ModelSolution, indicator)

            case 'cvxpy':

                from .result import cvxpy_result_generator
                return cvxpy_result_generator.Get(ModelObject, ModelSolution, indicator)

            case 'cylp':

                from .result import cylp_result_generator
                return cylp_result_generator.Get(ModelObject, ModelSolution, indicator)

            case 'pymprog':

                from .result import pymprog_result_generator
                return pymprog_result_generator.Get(ModelObject, ModelSolution, indicator)

            case 'cplex':

                from .result import cplex_result_generator
                return cplex_result_generator.Get(ModelObject, ModelSolution, indicator)

            case 'cplex_cp':

                from .result import cplex_cp_result_generator
                return cplex_cp_result_generator.Get(ModelObject, ModelSolution, indicator)


            case 'gurobi':

                from .result import gurobi_result_generator
                return gurobi_result_generator.Get(ModelObject, ModelSolution, indicator)

            case 'xpress':

                from .result import xpress_result_generator
                return xpress_result_generator.Get(ModelObject, ModelSolution, indicator)

            case 'mip':

                from .result import mip_result_generator
                return mip_result_generator.Get(ModelObject, ModelSolution, indicator)

            case 'linopy':

                from .result import linopy_result_generator
                return linopy_result_generator.Get(ModelObject, ModelSolution, indicator)
