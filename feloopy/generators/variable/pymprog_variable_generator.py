# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import pymprog as pymprog_interface
import itertools as it

sets = it.product

VariableGenerator = pymprog_interface.var

def generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim=0):

    match variable_type:

        case 'pvar':

            if variable_dim == 0:
                generated_variable = VariableGenerator(variable_name, bounds=(variable_bound[0], variable_bound[1]))
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: VariableGenerator(variable_name, bounds=(variable_bound[0], variable_bound[1])) for key in variable_dim}
                elif len(variable_dim) == 1:
                    generated_variable = {key: VariableGenerator(variable_name, bounds=(variable_bound[0], variable_bound[1])) for key in variable_dim[0]}
                else:
                    generated_variable = {key: VariableGenerator(variable_name, bounds=(variable_bound[0], variable_bound[1])) for key in it.product(*variable_dim)}

        case 'bvar':

            if variable_dim == 0:
                generated_variable = VariableGenerator(variable_name, bounds=(variable_bound[0], variable_bound[1]), kind=int)
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: VariableGenerator(variable_name, bounds=(variable_bound[0], variable_bound[1]), kind=int) for key in variable_dim}
                if len(variable_dim) == 1:
                    generated_variable = {key: VariableGenerator(variable_name, bounds=(variable_bound[0], variable_bound[1]), kind=int) for key in variable_dim[0]}
                else:
                    generated_variable = {key: VariableGenerator(variable_name, bounds=(variable_bound[0], variable_bound[1]), kind=int) for key in it.product(*variable_dim)}

        case 'ivar':

            if variable_dim == 0:
                generated_variable = VariableGenerator(variable_name, bounds=(variable_bound[0], variable_bound[1]), kind=int)
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: VariableGenerator(variable_name, bounds=(variable_bound[0], variable_bound[1]), kind=int) for key in variable_dim}
                elif len(variable_dim) == 1:
                    generated_variable = {key: VariableGenerator(variable_name, bounds=(variable_bound[0], variable_bound[1]), kind=int) for key in variable_dim[0]}
                else:
                    generated_variable = {key: VariableGenerator(variable_name, bounds=(variable_bound[0], variable_bound[1]), kind=int) for key in it.product(*variable_dim)}

        case 'fvar':

            if variable_dim == 0:
                generated_variable = VariableGenerator(variable_name, bounds=(variable_bound[0], variable_bound[1]))
            else:
                if isinstance(variable_dim,set):
                    generated_variable = {key: VariableGenerator(variable_name, bounds=(variable_bound[0], variable_bound[1])) for key in variable_dim}
                elif len(variable_dim) == 1:
                    generated_variable = {key: VariableGenerator(variable_name, bounds=(variable_bound[0], variable_bound[1])) for key in variable_dim[0]}
                else:
                    generated_variable = {key: VariableGenerator(variable_name, bounds=(variable_bound[0], variable_bound[1])) for key in it.product(*variable_dim)}

    return generated_variable
