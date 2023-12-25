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

                GeneratedVariable = model_object.continuous_var(
                    min=variable_bound[0], max=variable_bound[1])

            else:

                if len(variable_dim) == 1:

                    GeneratedVariable = {key: model_object.continuous_var(
                        min=variable_bound[0], max=variable_bound[1]) for key in variable_dim[0]}

                else:

                    GeneratedVariable = {key: model_object.continuous_var(
                        min=variable_bound[0], max=variable_bound[1]) for key in sets(*variable_dim)}

        case 'bvar':

            '''

            Binary Variable Generator


            '''

            if variable_dim == 0:

                GeneratedVariable = model_object.binary_var()

            else:

                if len(variable_dim) == 1:

                    GeneratedVariable = {
                        key: model_object.binary_var() for key in variable_dim[0]}

                else:

                    GeneratedVariable = {
                        key: model_object.binary_var() for key in sets(*variable_dim)}

        case 'ivar':

            '''

            Integer Variable Generator


            '''

            if variable_dim == 0:

                GeneratedVariable = model_object.integer_var(
                    min=variable_bound[0], max=variable_bound[1])

            else:
                if len(variable_dim) == 1:

                    GeneratedVariable = {key: model_object.integer_var(
                        min=variable_bound[0], max=variable_bound[1]) for key in variable_dim[0]}

                else:

                    GeneratedVariable = {key: model_object.integer_var(
                        min=variable_bound[0], max=variable_bound[1]) for key in sets(*variable_dim)}

        case 'fvar':

            '''

            Free Variable Generator


            '''

            if variable_dim == 0:

                GeneratedVariable = model_object.continuous_var(
                    min=variable_bound[0], max=variable_bound[1])

            else:

                if len(variable_dim) == 1:

                    GeneratedVariable = {key: model_object.continuous_var(
                        min=variable_bound[0], max=variable_bound[1]) for key in variable_dim[0]}

                else:

                    GeneratedVariable = {key: model_object.continuous_var(
                        min=variable_bound[0], max=variable_bound[1]) for key in sets(*variable_dim)}

    return GeneratedVariable
