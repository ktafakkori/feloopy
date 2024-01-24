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

            '''

            Positive Variable Generator


            '''

            if variable_dim == 0:
                GeneratedVariable = POSITIVE(
                    variable_name, lower=variable_bound[0], upper=variable_bound[1])
            else:
                if len(variable_dim) == 1:
                    GeneratedVariable = {key: POSITIVE(f'{variable_name}{key}', lower=variable_bound[0], upper=variable_bound[1]) for key in variable_dim[0]}
                else:
                    GeneratedVariable = {key: POSITIVE(f'{variable_name}{key}', lower=variable_bound[0], upper=variable_bound[1]) for key in it.product(*variable_dim)}

        case 'bvar':

            '''

            Binary Variable Generator


            '''
            if variable_dim == 0:
                GeneratedVariable = BINARY(variable_name)
            else:
                if len(variable_dim) == 1:
                    GeneratedVariable = {key: BINARY(f'{variable_name}{key}') for key in variable_dim[0]}
                else:
                    GeneratedVariable = {key: BINARY(f'{variable_name}{key}') for key in it.product(*variable_dim)}

        case 'ivar':

            '''

            Integer Variable Generator


            '''
            if variable_dim == 0:
                GeneratedVariable = INTEGER(
                    variable_name, lower=variable_bound[0], upper=variable_bound[1])
            else:
                if len(variable_dim) == 1:
                    GeneratedVariable = {key: INTEGER(f'{variable_name}{key}', lower=variable_bound[0], upper=variable_bound[1]) for key in variable_dim[0]}
                else:
                    GeneratedVariable = {key: INTEGER(f'{variable_name}{key}', lower=variable_bound[0], upper=variable_bound[1]) for key in it.product(*variable_dim)}

        case 'fvar':

            '''

            Free Variable Generator


            '''
            if variable_dim == 0:
                GeneratedVariable = FREE(
                    variable_name, lower=variable_bound[0], upper=variable_bound[1])
            else:
                if len(variable_dim) == 1:
                    GeneratedVariable = {key: FREE(f'{variable_name}{key}', lower=variable_bound[0], upper=variable_bound[1]) for key in variable_dim[0]}
                else:
                    GeneratedVariable = {key: FREE(f'{variable_name}{key}', lower=variable_bound[0], upper=variable_bound[1]) for key in it.product(*variable_dim)}

    return GeneratedVariable
