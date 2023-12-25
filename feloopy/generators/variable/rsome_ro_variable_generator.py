# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


from rsome import ro 
import itertools as it

sets = it.product

def generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim=0):

    match variable_type:

        case 'pvar':

            '''
            Positive Variable Generator
            '''

            if variable_dim == 0:
                generated_variable = model_object.dvar(1,vtype='C', name=variable_name)
            else:
                if len(variable_dim) == 1:
                    generated_variable = {key:  model_object.dvar(1,vtype='C', name=f"{variable_name}{key}") for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.dvar(1, name=f"{variable_name}{key}",vtype='C') for key in sets(*variable_dim)}

        case 'bvar':

            '''
            Binary Variable Generator
            '''

            if variable_dim == 0:
                generated_variable = model_object.dvar(1,vtype='B',name=variable_name)
            else:
                if len(variable_dim) == 1:
                    generated_variable = {key:  model_object.dvar(1,vtype='B', name=f"{variable_name}{key}") for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.dvar(1, name=f"{variable_name}{key}", vtype='B') for key in sets(*variable_dim)}
  
        case 'ivar':
            '''
            Integer Variable Generator
            '''

            if variable_dim == 0:
                generated_variable = model_object.dvar(1,vtype='I',name=variable_name)
            else:
                if len(variable_dim) == 1:
                    generated_variable = {key: model_object.dvar(1,vtype='I', name=f"{variable_name}{key}") for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.dvar(1, name=f"{variable_name}{key}", vtype='I') for key in sets(*variable_dim)}

        case 'fvar':

            '''
            Free Variable Generator
            '''

            if variable_dim == 0:
                generated_variable = model_object.dvar(1,vtype='C', name=variable_name)
            else:
                if len(variable_dim) == 1:
                    generated_variable = {key:  model_object.dvar(1,vtype='C', name=f"{variable_name}{key}") for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.dvar(1, name=f"{variable_name}{key}",vtype='C') for key in sets(*variable_dim)}

        case 'ptvar':

            '''
            Positive Tensor Variable Generator
            '''

            if variable_dim == 0:
                generated_variable = model_object.dvar(1,vtype='C', name=variable_name)
            else:
                generated_variable = model_object.dvar(tuple([len(key) for key in variable_dim]), vtype='C', name=variable_name)

        case 'btvar':

            '''
            Binary Tensor Variable Generator
            '''

            if variable_dim == 0:
                generated_variable = model_object.dvar(1,vtype='B', name=variable_name)
            else:
                generated_variable = model_object.dvar(tuple([len(key) for key in variable_dim]), vtype='B', name=variable_name)

        case 'itvar':
            '''
            Integer Tensor Variable Generator
            '''

            if variable_dim == 0:
                generated_variable = model_object.dvar(1,vtype='I', name=variable_name)
            else:
                generated_variable = model_object.dvar(tuple([len(key) for key in variable_dim]), vtype='I', name=variable_name)

        case 'ftvar':

            '''
            Free Tensor Variable Generator
            '''

            if variable_dim == 0:
                generated_variable = model_object.dvar(1,vtype='C', name=variable_name)
            else:
                generated_variable = model_object.dvar(tuple([len(key) for key in variable_dim]), vtype='C', name=variable_name)

        case 'rvar':

            '''
            Random Variable Generator
            '''
            if variable_dim == 0:
                generated_variable = model_object.rvar(1, name=variable_name)
            else:
                if len(variable_dim) == 1:
                    generated_variable = {key:  model_object.rvar(1, name=f"{variable_name}{key}") for key in variable_dim[0]}
                else:
                    generated_variable = {key: model_object.rvar(1, name=f"{variable_name}{key}") for key in sets(*variable_dim)}

        case 'rtvar':

            '''
            Random Tensor Variable Generator
            '''

            if variable_dim == 0:
                generated_variable = model_object.rvar(1, name=variable_name)
            else:
                generated_variable = model_object.rvar(tuple([len(key) for key in variable_dim]), name=variable_name)

    return generated_variable