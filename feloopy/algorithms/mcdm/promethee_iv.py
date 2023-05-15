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


def rank_promethee_iv(dataset, W, Q, S, P, F, sort=True, steps=0.001, topn=10, graph=False, verbose=False):
    """
    Ranks alternatives using the Promethee IV algorithm.

    Args:
    dataset (numpy.ndarray): m x n matrix of m alternatives and n criteria
    W (list): n x 1 vector of weights for each criterion
    Q (list): n x 1 vector of preference function parameters for each criterion
    S (list): n x 1 vector of indifference function parameters for each criterion
    P (list): n x 1 vector of preference threshold function parameters for each criterion
    F (list): n x 1 vector of preference function types for each criterion
    sort (bool, optional): whether to sort the alternatives by their global preference index (default True)
    steps (float, optional): step size for calculating the preference degree matrix (default 0.001)
    topn (int, optional): number of top alternatives to consider when calculating the preference degree matrix (default 10)
    graph (bool, optional): whether to plot the net flow and preference degrees (default False)
    verbose (bool, optional): whether to print the results in a verbose format (default False)

    Returns:
    dict: a dictionary with the following keys:
        - 'ranks': an m x 2 matrix of alternative ranks and scores
        - 'preference_degree': an m x m matrix of pairwise preference degrees between alternatives

    Example:
    >>> import numpy as np
    >>> dataset = np.array([[8.840, 8.790, 6.430, 6.950], [8.570, 8.510, 5.470, 6.910],
    ...                     [7.760, 7.750, 5.340, 8.760], [7.970, 9.120, 5.930, 8.090],
    ...                     [9.030, 8.970, 8.190, 8.100], [7.410, 7.870, 6.770, 7.230]])
    >>> W = [9.00, 8.24, 5.98, 8.48]
    >>> Q = [0.3, 0.3, 0.3, 0.3]
    >>> S = [0.4, 0.4, 0.4, 0.4]
    >>> P = [0.5, 0.5, 0.5, 0.5]
    >>> F = ['t5', 't5', 't5', 't5']
    >>> results = rank_promethee_iv(dataset, W, Q, S, P, F, sort=True, steps=0.001, topn=10, graph=False, verbose=True)
    Ranking Results:
    a5: 1.0
    a1: 0.9926
    a4: 0.9583
    a2: 0.937
    a6: 0.8475
    a3: 0.7649
    """

    from pyDecision.algorithm import promethee_iv

    # Call Promethee IV
    p4 = promethee_iv(dataset, W=W, Q=Q, S=S, P=P, F=F,
                      sort=sort, steps=steps, topn=topn, graph=graph)

    # Create dictionary of results
    ranks = dict()
    for i in range(p4.shape[0]):
        ranks['a' + str(i + 1)] = round(p4[i][1], 4)

    # Print verbose output if requested
    if verbose:
        print("Ranking Results:")
        for key, value in ranks.items():
            print(f"{key}: {value}")

    return {'ranks': p4[:, :2], 'preference_degree': p4[:, 2:]}


def example():
    # Required Libraries
    from pyDecision.algorithm import promethee_iv

    # Parameters
    Q = [0.3, 0.3, 0.3, 0.3]
    S = [0.4, 0.4, 0.4, 0.4]
    P = [0.5, 0.5, 0.5, 0.5]
    W = [9.00, 8.24, 5.98, 8.48]
    # 't1' = Usual; 't2' = U-Shape; 't3' = V-Shape; 't4' = Level; 't5' = V-Shape with Indifference; 't6' = Gaussian; 't7' = C-Form
    F = ['t5', 't5', 't5', 't5']

    # Dataset
    dataset = np.array([
        [8.840, 8.790, 6.430, 6.950],  # a1
        [8.570, 8.510, 5.470, 6.910],  # a2
        [7.760, 7.750, 5.340, 8.760],  # a3
        [7.970, 9.120, 5.930, 8.090],  # a4
        [9.030, 8.970, 8.190, 8.100],  # a5
        [7.410, 7.870, 6.770, 7.230]  # a6
    ])

    # Call Promethee IV
    results = rank_promethee_iv(dataset, W=W, Q=Q, S=S, P=P, F=F,
                                sort=True, steps=0.001, topn=10, graph=True, verbose=True)

    return results


example()
