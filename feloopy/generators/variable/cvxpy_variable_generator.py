# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import cvxpy as cvxpy_interface
import itertools as it
import warnings
warnings.filterwarnings("ignore")

sets = it.product
VariableGenerator = cvxpy_interface.Variable

def generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim=0):

    match variable_type:
        case 'pvar':
            if variable_dim == 0:
                generated_variable = VariableGenerator(1, integer=False, nonneg=True, name=variable_name)
            else:
                if len(variable_dim) == 1:
                    generated_variable = {key: VariableGenerator(1, integer=False, nonneg=True, name=f"{variable_name}_{key}") for key in variable_dim[0]}
                else:
                    generated_variable = {key: VariableGenerator(1, integer=False, nonneg=True, name=f"{variable_name}_{key}") for key in sets(*variable_dim)}

        case 'bvar':
            if variable_dim == 0:
                generated_variable = VariableGenerator(1, integer=True, name=variable_name)
            else:
                if len(variable_dim) == 1:
                    generated_variable = {key: VariableGenerator(1, integer=True, name=f"{variable_name}_{key}") for key in variable_dim[0]}
                else:
                    generated_variable = {key: VariableGenerator(1, integer=True, name=f"{variable_name}_{key}") for key in sets(*variable_dim)}

        case 'ivar':
            if variable_dim == 0:
                generated_variable = VariableGenerator(1, integer=True, name=variable_name)
            else:
                if len(variable_dim) == 1:
                    generated_variable = {key: VariableGenerator(1, integer=True, name=f"{variable_name}_{key}") for key in variable_dim[0]}
                else:
                    generated_variable = {key: VariableGenerator(1, integer=True, name=f"{variable_name}_{key}") for key in sets(*variable_dim)}

        case 'fvar':
            if variable_dim == 0:
                generated_variable = VariableGenerator(1, integer=False, nonneg=False, name=variable_name)
            else:
                if len(variable_dim) == 1:
                    generated_variable = {key: VariableGenerator(1, integer=False, nonneg=False, name=f"{variable_name}_{key}") for key in variable_dim[0]}
                else:
                    generated_variable = {key: VariableGenerator(1, integer=False, nonneg=False, name=f"{variable_name}_{key}") for key in sets(*variable_dim)}

        case 'ftvar':

            if variable_dim == 0:
                generated_variable = VariableGenerator(1, integer=False, nonneg=False, name=variable_name)
            else:
                dims = tuple(len(dim) for dim in variable_dim)
                generated_variable = VariableGenerator(dims, integer=False, name=variable_name)

        case 'ptvar':
            if variable_dim ==0:
                generated_variable = VariableGenerator(1, integer=False, nonneg=True, name=variable_name)
            else:
                dims = tuple(len(dim) for dim in variable_dim)
                generated_variable = VariableGenerator(dims, integer=False, nonneg=True, name=variable_name)

        case 'itvar':
            if variable_dim ==0:
                generated_variable = VariableGenerator(1, integer=True, name=variable_name)
            else:
                dims = tuple(len(dim) for dim in variable_dim)
                generated_variable = VariableGenerator(dims, integer=True, name=variable_name)

        case 'btvar':
            if variable_dim ==0:
                generated_variable = VariableGenerator(1, integer=True, name=variable_name)
            else:
                dims = tuple(len(dim) for dim in variable_dim)
                generated_variable = VariableGenerator(dims, integer=True, name=variable_name)

    return generated_variable
