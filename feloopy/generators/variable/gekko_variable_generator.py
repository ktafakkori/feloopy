'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
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
                GeneratedVariable = model_object.Var(
                    lb=variable_bound[0], ub=variable_bound[1], integer=False)
            else:
                if len(variable_dim) == 1:
                    GeneratedVariable = {key:  model_object.Var(
                        lb=variable_bound[0], ub=variable_bound[1], integer=False) for key in variable_dim[0]}
                else:
                    GeneratedVariable = {key: model_object.Var(
                        lb=variable_bound[0], ub=variable_bound[1], integer=False) for key in sets(*variable_dim)}

        case 'bvar':

            '''

            Binary Variable Generator


            '''

            if variable_dim == 0:
                GeneratedVariable = model_object.Var(
                    lb=variable_bound[0], ub=variable_bound[1], integer=True)
            else:
                if len(variable_dim) == 1:
                    GeneratedVariable = {key:  model_object.Var(
                        lb=0, ub=1, integer=True) for key in variable_dim[0]}
                else:
                    GeneratedVariable = {key: model_object.Var(
                        lb=0, ub=1, integer=True) for key in sets(*variable_dim)}

        case 'ivar':

            '''

            Integer Variable Generator


            '''

            if variable_dim == 0:
                GeneratedVariable = model_object.Var(
                    lb=variable_bound[0], ub=variable_bound[1], integer=True)
            else:
                if len(variable_dim) == 1:
                    GeneratedVariable = {key:  model_object.Var(
                        lb=variable_bound[0], ub=variable_bound[1], integer=True) for key in variable_dim[0]}
                else:
                    GeneratedVariable = {key: model_object.Var(
                        lb=variable_bound[0], ub=variable_bound[1], integer=True) for key in sets(*variable_dim)}

        case 'fvar':

            '''

            Free Variable Generator


            '''

            if variable_dim == 0:
                GeneratedVariable = model_object.Var()
            else:
                if len(variable_dim) == 1:
                    GeneratedVariable = {key:  model_object.Var()
                                         for key in variable_dim[0]}
                else:
                    GeneratedVariable = {key: model_object.Var()
                                         for key in sets(*variable_dim)}

    return GeneratedVariable
