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
from pyDecision.algorithm import idocriw_method


def rank_idocriw(dataset: np.ndarray, criterion_type: list, size: int = 20, gen: int = 12000, verbose: bool = False) -> Dict[str, np.ndarray]:
    """
    This function applies the IDOCRIW method to rank alternatives in a dataset based on multiple criteria.

    Args:
    - dataset (np.ndarray): The dataset of alternatives to be ranked.
    - criterion_type (list): A list of criterion types, either 'max' or 'min'.
    - size (int, optional): The size of the population. Defaults to 20.
    - gen (int, optional): The number of generations. Defaults to 12000.
    - verbose (bool, optional): If True, prints the final population and the best scores. Defaults to False.

    Returns:
    - A dictionary with the following keys:
        - 'rank': the rank of each alternative.
        - 'score': the score of each alternative.
        - 'population': the final population.
        - 'best_score': the best score obtained.
    """
    rank = idocriw_method(
        dataset, criterion_type, size=size, gen=gen, graph=verbose)
    result = {
        'rank': rank
    }
    return result
