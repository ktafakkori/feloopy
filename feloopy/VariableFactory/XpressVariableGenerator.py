'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

import xpress as xpress_interface
import itertools as it

sets = it.product

VariableGenerator = xpress_interface.var

INFINITY = xpress_interface.infinity
BINARY = xpress_interface.binary
INTEGER = xpress_interface.integer

def GenerateVariable(modelobject, var_type, var_name, b, dim=0):

    if b[0] == None: b[0] = -INFINITY
    
    if b[1] == None: b[1] = +INFINITY

    match var_type:

        case 'pvar':

            '''

            Positive Variable Generator


            '''

            if dim == 0:
                
                GeneratedVariable =VariableGenerator(lb=b[0],ub=b[1])
                
                modelobject.addVariable(GeneratedVariable)
                
            else:
                
                if len(dim) == 1:
                    
                    GeneratedVariable = [VariableGenerator(lb=b[0],ub=b[1]) for key in dim[0]]
                    
                    modelobject.addVariable(GeneratedVariable)
                    
                else:
                    
                    GeneratedVariable = {key:VariableGenerator(name= f"{var_name}{key}", lb=b[0],ub=b[1]) for key in sets(*dim)}
                    
                    modelobject.addVariable(GeneratedVariable)
                    
        case 'bvar':

            '''

            Binary Variable Generator


            '''

            if dim == 0:
                
                GeneratedVariable =VariableGenerator(vartype=BINARY)
                
                modelobject.addVariable(GeneratedVariable)
                
            else:
                
                if len(dim) == 1:
                    
                    GeneratedVariable = [VariableGenerator(vartype=BINARY) for key in dim[0]]
                    
                    modelobject.addVariable(GeneratedVariable)
                    
                else:
                    
                    GeneratedVariable = {key:VariableGenerator(name= f"{var_name}{key}", lb=b[0],ub=b[1],vartype=BINARY) for key in sets(*dim)}
                    
                    modelobject.addVariable(GeneratedVariable)
                    
        case 'ivar':

            '''

            Integer Variable Generator


            '''

            if dim == 0:
                
                GeneratedVariable =VariableGenerator(vartype=INTEGER)
                
                modelobject.addVariable(GeneratedVariable)
                
            else:
                
                if len(dim) == 1:
                    
                    GeneratedVariable = {key:VariableGenerator(vartype=INTEGER) for key in dim[0]}
                    
                    modelobject.addVariable(GeneratedVariable)
                    
                else:
                    
                    GeneratedVariable = {key:VariableGenerator(name= f"{var_name}{key}", lb=b[0],ub=b[1],vartype=INTEGER) for key in sets(*dim)}
                    
                    modelobject.addVariable(GeneratedVariable)
                    
        case 'fvar':

            '''

            Free Variable Generator


            '''

            if dim == 0:
                
                GeneratedVariable =VariableGenerator(lb=b[0],ub=b[1])
                
                modelobject.addVariable(GeneratedVariable)
                
            else:
                
                if len(dim) == 1:
                    
                    GeneratedVariable = [VariableGenerator(lb=b[0],ub=b[1]) for key in dim[0]]
                    
                    modelobject.addVariable(GeneratedVariable)
                    
                else:
                    
                    GeneratedVariable = {key:VariableGenerator(name= f"{var_name}{key}", lb=b[0],ub=b[1]) for key in sets(*dim)}
                    
                    modelobject.addVariable(GeneratedVariable)
    
    return GeneratedVariable

    
    
    
    

