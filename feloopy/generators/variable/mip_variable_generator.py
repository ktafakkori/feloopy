'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.8)                               |
|  Modified: Wednesday, 27th September 2023 11:35:24 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''

import mip as mip_interface
import itertools as it

sets = it.product

BINARY = mip_interface.BINARY
POSITIVE = mip_interface.CONTINUOUS
INTEGER = mip_interface.INTEGER
FREE = mip_interface.CONTINUOUS


def generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim=0):

    match variable_type:

        case 'pvar':

            '''

            Positive Variable Generator


            '''

            if variable_dim == 0:
                GeneratedVariable = model_object.add_var(var_type=POSITIVE)
            else:
                if len(variable_dim) == 1:
                    GeneratedVariable = {key: model_object.add_var(
                        var_type=POSITIVE) for key in variable_dim[0]}
                else:
                    GeneratedVariable = {key: model_object.add_var(
                        var_type=POSITIVE) for key in it.product(*variable_dim)}

        case 'bvar':

            '''

            Binary Variable Generator


            '''

            if variable_dim == 0:
                GeneratedVariable = model_object.add_var(var_type=BINARY)
            else:
                if len(variable_dim) == 1:
                    GeneratedVariable = {key: model_object.add_var(
                        var_type=BINARY) for key in variable_dim[0]}
                else:
                    GeneratedVariable = {key: model_object.add_var(
                        var_type=BINARY) for key in it.product(*variable_dim)}

        case 'ivar':

            '''

            Integer Variable Generator


            '''

            if variable_dim == 0:
                GeneratedVariable = model_object.add_var(var_type=INTEGER)
            else:
                if len(variable_dim) == 1:
                    GeneratedVariable = {key: model_object.add_var(
                        var_type=INTEGER) for key in variable_dim[0]}
                else:
                    GeneratedVariable = {key: model_object.add_var(
                        var_type=INTEGER) for key in it.product(*variable_dim)}

        case 'fvar':

            '''

            Free Variable Generator


            '''
            if variable_dim == 0:
                GeneratedVariable = model_object.add_var(var_type=POSITIVE)
            else:
                if len(variable_dim) == 1:
                    GeneratedVariable = {key: model_object.add_var(
                        var_type=POSITIVE) for key in variable_dim[0]}
                else:
                    GeneratedVariable = {key: model_object.add_var(
                        var_type=POSITIVE) for key in it.product(*variable_dim)}

    return GeneratedVariable
