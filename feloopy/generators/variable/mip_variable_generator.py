# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

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

            if variable_dim == 0:
                generated_variable = model_object.add_var(var_type=POSITIVE)
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: model_object.add_var(var_type=POSITIVE) for key in variable_dim}
                elif len(variable_dim) == 1:
                    generated_variable = {key: model_object.add_var(var_type=POSITIVE) for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.add_var(var_type=POSITIVE) for key in it.product(*variable_dim)}

        case 'bvar':

            if variable_dim == 0:
                generated_variable = model_object.add_var(var_type=BINARY)
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: model_object.add_var(var_type=BINARY) for key in variable_dim}
                elif len(variable_dim) == 1:
                    generated_variable = {key: model_object.add_var(var_type=BINARY) for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.add_var(var_type=BINARY) for key in it.product(*variable_dim)}

        case 'ivar':

            if variable_dim == 0:
                generated_variable = model_object.add_var(var_type=INTEGER)
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: model_object.add_var(var_type=INTEGER) for key in variable_dim[0]}
                elif len(variable_dim) == 1:
                    generated_variable = {key: model_object.add_var(var_type=INTEGER) for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.add_var(var_type=INTEGER) for key in it.product(*variable_dim)}

        case 'fvar':

            if variable_dim == 0:
                generated_variable = model_object.add_var(var_type=POSITIVE)
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: model_object.add_var(var_type=POSITIVE) for key in variable_dim}
                elif len(variable_dim) == 1:
                    generated_variable = {key: model_object.add_var(var_type=POSITIVE) for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.add_var(var_type=POSITIVE) for key in it.product(*variable_dim)}

    return generated_variable
