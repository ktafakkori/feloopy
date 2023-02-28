import pymprog as pymprog_interface
import itertools as it

sets = it.product

VariableGenerator = pymprog_interface.var


def generate_variable(modelobject, var_type, var_name, b, dim=0):

    match var_type:

        case 'pvar':

            '''

            Positive Variable Generator


            '''

            if dim == 0:
                GeneratedVariable =  VariableGenerator(var_name, bounds=(b[0], b[1]))
            else:
                if len(dim) == 1:
                    GeneratedVariable =  {key: VariableGenerator(var_name, bounds=(b[0], b[1])) for key in dim[0]}
                else:
                    GeneratedVariable =  {key: VariableGenerator(var_name, bounds=(b[0], b[1])) for key in it.product(*dim)}


        case 'bvar':

            '''

            Binary Variable Generator


            '''
            if dim == 0:
                GeneratedVariable =  VariableGenerator(var_name, bounds=(b[0], b[1]), kind=int)
            else:
                if len(dim) == 1:
                    GeneratedVariable =  {key: VariableGenerator(var_name, bounds=(b[0], b[1]), kind=int) for key in dim[0]}
                else:
                    GeneratedVariable =  {key: VariableGenerator(var_name, bounds=(b[0], b[1]), kind=int) for key in it.product(*dim)}
       
        case 'ivar':

            '''

            Integer Variable Generator


            '''

            if dim == 0:
                GeneratedVariable =  VariableGenerator(var_name, bounds=(b[0], b[1]), kind=int)
            else:
                if len(dim) == 1:
                    GeneratedVariable =  {key: VariableGenerator(var_name, bounds=(b[0], b[1]), kind=int) for key in dim[0]}
                else:
                    GeneratedVariable =  {key: VariableGenerator(var_name, bounds=(b[0], b[1]), kind=int) for key in it.product(*dim)}

                
        case 'fvar':

            '''

            Free Variable Generator


            '''

            if dim == 0:
                GeneratedVariable =  VariableGenerator(var_name, bounds=(b[0], b[1]))
            else:
                if len(dim) == 1:
                    GeneratedVariable =  {key: VariableGenerator(var_name, bounds=(b[0], b[1])) for key in dim[0]}
                else:
                    GeneratedVariable =  {key: VariableGenerator(var_name, bounds=(b[0], b[1])) for key in it.product(*dim)}

    return  GeneratedVariable