# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import itertools as it

sets = it.product

def generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim=0):

    match variable_type:

        case 'pvar':

            if variable_bound[0] == 0:
                variable_bound[0] = 0

            if variable_dim == 0:
                generated_variable = model_object.NewNumVar(variable_bound[0], variable_bound[1], variable_name)
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: model_object.NewNumVar(variable_bound[0], variable_bound[1], f"{variable_name}{key}") for key in variable_dim}
                elif len(variable_dim) == 1:
                    generated_variable = {key: model_object.NewNumVar(variable_bound[0], variable_bound[1], f"{variable_name}{key}") for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.NewNumVar(variable_bound[0], variable_bound[1], f"{variable_name}{key}") for key in it.product(*variable_dim)}

        case 'bvar':

            if variable_bound[0] == 0:
                variable_bound[0] = 0
            if variable_bound[1] == 1:
                variable_bound[1] = 1
            if variable_dim == 0:
                generated_variable = model_object.NewIntVar(variable_bound[0], variable_bound[1], variable_name)
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: model_object.NewIntVar(variable_bound[0], variable_bound[1], f"{variable_name}{key}") for key in variable_dim}
                elif len(variable_dim) == 1:
                    generated_variable = {key: model_object.NewIntVar(variable_bound[0], variable_bound[1], f"{variable_name}{key}") for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.NewIntVar(variable_bound[0], variable_bound[1], f"{variable_name}{key}") for key in it.product(*variable_dim)}

        case 'ivar':

            if variable_bound[0] == 0:
                variable_bound[0] = 0
            if variable_dim == 0:
                generated_variable = model_object.NewIntVar(variable_bound[0], variable_bound[1], variable_name)
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: model_object.NewIntVar(variable_bound[0], variable_bound[1], f"{variable_name}{key}") for key in variable_dim}
                elif len(variable_dim) == 1:
                    generated_variable = {key: model_object.NewIntVar(variable_bound[0], variable_bound[1], f"{variable_name}{key}") for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.NewIntVar(variable_bound[0], variable_bound[1], f"{variable_name}{key}") for key in it.product(*variable_dim)}

        case 'fvar':
            if variable_dim == 0:
                generated_variable = model_object.NewNumVar(variable_bound[0], variable_bound[1], variable_name)
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: model_object.NewNumVar(variable_bound[0], variable_bound[1], f"{variable_name}{key}") for key in variable_dim}
                elif len(variable_dim) == 1:
                    generated_variable = {key: model_object.NewNumVar(variable_bound[0], variable_bound[1], f"{variable_name}{key}") for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.NewNumVar(variable_bound[0], variable_bound[1], f"{variable_name}{key}") for key in it.product(*variable_dim)}

    return generated_variable
