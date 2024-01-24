# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


import itertools as it

sets = it.product


def generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim=0):

    match variable_type:

        case 'pvar':

            '''

            Positive Variable Generator


            '''

            if variable_dim == 0:
                generated_variable = model_object.addVariable(
                    variable_name, 1, isInt=False)
            else:
                if len(variable_dim) == 1:
                    generated_variable = {key: model_object.addVariable(
                        f"{variable_name}{key}", 1, isInt=False) for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.addVariable(
                        f"{variable_name}{key}", 1, isInt=False) for key in it.product(*variable_dim)}

        case 'bvar':

            '''

            Binary Variable Generator


            '''

            if variable_dim == 0:
                generated_variable = model_object.addVariable(
                    variable_name, 0, isInt=False)
            else:
                if len(variable_dim) == 1:
                    generated_variable = {key: model_object.addVariable(
                        f"{variable_name}{key}", 1, isInt=True) for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.addVariable(
                        f"{variable_name}{key}", 1, isInt=True) for key in it.product(*variable_dim)}

        case 'ivar':

            '''

            Integer Variable Generator


            '''

            if variable_dim == 0:
                generated_variable = model_object.addVariable(
                    variable_name, 1, isInt=False)
            else:
                if len(variable_dim) == 1:
                    generated_variable = {key: model_object.addVariable(
                        f"{variable_name}{key}", 1, isInt=True) for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.addVariable(
                        f"{variable_name}{key}", 1, isInt=True) for key in it.product(*variable_dim)}

        case 'fvar':

            '''

            Free Variable Generator


            '''

            if variable_dim == 0:
                generated_variable = model_object.addVariable(
                    variable_name, 1, isInt=False)
            else:
                if len(variable_dim) == 1:
                    generated_variable = {key: model_object.addVariable(
                        f"{variable_name}{key}", 1, isInt=False) for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.addVariable(
                        f"{variable_name}{key}", 1, isInt=False) for key in it.product(*variable_dim)}

    
    if variable_bound[0] is not None and variable_bound[1] is not None and len(variable_bound) == 2:
        lb, ub = variable_bound
        if isinstance(generated_variable, dict):
            for key in generated_variable:
                model_object.setLowerBounds(generated_variable[key], lb)
                model_object.setUpperBounds(generated_variable[key], ub)
        else:
            model_object.setLowerBounds(generated_variable, lb)
            model_object.setUpperBounds(generated_variable, ub)
    
    return generated_variable
