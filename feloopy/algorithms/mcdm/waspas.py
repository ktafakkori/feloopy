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


def mcdm_waspas(dataset, criterion_type, weights, lambda_value, verbose=False):
    """
    Calculate the weighted sum model (WSM), weighted product model (WPM), and WASPAS values of alternatives.

    Args:
    - dataset (numpy.ndarray): A 2D array representing the decision matrix.
    - criterion_type (list): A list of strings representing the type of each criterion ('max' or 'min').
    - weights (numpy.ndarray): A 2D array representing the weights of each criterion.
    - lambda_value (float): A float representing the value of lambda.
    - verbose (bool, optional): Whether to print the output.

    Returns:
    - result (dict): A dictionary containing the following keys:
        - wsm (list): WSM values of each alternative.
        - wpm (list): WPM values of each alternative.
        - waspas (list): WASPAS values of each alternative.

    Example:
    >>> dataset = np.array([
    ...     [250, 16, 12, 5],
    ...     [200, 16, 8, 3],
    ...     [300, 32, 16, 4],
    ...     [275, 32, 8, 4],
    ...     [225, 16, 16, 2]
    ... ])
    >>> criterion_type = ['min', 'max', 'max', 'max']
    >>> weights = np.array([[0.35, 0.30, 0.20, 0.15]])
    >>> lambda_value = 0.5
    >>> result = score_waspas(dataset, criterion_type, weights, lambda_value, verbose=True)
    """

    # Required Libraries
    from pyDecision.algorithm import waspas_method

    # Call WASPAS Function
    wsm, wpm, waspas = waspas_method(
        dataset, criterion_type, weights, lambda_value)

    # Print the results
    if verbose:
        print("------------- WSM -------------")
        for i in range(len(wsm)):
            print(f"a{i+1}: {round(wsm[i], 4)}")
        print("-------------------------------")
        print("------------- WPM -------------")
        for i in range(len(wpm)):
            print(f"a{i+1}: {round(wpm[i], 4)}")
        print("-------------------------------")
        print("------------- WASPAS -------------")
        for i in range(len(waspas)):
            print(f"a{i+1}: {round(waspas[i], 4)}")
        print("----------------------------------")

    # Return the results in a dictionary
    return {
        'wsm': list(map(lambda x: round(x, 4), wsm)),
        'wpm': list(map(lambda x: round(x, 4), wpm)),
        'waspas': list(map(lambda x: round(x, 4), waspas))
    }
