'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

import pyomo.environ as pyomo_interface
import itertools as it

sets = it.product

variable = pyomo_interface.Var

POSITIVE = pyomo_interface.NonNegativeReals
BINARY = pyomo_interface.Binary
INTEGER = pyomo_interface.NonNegativeIntegers
FREE = pyomo_interface.Reals


def GenerateVariable(modelobject, var_type, var_name, b, dim=0):

    match var_type:

        case 'pvar':

            '''

            Positive Variable Generator


            '''

            if dim == 0:

                modelobject.add_component(var_name, variable(initialize=0, domain=POSITIVE, bounds=(b[0], b[1])))

            else:
                modelobject.add_component(var_name, variable([i for i in sets(*dim)], domain=POSITIVE, bounds=(b[0], b[1])))

        case 'bvar':

            '''

            Binary Variable Generator


            '''

            if dim == 0:

                modelobject.add_component(var_name, variable(domain=BINARY, bounds=(b[0], b[1])))

            else:

                modelobject.add_component(var_name, variable([i for i in sets(*dim)], domain=BINARY, bounds=(b[0], b[1])))

        case 'ivar':

            '''

            Integer Variable Generator


            '''

            if dim == 0:

                modelobject.add_component(var_name, variable(domain=INTEGER, bounds=(b[0], b[1])))

            else:

                modelobject.add_component(var_name, variable([i for i in sets(*dim)], domain=INTEGER, bounds=(b[0], b[1])))

        case 'fvar':

            '''

            Free Variable Generator


            '''

            if dim == 0:

                modelobject.add_component(var_name, variable(domain=FREE, bounds=(b[0], b[1])))

            else:

                modelobject.add_component(var_name, variable([i for i in sets(*dim)], domain=FREE, bounds=(b[0], b[1])))

    return modelobject.component(var_name)