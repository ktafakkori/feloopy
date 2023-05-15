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
from pyDecision.algorithm import promethee_gaia


def score_promethee_gaia(dataset: np.ndarray, W: np.ndarray, Q: np.ndarray, S: np.ndarray, P: np.ndarray, F: List[str], size_x: float = 12, size_y: float = 12, show_graph: bool = False) -> Dict[str, Union[float, np.ndarray]]:
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

    scores = promethee_gaia(dataset, W=W, Q=Q, S=S, P=P,
                            F=F, size_x=size_x, size_y=size_y)

    results = {'Scores': scores}

    return results


# Parameters
Q = np.array([0.3, 0.3, 0.3, 0.3])
S = np.array([0.4, 0.4, 0.4, 0.4])
P = np.array([0.5, 0.5, 0.5, 0.5])
W = np.array([9.00, 8.24, 5.98, 8.48])
# 't1' = Usual; 't2' = U-Shape; 't3' = V-Shape; 't4' = Level; 't5' = V-Shape with Indifference; 't6' = Gaussian; 't7' = C-Form
F = ['t5', 't5', 't5', 't5']

# Dataset
dataset = np.array([
    [8.840, 8.790, 6.430, 6.950],  # a1
    [8.570, 8.510, 5.470, 6.910],  # a2
    [7.760, 7.750, 5.340, 8.760],  # a3
    [7.970, 9.120, 5.930, 8.090],  # a4
    [9.030, 8.970, 8.190, 8.100],  # a5
    [7.410, 7.870, 6.770, 7.230]  # a6
])

# Call score_promethee_gaia
results = score_promethee_gaia(
    dataset, W=W, Q=Q, S=S, P=P, F=F, size_x=12, size_y=12, show_graph=True)

# Print the scores
print(results['Scores'])
