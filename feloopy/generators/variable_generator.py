# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.



def generate_variable(interface_name, model_object, variable_type, variable_name, variable_bound, variable_dim):

    inputs = {'model_object': model_object,
              'variable_type': variable_type,
              'variable_name': variable_name,
              'variable_bound': variable_bound,
              'variable_dim': variable_dim}

    match interface_name:

        case 'pulp':

            from .variable import pulp_variable_generator
            return pulp_variable_generator.generate_variable(**inputs)

        case 'pyomo':

            from .variable import pyomo_variable_generator
            return pyomo_variable_generator.generate_variable(**inputs)

        case 'insideopt':

            from .variable import seeker_variable_generator
            return seeker_variable_generator.generate_variable(**inputs)

        case 'insideopt-demo':

            from .variable import seeker_variable_generator
            return seeker_variable_generator.generate_variable(**inputs)

        case 'gams':

            from .variable import gamspy_variable_generator
            return gamspy_variable_generator.generate_variable(**inputs)

        case 'highs':

            from .variable import highs_variable_generator
            return highs_variable_generator.generate_variable(**inputs)

        case 'ortools':

            from .variable import ortools_variable_generator
            return ortools_variable_generator.generate_variable(**inputs)

        case 'ortools_cp':

            from .variable import ortools_cp_variable_generator
            return ortools_cp_variable_generator.generate_variable(**inputs)

        case 'gekko':

            from .variable import gekko_variable_generator
            return gekko_variable_generator.generate_variable(**inputs)

        case 'picos':

            from .variable import picos_variable_generator
            return picos_variable_generator.generate_variable(**inputs)

        case 'cvxpy':

            from .variable import cvxpy_variable_generator
            return cvxpy_variable_generator.generate_variable(**inputs)

        case 'cylp':

            from .variable import cylp_variable_generator
            return cylp_variable_generator.generate_variable(**inputs)

        case 'pymprog':

            from .variable import pymprog_variable_generator
            return pymprog_variable_generator.generate_variable(**inputs)

        case 'cplex':

            from .variable import cplex_variable_generator
            return cplex_variable_generator.generate_variable(**inputs)
        
        case 'cplex_cp':

            from .variable import cplex_cp_variable_generator
            return cplex_cp_variable_generator.generate_variable(**inputs)

        case 'gurobi':

            from .variable import gurobi_variable_generator
            return gurobi_variable_generator.generate_variable(**inputs)

        case 'copt':

            from .variable import copt_variable_generator
            return copt_variable_generator.generate_variable(**inputs)
        
        case 'xpress':

            from .variable import xpress_variable_generator
            return xpress_variable_generator.generate_variable(**inputs)

        case 'mip':

            from .variable import mip_variable_generator
            return mip_variable_generator.generate_variable(**inputs)

        case 'linopy':

            from .variable import linopy_variable_generator
            return linopy_variable_generator.generate_variable(**inputs)

        case 'rsome_ro':

            from .variable import rsome_ro_variable_generator
            return rsome_ro_variable_generator.generate_variable(**inputs)
        
        case 'rsome_dro':

            from .variable import rsome_dro_variable_generator
            return rsome_dro_variable_generator.generate_variable(**inputs)