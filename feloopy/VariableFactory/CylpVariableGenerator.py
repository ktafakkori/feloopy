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
                GeneratedVariable =  modelobject.addVariable(var_name, 1, isInt=False)
            else:
                if len(dim) == 1:
                    GeneratedVariable =  {key: modelobject.addVariable(f"{var_name}{key}", 1, isInt=False) for key in dim[0]}
                else:
                    GeneratedVariable =  {key: modelobject.addVariable(f"{var_name}{key}", 1, isInt=False) for key in it.product(*dim)}
                    
                    
        case 'bvar':

            '''

            Binary Variable Generator


            '''

            if dim == 0:
                GeneratedVariable =  modelobject.addVariable(var_name, 1, isInt=False)
            else:
                if len(dim) == 1:
                    GeneratedVariable =  {key: modelobject.addVariable(f"{var_name}{key}", 1, isInt=True) for key in dim[0]}
                else:
                    GeneratedVariable =  {key: modelobject.addVariable(f"{var_name}{key}", 1, isInt=True) for key in it.product(*dim)}


                    
        case 'ivar':

            '''

            Integer Variable Generator


            '''

            if dim == 0:
                GeneratedVariable =  modelobject.addVariable(var_name, 1, isInt=False)
            else:
                if len(dim) == 1:
                    GeneratedVariable =  {key: modelobject.addVariable(f"{var_name}{key}", 1, isInt=True) for key in dim[0]}
                else:
                    GeneratedVariable =  {key: modelobject.addVariable(f"{var_name}{key}", 1, isInt=True) for key in it.product(*dim)}

                            
        case 'fvar':

            '''

            Free Variable Generator


            '''

            if dim == 0:
                GeneratedVariable =  modelobject.addVariable(var_name, 1, isInt=False)
            else:
                if len(dim) == 1:
                    GeneratedVariable =  {key: modelobject.addVariable(f"{var_name}{key}", 1, isInt=False) for key in dim[0]}
                else:
                    GeneratedVariable =  {key: modelobject.addVariable(f"{var_name}{key}", 1, isInt=False) for key in it.product(*dim)}
                   
    return GeneratedVariable
