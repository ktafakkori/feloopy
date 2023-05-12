'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

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
