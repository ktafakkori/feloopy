'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''


def fix_dims(dim):

    if dim == 0:

        return dim

    elif dim != 0:

        for i in range(len(dim)):

            if type(dim[i]) != range:

                dim[i] = range(dim[i])

        return dim
