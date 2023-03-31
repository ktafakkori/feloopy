import cvxpy as cvxpy_interface
import itertools as it

sets = it.product

VariableGenerator = cvxpy_interface.Variable

def generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim=0):

    match variable_type:

        case 'pvar':

            '''

            Positive Variable Generator


            '''

            if variable_dim == 0:
                
                GeneratedVariable = VariableGenerator(1, integer=False)
            
            else:
                
                if len(variable_dim) == 1:
                    
                    GeneratedVariable = {key: VariableGenerator(1, integer=False) for key in variable_dim[0]}
                
                else:
                    
                    GeneratedVariable = {key: VariableGenerator(1, integer=False) for key in sets(*variable_dim)}
                    
        case 'bvar':

            '''

            Binary Variable Generator


            '''

            if variable_dim == 0:
                
                GeneratedVariable = VariableGenerator(1, integer=True)
            
            else:
                
                if len(variable_dim) == 1:
                    
                    GeneratedVariable = {key: VariableGenerator(1, integer=True) for key in variable_dim[0]}
                
                else:
                    
                    GeneratedVariable = {key: VariableGenerator(1, integer=True) for key in sets(*variable_dim)}
                    
                    
        case 'ivar':

            '''

            Integer Variable Generator


            '''

            if variable_dim == 0:
                
                GeneratedVariable = VariableGenerator(1, integer=True)
            
            else:
                
                if len(variable_dim) == 1:
                    
                    GeneratedVariable = {key: VariableGenerator(1, integer=True) for key in variable_dim[0]}
                
                else:
                    
                    GeneratedVariable = {key: VariableGenerator(1, integer=True) for key in sets(*variable_dim)}
                            
        case 'fvar':

            '''

            Free Variable Generator


            '''

            if variable_dim == 0:
                
                GeneratedVariable = VariableGenerator(1, integer=False)
            
            else:
                
                if len(variable_dim) == 1:
                    
                    GeneratedVariable = {key: VariableGenerator(1, integer=False) for key in variable_dim[0]}
                
                else:
                    
                    GeneratedVariable = {key: VariableGenerator(1, integer=False) for key in sets(*variable_dim)}
    
    return GeneratedVariable

