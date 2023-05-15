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


def mcdm_promethee_v(dataset: np.ndarray, W: List[float], Q: List[float], S: List[float], P: List[float], F: List[str], sort: bool = True, criteria: int = None, cost: List[float] = None, budget: float = None, forbidden: List[List[str]] = None, iterations: int = None, verbose: bool = False, show_plot: bool = False) -> Dict[str, Union[float, np.ndarray]]:
    """
    Calculate the scores of the alternatives using the Promethee V algorithm.

    Args:
        dataset (np.ndarray): A 2D numpy array containing the performance table of the alternatives.
        W (List[float]): A list of weights for each criterion.
        Q (List[float]): A list of preference threshold values for each criterion.
        S (List[float]): A list of indifference threshold values for each criterion.
        P (List[float]): A list of preference function shape parameters for each criterion.
        F (List[str]): A list of preference function types for each criterion.
        sort (bool, optional): A boolean indicating whether to sort the results in descending order. Defaults to True.
        criteria (int, optional): The maximum number of criteria to be selected. Defaults to None.
        cost (List[float], optional): A list of costs for each criterion. Defaults to None.
        budget (float, optional): The maximum budget for selecting criteria. Defaults to None.
        forbidden (List[List[str]], optional): A list of forbidden sets of selected criteria. Defaults to None.
        iterations (int, optional): The number of iterations for the Monte Carlo simulation. Defaults to None.
        verbose (bool, optional): A boolean indicating whether to print the progress of the algorithm. Defaults to False.
        show_plot (bool, optional): A boolean indicating whether to show the plot of the performance table. Defaults to False.

    Returns:
        Dict[str, Union[float, np.ndarray]]: A dictionary containing the calculated scores and rankings. The keys are:
            - 'scores': A 1D numpy array containing the scores of the alternatives.
            - 'rankings': A 1D numpy array containing the rankings of the alternatives.
    """
    from pyDecision.algorithm import promethee_v

    # Call Promethee V
    p5 = promethee_v(dataset, W=W, Q=Q, S=S, P=P, F=F, sort=sort, criteria=criteria, cost=cost,
                     budget=budget, forbidden=forbidden, iterations=iterations)

    # Create a dictionary with the scores and rankings
    result = {'scores': p5[:, 1], 'rankings': p5[:, 0]}

    return result
