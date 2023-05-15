from typing import Dict
import numpy as np


def score_electre_i(dataset: np.ndarray, W: list, remove_cycles: bool = True, c_hat: float = 1.0,
                    d_hat: float = 0.4, graph: bool = False, verbose: bool = False) -> Dict[str, any]:
    """
    This function performs the Electre I algorithm on a given dataset and returns the concordance, discordance, dominance,
    kernel, and dominated matrices as a dictionary.

    Args:
    - dataset (np.ndarray): The decision matrix with shape (alternatives, criteria).
    - W (list): The weights for the criteria. A list with length equal to the number of criteria.
    - remove_cycles (bool): Whether or not to remove the cycles in the outranking relation. Defaults to True.
    - c_hat (float): The threshold for concordance. Defaults to 1.0.
    - d_hat (float): The threshold for discordance. Defaults to 0.4.
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
                    [1, 2, 1, 5, 2, 2, 4],   #a1
                    [3, 5, 3, 5, 3, 3, 3],   #a2
                    [3, 5, 3, 5, 3, 2, 2],   #a3
                    [1, 2, 2, 5, 1, 1, 1],   #a4
                    [1, 1, 3, 5, 4, 1, 5]    #a5
                    ])

    # Parameters
    c_hat = 1.00
    d_hat = 0.40
    W = [0.0780, 0.1180, 0.1570, 0.3140, 0.2350, 0.0390, 0.0590]

    # Call Electre I Function
    results = score_electre_i(dataset, W=W, remove_cycles=True, c_hat=c_hat, d_hat=d_hat, graph=True, verbose=True)

    # Print Results
    for key, value in results.items():
        print(key + ":")
        print(np.round(value, decimals=4))
    ```

    """

    from pyDecision.algorithm import electre_i

    # Call Electre I Function
    concordance, discordance, dominance, kernel, dominated = electre_i(
        dataset, W=W, remove_cycles=remove_cycles, c_hat=c_hat, d_hat=d_hat, graph=graph
    )

    # Print Results
    if verbose:
        print("Concordance Matrix:")
        print(np.round(concordance, decimals=4))
        print("\nDiscordance Matrix:")
        print(np.round(discordance, decimals=4))
        print("\nDominance Matrix:")
        print(np.round(dominance, decimals=4))
        print("\nKernel of Outranking Relation:")
        print(kernel)
        print("\nAlternatives that are Dominated:")
        print(dominated)

    # Return Results as a Dictionary
    return {"concordance": concordance, "discordance": discordance, "dominance": dominance, "kernel": kernel, "dominated": dominated}
