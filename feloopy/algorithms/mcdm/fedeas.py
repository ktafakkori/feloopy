'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-15
 # @ Modified: 2023-05-15
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

from typing import Dict, List, Tuple
import numpy as np


def mcdm_fuzzy_edas(dataset: List[np.ndarray], criterion_type: List[str], weights: List[Tuple[Tuple[float, float, float]]], verbose: bool = False) -> Dict[str, np.ndarray]:
    """
    This function applies the fuzzy EDAS method to rank alternatives in a dataset based on multiple criteria.

    Args:
    - dataset (List[np.ndarray]): The dataset of alternatives to be ranked.
    - criterion_type (List[str]): A list of criterion types, either 'max' or 'min'.
    - weights (List[Tuple[Tuple[float, float, float]]]): A list of tuples containing the fuzzy weights for each criterion.
    - verbose (bool, optional): If True, prints the final rank. Defaults to False.

    Returns:
    - A dictionary with the following keys:
        - 'rank': the rank of each alternative.
    """
    from pyDecision.algorithm import fuzzy_edas_method

    rank = fuzzy_edas_method(dataset, criterion_type, weights, graph=verbose)
    result = {
        'rank': np.round(rank, 4)
    }
    return result
