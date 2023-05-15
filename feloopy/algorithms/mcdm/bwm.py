'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-15
 # @ Modified: 2023-05-15
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

from typing import Dict, Union
import numpy as np
from pyDecision.algorithm import bw_method


def weight_bw_method(dataset: np.ndarray, mic: np.ndarray, lic: np.ndarray, size: int, iterations: int, show_output: bool = True, show_graph: bool = False) -> Dict[str, Union[np.ndarray, None]]:
    """
    This function takes the dataset, most important criteria (mic) and least important criteria (lic) as input for the
    BWM method of multi-criteria decision making. It returns the output of the main function (which is imported from
    Pydecision) in the form of a dictionary with keys representing the name of the output and values the value of the outputs.

    Args:
        dataset: A numpy array containing the performance values of each alternative on each criterion. Each row
                 represents an alternative, and each column represents a criterion.
        mic: A numpy array containing the indices of the most important criteria.
        lic: A numpy array containing the indices of the least important criteria.
        size: An integer representing the size of the population in the genetic algorithm.
        iterations: An integer representing the number of iterations for the genetic algorithm.
        show_output: A boolean value indicating whether to show the calculated weights or not.
        show_graph: A boolean value indicating whether to show the visualization of the convergence graph or not.

    Returns:
        A dictionary containing the following keys:
        - 'weights': A numpy array representing the calculated weights for each criterion.
        - 'graph': If show_graph is True, a matplotlib figure object representing the visualization of the convergence graph.
                   Otherwise, None.
    """

    from pyDecision.algorithm import bw_method
    import matplotlib.pyplot as plt

    # Call BWM Function
    weights = bw_method(dataset, mic, lic, size=size, iterations=iterations)

    # Create the output dictionary
    output_dict = {'weights': weights}

    # If show_output is True, print the calculated weights
    if show_output:
        print('Weights:')
        for i in range(weights.shape[0]):
            print('w(g' + str(i + 1) + '):', round(weights[i], 4))
        print()

    return output_dict
