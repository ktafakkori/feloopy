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


def mcdm_moosra(dataset, weights, criterion_type, verbose=False):
    """
    Score alternatives using the MOOSRA method.

    Args:
    - dataset (numpy.ndarray): A 2D array representing the decision matrix.
    - weights (numpy.ndarray): A 1D array representing the weight of each criterion.
    - criterion_type (list): A list of strings representing the type of each criterion ('max' or 'min').
    - verbose (bool, optional): Whether to print the output.

    Returns:
    - result (dict): A dictionary containing the following keys:
        - score (numpy.ndarray): A 1D array containing the score of each alternative.
        - rank (numpy.ndarray): A 1D array containing the rank of each alternative.

    Example:
    >>> dataset = np.array([
    ...     [3.5, 6, 1256, 4, 16, 3, 17.3, 8, 2.82, 4100],
    ...     [3.1, 4, 1000, 2, 8,  1, 15.6, 5, 3.08, 3800],
    ...     [3.6, 6, 2000, 4, 16, 3, 17.3, 5, 2.9,  4000],
    ...     [3,   4, 1000, 2, 8,  2, 17.3, 5, 2.6,  3500],
    ...     [3.3, 6, 1008, 4, 12, 3, 15.6, 8, 2.3,  3800],
    ...     [3.6, 6, 1000, 2, 16, 3, 15.6, 5, 2.8,  4000],
    ...     [3.5, 6, 1256, 2, 16, 1, 15.6, 6, 2.9,  4000]
    ... ])
    >>> weights = np.array([0.297, 0.025, 0.035, 0.076, 0.154, 0.053, 0.104, 0.017, 0.025, 0.214])
    >>> criterion_type = ['max', 'max', 'max', 'max', 'max', 'max', 'max', 'max', 'min', 'min']
    >>> result = score_moosra(dataset, weights, criterion_type, verbose=True)
    """

    # Required Libraries
    from pyDecision.algorithm import moosra_method

    # Call MOOSRA Function
    score, rank = moosra_method(dataset, weights, criterion_type, graph=True)

    # Print the results
    if verbose:
        print("------------- MOOSRA RESULTS -------------")
        print("Score:", score)
        print("------------------------------------------")

    # Return the results in a dictionary
    return {
        'score': score,
        'rank': rank
    }
