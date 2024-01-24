# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


import itertools as it

sets = it.product

def generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim=0):

    match variable_type:
        case 'pvar':
            if variable_dim == 0:
                generated_variable = model_object.Var(lb=variable_bound[0], ub=variable_bound[1], integer=False, name=variable_name)
            else:
                if len(variable_dim) == 1:
                    generated_variable = {key: model_object.Var(lb=variable_bound[0], ub=variable_bound[1], integer=False, name=f'{variable_name}_{key}') for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.Var(lb=variable_bound[0], ub=variable_bound[1], integer=False, name=f'{variable_name}_{key}') for key in sets(*variable_dim)}

        case 'bvar':
            if variable_dim == 0:
                generated_variable = model_object.Var(lb=variable_bound[0], ub=variable_bound[1], integer=True, name=variable_name)
            else:
                if len(variable_dim) == 1:
                    generated_variable = {key: model_object.Var(lb=0, ub=1, integer=True, name=f'{variable_name}_{key}') for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.Var(lb=0, ub=1, integer=True, name=f'{variable_name}_{key}') for key in sets(*variable_dim)}

        case 'ivar':
            if variable_dim == 0:
                generated_variable = model_object.Var(lb=variable_bound[0], ub=variable_bound[1], integer=True, name=variable_name)
            else:
                if len(variable_dim) == 1:
                    generated_variable = {key: model_object.Var(lb=variable_bound[0], ub=variable_bound[1], integer=True, name=f'{variable_name}_{key}') for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.Var(lb=variable_bound[0], ub=variable_bound[1], integer=True, name=f'{variable_name}_{key}') for key in sets(*variable_dim)}

        case 'fvar':
            if variable_dim == 0:
                generated_variable = model_object.Var(name=variable_name)
            else:
                if len(variable_dim) == 1:
                    generated_variable = {key: model_object.Var(name=f'{variable_name}_{key}') for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.Var(name=f'{variable_name}_{key}') for key in sets(*variable_dim)}

        case 'ftvar':
            if variable_dim==0:
                generated_variable = model_object.Var(name=variable_name)
            else:
                dims = tuple(len(dim) for dim in variable_dim)
                generated_variable = model_object.Array(model_object.Var, dims)

        case 'ptvar':
            if variable_dim==0:
                generated_variable = model_object.Var(lb=variable_bound[0], ub=variable_bound[1], integer=False, name=variable_name)
            else:
                dims = tuple(len(dim) for dim in variable_dim)
                generated_variable = model_object.Array(model_object.Var, dims, lb=0)

        case 'itvar':
            if variable_dim==0:
                generated_variable = model_object.Var(lb=variable_bound[0], ub=variable_bound[1], integer=True, name=variable_name)
            else:
                dims = tuple(len(dim) for dim in variable_dim)
                generated_variable = model_object.Array(model_object.Var, dims, integer=True)

        case 'btvar':
            if variable_dim==0:
                 generated_variable = model_object.Var(lb=variable_bound[0], ub=variable_bound[1], integer=True, name=variable_name)
            else:
                dims = tuple(len(dim) for dim in variable_dim)
                generated_variable = model_object.Array(model_object.Var, dims, lb=0, ub=1, integer=True)

    return generated_variable

