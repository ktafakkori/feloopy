'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

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
                    GeneratedVariable = {key: POSITIVE(
                        variable_name, lower=variable_bound[0], upper=variable_bound[1]) for key in variable_dim[0]}
                else:
                    GeneratedVariable = {key: POSITIVE(
                        variable_name, lower=variable_bound[0], upper=variable_bound[1]) for key in it.product(*variable_dim)}

        case 'bvar':

            '''

            Binary Variable Generator


            '''
            if variable_dim == 0:
                GeneratedVariable = BINARY(variable_name)
            else:
                if len(variable_dim) == 1:
                    GeneratedVariable = {key: BINARY(
                        variable_name) for key in variable_dim[0]}
                else:
                    GeneratedVariable = {key: BINARY(
                        variable_name) for key in it.product(*variable_dim)}

        case 'ivar':

            '''

            Integer Variable Generator


            '''
            if variable_dim == 0:
                GeneratedVariable = INTEGER(
                    variable_name, lower=variable_bound[0], upper=variable_bound[1])
            else:
                if len(variable_dim) == 1:
                    GeneratedVariable = {key: INTEGER(
                        variable_name, lower=variable_bound[0], upper=variable_bound[1]) for key in variable_dim[0]}
                else:
                    GeneratedVariable = {key: INTEGER(
                        variable_name, lower=variable_bound[0], upper=variable_bound[1]) for key in it.product(*variable_dim)}

        case 'fvar':

            '''

            Free Variable Generator


            '''
            if variable_dim == 0:
                GeneratedVariable = FREE(
                    variable_name, lower=variable_bound[0], upper=variable_bound[1])
            else:
                if len(variable_dim) == 1:
                    GeneratedVariable = {key: FREE(
                        variable_name, lower=variable_bound[0], upper=variable_bound[1]) for key in variable_dim[0]}
                else:
                    GeneratedVariable = {key: FREE(
                        variable_name, lower=variable_bound[0], upper=variable_bound[1]) for key in it.product(*variable_dim)}

    return GeneratedVariable
