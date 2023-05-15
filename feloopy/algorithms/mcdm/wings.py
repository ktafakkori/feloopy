'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-15
 # @ Modified: 2023-05-15
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

import numpy as np


def score_wings(dataset, size_x=15, size_y=10, verbose=False):
    """
    Calculate the weights and ranks of alternatives using WINGS method.

    Args:
    - dataset (numpy.ndarray): A 2D array representing the decision matrix.
    - size_x (int, optional): The number of iterations for the row reduction algorithm.
    - size_y (int, optional): The number of iterations for the column reduction algorithm.
    - verbose (bool, optional): Whether to print the output.

    Returns:
    - result (dict): A dictionary containing the following keys:
        - R_plus_C (list): R + C values of each alternative.
        - R_minus_C (list): R - C values of each alternative.
        - weights (list): Weights of each alternative.

    Example:
    >>> dataset = np.array([
    ...     [4, 1, 4],
    ...     [3, 2, 2],
    ...     [2, 3, 2]
    ... ])
    >>> result = score_wings(dataset, size_x=15, size_y=10, verbose=True)
    """

    # Required Libraries
    from pyDecision.algorithm import wings_method

    # Call WINGS Function
    R_plus_C, R_minus_C, weights = wings_method(
        dataset, size_x=size_x, size_y=size_y)

    # Print the results
    if verbose:
        print("----- R + C -----")
        for i in range(len(R_plus_C)):
            print(f"g{i+1}: {round(R_plus_C[i], 4)}")
        print("-----------------")
        print("----- R - C -----")
        for i in range(len(R_minus_C)):
            print(f"g{i+1}: {round(R_minus_C[i], 4)}")
        print("-----------------")
        print("----- Weights -----")
        for i in range(len(weights)):
            print(f"g{i+1}: {round(weights[i], 4)}")

    # Return the results in a dictionary
    return {
        'R_plus_C': list(map(lambda x: round(x, 4), R_plus_C)),
        'R_minus_C': list(map(lambda x: round(x, 4), R_minus_C)),
        'weights': list(map(lambda x: round(x, 4), weights))
    }
