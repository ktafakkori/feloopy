import numpy as np


def rank_promethee_i(Q, S, P, W, F, dataset, show_plot=False):
    """
    Calculates the partial ranking for a given dataset using the Promethee I method.

    Args:
    - Q (list): The preference threshold for indifference.
    - S (list): The preference threshold for preference.
    - P (list): The preference threshold for veto.
    - W (list): The weights of each criterion.
    - F (list): The preference function for each criterion.
    - dataset (numpy.ndarray): The decision matrix to be evaluated.
    - show_plot (bool): Whether to show the Promethee I graph or not.

    Returns:
    - A dictionary containing:
        - 'partial_ranking': The partial ranking for each alternative.
        - 'full_ranking': The full ranking for each alternative (including ties).
    """
    from pyDecision.algorithm import promethee_i

    # Call Promethee I
    ranking = promethee_i(
        dataset, W=W, Q=Q, S=S, P=P, F=F, graph=show_plot)

    # Return results as a dictionary
    return {'ranking': ranking}
