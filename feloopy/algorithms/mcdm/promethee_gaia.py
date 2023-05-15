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


def mcdm_promethee_gaia(dataset: np.ndarray, W: np.ndarray, Q: np.ndarray, S: np.ndarray, P: np.ndarray, F: List[str], size_x: float = 12, size_y: float = 12, show_graph: bool = False) -> Dict[str, Union[float, np.ndarray]]:
    """
    Calculate the scores of the alternatives using the Promethee Gaia algorithm.

    Args:
        dataset (np.ndarray): A 2D numpy array containing the performance table of the alternatives.
        W (np.ndarray): A 1D numpy array containing the weights for each criterion.
        Q (np.ndarray): A numpy array of preference threshold values for each criterion.
        S (np.ndarray): A numpy array of indifference threshold values for each criterion.
        P (np.ndarray): A numpy array of preference function shape parameters for each criterion.
        F (List[str]): A list of preference function types for each criterion.
        size_x (float, optional): A float indicating the size of the x-axis for the Gaia graph. Defaults to 12.
        size_y (float, optional): A float indicating the size of the y-axis for the Gaia graph. Defaults to 12.
        show_graph (bool, optional): A boolean indicating whether to display the Gaia graph. Defaults to False.

    Returns:
        Dict[str, Union[float, np.ndarray]]: A dictionary containing the scores of the alternatives.
    """
    from pyDecision.algorithm import promethee_gaia

    scores = promethee_gaia(dataset, W=W, Q=Q, S=S, P=P,
                            F=F, size_x=size_x, size_y=size_y)

    results = {'Scores': scores}

    return results
