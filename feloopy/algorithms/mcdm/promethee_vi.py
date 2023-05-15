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
from pyDecision.algorithm import promethee_vi


def rank_promethee_vi(dataset: np.ndarray, W_lower: np.ndarray, W_upper: np.ndarray, Q: List[float], S: List[float], P: List[float], F: List[str], sort: bool = True, topn: int = None, iterations: int = None, graph: bool = False) -> Dict[str, Union[float, np.ndarray]]:
    """
    Calculate the rankings of the alternatives using the Promethee VI algorithm.

    Args:
        dataset (np.ndarray): A 2D numpy array containing the performance table of the alternatives.
        W_lower (np.ndarray): A 1D numpy array containing the lower bounds of the weights for each criterion.
        W_upper (np.ndarray): A 1D numpy array containing the upper bounds of the weights for each criterion.
        Q (List[float]): A list of preference threshold values for each criterion.
        S (List[float]): A list of indifference threshold values for each criterion.
        P (List[float]): A list of preference function shape parameters for each criterion.
        F (List[str]): A list of preference function types for each criterion.
        sort (bool, optional): A boolean indicating whether to sort the results in descending order. Defaults to True.
        topn (int, optional): An integer indicating the top N alternatives to return. Defaults to None.
        iterations (int, optional): An integer indicating the number of iterations for the Monte Carlo simulation. Defaults to None.
        graph (bool, optional): A boolean indicating whether to display the graph of the Monte Carlo simulation. Defaults to False.

    Returns:
        Dict[str, Union[float, np.ndarray]]: A dictionary containing the rankings of the alternatives.
    """

    p6_minus, p6, p6_plus = promethee_vi(dataset, W_lower=W_lower, W_upper=W_upper,
                                         Q=Q, S=S, P=P, F=F, sort=sort, topn=topn, iterations=iterations, graph=graph)

    results = {'Rank_Minus_Lower': p6_minus[:, 1],
               'Rank_Favorable': p6[:, 1], 'Rank_Plus_Upper': p6_plus[:, 1]}

    return results
