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
from pyDecision.algorithm import copras_method


def rank_copras_method(dataset: np.ndarray, weights: np.ndarray, criterion_type: list, show_output: bool = True, show_graph: bool = False) -> Dict[str, Union[np.ndarray, None]]:
    """
    This function takes the dataset, weights and criterion type as input for the COPRAS method of multi-criteria decision making. It
    returns the output of the main function (which is imported from Pydecision) in the form of a dictionary with keys
    representing the name of the output and values the value of the outputs.

    Args:
        dataset: A numpy array containing the performance values of each alternative on each criterion. Each row
                 represents an alternative, and each column represents a criterion.
        weights: A numpy array containing the weight values for each criterion.
        criterion_type: A list of strings representing the type of each criterion. Each element of the list should be
                        either 'max' or 'min', indicating whether the criterion should be maximized or minimized,
                        respectively.
        show_output: A boolean value indicating whether to show the calculated rank or not.
        show_graph: A boolean value indicating whether to show the visualization of the ranking graph or not.

    Returns:
        A dictionary containing the following keys:
        - 'rank': A numpy array representing the calculated rank for each alternative.
        - 'graph': If show_graph is True, a matplotlib figure object representing the visualization of the ranking graph.
                   Otherwise, None.
    """

    from pyDecision.algorithm import copras_method
    import matplotlib.pyplot as plt

    # Call COPRAS Function
    rank = copras_method(dataset, weights, criterion_type, graph=show_graph)

    # Create the output dictionary
    output_dict = {'rank': rank}

    # If show_output is True, print the calculated rank
    if show_output:
        print('Ranking:')
        for i in range(rank.shape[0]):
            print(rank[i])
        print()

    return output_dict
