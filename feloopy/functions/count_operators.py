import math as mt

product = mt.prod

def count_variable(variable_dim, total_count, special_count):
    """ For calculating total number of variables of each category.
    """
    total_count[0] += 1
    special_count[0] += 1
    special_count[1] += 1 if variable_dim == 0 else product(
        len(dims) for dims in variable_dim)
    total_count[1] += 1 if variable_dim == 0 else product(
        len(dims) for dims in variable_dim)
    return total_count, special_count