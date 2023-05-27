'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

import cvxpy as cvxpy_interface
import itertools as it
import warnings
warnings.filterwarnings("ignore")

sets = it.product

VariableGenerator = cvxpy_interface.Variable


def generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim=0):

    match variable_type:

        case 'pvar':

            '''

            Positive Variable Generator


            '''

            if variable_dim == 0:

                generated_variable = VariableGenerator(
                    1, integer=False,  nonneg=True, name=variable_name)

            else:

                if len(variable_dim) == 1:

                    generated_variable = {key: VariableGenerator(
                        1, integer=False,  nonneg=True, name=f"{variable_name}{key}") for key in variable_dim[0]}

                else:

                    generated_variable = {key: VariableGenerator(
                        1, integer=False,  nonneg=True, name=f"{variable_name}{key}") for key in sets(*variable_dim)}

        case 'bvar':

            '''

            Binary Variable Generator


            '''

            if variable_dim == 0:

                generated_variable = VariableGenerator(
                    1,  nonneg=True, integer=True, name=variable_name)

            else:

                if len(variable_dim) == 1:

                    generated_variable = {key: VariableGenerator(
                        1, integer=True, nonneg=True, name=f"{variable_name}{key}") for key in variable_dim[0]}

                else:

                    generated_variable = {key: VariableGenerator(
                        1, integer=True, nonneg=True, name=f"{variable_name}{key}") for key in sets(*variable_dim)}

        case 'ivar':

            '''

            Integer Variable Generator


            '''

            if variable_dim == 0:

                generated_variable = VariableGenerator(
                    1,  nonneg=True, integer=True, name=variable_name)

            else:

                if len(variable_dim) == 1:

                    generated_variable = {key: VariableGenerator(
                        1,  nonneg=True, integer=True, name=f"{variable_name}{key}") for key in variable_dim[0]}

                else:

                    generated_variable = {key: VariableGenerator(
                        1,  nonneg=True, integer=True, name=f"{variable_name}{key}") for key in sets(*variable_dim)}

        case 'fvar':

            '''

            Free Variable Generator


            '''

            if variable_dim == 0:

                generated_variable = VariableGenerator(
                    1, integer=False,  nonneg=False, name=variable_name)

            else:

                if len(variable_dim) == 1:

                    generated_variable = {key: VariableGenerator(
                        1, integer=False,  nonneg=False, name=f"{variable_name}{key}") for key in variable_dim[0]}

                else:

                    generated_variable = {key: VariableGenerator(
                        1, integer=False,  nonneg=False, name=f"{variable_name}{key}") for key in sets(*variable_dim)}

        case 'ftvar':

            '''

            Free Tensor Variable Generator

            '''

            if variable_dim == 0:

                generated_variable = VariableGenerator(
                    1, integer=False, name=variable_name)

            else:

                if len(variable_dim) == 1:

                    generated_variable = VariableGenerator(
                        len(variable_dim[0]), integer=False, name=variable_name)

                if len(variable_dim) == 2:

                    generated_variable = VariableGenerator(
                        len(variable_dim[0]), len(variable_dim[1]), integer=False)

        case 'ptvar':

            '''

            Positive Tensor Variable Generator

            '''

            if variable_dim == 0:

                generated_variable = VariableGenerator(
                    1, integer=False,  nonneg=True, name=variable_name)

            else:

                if len(variable_dim) == 1:

                    generated_variable = VariableGenerator(
                        len(variable_dim[0]), integer=False,  nonneg=True, name=variable_name)

                if len(variable_dim) == 2:

                    generated_variable = VariableGenerator(len(variable_dim[0]), len(
                        variable_dim[1]), integer=False,  nonneg=True, name=variable_name)

        case 'itvar':

            '''

            Integer Tensor Variable Generator

            '''

            if variable_dim == 0:

                generated_variable = VariableGenerator(
                    1, integer=True,  nonneg=True, name=variable_name)

            else:

                if len(variable_dim) == 1:

                    generated_variable = VariableGenerator(
                        len(variable_dim[0]), integer=True,  nonneg=True, name=variable_name)

                if len(variable_dim) == 2:

                    generated_variable = VariableGenerator(len(variable_dim[0]), len(
                        variable_dim[1]), integer=True,  nonneg=True, name=variable_name)

        case 'btvar':

            '''

            Binary Tensor Variable Generator

            '''

            if variable_dim == 0:

                generated_variable = VariableGenerator(
                    1, integer=True,  nonneg=True, name=variable_name)

            else:

                if len(variable_dim) == 1:

                    print('i am here', len(variable_dim[0]))

                    generated_variable = VariableGenerator(
                        len(variable_dim[0]), integer=True,  nonneg=True, name=variable_name)

                if len(variable_dim) == 2:

                    generated_variable = VariableGenerator(len(variable_dim[0]), len(
                        variable_dim[1]), integer=True,  nonneg=True, name=variable_name)

    return generated_variable
