'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-15
 # @ Modified: 2023-05-15
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

import numpy as np


def mcdm_electre_i_s(dataset, Q, P, V, W, lambda_value=0.7, graph=False, verbose=False):
    """
    This function calculates the global concordance, discordance, kernel, credibility, and dominated
    matrices using the Electre I_s algorithm and returns them as a dictionary.

    Parameters:
    dataset (np.ndarray): 2D array of shape (n, m) representing the performance table where n is the number of alternatives and m is the number of criteria
    Q (list): list of positive ideal values for each criterion
    P (list): list of negative ideal values for each criterion
    V (list): list of veto thresholds for each criterion
    W (list): list of weights for each criterion
    lambda_value (float): lambda value for the concordance threshold, default is 0.7
    graph (bool): if True, the function will plot the graph of the kernel and dominated sets
    verbose (bool): if True, the function will print the matrices and graphs

    Returns:
    dict: a dictionary containing the global concordance, discordance, kernel, credibility, and dominated matrices
    """
    from pyDecision.algorithm import electre_i_s

    # Call Electre I_s Function
    global_concordance, discordance, kernel, credibility, dominated = electre_i_s(
        dataset, Q=Q, P=P, V=V, W=W, graph=graph, lambda_value=lambda_value)

    # Create dictionary of matrices
    matrices_dict = {
        "global_concordance": global_concordance,
        "discordance": discordance,
        "kernel": kernel,
        "credibility": credibility,
        "dominated": dominated
    }

    # Print matrices
    if verbose:
        print("Global Concordance Matrix:")
        print(np.round(global_concordance, decimals=4))
        print("\nDiscordance Matrix:")
        print(np.round(discordance, decimals=4))
        print("\nCredibility Matrix:")
        print(np.round(credibility, decimals=4))

    return matrices_dict
