'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.8)                               |
|  Modified: Wednesday, 27th September 2023 11:35:48 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''


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

            '''

            Positive Variable Generator


            '''

            if variable_dim == 0:

                GeneratedVariable = VariableGenerator(
                    variable_name, variable_bound[0], variable_bound[1], POSITIVE)

            else:

                if len(variable_dim) == 1:

                    GeneratedVariable = {key: VariableGenerator(
                        f"{variable_name}{key}", variable_bound[0], variable_bound[1], POSITIVE) for key in variable_dim[0]}

                else:

                    GeneratedVariable = {key: VariableGenerator(
                        f"{variable_name}{key}", variable_bound[0], variable_bound[1], POSITIVE) for key in sets(*variable_dim)}

        case 'bvar':

            '''

            Binary Variable Generator


            '''

            if variable_dim == 0:

                GeneratedVariable = VariableGenerator(
                    variable_name, variable_bound[0], variable_bound[1], BINARY)

            else:

                if len(variable_dim) == 1:

                    GeneratedVariable = {key: VariableGenerator(
                        f"{variable_name}{key}", variable_bound[0], variable_bound[1], BINARY) for key in variable_dim[0]}

                else:

                    GeneratedVariable = {key: VariableGenerator(
                        f"{variable_name}{key}", variable_bound[0], variable_bound[1], BINARY) for key in sets(*variable_dim)}

        case 'ivar':

            '''

            Integer Variable Generator


            '''

            if variable_dim == 0:

                GeneratedVariable = VariableGenerator(
                    variable_name, variable_bound[0], variable_bound[1], INTEGER)

            else:

                if len(variable_dim) == 1:

                    GeneratedVariable = {key: VariableGenerator(
                        f"{variable_name}{key}", variable_bound[0], variable_bound[1], INTEGER) for key in variable_dim[0]}

                else:

                    GeneratedVariable = {key: VariableGenerator(
                        f"{variable_name}{key}", variable_bound[0], variable_bound[1], INTEGER) for key in sets(*variable_dim)}

        case 'fvar':

            '''

            Free Variable Generator


            '''

            if variable_dim == 0:

                GeneratedVariable = VariableGenerator(
                    variable_name, variable_bound[0], variable_bound[1], FREE)

            else:

                if len(variable_dim) == 1:

                    GeneratedVariable = {key: VariableGenerator(
                        f"{variable_name}{key}", variable_bound[0], variable_bound[1], FREE) for key in variable_dim[0]}

                else:

                    GeneratedVariable = {key: VariableGenerator(
                        f"{variable_name}{key}", variable_bound[0], variable_bound[1], FREE) for key in sets(*variable_dim)}

    return GeneratedVariable
