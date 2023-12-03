'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.8)                               |
|  Modified: Wednesday, 27th September 2023 11:35:36 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''


import itertools as it

sets = it.product


def generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim=0):

    if variable_bound[0] == None:
        variable_bound[0] = -model_object.infinity()

    if variable_bound[1] == None:
        variable_bound[1] = model_object.infinity()

    match variable_type:

        case 'pvar':

            '''

            Positive Variable Generator


            '''

            if variable_dim == 0:

                GeneratedVariable = model_object.NumVar(
                    variable_bound[0], variable_bound[1], variable_name)

            else:

                if len(variable_dim) == 1:

                    GeneratedVariable = {key: model_object.NumVar(
                        variable_bound[0], variable_bound[1], f"{variable_name}{key}") for key in variable_dim[0]}

                else:

                    GeneratedVariable = {key: model_object.NumVar(
                        variable_bound[0], variable_bound[1], f"{variable_name}{key}") for key in it.product(*variable_dim)}

        case 'bvar':

            '''

            Binary Variable Generator


            '''

            if variable_dim == 0:

                GeneratedVariable = model_object.IntVar(
                    variable_bound[0], variable_bound[1], variable_name)

            else:

                if len(variable_dim) == 1:

                    GeneratedVariable = {key: model_object.IntVar(
                        variable_bound[0], variable_bound[1], f"{variable_name}{key}") for key in variable_dim[0]}

                else:

                    GeneratedVariable = {key: model_object.IntVar(
                        variable_bound[0], variable_bound[1], f"{variable_name}{key}") for key in it.product(*variable_dim)}

        case 'ivar':

            '''

            Integer Variable Generator


            '''

            if variable_bound[0] == 0:

                variable_bound[0] = 0

            if variable_bound[1] == None:

                variable_bound[1] = model_object.infinity()

            if variable_dim == 0:

                GeneratedVariable = model_object.IntVar(
                    variable_bound[0], variable_bound[1], variable_name)

            else:

                if len(variable_dim) == 1:

                    GeneratedVariable = {key: model_object.IntVar(
                        variable_bound[0], variable_bound[1], f"{variable_name}{key}") for key in variable_dim[0]}

                else:

                    GeneratedVariable = {key: model_object.IntVar(
                        variable_bound[0], variable_bound[1], f"{variable_name}{key}") for key in it.product(*variable_dim)}

        case 'fvar':

            '''

            Free Variable Generator


            '''

            if variable_bound[0] == None:

                variable_bound[0] = -model_object.infinity()

            if variable_bound[1] == None:

                variable_bound[1] = model_object.infinity()

            if variable_dim == 0:

                GeneratedVariable = model_object.NumVar(
                    variable_bound[0], variable_bound[1], variable_name)

            else:

                if len(variable_dim) == 1:

                    GeneratedVariable = {key: model_object.NumVar(
                        variable_bound[0], variable_bound[1], f"{variable_name}{key}") for key in variable_dim[0]}

                else:

                    GeneratedVariable = {key: model_object.NumVar(
                        variable_bound[0], variable_bound[1], f"{variable_name}{key}") for key in it.product(*variable_dim)}

    return GeneratedVariable
