import itertools as it
import picos as picos_interface


sets = it.product

BINARY = picos_interface.BinaryVariable
POSITIVE = picos_interface.RealVariable
INTEGER = picos_interface.IntegerVariable
FREE = picos_interface.RealVariable

def generate_variable(modelobject, var_type, var_name, b, dim=0):

    match var_type:

        case 'pvar':

            '''

            Positive Variable Generator


            '''

            if dim == 0:
                GeneratedVariable =  POSITIVE(var_name, lower=b[0], upper=b[1])
            else:
                if len(dim) == 1:
                    GeneratedVariable =  {key: POSITIVE(var_name, lower=b[0], upper=b[1]) for key in dim[0]}
                else:
                    GeneratedVariable =  {key: POSITIVE(var_name, lower=b[0], upper=b[1]) for key in it.product(*dim)}
                            
        case 'bvar':

            '''

            Binary Variable Generator


            '''
            if dim == 0:
                GeneratedVariable =  BINARY(var_name)
            else:
                if len(dim) == 1:
                    GeneratedVariable =  {key: BINARY(var_name) for key in dim[0]}
                else:
                    GeneratedVariable =  {key: BINARY(var_name) for key in it.product(*dim)}

        case 'ivar':

            '''

            Integer Variable Generator


            '''
            if dim == 0:
                GeneratedVariable =  INTEGER(var_name, lower=b[0], upper=b[1])
            else:
                if len(dim) == 1:
                    GeneratedVariable =  {key: INTEGER(var_name, lower=b[0], upper=b[1]) for key in dim[0]}
                else:
                    GeneratedVariable =  {key: INTEGER(var_name, lower=b[0], upper=b[1]) for key in it.product(*dim)}
                            
        case 'fvar':

            '''

            Free Variable Generator


            '''
            if dim == 0:
                GeneratedVariable = FREE(var_name, lower=b[0], upper=b[1])
            else:
                if len(dim) == 1:
                    GeneratedVariable =  {key: FREE(var_name, lower=b[0], upper=b[1]) for key in dim[0]}
                else:
                    GeneratedVariable =  {key: FREE(var_name, lower=b[0], upper=b[1]) for key in it.product(*dim)}

    return  GeneratedVariable

