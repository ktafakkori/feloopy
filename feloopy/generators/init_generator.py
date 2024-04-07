# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

def generate_init(features, variable, value, fix):
    
    data = {
        
        'features': features,
        'variable': variable,
        'value': value,
        'fix': fix
    }

    match features['interface_name']:

        case 'pulp':

            from .init import pulp_init_generator
            model_object = pulp_init_generator.set_init_value(**data)

        case 'pyomo':

            from .init import pyomo_init_generator
            model_object = pyomo_init_generator.set_init_value(**data)

        case 'gurobi':

            from .init import gurobi_init_generator
            model_object = gurobi_init_generator.set_init_value(**data)

        case 'cplex':
            from .init import cplex_init_generator
            model_object = cplex_init_generator.set_init_value(**data)

        case 'gekko':
            from .init import gekko_init_generator
            model_object = gekko_init_generator.set_init_value(**data)

        case 'copt':
            from .init import copt_init_generator
            model_object = copt_init_generator.set_init_value(**data)
                       
    return model_object
