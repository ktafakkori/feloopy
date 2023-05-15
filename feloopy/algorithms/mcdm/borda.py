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
from pyDecision.algorithm import borda_method


def rank_borda_method(dataset: np.ndarray, criterion_type: list, show_output: bool = True, show_graph: bool = False) -> Dict[str, Union[np.ndarray, None]]:
    """
    This function takes the dataset and criterion type as input for the Borda method of multi-criteria decision making.
    It returns the output of the main function (which is imported from Pydecision) in the form of a dictionary with keys
    representing the name of the output and values the value of the outputs.

    Args:
        dataset: A numpy array containing the performance values of each alternative on each criterion. Each row
                 represents an alternative, and each column represents a criterion.
        criterion_type: A list containing the type of each criterion. 'max' indicates that the criterion is a benefit
                        criterion, and 'min' indicates that the criterion is a cost criterion.
        show_output: A boolean value indicating whether to show the calculated ranks or not.
        show_graph: A boolean value indicating whether to show the visualization of the convergence graph or not.

    Returns:
        A dictionary containing the following keys:
        - 'rank': A numpy array representing the calculated ranks for each alternative.
        - 'graph': If show_graph is True, a matplotlib figure object representing the visualization of the convergence
                   graph. Otherwise, None.
    """

    from pyDecision.algorithm import borda_method
    import matplotlib.pyplot as plt

    # Call Borda Function
    rank = borda_method(dataset, criterion_type)

    # Create the output dictionary
    output_dict = {'rank': rank}

    # If show_output is True, print the calculated ranks
    if show_output:
        print('Rank:')
        for i in range(rank.shape[0]):
            print('a' + str(i + 1) + ':', int(rank[i]))
        print()

    return output_dict
