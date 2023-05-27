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


def mcdm_bwm(dataset: np.ndarray, mic: np.ndarray, lic: np.ndarray, size: int, iterations: int, show_output: bool = True, show_graph: bool = False) -> Dict[str, Union[np.ndarray, None]]:
    """
    Computes the weights of criteria using the Best Worst Method (BWM) of multi-criteria decision making.

    Args:
        dataset (np.ndarray): A numpy array containing the performance values of each alternative on each criterion.
                              Each row represents an alternative, and each column represents a criterion.
        mic (np.ndarray): A numpy array containing the index of the most important criterion.
        lic (np.ndarray): A numpy array containing the index of the least important criterion.
        size (int): An integer representing the size of the population in the genetic algorithm.
        iterations (int): An integer representing the number of iterations for the genetic algorithm.
        show_output (bool, optional): A boolean value indicating whether to show the calculated weights or not.
                                      Defaults to True.
        show_graph (bool, optional): A boolean value indicating whether to show the visualization of the convergence graph
                                     or not. Defaults to False.

    Returns:
        A dictionary with the following keys:
        - 'weights' (np.ndarray): An array of the calculated weights for each criterion.
        - 'graph' (Optional[matplotlib.figure.Figure]): If show_graph is True, a matplotlib figure object representing
                                                        the visualization of the convergence graph. Otherwise, None.

    Example usage:
    ```
    dataset = np.array([[2, 3, 4], [5, 6, 7]])
    mic = np.array([1])
    lic = np.array([2])
    size = 50
    iterations = 100
    result = mcdm_bwm(dataset, mic, lic, size, iterations, show_graph=True)
    ```
    """

    from pyDecision.algorithm import bw_method

    weights = bw_method(dataset, mic, lic, size=size, iterations=iterations)

    output_dict = {'weights': weights}

    if show_output:
        print('Weights:')
        for i in range(weights.shape[0]):
            print('w(g' + str(i + 1) + '):', round(weights[i], 4))
        print()

    return output_dict