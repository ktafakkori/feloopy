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


def mcdm_topsis(dataset: np.ndarray, weights: np.ndarray, criterion_type: List[str], graph: bool = False) -> Dict[str, Union[float, np.ndarray]]:
    """
    Score the alternatives using the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) method.

    Args:
        dataset (np.ndarray): A 2D numpy array containing the performance table of the alternatives.
        weights (np.ndarray): A 2D numpy array containing the weights for each criterion. The sum of the weights for each column must be 1.
        criterion_type (List[str]): A list of strings indicating the criterion type for each column. Must be either 'max' or 'min'.
        graph (bool, optional): A boolean indicating whether to display the ranking graph. Defaults to False.

    Returns:
        Dict[str, Union[float, np.ndarray]]: A dictionary containing the score of the alternatives.
    """
    from pyDecision.algorithm import topsis_method

    score = topsis_method(dataset, weights=weights,
                          criterion_type=criterion_type, graph=graph)

    results = {'Score': score}

    return results
