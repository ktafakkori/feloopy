def generate_model(interface_name):

    match interface_name:

        case 'pulp':

            from .model import pulp_model_generator
            model_object = pulp_model_generator.generate_model()

        case 'pyomo':

            from .model import pyomo_model_generator
            model_object = pyomo_model_generator.generate_model()

        case 'ortools':

            from .model import ortools_model_generator
            model_object = ortools_model_generator.generate_model()

        case 'gekko':

            from .model import gekko_model_generator
            model_object = gekko_model_generator.generate_model()

        case 'picos':

            from .model import picos_model_generator
            model_object = picos_model_generator.generate_model()

        case 'cvxpy':

            from .model import cvxpy_model_generator
            model_object = cvxpy_model_generator.generate_model()

        case 'cylp':

            from .model import cylp_model_generator
            model_object = cylp_model_generator.generate_model()

        case 'pymprog':

            from .model import pymprog_model_generator
            model_object = pymprog_model_generator.generate_model()

        case 'cplex':

            from .model import cplex_model_generator
            model_object = cplex_model_generator.generate_model()

        case 'gurobi':

            from .model import gurobi_model_generator
            model_object = gurobi_model_generator.generate_model()

        case 'xpress':

            from .model import xpress_model_generator
            model_object = xpress_model_generator.generate_model()

        case 'mip':

            from .model import mip_model_generator
            model_object = mip_model_generator.generate_model()

        case 'linopy':

            from .model import linopy_model_generator
            model_object = linopy_model_generator.generate_model()
    
    return model_object