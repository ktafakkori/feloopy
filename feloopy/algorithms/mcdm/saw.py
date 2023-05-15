'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-15
 # @ Modified: 2023-05-15
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

from typing import Dict, List, Union
import numpy as np


def mcdm_saw(dataset: np.ndarray, criterion_type: List[str], weights: np.ndarray, graph: bool = False) -> Dict[str, Union[float, np.ndarray]]:
    """
    Rank the alternatives using the Simple Additive Weighting (SAW) method.

    Args:
        dataset (np.ndarray): A 2D numpy array containing the performance table of the alternatives.
        criterion_type (List[str]): A list of strings indicating the criterion type for each column. Must be either 'max' or 'min'.
        weights (np.ndarray): A 1D numpy array containing the weights for each criterion.
        graph (bool, optional): A boolean indicating whether to display the ranking graph. Defaults to False.

    Returns:
        Dict[str, Union[float, np.ndarray]]: A dictionary containing the ranking of the alternatives.
    """
    from pyDecision.algorithm import saw_method

    ranking = saw_method(
        dataset, criterion_type=criterion_type, weights=weights, graph=graph)

    results = {'Ranking': ranking}

    return results
