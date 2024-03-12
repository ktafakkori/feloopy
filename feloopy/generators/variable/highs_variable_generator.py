# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


import highspy as highs_interface
import itertools as it

sets = it.product

POSITIVE = highs_interface.HighsVarType.kContinuous
INTEGER = highs_interface.HighsVarType.kInteger
BINARY = highs_interface.HighsVarType.kInteger
FREE = highs_interface.HighsVarType.kContinuous
INFINITY = highs_interface.kHighsInf

def generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim=0):

    if variable_bound[0] == None:
        variable_bound[0] = -INFINITY

    if variable_bound[1] == None:
        variable_bound[1] = +INFINITY

    match variable_type:

        case 'pvar':

            if variable_dim == 0:

                generated_variable = model_object.addVar(
                    type=POSITIVE, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)

            else:

                if len(variable_dim) == 1:

                    generated_variable = {key: model_object.addVar(
                        type=POSITIVE, lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}") for key in variable_dim[0]}

                else:

                    generated_variable = {key: model_object.addVar(
                        type=POSITIVE, lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}") for key in sets(*variable_dim)}

        case 'bvar':

            if variable_dim == 0:

                generated_variable = model_object.addVar(
                    type=BINARY, lb=0, ub=1, name=variable_name)

            else:

                if len(variable_dim) == 1:

                    generated_variable = {key: model_object.addVar(
                        type=BINARY, lb=0, ub=1, name=f"{variable_name}{key}") for key in variable_dim[0]}

                else:

                    generated_variable = {key: model_object.addVar(
                        type=BINARY, lb=0, ub=1, name=f"{variable_name}{key}") for key in sets(*variable_dim)}

        case 'ivar':

            if variable_dim == 0:

                generated_variable = model_object.addVar(
                    type=INTEGER, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)

            else:

                if len(variable_dim) == 1:

                    generated_variable = {key: model_object.addVar(
                        type=INTEGER, lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}") for key in variable_dim[0]}

                else:

                    generated_variable = {key: model_object.addVar(
                        type=INTEGER, lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}") for key in sets(*variable_dim)}

        case 'fvar':

            if variable_dim == 0:

                generated_variable = model_object.addVar(
                    type=POSITIVE, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)

            else:

                if len(variable_dim) == 1:

                    generated_variable = {key: model_object.addVar(
                        type=POSITIVE, lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}") for key in variable_dim[0]}

                else:

                    generated_variable = {key: model_object.addVar(
                        type=POSITIVE, lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}") for key in sets(*variable_dim)}

    return generated_variable
