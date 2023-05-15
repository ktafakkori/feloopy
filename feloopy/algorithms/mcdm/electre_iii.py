from typing import Dict
import numpy as np


def rank_electre_iii(dataset: np.ndarray, P: list, Q: list, V: list, W: list, graph: bool = False, verbose: bool = False) -> Dict[str, any]:
    """
    This function performs the Electre III algorithm on a given dataset and returns the global concordance, credibility, rank_D,
    rank_A, and rank_P matrices as a dictionary.

    Args:
    - dataset (np.ndarray): The decision matrix with shape (alternatives, criteria).
    - P (list): The preference thresholds for the concordance indices. A list with length equal to the number of criteria.
    - Q (list): The indifference thresholds for the concordance indices. A list with length equal to the number of criteria.
    - V (list): The veto thresholds for the discordance indices. A list with length equal to the number of criteria.
    - W (list): The weights for the criteria. A list with length equal to the number of criteria.
    - graph (bool): Whether or not to show the graph of the outranking relation. Defaults to False.
    - verbose (bool): Whether or not to print additional information to the console. Defaults to False.

    Returns:
    - A dictionary containing the following keys:
        - 'global_concordance': The global concordance matrix.
        - 'credibility': The credibility matrix.
        - 'rank_D': The descending ranking of the alternatives.
        - 'rank_A': The ascending ranking of the alternatives.
        - 'rank_P': The partial ranking of the alternatives.

    Example Usage:
    ```
    # Required Libraries
    import numpy as np

    # Dataset
    dataset = np.array([
                    [8.84, 8.79, 6.43, 6.95],   #a1
                    [8.57, 8.51, 5.47, 6.91],   #a2
                    [7.76, 7.75, 5.34, 8.76],   #a3
                    [7.97, 9.12, 5.93, 8.09],   #a4
                    [9.03, 8.97, 8.19, 8.10],   #a5
                    [7.41, 7.87, 6.77, 7.23]    #a6
                    ])

    # Parameters
    Q = [0.30, 0.30, 0.30, 0.30]
    P = [0.50, 0.50, 0.50, 0.50]
    V = [0.70, 0.70, 0.70, 0.70]
    W = [9.00, 8.24, 5.98, 8.48]

    # Call Electre III Function
    results = rank_electre_iii(dataset, P=P, Q=Q, V=V, W=W, graph=True, verbose=True)
    ```
    """

    from pyDecision.algorithm import electre_iii
    global_concordance, credibility, rank_D, rank_A, rank_N, rank_P = electre_iii(
        dataset, P=P, Q=Q, V=V, W=W, graph=graph)

    results = {
        'global_concordance': np.round(global_concordance, decimals=4),
        'credibility': np.round(credibility, decimals=4),
        'rank_D': rank_D,
        'rank_A': rank_A,
        'rank_N': rank_N,
        'rank_P': rank_P
    }

    if verbose:
        print(f"Global Concordance Matrix:\n{results['global_concordance']}\n")
        print(f"Credibility Matrix:\n{results['credibility']}\n")
        print("Rank - Descending")
        for i, alt in enumerate(results['rank_D']):
            print(f"{i+1}. {alt}")
        print("\nRank - Ascending")
        for i, alt in enumerate(results['rank_A']):
            print(f"{i+1}. {alt}")
        print("\nRank - Partial")
        for i, alt in enumerate(results['rank_P']):
            print(f"a{i+1}: {alt}")

    return results


# Dataset
dataset = np.array([
    [8.84, 8.79, 6.43, 6.95],  # a1
    [8.57, 8.51, 5.47, 6.91],  # a2
    [7.76, 7.75, 5.34, 8.76],  # a3
    [7.97, 9.12, 5.93, 8.09],  # a4
    [9.03, 8.97, 8.19, 8.10],  # a5
    [7.41, 7.87, 6.77, 7.23]  # a6
])

# Parameters
Q = [0.30, 0.30, 0.30, 0.30]
P = [0.50, 0.50, 0.50, 0.50]
V = [0.70, 0.70, 0.70, 0.70]
W = [9.00, 8.24, 5.98, 8.48]

# Call Electre III Function
results = rank_electre_iii(dataset, P=P, Q=Q, V=V,
                           W=W, graph=True, verbose=True)
