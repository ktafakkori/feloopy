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


def mcdm_borda(dataset: np.ndarray, criterion_type: List[str], show_output: bool = True, show_graph: bool = False) -> Dict[str, Union[np.ndarray, None]]:
    """
    Computes the ranks of alternatives using the Borda method of multi-criteria decision making.

    Args:
        dataset (np.ndarray): A numpy array containing the performance values of each alternative on each criterion.
                              Each row represents an alternative, and each column represents a criterion.
        criterion_type (List[str]): A list containing the type of each criterion. 'max' indicates that the criterion
                                    is a benefit criterion, and 'min' indicates that the criterion is a cost criterion.
        show_output (bool, optional): A boolean value indicating whether to show the calculated ranks or not.
                                      Defaults to True.
        show_graph (bool, optional): A boolean value indicating whether to show the visualization of the convergence graph
                                     or not. Defaults to False.

    Returns:
        A dictionary with the following keys:
        - 'rank' (np.ndarray): An array of the calculated ranks for each alternative.
        - 'graph' (Optional[matplotlib.figure.Figure]): If show_graph is True, a matplotlib figure object representing
                                                        the visualization of the convergence graph. Otherwise, None.

    Example usage:
    ```
    dataset = np.array([[2, 3, 4], [5, 6, 7]])
    criterion_type = ['max', 'max', 'max']
    result = mcdm_borda(dataset, criterion_type, show_graph=True)
    ```
    """

    from pyDecision.algorithm import borda_method
    import matplotlib.pyplot as plt

    rank = borda_method(dataset, criterion_type)

    output_dict = {'rank': rank}

    if show_output:
        print('Rank:')
        for i in range(rank.shape[0]):
            print('a' + str(i + 1) + ':', int(rank[i]))
        print()

    return output_dict