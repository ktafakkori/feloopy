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


def rank_multimoora(dataset, criterion_type, verbose=False):
    """
    Rank alternatives using the MULTIMOORA method.

    Args:
    - dataset (numpy.ndarray): A 2D array representing the decision matrix.
    - criterion_type (list): A list of strings representing the type of each criterion ('max' or 'min').
    - verbose (bool, optional): Whether to print the output.

    Returns:
    - result (dict): A dictionary containing the following keys:
        - rank (list): A list of tuples where each tuple contains the rank of an alternative and its name.

    Example:
    >>> dataset = np.array([
    ...     [33.95, 23.78, 11.45, 39.97, 29.44, 167.10, 3.852],
    ...     [38.90, 4.17, 6.32, 0.01, 4.29, 132.52, 25.184],
    ...     [37.59, 9.36, 8.23, 4.35, 10.22, 136.71, 10.845],
    ...     [30.44, 37.59, 13.91, 74.08, 45.10, 198.34, 2.186],
    ...     [36.21, 14.79, 9.17, 17.77, 17.06, 148.30, 6.610],
    ...     [37.80, 8.55, 7.97, 2.35, 9.25, 134.83, 11.935]
    ... ])
    >>> criterion_type = ['min', 'min', 'min', 'min', 'max', 'min', 'max']
    >>> result = rank_multimoora(dataset, criterion_type, verbose=True)
    """

    # Required Libraries
    from pyDecision.algorithm import multimoora_method

    # Call MULTIMOORA Function
    rank = multimoora_method(dataset, criterion_type, graph=True)

    # Print the results
    pp = ['MOORA', 'MOORA REFRENCE POINT', 'MULTIMOORA']
    if verbose:
        for i in range(3):
            print(f"------------ RANKING {pp[i]}-------------")

            for r, a in rank[i]:
                print(f"Rank {r}: {a}")
            print("----------------------------------------------")

    # Return the results in a dictionary
    return {
        'rank': rank
    }
