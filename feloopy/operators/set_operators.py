'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.7)                               |
|  Modified: Wednesday, 27th September 2023 11:38:19 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
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
