# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


def generate_model(features):

    match features['interface_name']:

        case 'pulp':

            from .model import pulp_model_generator
            model_object = pulp_model_generator.generate_model(features)

        case 'pyomo':

            from .model import pyomo_model_generator
            model_object = pyomo_model_generator.generate_model(features)

        case 'insideopt-demo':

            from .model import seeker_model_generator
            model_object = seeker_model_generator.generate_demo_model(features)

        case 'insideopt':

            from .model import seeker_model_generator
            model_object = pyomo_model_generator.generate_model(features)

        case 'gams':

            from .model import gamspy_model_generator
            model_object = gamspy_model_generator.generate_model(features)

        case 'ortools':

            from .model import ortools_model_generator
            model_object = ortools_model_generator.generate_model(features)

        case 'highs':

            from .model import highs_model_generator
            model_object = highs_model_generator.generate_model(features)

        case 'ortools_cp':

            from .model import ortools_cp_model_generator
            model_object = ortools_cp_model_generator.generate_model(features)

        case 'gekko':

            from .model import gekko_model_generator
            model_object = gekko_model_generator.generate_model(features)

        case 'picos':

            from .model import picos_model_generator
            model_object = picos_model_generator.generate_model(features)

        case 'cvxpy':

            from .model import cvxpy_model_generator
            model_object = cvxpy_model_generator.generate_model(features)

        case 'cylp':

            from .model import cylp_model_generator
            model_object = cylp_model_generator.generate_model(features)

        case 'pymprog':

            from .model import pymprog_model_generator
            model_object = pymprog_model_generator.generate_model(features)

        case 'cplex':

            from .model import cplex_model_generator
            model_object = cplex_model_generator.generate_model(features)

        case 'cplex_cp':

            from .model import cplex_cp_model_generator
            model_object = cplex_cp_model_generator.generate_model(features)

        case 'gurobi':

            from .model import gurobi_model_generator
            model_object = gurobi_model_generator.generate_model(features)

        case 'copt':

            from .model import copt_model_generator
            model_object = copt_model_generator.generate_model(features)

        case 'xpress':

            from .model import xpress_model_generator
            model_object = xpress_model_generator.generate_model(features)

        case 'mip':

            from .model import mip_model_generator
            model_object = mip_model_generator.generate_model(features)

        case 'linopy':

            from .model import linopy_model_generator
            model_object = linopy_model_generator.generate_model(features)

        case 'rsome_ro':

            from .model import rsome_ro_model_generator
            model_object = rsome_ro_model_generator.generate_model(features)

        case 'rsome_dro':

            from .model import rsome_dro_model_generator
            model_object = rsome_dro_model_generator.generate_model(features)    

    return model_object
