'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-15
 # @ Modified: 2023-05-15
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

from typing import Dict
import numpy as np


def score_electre_i_v(dataset: np.ndarray, V: list, W: list, remove_cycles: bool = True, c_hat: float = 0.5,
                      graph: bool = False, verbose: bool = False) -> Dict[str, any]:
    """
    This function performs the Electre I_v algorithm on a given dataset and returns the concordance, discordance,
    dominance, kernel, and dominated matrices as a dictionary.

    Args:
    - dataset (np.ndarray): The decision matrix with shape (alternatives, criteria).
    - V (list): The thresholds for the criteria. A list with length equal to the number of criteria.
    - W (list): The weights for the criteria. A list with length equal to the number of criteria.
    - remove_cycles (bool): Whether or not to remove the cycles in the outranking relation. Defaults to True.
    - c_hat (float): The threshold for concordance. Defaults to 0.5.
    - graph (bool): Whether or not to show the graph of the outranking relation. Defaults to False.
    - verbose (bool): Whether or not to print additional information to the console. Defaults to False.

    Returns:
    - A dictionary containing the following keys:
        - 'concordance': The concordance matrix.
        - 'discordance': The discordance matrix.
        - 'dominance': The dominance matrix.
        - 'kernel': The kernel of the outranking relation.
        - 'dominated': The alternatives that are dominated.

    Example Usage:
    ```
    # Required Libraries
    import numpy as np

    # Dataset
    dataset = np.array([
                    [15,  9, 6, 10],   #a1
                    [10,  5, 7,  8],   #a2
                    [22, 12, 1, 14],   #a3
                    [31, 10, 6, 18],   #a4
                    [ 8,  9, 0,  9]    #a5
                    ])

    # Parameters
    c_hat = 0.50
    V = [2, 2, 2, 2]
    W = [7, 3, 5, 6]

    # Call Electre I_v Function
    results = score_electre_i_v(dataset, V=V, W=W, remove_cycles=True, c_hat=c_hat, graph=True, verbose=True)

    # Print Results
    for key, value in results.items():
        print(key + ":")
        print(np.round(value, decimals=4))
    ```

    """

    from pyDecision.algorithm import electre_i_v

    # Call Electre I_v Function
    concordance, discordance, dominance, kernel, dominated = electre_i_v(dataset, V=V, W=W,
                                                                         remove_cycles=remove_cycles,
                                                                         c_hat=c_hat, graph=graph)

    # Create a dictionary to store the results
    results = {
        'concordance': concordance,
        'discordance': discordance,
        'dominance': dominance,
        'kernel': kernel,
        'dominated': dominated
    }

    # Print additional information if verbose is True
    if verbose:
        print("Concordance Matrix:")
        print(np.round(concordance, decimals=4))
        print("\nDominance Matrix:")
        print(np.round(dominance, decimals=4))
        print("\nKernel Alternatives:")
        print(kernel)
        print("\nDominated Alternatives:")
        print(dominated)

    return results
