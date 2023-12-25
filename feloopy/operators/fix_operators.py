# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

def fix_dims(dim):
    if dim == 0:
        return dim

    if not isinstance(dim, set):
        if len(dim)>=1:
            if not isinstance(dim[0], set):
                dim = [range(d) if not isinstance(d, range) else d for d in dim]
                
    return dim
