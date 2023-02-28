import pulp as pulp_interface
import itertools as it

sets = it.product

VariableGenerator = pulp_interface.LpVariable

POSITIVE = pulp_interface.LpContinuous
BINARY = pulp_interface.LpBinary
INTEGER = pulp_interface.LpInteger
FREE = pulp_interface.LpContinuous

def generate_variable(modelobject, var_type, var_name, b, dim=0):

    match var_type:

        case 'pvar':

            '''

            Positive Variable Generator


            '''

            if dim == 0:
                
                GeneratedVariable = VariableGenerator(var_name, b[0], b[1], POSITIVE)
            
            else:
                
                if len(dim) == 1:
                    
                    GeneratedVariable = {key: VariableGenerator(f"{var_name}{key}", b[0], b[1], POSITIVE) for key in dim[0]}
                
                else:
                    
                    GeneratedVariable = {key: VariableGenerator(f"{var_name}{key}", b[0], b[1], POSITIVE) for key in sets(*dim)}


        case 'bvar':

            '''

            Binary Variable Generator


            '''

            if dim == 0:

                GeneratedVariable = VariableGenerator(var_name, b[0], b[1], BINARY)

            else:
                
                if len(dim) == 1:
                    
                    GeneratedVariable = {key: VariableGenerator(f"{var_name}{key}", b[0], b[1], BINARY) for key in dim[0]}
                
                else:
                    
                    GeneratedVariable = {key: VariableGenerator(f"{var_name}{key}", b[0], b[1], BINARY) for key in sets(*dim)}

        case 'ivar':

            '''

            Integer Variable Generator


            '''

            if dim == 0:
                
                GeneratedVariable =  VariableGenerator(var_name, b[0], b[1], INTEGER)
            
            else:
                
                if len(dim) == 1:
                    
                    GeneratedVariable = {key: VariableGenerator(f"{var_name}{key}", b[0], b[1], INTEGER) for key in dim[0]}
                
                else:
                    
                    GeneratedVariable = {key: VariableGenerator(f"{var_name}{key}", b[0], b[1], INTEGER) for key in sets(*dim)}


        case 'fvar':

            '''

            Free Variable Generator


            '''

            if dim == 0:

                GeneratedVariable = VariableGenerator(var_name, b[0], b[1], FREE)

            else:
                
                if len(dim) == 1:
                    
                    GeneratedVariable = {key: VariableGenerator(f"{var_name}{key}", b[0], b[1], FREE) for key in dim[0]}
                
                else:
                    
                    GeneratedVariable = {key: VariableGenerator(f"{var_name}{key}", b[0], b[1], FREE) for key in sets(*dim)}      

    return GeneratedVariable