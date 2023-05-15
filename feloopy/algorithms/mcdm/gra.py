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


def score_gra(dataset: np.ndarray, criterion_type: list, weights: np.ndarray, epsilon: float = 0.5, verbose: bool = False) -> Dict[str, np.ndarray]:
    """
    This function applies the GRA method to score alternatives in a dataset based on multiple criteria.

    Args:
    - dataset (np.ndarray): The dataset of alternatives to be scored.
    - criterion_type (list): A list of criterion types, either 'max' or 'min'.
    - weights (np.ndarray): A 2D array of criterion weights.
    - epsilon (float, optional): The threshold value used to determine the discriminating power of each criterion. Defaults to 0.5.
    - verbose (bool, optional): If True, prints the final grades. Defaults to False.

    Returns:
    - A dictionary with the following keys:
        - 'grade': the grade of each alternative.
    """

    from pyDecision.algorithm import gra_method
    grade = gra_method(dataset, criterion_type,
                       weights, epsilon, graph=verbose)
    result = {
        'grade': np.round(grade, 4)
    }
    return result
