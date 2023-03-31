import gurobipy as gurobi_interface
import itertools as it

sets = it.product

POSITIVE = gurobi_interface.GRB.CONTINUOUS
INTEGER = gurobi_interface.GRB.INTEGER
BINARY = gurobi_interface.GRB.BINARY
FREE = gurobi_interface.GRB.CONTINUOUS
INFINITY = gurobi_interface.GRB.INFINITY

def generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim=0):

    if variable_bound[0] == None: variable_bound[0] = -INFINITY
    
    if variable_bound[1] == None: variable_bound[1] = +INFINITY

    match variable_type:

        case 'pvar':

            '''

            Positive Variable Generator


            '''

            if variable_dim == 0:
                
                generated_variable = model_object.addVar(vtype=POSITIVE, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)

            else:
                
                if len(variable_dim) == 1:
                
                    generated_variable = {key: model_object.addVar(vtype=POSITIVE, lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}") for key in variable_dim[0]}
                
                else:
                    
                    generated_variable = {key: model_object.addVar(vtype=POSITIVE, lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}") for key in sets(*variable_dim)}

        case 'bvar':

            '''

            Binary Variable Generator


            '''

            if variable_dim == 0:
                
                generated_variable = model_object.addVar(vtype=BINARY, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)

            else:
                
                if len(variable_dim) == 1:
                
                    generated_variable = {key: model_object.addVar(vtype=BINARY, lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}") for key in variable_dim[0]}
                
                else:
                    
                    generated_variable = {key: model_object.addVar(vtype=BINARY, lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}") for key in sets(*variable_dim)}

       
        case 'ivar':

            '''

            Integer Variable Generator


            '''

            if variable_dim == 0:
                
                generated_variable = model_object.addVar(vtype=INTEGER, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)

            else:
                
                if len(variable_dim) == 1:
                
                    generated_variable = {key: model_object.addVar(vtype=INTEGER, lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}") for key in variable_dim[0]}
                
                else:
                    
                    generated_variable = {key: model_object.addVar(vtype=INTEGER, lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}") for key in sets(*variable_dim)}


    

        case 'fvar':

            '''

            Free Variable Generator


            '''

            if variable_dim == 0:
                
                generated_variable = model_object.addVar(vtype=POSITIVE, lb=variable_bound[0], ub=variable_bound[1], name=variable_name)

            else:
                
                if len(variable_dim) == 1:
                
                    generated_variable = {key: model_object.addVar(vtype=POSITIVE, lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}") for key in variable_dim[0]}
                
                else:
                    
                    generated_variable = {key: model_object.addVar(vtype=POSITIVE, lb=variable_bound[0], ub=variable_bound[1], name=f"{variable_name}{key}") for key in sets(*variable_dim)}

    
    return generated_variable
    
    