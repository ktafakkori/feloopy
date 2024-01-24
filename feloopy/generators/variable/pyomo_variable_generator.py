# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

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
