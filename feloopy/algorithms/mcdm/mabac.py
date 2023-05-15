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
from pyDecision.algorithm import mabac_method


def score_mabac(dataset: np.ndarray, criterion_type: list, verbose: bool = False) -> Dict[str, float]:
    """
    This function applies the MABAC method to score alternatives in a dataset based on multiple criteria.

    Args:
    - dataset (np.ndarray): The dataset of alternatives to be scored.
    - criterion_type (list): A list of criterion types, either 'max' or 'min'.
    - verbose (bool, optional): If True, prints a graph of the criteria and their weights. Defaults to False.

    Returns:
    - A dictionary with the following keys:
        - 'score': the score of each alternative, ranging from 0 to 1.
    """
    # Set weights to 1 for equal weighting
    weights = np.ones(len(criterion_type)) / len(criterion_type)

    score = mabac_method(dataset, criterion_type, graph=verbose)
    result = {'score': np.round(score, 4)}
    return result
