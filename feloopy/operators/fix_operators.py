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

    if not isinstance(dim, set):
        if len(dim)>=1:
            if not isinstance(dim[0], set):
                dim = [range(d) if not isinstance(d, range) else d for d in dim]
                
    return dim
