'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

import itertools as it

sets = it.product

def GenerateVariable(modelobject, var_type, var_name, b, dim=0):

    match var_type:

        case 'pvar':

            '''

            Positive Variable Generator


            '''

            if dim == 0:

                GeneratedVariable = modelobject.continuous_var(lb=b[0], ub=b[1])

            else:

                if len(dim) == 1:

                    GeneratedVariable = {key: modelobject.continuous_var(lb=b[0], ub=b[1]) for key in dim[0]}

                else:

                    GeneratedVariable = {key: modelobject.continuous_var(lb=b[0], ub=b[1]) for key in sets(*dim)}

        case 'bvar':

            '''

            Binary Variable Generator


            '''

            if dim == 0:

                GeneratedVariable = modelobject.binary_var()

            else:

                if len(dim) == 1:

                    GeneratedVariable = {key: modelobject.binary_var() for key in dim[0]}

                else:

                    GeneratedVariable = {key: modelobject.binary_var() for key in sets(*dim)}

        case 'ivar':

            '''

            Integer Variable Generator


            '''

            if dim == 0:

                GeneratedVariable = modelobject.integer_var(lb=b[0], ub=b[1])

            else:
                if len(dim) == 1:

                    GeneratedVariable = {key: modelobject.integer_var(lb=b[0], ub=b[1]) for key in dim[0]}

                else:

                    GeneratedVariable = {key: modelobject.integer_var(lb=b[0], ub=b[1]) for key in sets(*dim)}

        case 'fvar':

            '''

            Free Variable Generator


            '''

            if dim == 0:

                GeneratedVariable = modelobject.continuous_var(lb=b[0], ub=b[1])

            else:

                if len(dim) == 1:

                    GeneratedVariable = {key: modelobject.continuous_var(lb=b[0], ub=b[1]) for key in dim[0]}

                else:

                    GeneratedVariable = {key: modelobject.continuous_var(lb=b[0], ub=b[1]) for key in sets(*dim)}

    return GeneratedVariable