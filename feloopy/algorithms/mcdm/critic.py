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


def mcdm_critic(dataset: np.ndarray, criterion_type: list, show_output: bool = True) -> Dict[str, np.ndarray]:
    """
    Computes the weights of each criterion using the Criteria Importance Through Intercriteria Correlation (CRITIC)
    method of multi-criteria decision making.

    Args:
        dataset (np.ndarray): A numpy array containing the performance values of each alternative on each criterion.
                              Each row represents an alternative, and each column represents a criterion.
        criterion_type (list): A list of strings representing the type of each criterion. Each element of the list
                               should be either 'max' or 'min', indicating whether the criterion should be maximized
                               or minimized, respectively.
        show_output (bool, optional): A boolean value indicating whether to show the calculated weights or not.
                                      Defaults to True.

    Returns:
        A dictionary with the following keys:
        - 'weights' (np.ndarray): An array of the calculated weights for each criterion.

    Example usage:
    ```
    dataset = np.array([[2, 3, 4], [5, 6, 7]])
    criterion_type = ['max', 'max', 'max']
    result = mcdm_critic(dataset, criterion_type)
    ```
    """

    from pyDecision.algorithm import critic_method

    weights = critic_method(dataset, criterion_type)

    output_dict = {'weights': weights}

    if show_output:
        print('Weights:')
        for i in range(weights.shape[0]):
            print('w(g'+str(i+1)+'):', round(weights[i], 4))
        print()

    return output_dict
