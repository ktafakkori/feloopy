from typing import Dict
import numpy as np


def rank_electre_tri_b(dataset: np.ndarray, W: list, Q: list, P: list, V: list, B: list, cut_level: float = 0.75,
                       verbose: bool = False, rule: str = 'oc', graph: bool = False) -> Dict[str, any]:
    """
    This function performs the Electre Tri-B algorithm on a given dataset and returns the classification as a dictionary.

    Args:
    - dataset (np.ndarray): The decision matrix with shape (alternatives, criteria).
    - W (list): The preference weights for the criteria. A list with length equal to the number of criteria.
    - Q (list): The veto thresholds for the criteria. A list with length equal to the number of criteria.
    - P (list): The preference thresholds for the criteria. A list with length equal to the number of criteria.
    - V (list): The thresholds for the criteria. A list with length equal to the number of criteria.
    - B (list): The indifference and preference thresholds for the criteria. A list with shape (2, criteria).
    - cut_level (float): The cut level of the classification. Defaults to 0.75.
    - verbose (bool): Whether or not to print additional information to the console. Defaults to False.
    - rule (str): The decision rule to be used. Can be either 'oc' (ordered classification) or 'c' (cardinal ranking).
                  Defaults to 'oc'.
    - graph (bool): Whether or not to show the graph of the outranking relation. Defaults to False.

    Returns:
    - A dictionary containing the following keys:
        - 'classification': The classification of the alternatives according to the Electre Tri-B algorithm.

    Example Usage:
    ```
    # Required Libraries
    import numpy as np

    # Dataset
    dataset = np.array([
                    [75, 67, 85, 82, 90],   #a1
                    [28, 35, 70, 90, 95],   #a2
                    [45, 60, 55, 68, 60]    #a3
                    ])

    # Parameters 
    Q = [ 5,  5,  5,  5,  5]
    P = [10, 10, 10, 10, 10]
    V = [30, 30, 30, 30, 30]
    W = [ 1,  1,  1,  1,  1]
    B = [[50, 48, 55, 55, 60], [70, 75, 80, 75, 85]]

    # Call Electre Tri-B Function
    results = rank_electre_tri_b(dataset, W=W, Q=Q, P=P, V=V, B=B, cut_level=0.75, verbose=True, rule='oc', graph=True)

    # Print Results
    print("Classification:")
    print(results['classification'])
    ```

    """

    from pyDecision.algorithm import electre_tri_b

    # Call Electre Tri-B Function
    classification = electre_tri_b(dataset, W=W, Q=Q, P=P, V=V, B=B, cut_level=cut_level, verbose=verbose, rule=rule,
                                   graph=graph)

    # Create a dictionary to store the results
    results = {
        'classification': classification
    }

    return results
