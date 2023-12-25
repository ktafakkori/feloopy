# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


import itertools as it

def sets(*args):
    """ 
    Used to mimic 'for all' in mathamatical modeling, for multiple sets.

    Arguments:

        * Multiple sets separated by commas.
        * Required

    Example: `for i,j in sets(I,J):`

    """

    return it.product(*args)
