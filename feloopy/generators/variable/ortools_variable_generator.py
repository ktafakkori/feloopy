import itertools as it

sets = it.product


def generate_variable(modelobject, var_type, var_name, b, dim=0):

    if b[0] == None: b[0] = -modelobject.infinity()
    
    if b[1] == None: b[1] = modelobject.infinity()

    match var_type:

        case 'pvar':

            '''

            Positive Variable Generator


            '''

            
            if dim == 0:
                
                GeneratedVariable =  modelobject.NumVar(b[0], b[1], var_name)
            
            else:
                
                if len(dim) == 1:
                    
                    GeneratedVariable =  {key: modelobject.NumVar(b[0], b[1], f"{var_name}{key}") for key in dim[0]}
                
                else:
                    
                    GeneratedVariable =  {key: modelobject.NumVar(b[0], b[1], f"{var_name}{key}") for key in it.product(*dim)}


                    
        case 'bvar':

            '''

            Binary Variable Generator


            '''

            if dim == 0:
                
                GeneratedVariable =  modelobject.IntVar(b[0], b[1], var_name)
            
            else:
                
                if len(dim) == 1:
                    
                    GeneratedVariable =  {key: modelobject.IntVar(b[0], b[1], f"{var_name}{key}") for key in dim[0]}
                
                else:
                    
                    GeneratedVariable =  {key: modelobject.IntVar(b[0], b[1], f"{var_name}{key}") for key in it.product(*dim)}

                  
                    
        case 'ivar':

            '''

            Integer Variable Generator


            '''

            if b[0] == 0:

                b[0] = 0

            if b[1] == None:

                b[1] = modelobject.infinity()

            if dim == 0:

                GeneratedVariable = modelobject.IntVar(b[0], b[1], var_name)

            else:
                
                if len(dim) == 1:
                    
                    GeneratedVariable = {key: modelobject.IntVar(b[0], b[1], f"{var_name}{key}") for key in dim[0]}
                
                else:
                    
                    GeneratedVariable = {key: modelobject.IntVar(b[0], b[1], f"{var_name}{key}") for key in it.product(*dim)}



        case 'fvar':

            '''

            Free Variable Generator


            '''

            if b[0] == None:
                
                b[0] = -modelobject.infinity()
            
            if b[1] == None:
                
                b[1] = modelobject.infinity()

            if dim == 0:
                
                GeneratedVariable = modelobject.NumVar(b[0], b[1], var_name)
            
            else:
                
                if len(dim) == 1:
                    
                    GeneratedVariable = {key: modelobject.NumVar(b[0], b[1], f"{var_name}{key}") for key in dim[0]}
                
                else:
                    
                    GeneratedVariable = {key: modelobject.NumVar(b[0], b[1], f"{var_name}{key}") for key in it.product(*dim)}
    
    return GeneratedVariable