# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import itertools as it
sets = it.product

def generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim=0):
    
    
    print(variable_bound)
    
    if variable_bound[0] == 0:
        variable_bound = 0.0000001
         
    if variable_bound[0] == None:
        variable_bound = -1e9
        
    if variable_bound[1] == None:
        variable_bound = 1e+9
        
    match variable_type:

        case 'pvar':

            '''
            Positive Variable Generator
            '''

            if variable_dim == 0:
                GeneratedVariable = model_object.continuous(low=variable_bound[0], high=variable_bound[1])
            else:
                if len(variable_dim) == 1:
                    GeneratedVariable = {key: model_object.continuous(low=variable_bound[0], high=variable_bound[1]) for key in variable_dim[0]}
                else:
                    GeneratedVariable = {key: model_object.continuous(low=variable_bound[0], high=variable_bound[1]) for key in sets(*variable_dim)}

        case 'bvar':

            '''
            Binary Variable Generator
            '''

            if variable_dim == 0:
                GeneratedVariable = model_object.categorical(low=0, high=1)

            else:
                if len(variable_dim) == 1:
                    GeneratedVariable = {key: model_object.categorical(low=0, high=1) for key in variable_dim[0]}
                else:
                    GeneratedVariable = {key: model_object.categorical(low=0, high=1) for key in sets(*variable_dim)}

        case 'ivar':

            '''
            Integer Variable Generator
            '''

            if variable_dim == 0:
                GeneratedVariable = model_object.categorical(low=variable_bound[0], high=variable_bound[1])
            else:
                if len(variable_dim) == 1:
                    GeneratedVariable = {key: model_object.categorical(low=variable_bound[0], high=variable_bound[1]) for key in variable_dim[0]}
                else:
                    GeneratedVariable = {key: model_object.categorical(low=variable_bound[0], high=variable_bound[1])  for key in sets(*variable_dim)}

        case 'fvar':

            '''
            Free Variable Generator
            '''

            if variable_dim == 0:
                GeneratedVariable = model_object.continuous(low=variable_bound[0], high=variable_bound[1])
            else:
                if len(variable_dim) == 1:
                    GeneratedVariable = {key: model_object.continuous(low=variable_bound[0], high=variable_bound[1]) for key in variable_dim[0]}
                else:
                    GeneratedVariable = {key: model_object.continuous(low=variable_bound[0], high=variable_bound[1]) for key in sets(*variable_dim)}

    return GeneratedVariable
