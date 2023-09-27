'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.7)                               |
|  Modified: Wednesday, 27th September 2023 11:35:56 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''

import pyomo.environ as pyomo_interface
import itertools as it

sets = it.product

variable = pyomo_interface.Var

POSITIVE = pyomo_interface.NonNegativeReals
BINARY = pyomo_interface.Binary
INTEGER = pyomo_interface.NonNegativeIntegers
FREE = pyomo_interface.Reals


def generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim=0):

    match variable_type:

        case 'pvar':

            '''

            Positive Variable Generator


            '''

            if variable_dim == 0:

                model_object.add_component(variable_name, variable(
                    initialize=0, domain=POSITIVE, bounds=(variable_bound[0], variable_bound[1])))

            else:
                model_object.add_component(variable_name, variable([i for i in sets(
                    *variable_dim)], domain=POSITIVE, bounds=(variable_bound[0], variable_bound[1])))

        case 'bvar':

            '''

            Binary Variable Generator


            '''

            if variable_dim == 0:

                model_object.add_component(variable_name, variable(
                    domain=BINARY, bounds=(variable_bound[0], variable_bound[1])))

            else:

                model_object.add_component(variable_name, variable([i for i in sets(
                    *variable_dim)], domain=BINARY, bounds=(variable_bound[0], variable_bound[1])))

        case 'ivar':

            '''

            Integer Variable Generator


            '''

            if variable_dim == 0:

                model_object.add_component(variable_name, variable(
                    domain=INTEGER, bounds=(variable_bound[0], variable_bound[1])))

            else:

                model_object.add_component(variable_name, variable([i for i in sets(
                    *variable_dim)], domain=INTEGER, bounds=(variable_bound[0], variable_bound[1])))

        case 'fvar':

            '''

            Free Variable Generator


            '''

            if variable_dim == 0:

                model_object.add_component(variable_name, variable(
                    domain=FREE, bounds=(variable_bound[0], variable_bound[1])))

            else:

                model_object.add_component(variable_name, variable([i for i in sets(
                    *variable_dim)], domain=FREE, bounds=(variable_bound[0], variable_bound[1])))

    return model_object.component(variable_name)
