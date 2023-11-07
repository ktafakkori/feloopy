'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.8)                               |
|  Modified: Wednesday, 27th September 2023 11:34:39 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''

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
