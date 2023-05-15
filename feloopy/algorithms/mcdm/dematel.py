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
from pyDecision.algorithm import dematel_method


def weight_dematel_method(dataset: np.ndarray,
                          size_x: int = 15,
                          size_y: int = 10,
                          show_output: bool = True) -> Dict[str, Union[np.ndarray, None]]:
    """
    This function takes the dataset as input for the DEMATEL method of multi-criteria decision making. It returns the
    output of the main function (which is imported from Pydecision) in the form of a dictionary with keys representing
    the name of the output and values the value of the outputs.

    Args:
        dataset: A numpy array containing the influence values of each group on each other group.
        size_x: The size of the x-axis for the DEMATEL chart.
        size_y: The size of the y-axis for the DEMATEL chart.
        show_output: A boolean value indicating whether to show the output of D + R, D - R, and the criteria weights or not.

    Returns:
        A dictionary containing the following keys:
        - 'D_plus_R': A numpy array representing the sum of the direct and indirect influences of each group.
        - 'D_minus_R': A numpy array representing the difference between the direct and indirect influences of each group.
        - 'weights': A numpy array representing the calculated weights for each group.
    """

    from pyDecision.algorithm import dematel_method

    # Call DEMATEL Function
    D_plus_R, D_minus_R, weights = dematel_method(
        dataset, size_x=size_x, size_y=size_y)

    # Create the output dictionary
    output_dict = {'D_plus_R': D_plus_R,
                   'D_minus_R': D_minus_R, 'weights': weights}

    # If show_output is True, print the output of D + R, D - R, and the criteria weights
    if show_output:
        print('D + R:')
        for i in range(D_plus_R.shape[0]):
            print('g'+str(i+1), round(D_plus_R[i], 3))
        print()

        print('D - R:')
        for i in range(D_minus_R.shape[0]):
            print('g'+str(i+1), round(D_minus_R[i], 3))
        print()

        print('Criteria Weights:')
        for i in range(weights.shape[0]):
            print('g'+str(i+1), round(weights[i], 3))
        print()

    return output_dict
