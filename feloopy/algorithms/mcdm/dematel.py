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


def mcdm_dematel(dataset: np.ndarray, size_x: int = 15, size_y: int = 10, show_output: bool = True) -> Dict[str, Union[np.ndarray, None]]:
    """
    Computes the weights of each group using the Decision Making Trial and Evaluation Laboratory (DEMATEL) method of
    multi-criteria decision making.

    Args:
        dataset (np.ndarray): A numpy array containing the influence values of each group on each other group.
        size_x (int, optional): The size of the x-axis for the DEMATEL chart. Defaults to 15.
        size_y (int, optional): The size of the y-axis for the DEMATEL chart. Defaults to 10.
        show_output (bool, optional): A boolean value indicating whether to show the output of D + R, D - R, and the
                                       criteria weights or not. Defaults to True.

    Returns:
        A dictionary with the following keys:
        - 'D_plus_R' (np.ndarray): An array representing the sum of the direct and indirect influences of each group.
        - 'D_minus_R' (np.ndarray): An array representing the difference between the direct and indirect influences of
                                    each group.
        - 'weights' (np.ndarray): An array representing the calculated weights for each group.
        - 'chart' (Optional[matplotlib.pyplot]): If show_output is True, a matplotlib figure object representing the
                                                  DEMATEL chart. Otherwise, None.
                                                  
    Example usage:
    ```
    dataset = np.array([[0, 0.2, 0.4, 0.6], [0.1, 0, 0.3, 0.5], [0.2, 0.1, 0, 0.4], [0.3, 0.2, 0.1, 0]])
    result = mcdm_dematel(dataset, show_output=True)
    ```
    """

    from pyDecision.algorithm import dematel_method
    import matplotlib.pyplot as plt

    # Call DEMATEL Function
    D_plus_R, D_minus_R, weights = dematel_method(dataset, size_x=size_x, size_y=size_y)

    # Create the output dictionary
    output_dict = {'D_plus_R': D_plus_R, 'D_minus_R': D_minus_R, 'weights': weights}

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

    if show_output:
        x = range(1, size_x + 1)
        y = range(1, size_y + 1)
        X, Y = np.meshgrid(x, y)
        Z = np.zeros((size_y, size_x))
        for i in range(size_y):
            for j in range(size_x):
                Z[i, j] = dataset[i, j] - dataset[j, i]
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap='coolwarm')
        ax.set_xlabel('Group')
        ax.set_ylabel('Group')
        ax.set_zlabel('Difference')
        plt.show()
        output_dict['chart'] = plt

    return output_dict