# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import itertools as it

sets = it.product

def generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim=0):

    if variable_bound[0] == None:
        variable_bound[0] = -float('inf')

    if variable_bound[1] == None:
        variable_bound[1] = float('inf')

    match variable_type:

        case 'pvar':

            if variable_dim == 0:
                generated_variable = model_object.add_variable(lb=variable_bound[0], ub=variable_bound[1], name=variable_name, is_integer=False)
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: model_object.add_variable(lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}", is_integer=False) for key in variable_dim}
                elif len(variable_dim) == 1:
                    generated_variable = {key: model_object.add_variable(lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}", is_integer=False) for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.add_variable(lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}", is_integer=False) for key in it.product(*variable_dim)}

        case 'bvar':

            if variable_dim == 0:
                generated_variable = model_object.add_binary_variable(name=variable_name)
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: model_object.add_binary_variable(name=f"{variable_name}{key}") for key in variable_dim}
                elif len(variable_dim) == 1:
                    generated_variable = {key: model_object.add_binary_variable(name=f"{variable_name}{key}") for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.add_binary_variable(name=f"{variable_name}{key}") for key in it.product(*variable_dim)}

        case 'ivar':

            if variable_dim == 0:
                generated_variable = model_object.add_integer_variable(lb=variable_bound[0], ub=variable_bound[1], name=variable_name)
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: model_object.add_integer_variable(lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}") for key in variable_dim}
                elif len(variable_dim) == 1:
                    generated_variable = {key: model_object.add_integer_variable(lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}") for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.add_integer_variable(lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}") for key in it.product(*variable_dim)}

        case 'fvar':

            if variable_dim == 0:
                generated_variable = model_object.add_variable(lb=variable_bound[0], ub=variable_bound[1], name=variable_name, is_integer=False)
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: model_object.add_variable(lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}", is_integer=False) for key in variable_dim}
                elif len(variable_dim) == 1:
                    generated_variable = {key: model_object.add_variable(lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}", is_integer=False) for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.add_variable(lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}", is_integer=False) for key in it.product(*variable_dim)}

    return generated_variable
