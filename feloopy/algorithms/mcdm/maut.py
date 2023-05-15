'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-15
 # @ Modified: 2023-05-15
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

from typing import Dict
import numpy as np


def mcdm_maut(dataset: np.ndarray, weights: np.ndarray, criterion_type: list, utility_functions: list, step_size: int = None, verbose: bool = False) -> Dict[str, float]:
    """
    This function applies the MAUT method to rank a dataset based on given criteria.

    Args:
    - dataset (np.ndarray): The dataset to be ranked.
    - weights (np.ndarray): An array of weights for each criterion.
    - criterion_type (list): A list of criterion types, either 'max' or 'min'.
    - utility_functions (list): A list of utility functions, one for each criterion. Possible values: 'exp', 'ln', 'log', 'quad', or 'step'.
    - step_size (int, optional): Only relevant if 'step' is used as a utility function. Defaults to None.
    - verbose (bool, optional): If True, prints a graph of the criteria and their weights. Defaults to False.

    Returns:
    - A dictionary with the following keys:
        - 'rank': the rank of each alternative in the dataset, starting from 1.
        - 'score': the score of each alternative.
    """
    from pyDecision.algorithm import maut_method
    rank = maut_method(dataset, weights, criterion_type,
                       utility_functions, step_size, graph=verbose)
    score = np.round(rank / np.max(rank), 4)
    result = {'rank': rank, 'score': score}
    return result
