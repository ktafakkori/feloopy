

def fix_dims(dim):

    if dim ==0:

        return dim
    
    elif dim!=0:

        for i in dim:

            if type(dim) != range:

                dim[i] = range(dim)

        return dim