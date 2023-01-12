'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

import gurobipy as gurobi_interface
import itertools as it

sets = it.product

POSITIVE = gurobi_interface.GRB.CONTINUOUS
INTEGER = gurobi_interface.GRB.INTEGER
BINARY = gurobi_interface.GRB.BINARY
FREE = gurobi_interface.GRB.CONTINUOUS
INFINITY = gurobi_interface.GRB.INFINITY

def GenerateVariable(modelobject, var_type, var_name, b, dim=0):

    if b[0] == None: b[0] = -INFINITY
    
    if b[1] == None: b[1] = +INFINITY

    match var_type:

        case 'pvar':

            '''

            Positive Variable Generator


            '''

            if dim == 0:
                
                GeneratedVariable = modelobject.addVar(vtype=POSITIVE, lb=b[0], ub=b[1], name=var_name)

            else:
                
                if len(dim) == 1:
                
                    GeneratedVariable = {key: modelobject.addVar(vtype=POSITIVE, lb=b[0], ub=b[1], name=f"{var_name}{key}") for key in dim[0]}
                
                else:
                    
                    GeneratedVariable = {key: modelobject.addVar(vtype=POSITIVE, lb=b[0], ub=b[1], name=f"{var_name}{key}") for key in sets(*dim)}

        case 'bvar':

            '''

            Binary Variable Generator


            '''

            if dim == 0:
                
                GeneratedVariable = modelobject.addVar(vtype=BINARY, lb=b[0], ub=b[1], name=var_name)

            else:
                
                if len(dim) == 1:
                
                    GeneratedVariable = {key: modelobject.addVar(vtype=BINARY, lb=b[0], ub=b[1], name=f"{var_name}{key}") for key in dim[0]}
                
                else:
                    
                    GeneratedVariable = {key: modelobject.addVar(vtype=BINARY, lb=b[0], ub=b[1], name=f"{var_name}{key}") for key in sets(*dim)}

       
        case 'ivar':

            '''

            Integer Variable Generator


            '''

            if dim == 0:
                
                GeneratedVariable = modelobject.addVar(vtype=INTEGER, lb=b[0], ub=b[1], name=var_name)

            else:
                
                if len(dim) == 1:
                
                    GeneratedVariable = {key: modelobject.addVar(vtype=INTEGER, lb=b[0], ub=b[1], name=f"{var_name}{key}") for key in dim[0]}
                
                else:
                    
                    GeneratedVariable = {key: modelobject.addVar(vtype=INTEGER, lb=b[0], ub=b[1], name=f"{var_name}{key}") for key in sets(*dim)}


    

        case 'fvar':

            '''

            Free Variable Generator


            '''

            if dim == 0:
                
                GeneratedVariable = modelobject.addVar(vtype=POSITIVE, lb=b[0], ub=b[1], name=var_name)

            else:
                
                if len(dim) == 1:
                
                    GeneratedVariable = {key: modelobject.addVar(vtype=POSITIVE, lb=b[0], ub=b[1], name=f"{var_name}{key}") for key in dim[0]}
                
                else:
                    
                    GeneratedVariable = {key: modelobject.addVar(vtype=POSITIVE, lb=b[0], ub=b[1], name=f"{var_name}{key}") for key in sets(*dim)}

    
    return GeneratedVariable
    
    