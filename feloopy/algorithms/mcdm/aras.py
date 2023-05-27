'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-15
 # @ Modified: 2023-05-15
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

from typing import Dict, List, Union
import numpy as np

def mcdm_aras(dataset: np.ndarray, weights: np.ndarray, criterion_type: List[str], show_output: bool = True, show_graph: bool = False) -> Dict[str, Union[np.ndarray, None]]:
    """
    Computes the scores of alternatives using the Additive Ratio Assessment System (ARAS) method of multi-criteria decision making.

    Args:
        dataset (np.ndarray): A numpy array containing the performance values of each alternative on each criterion.
                              Each row represents an alternative, and each column represents a criterion.
        weights (np.ndarray): A numpy array containing the weight values for each criterion.
        criterion_type (List[str]): A list containing the type of each criterion. 'max' indicates that the criterion
                                    is a benefit criterion, and 'min' indicates that the criterion is a cost criterion.
        show_output (bool, optional): A boolean value indicating whether to show the calculated scores or not.
                                      Defaults to True.
        show_graph (bool, optional): A boolean value indicating whether to show the visualization of the convergence graph
                                     or not. Defaults to False.

    Returns:
        A dictionary with the following keys:
        - 'score' (np.ndarray): An array of the calculated scores for each alternative.
        - 'graph' (Optional[matplotlib.figure.Figure]): If show_graph is True, a matplotlib figure object representing
                                                        the visualization of the convergence graph. Otherwise, None.
    Example usage:
    ```
    dataset = np.array([[2, 3, 4], [5, 6, 7]])
    weights = np.array([0.5, 0.3, 0.2])
    criterion_type = ['max', 'max', 'max']
    result = mcdm_aras(dataset, weights, criterion_type, show_graph=True)
    ```
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
