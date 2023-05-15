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
from pyDecision.algorithm import aras_method


def score_aras_method(dataset: np.ndarray, weights: np.ndarray, criterion_type: list, show_output: bool = True, show_graph: bool = False) -> Dict[str, Union[np.ndarray, None]]:
    """
    This function takes the dataset, weights, and criterion type as input for the ARAS method of multi-criteria decision making.
    It returns the output of the main function (which is imported from Pydecision) in the form of a dictionary with keys
    representing the name of the output and values the value of the outputs.

    Args:
        dataset: A numpy array containing the performance values of each alternative on each criterion. Each row
                 represents an alternative, and each column represents a criterion.
        weights: A numpy array containing the weight values for each criterion.
        criterion_type: A list containing the type of each criterion. 'max' indicates that the criterion is a benefit
                        criterion, and 'min' indicates that the criterion is a cost criterion.
        show_output: A boolean value indicating whether to show the calculated scores or not.
        show_graph: A boolean value indicating whether to show the visualization of the convergence graph or not.

    Returns:
        A dictionary containing the following keys:
        - 'score': A numpy array representing the calculated scores for each alternative.
        - 'graph': If show_graph is True, a matplotlib figure object representing the visualization of the convergence
                   graph. Otherwise, None.
    """

    from pyDecision.algorithm import aras_method
    import matplotlib.pyplot as plt

    # Call ARAS Function
    score = aras_method(dataset, weights, criterion_type)

    # Create the output dictionary
    output_dict = {'score': score}

    # If show_output is True, print the calculated scores
    if show_output:
        print('Score:')
        for i in range(score.shape[0]):
            print(score[i])
        print()

    return output_dict
