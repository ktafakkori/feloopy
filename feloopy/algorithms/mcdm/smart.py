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
from pyDecision.algorithm import smart_method


def score_smart_method(dataset: np.ndarray, grades: np.ndarray, lower: np.ndarray, upper: np.ndarray, criterion_type: List[str], graph: bool = False) -> Dict[str, Union[float, np.ndarray]]:
    """
    Score the alternatives using the Simple Multi-Attribute Rating Technique (SMART) method.

    Args:
        dataset (np.ndarray): A 2D numpy array containing the performance table of the alternatives.
        grades (np.ndarray): A 1D numpy array containing the grades of the alternatives, from worst to best.
        lower (np.ndarray): A 1D numpy array containing the minimum threshold for each criterion.
        upper (np.ndarray): A 1D numpy array containing the maximum threshold for each criterion.
        criterion_type (List[str]): A list of strings indicating the criterion type for each column. Must be either 'max' or 'min'.
        graph (bool, optional): A boolean indicating whether to display the ranking graph. Defaults to False.

    Returns:
        Dict[str, Union[float, np.ndarray]]: A dictionary containing the score of the alternatives.
    """

    score = smart_method(dataset, grades=grades, lower=lower,
                         upper=upper, criterion_type=criterion_type, graph=graph)

    results = {'Score': score}

    return results
