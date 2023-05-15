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
from pyDecision.algorithm import fuzzy_ahp_method


def weight_fuzzy_ahp(dataset: list, verbose: bool = False) -> Dict[str, np.ndarray]:
    """
    This function applies the Fuzzy AHP method to compute weights for a set of criteria.

    Args:
    - dataset (list): The fuzzy pairwise comparison matrix of criteria.
    - verbose (bool, optional): If True, prints the fuzzy weights, crisp weights, normalized weights, and consistency ratio. Defaults to False.

    Returns:
    - A dictionary with the following keys:
        - 'fuzzy_weights': the fuzzy weights of each criterion.
        - 'crisp_weights': the crisp weights of each criterion.
        - 'normalized_weights': the normalized weights of each criterion.
        - 'consistency_ratio': the consistency ratio of the pairwise comparison matrix.
        - 'consistent': a boolean indicating whether the pairwise comparison matrix is consistent or not.
    """
    fuzzy_weights, defuzzified_weights, normalized_weights, rc = fuzzy_ahp_method(
        dataset)

    consistent = rc <= 0.10
    result = {
        'fuzzy_weights': np.around(fuzzy_weights, 4),
        'crisp_weights': np.round(defuzzified_weights, 4),
        'normalized_weights': np.round(normalized_weights, 4),
        'consistency_ratio': np.round(rc, 2),
        'consistent': consistent
    }
    if verbose:
        for i in range(len(fuzzy_weights)):
            print(f"g{i+1}: {result['fuzzy_weights'][i]}")
        for i in range(len(defuzzified_weights)):
            print(f"g{i+1}: {result['crisp_weights'][i]}")
        for i in range(len(normalized_weights)):
            print(f"g{i+1}: {result['normalized_weights'][i]}")
        print(f"RC: {result['consistency_ratio']}")
        if not consistent:
            print(
                "The solution is inconsistent, the pairwise comparisons must be reviewed")
        else:
            print("The solution is consistent")
    return result
