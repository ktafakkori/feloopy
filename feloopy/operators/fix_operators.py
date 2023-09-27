'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.7)                               |
|  Modified: Wednesday, 27th September 2023 11:37:43 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''

def fix_dims(dim):
    if dim == 0:
        return dim

    if not isinstance(dim, set):
        if len(dim)>=1:
            if not isinstance(dim[0], set):
                dim = [range(d) if not isinstance(d, range) else d for d in dim]
                
    return dim
