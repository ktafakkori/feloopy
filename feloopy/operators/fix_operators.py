

def fix_dims(dim):

    if dim ==0:

        return dim
    
    elif dim!=0:

        for i in range(len(dim)):

            if type(dim[i]) != range:

                dim[i] = range(dim[i])

        return dim