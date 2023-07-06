import localsolver as ls
import itertools as it

sets = it.product

def generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim=0):
    match variable_type:
        case 'pvar':
            '''
            Positive Variable Generator
            '''
            if variable_dim == 0:
                GeneratedVariable = model_object.Float(
                    variable_bound[0], variable_bound[1], name=variable_name)
            else:
                GeneratedVariable = generate_multi_dimensional_var(model_object, variable_bound, variable_name, variable_dim, 'Float')
                
        case 'bvar':
            '''
            Binary Variable Generator
            '''
            if variable_dim == 0:
                GeneratedVariable = model_object.Bool(name=variable_name)
            else:
                GeneratedVariable = generate_multi_dimensional_var(model_object, variable_bound, variable_name, variable_dim, 'Bool')

        case 'ivar':
            '''
            Integer Variable Generator
            '''
            if variable_dim == 0:
                GeneratedVariable = model_object.Int(
                    variable_bound[0], variable_bound[1], name=variable_name)
            else:
                GeneratedVariable = generate_multi_dimensional_var(model_object, variable_bound, variable_name, variable_dim, 'Int')

        case 'fvar':
            '''
            Free Variable Generator
            '''
            if variable_dim == 0:
                GeneratedVariable = model_object.Float(
                    variable_bound[0], variable_bound[1], name=variable_name)
            else:
                GeneratedVariable = generate_multi_dimensional_var(model_object, variable_bound, variable_name, variable_dim, 'Float')

    return GeneratedVariable

def generate_multi_dimensional_var(model_object, variable_bound, variable_name, variable_dim, var_type):
    if len(variable_dim) == 1:
        GeneratedVariable = {key: getattr(model_object, var_type)(
            variable_bound[0], variable_bound[1], name=f"{variable_name}{key}") for key in variable_dim[0]}
    else:
        GeneratedVariable = {key: getattr(model_object, var_type)(
            variable_bound[0], variable_bound[1], name=f"{variable_name}{key}") for key in sets(*variable_dim)}
    return GeneratedVariable
