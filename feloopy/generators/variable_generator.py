def generate_variable(interface_name, model_object, variable_type, variable_name, variable_bound, variable_dim):

    match interface_name:

        case 'pulp':

            from .variable import pulp_variable_generator
            return pulp_variable_generator.generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim)

        case 'pyomo':

            from .variable import pyomo_variable_generator
            return pyomo_variable_generator.generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim)

        case 'ortools':

            from .variable import ortools_variable_generator
            return ortools_variable_generator.generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim)

        case 'gekko':

            from .variable import gekko_variable_generator
            return gekko_variable_generator.generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim)

        case 'picos':

            from .variable import picos_variable_generator
            return picos_variable_generator.generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim)

        case 'cvxpy':

            from .variable import cvxpy_variable_generator
            return cvxpy_variable_generator.generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim)

        case 'cylp':

            from .variable import cylp_variable_generator
            return cylp_variable_generator.generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim)

        case 'pymprog':

            from .variable import pymprog_variable_generator
            return pymprog_variable_generator.generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim)

        case 'cplex':

            from .variable import cplex_variable_generator
            return cplex_variable_generator.generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim)

        case 'gurobi':

            from .variable import gurobi_variable_generator
            return gurobi_variable_generator.generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim)

        case 'xpress':

            from .variable import xpress_variable_generator
            return xpress_variable_generator.generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim)

        case 'mip':

            from .variable import mip_variable_generator
            return mip_variable_generator.generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim)

        case 'linopy':

            from .variable import linopy_variable_generator
            return linopy_variable_generator.generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim)