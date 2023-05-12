'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

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
