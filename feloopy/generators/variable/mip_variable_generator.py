'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
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
