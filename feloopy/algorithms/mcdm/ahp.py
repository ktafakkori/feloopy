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


def mcdm_ahp(dataset: np.ndarray, mcdm_derivation: str, verbose: bool = False) -> Dict[str, np.ndarray]:
    """
    Analytic Hierarchy Process
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    This function applies the AHP method to compute weights for a set of criteria.

    Args:
    - dataset (np.ndarray): The pairwise comparison matrix of criteria.
    - mcdm_derivation (str): The method for deriving the weights, either 'mean' or 'geometric'.
    - verbose (bool, optional): If True, prints the weights and consistency ratio. Defaults to False.

    Returns:
    - A dictionary with the following keys:
        - 'weights': the weights of each criterion.
        - 'consistency_ratio': the consistency ratio of the pairwise comparison matrix.
        - 'consistent': a boolean indicating whether the pairwise comparison matrix is consistent or not.
    """
    from pyDecision.algorithm import ahp_method

    weights, rc = ahp_method(dataset, wd=mcdm_derivation)
    consistent = rc <= 0.10
    result = {
        'weights': np.round(weights, 4),
        'consistency_ratio': np.round(rc, 2),
        'consistent': consistent
    }
    if verbose:
        mcdm_strings = [
            f"w(g{i+1}): {result['weights'][i]}" for i in range(len(result['weights']))]
        print('\n'.join(mcdm_strings))
        print(f"RC: {result['consistency_ratio']}")
        if not consistent:
            print(
                "The solution is inconsistent, the pairwise comparisons must be reviewed")
        else:
            print("The solution is consistent")
    return result
