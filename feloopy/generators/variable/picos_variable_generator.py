# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import itertools as it
import picos as picos_interface

sets = it.product

BINARY = picos_interface.BinaryVariable
POSITIVE = picos_interface.RealVariable
INTEGER = picos_interface.IntegerVariable
FREE = picos_interface.RealVariable

def generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim=0):

    match variable_type:

        case 'pvar':

            if variable_dim == 0:
                generated_variable = POSITIVE(variable_name, lower=variable_bound[0], upper=variable_bound[1])
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: POSITIVE(f'{variable_name}{key}', lower=variable_bound[0], upper=variable_bound[1]) for key in variable_dim}
                elif len(variable_dim) == 1:
                    generated_variable = {key: POSITIVE(f'{variable_name}{key}', lower=variable_bound[0], upper=variable_bound[1]) for key in variable_dim[0]}
                else:
                    generated_variable = {key: POSITIVE(f'{variable_name}{key}', lower=variable_bound[0], upper=variable_bound[1]) for key in it.product(*variable_dim)}

        case 'bvar':

            if variable_dim == 0:
                generated_variable = BINARY(variable_name)
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: BINARY(f'{variable_name}{key}') for key in variable_dim}
                elif len(variable_dim) == 1:
                    generated_variable = {key: BINARY(f'{variable_name}{key}') for key in variable_dim[0]}
                else:
                    generated_variable = {key: BINARY(f'{variable_name}{key}') for key in it.product(*variable_dim)}

        case 'ivar':

            if variable_dim == 0:
                generated_variable = INTEGER(variable_name, lower=variable_bound[0], upper=variable_bound[1])
            else:
                if isinstance(variable_dim,set):
                     generated_variable = {key: INTEGER(f'{variable_name}{key}', lower=variable_bound[0], upper=variable_bound[1]) for key in variable_dim}
                elif len(variable_dim) == 1:
                    generated_variable = {key: INTEGER(f'{variable_name}{key}', lower=variable_bound[0], upper=variable_bound[1]) for key in variable_dim[0]}
                else:
                    generated_variable = {key: INTEGER(f'{variable_name}{key}', lower=variable_bound[0], upper=variable_bound[1]) for key in it.product(*variable_dim)}

        case 'fvar':

            if variable_dim == 0:
                generated_variable = FREE(variable_name, lower=variable_bound[0], upper=variable_bound[1])
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: FREE(f'{variable_name}{key}', lower=variable_bound[0], upper=variable_bound[1]) for key in variable_dim}
                elif len(variable_dim) == 1:
                    generated_variable = {key: FREE(f'{variable_name}{key}', lower=variable_bound[0], upper=variable_bound[1]) for key in variable_dim[0]}
                else:
                    generated_variable = {key: FREE(f'{variable_name}{key}', lower=variable_bound[0], upper=variable_bound[1]) for key in it.product(*variable_dim)}              
    
    return generated_variable