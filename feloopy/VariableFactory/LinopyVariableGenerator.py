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
                GeneratedVariable =  modelobject.add_variables(lower=b[0], upper=b[1], name=var_name)
            else:
                GeneratedVariable =  modelobject.add_variables(lower=b[0], upper=b[1], coords=[i for i in it.product(*dim)], name=var_name)
      
        case 'bvar':

            '''

            Binary Variable Generator


            '''

            if dim == 0:
                GeneratedVariable =  modelobject.add_variables(lower=b[0], upper=b[1], name=var_name, binary=True)
            else:
                GeneratedVariable =  modelobject.add_variables(lower=b[0], upper=b[1], coords=[i for i in it.product(*dim)], name=var_name,  binary=True)

                    
                    
        case 'ivar':

            '''

            Integer Variable Generator


            '''

            if dim == 0:
                GeneratedVariable =  modelobject.add_variables(lower=b[0], upper=b[1], name=var_name, binary=True)
            else:
                GeneratedVariable =  modelobject.add_variables(lower=b[0], upper=b[1], coords=[i for i in it.product(*dim)], name=var_name,  binary=True)

                            
        case 'fvar':

            '''

            Free Variable Generator


            '''

            if dim == 0:
                GeneratedVariable =  modelobject.add_variables(lower=b[0], upper=b[1], name=var_name)
            else:
                GeneratedVariable =  modelobject.add_variables(lower=b[0], upper=b[1], coords=[i for i in it.product(*dim)], name=var_name)

    
    return  GeneratedVariable
    
