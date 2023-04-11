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