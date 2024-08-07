# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import itertools as it
sets = it.product

def generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim=0):

    match variable_type:

        case 'pvar':

            if variable_dim == 0:
                generated_variable = model_object.continuous(low=variable_bound[0], high=variable_bound[1])
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: model_object.continuous(low=variable_bound[0], high=variable_bound[1]) for key in variable_dim}
                elif len(variable_dim) == 1:
                    generated_variable = {key: model_object.continuous(low=variable_bound[0], high=variable_bound[1]) for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.continuous(low=variable_bound[0], high=variable_bound[1]) for key in sets(*variable_dim)}

        case 'bvar':

            if variable_dim == 0:
                generated_variable = model_object.categorical(low=0, high=1)
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: model_object.categorical(low=0, high=1) for key in variable_dim}
                elif len(variable_dim) == 1:
                    generated_variable = {key: model_object.categorical(low=0, high=1) for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.categorical(low=0, high=1) for key in sets(*variable_dim)}

        case 'ivar':

            if variable_dim == 0:
                generated_variable = model_object.categorical(low=variable_bound[0], high=variable_bound[1])
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: model_object.categorical(low=variable_bound[0], high=variable_bound[1]) for key in variable_dim}
                elif len(variable_dim) == 1:
                    generated_variable = {key: model_object.categorical(low=variable_bound[0], high=variable_bound[1]) for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.categorical(low=variable_bound[0], high=variable_bound[1])  for key in sets(*variable_dim)}

        case 'fvar':

            if variable_dim == 0:
                generated_variable = model_object.continuous(low=variable_bound[0], high=variable_bound[1])
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: model_object.continuous(low=variable_bound[0], high=variable_bound[1]) for key in variable_dim}
                elif len(variable_dim) == 1:
                    generated_variable = {key: model_object.continuous(low=variable_bound[0], high=variable_bound[1]) for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.continuous(low=variable_bound[0], high=variable_bound[1]) for key in sets(*variable_dim)}

    return generated_variable
