# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import pulp as pulp_interface
import itertools as it

sets = it.product

VariableGenerator = pulp_interface.LpVariable

POSITIVE = pulp_interface.LpContinuous
BINARY = pulp_interface.LpBinary
INTEGER = pulp_interface.LpInteger
FREE = pulp_interface.LpContinuous

def generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim=0):

    match variable_type:

        case 'pvar':

            if variable_dim == 0:
                generated_variable = VariableGenerator(variable_name, variable_bound[0], variable_bound[1], POSITIVE)
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: VariableGenerator(f"{variable_name}{key}", variable_bound[0], variable_bound[1], POSITIVE) for key in variable_dim}
                elif len(variable_dim) == 1:
                    generated_variable = {key: VariableGenerator(f"{variable_name}{key}", variable_bound[0], variable_bound[1], POSITIVE) for key in variable_dim[0]}
                else:
                    generated_variable = {key: VariableGenerator(f"{variable_name}{key}", variable_bound[0], variable_bound[1], POSITIVE) for key in sets(*variable_dim)}

        case 'bvar':

            if variable_dim == 0:
                generated_variable = VariableGenerator(variable_name, variable_bound[0], variable_bound[1], BINARY)
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: VariableGenerator(f"{variable_name}{key}", variable_bound[0], variable_bound[1], BINARY) for key in variable_dim}
                elif len(variable_dim) == 1:
                    generated_variable = {key: VariableGenerator(f"{variable_name}{key}", variable_bound[0], variable_bound[1], BINARY) for key in variable_dim[0]}
                else:
                    generated_variable = {key: VariableGenerator(f"{variable_name}{key}", variable_bound[0], variable_bound[1], BINARY) for key in sets(*variable_dim)}

        case 'ivar':

            if variable_dim == 0:
                generated_variable = VariableGenerator(variable_name, variable_bound[0], variable_bound[1], INTEGER)
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: VariableGenerator(f"{variable_name}{key}", variable_bound[0], variable_bound[1], INTEGER) for key in variable_dim}
                elif len(variable_dim) == 1 or isinstance(variable_dim,set):
                    generated_variable = {key: VariableGenerator(f"{variable_name}{key}", variable_bound[0], variable_bound[1], INTEGER) for key in variable_dim[0]}
                else:
                    generated_variable = {key: VariableGenerator(f"{variable_name}{key}", variable_bound[0], variable_bound[1], INTEGER) for key in sets(*variable_dim)}

        case 'fvar':

            if variable_dim == 0:
                generated_variable = VariableGenerator(variable_name, variable_bound[0], variable_bound[1], FREE)
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: VariableGenerator(f"{variable_name}{key}", variable_bound[0], variable_bound[1], FREE) for key in variable_dim}
                elif len(variable_dim) == 1 or isinstance(variable_dim,set):
                    generated_variable = {key: VariableGenerator(f"{variable_name}{key}", variable_bound[0], variable_bound[1], FREE) for key in variable_dim[0]}
                else:
                    generated_variable = {key: VariableGenerator(f"{variable_name}{key}", variable_bound[0], variable_bound[1], FREE) for key in sets(*variable_dim)}

    return generated_variable