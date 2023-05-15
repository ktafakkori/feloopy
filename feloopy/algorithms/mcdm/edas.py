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


def mcdm_edas(dataset: np.ndarray, criterion_type: list, weights: np.ndarray, verbose: bool = False) -> Dict[str, np.ndarray]:
    """
    This function applies the EDAS method to rank alternatives in a dataset based on multiple criteria.

    Args:
    - dataset (np.ndarray): The dataset of alternatives to be ranked.
    - criterion_type (list): A list of criterion types, either 'max' or 'min'.
    - weights (np.ndarray): A 2D array of criterion weights.
    - verbose (bool, optional): If True, prints the final rank. Defaults to False.

    Returns:
    - A dictionary with the following keys:
        - 'rank': the rank of each alternative.
    """

    from pyDecision.algorithm import edas_method

    rank = edas_method(dataset, criterion_type, weights, graph=verbose)
    result = {
        'rank': np.round(rank, 4)
    }
    return result
