# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

from gamspy import Variable

import itertools as it
sets = it.product

def generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim=0):

    match variable_type:

        case 'pvar':

            '''
            Positive Variable Generator
            '''

            if variable_dim == 0:
                GeneratedVariable = Variable(model_object, name=variable_name, type="positive")
            else:
                if len(variable_dim) == 1:
                    GeneratedVariable = {key: Variable(model_object, name=f"{variable_name}{key}", type="positive") for key in variable_dim[0]}
                else:
                    GeneratedVariable = {key: Variable(model_object, name=f"{variable_name}{key}", type="positive") for key in sets(*variable_dim)}
        case 'bvar':

            '''
            Binary Variable Generator
            '''

            if variable_dim == 0:

                GeneratedVariable = Variable(model_object, name=variable_name, type="binary")

            else:

                if len(variable_dim) == 1:

                    GeneratedVariable = {key: Variable(model_object, name=f"{variable_name}{key}", type="binary") for key in variable_dim[0]}

                else:

                    GeneratedVariable = {key: Variable(model_object, name=f"{variable_name}{key}", type="binary") for key in sets(*variable_dim)}

        case 'ivar':

            '''

            Integer Variable Generator


            '''

            if variable_dim == 0:

                GeneratedVariable = Variable(model_object, name=variable_name, type="integer")

            else:

                if len(variable_dim) == 1:

                    GeneratedVariable = {key: Variable(model_object, name=f"{variable_name}{key}", type="integer") for key in variable_dim[0]}

                else:

                    GeneratedVariable = {key: Variable(model_object, name=f"{variable_name}{key}", type="integer") for key in sets(*variable_dim)}

        case 'fvar':

            '''

            Free Variable Generator


            '''

            if variable_dim == 0:

                GeneratedVariable = Variable(model_object, name=variable_name, type="free")

            else:

                if len(variable_dim) == 1:

                    GeneratedVariable = {key: Variable(model_object, name=f"{variable_name}{key}", type="free") for key in variable_dim[0]}

                else:

                    GeneratedVariable = {key: Variable(model_object, name=f"{variable_name}{key}", type="free") for key in sets(*variable_dim)}

    return GeneratedVariable
