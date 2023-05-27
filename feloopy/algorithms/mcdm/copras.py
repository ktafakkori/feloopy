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


def mcdm_copras(dataset: np.ndarray, weights: np.ndarray, criterion_type: list, show_output: bool = True, show_graph: bool = False) -> Dict[str, Union[np.ndarray, None]]:
    """
    Computes the rank of each alternative using the Complex Proportional Assessment (COPRAS) method of multi-criteria
    decision making.

    Args:
        dataset (np.ndarray): A numpy array containing the performance values of each alternative on each criterion.
                              Each row represents an alternative, and each column represents a criterion.
        weights (np.ndarray): A numpy array containing the weight values for each criterion.
        criterion_type (list): A list of strings representing the type of each criterion. Each element of the list
                               should be either 'max' or 'min', indicating whether the criterion should be maximized
                               or minimized, respectively.
        show_output (bool, optional): A boolean value indicating whether to show the calculated rank or not.
                                      Defaults to True.
        show_graph (bool, optional): A boolean value indicating whether to show the visualization of the ranking graph
                                     or not. Defaults to False.

    Returns:
        A dictionary with the following keys:
        - 'rank' (np.ndarray): An array of the calculated rank for each alternative.
        - 'graph' (Optional[matplotlib.pyplot]): If show_graph is True, a matplotlib figure object representing the
                                                  visualization of the ranking graph. Otherwise, None.

    Example usage:
    ```
    dataset = np.array([[2, 3, 4], [5, 6, 7]])
    weights = np.array([0.3, 0.4, 0.3])
    criterion_type = ['max', 'max', 'max']
    result = mcdm_copras(dataset, weights, criterion_type, show_graph=True)
    ```
    """

    from pyDecision.algorithm import copras_method
    import matplotlib.pyplot as plt

    rank = copras_method(dataset, weights, criterion_type, graph=show_graph)

    output_dict = {'rank': rank}

    if show_output:
        print('Ranking:')
        for i in range(rank.shape[0]):
            print(rank[i])
        print()

    if show_graph:
        plt.show()
        output_dict['graph'] = plt

    return output_dict