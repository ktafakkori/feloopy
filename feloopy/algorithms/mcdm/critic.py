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
from pyDecision.algorithm import critic_method


def weight_critic_method(dataset: np.ndarray, criterion_type: list, show_output: bool = True) -> Dict[str, np.ndarray]:
    """
    This function takes the dataset and criterion type as input for the CRITIC method of multi-criteria decision making. It
    returns the output of the main function (which is imported from Pydecision) in the form of a dictionary with keys
    representing the name of the output and values the value of the outputs.

    Args:
        dataset: A numpy array containing the performance values of each alternative on each criterion. Each row
                 represents an alternative, and each column represents a criterion.
        criterion_type: A list of strings representing the type of each criterion. Each element of the list should be
                        either 'max' or 'min', indicating whether the criterion should be maximized or minimized,
                        respectively.
        show_output: A boolean value indicating whether to show the calculated weights or not.

    Returns:
        A dictionary containing the following keys:
        - 'weights': A numpy array representing the calculated weights for each criterion.
    """

    from pyDecision.algorithm import critic_method

    # Call CRITIC Function
    weights = critic_method(dataset, criterion_type)

    # Create the output dictionary
    output_dict = {'weights': weights}

    # If show_output is True, print the calculated weights
    if show_output:
        print('Weights:')
        for i in range(weights.shape[0]):
            print('w(g'+str(i+1)+'):', round(weights[i], 4))
        print()

    return output_dict
