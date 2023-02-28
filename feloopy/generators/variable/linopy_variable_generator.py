import itertools as it
import pandas as pd

sets = it.product

def generate_variable(modelobject, var_type, var_name, b, dim=0):

    match var_type:

        case 'pvar':

            '''

            Positive Variable Generator


            '''
            if dim == 0:
                GeneratedVariable =  modelobject.add_variables(lower=b[0], upper=b[1], name=var_name)
            else:
                GeneratedVariable =  modelobject.add_variables(lower=b[0], upper=b[1], coords=pd.Index(dim), name=var_name)
      
        case 'bvar':

            '''

            Binary Variable Generator


            '''

            if dim == 0:
                GeneratedVariable =  modelobject.add_variables(name=var_name, binary=True)
            else:
                GeneratedVariable =  modelobject.add_variables(coords=pd.Index(dim), name=var_name,  binary=True)

                    
                    
        case 'ivar':

            '''

            Integer Variable Generator


            '''

            if dim == 0:
                GeneratedVariable =  modelobject.add_variables(lower=b[0], upper=b[1], name=var_name, binary=True)
            else:
                GeneratedVariable =  modelobject.add_variables(lower=b[0], upper=b[1], coords=pd.Index(dim), name=var_name,  integer=True)

                            
        case 'fvar':

            '''

            Free Variable Generator


            '''

            if dim == 0:
                GeneratedVariable =  modelobject.add_variables(lower=b[0], upper=b[1], name=var_name)
            else:
                GeneratedVariable =  modelobject.add_variables(lower=b[0], upper=b[1], coords=pd.Index(dim), name=var_name)

    
    return  GeneratedVariable
    
