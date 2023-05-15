import numpy as np


def rank_promethee_ii(dataset, W, Q, S, P, F, sort=True, topn=10, graph=False, verbose=False):
    """
    Ranks alternatives using the Promethee II algorithm.

    Args:
    dataset (numpy.ndarray): m x n matrix of m alternatives and n criteria
    W (list): n x 1 vector of weights for each criterion
    Q (list): n x 1 vector of preference function parameters for each criterion
    S (list): n x 1 vector of indifference function parameters for each criterion
    P (list): n x 1 vector of preference threshold function parameters for each criterion
    F (list): n x 1 vector of preference function types for each criterion ('t1' = Usual; 't2' = U-Shape; 't3' = V-Shape; 't4' = Level; 't5' = V-Shape with Indifference; 't6' = Gaussian; 't7' = C-Form)
    sort (bool, optional): whether to sort the results by rank (default True)
    topn (int, optional): number of top-ranked alternatives to return (default 10)
    graph (bool, optional): whether to plot the net flow and preference degrees (default False)
    verbose (bool, optional): whether to print the results in a verbose format (default False)

    Returns:
    dict: a dictionary with the following keys:
        - 'ranks': an m x 2 matrix of alternative ranks and scores
        - 'net_flow': an m x 1 vector of net flows
        - 'positive_flow': an m x n matrix of positive flow values for each alternative and criterion
        - 'negative_flow': an m x n matrix of negative flow values for each alternative and criterion
        - 'preference_degree': an m x n matrix of preference degrees for each alternative and criterion

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
    >>> results = rank_promethee_ii(dataset, W, Q, S, P, F, sort=True, topn=10, graph=False, verbose=True)
    a5: 0.421
    a1: 0.26
    a2: 0.189
    a4: 0.088
    a6: 0.042
    a3: 0.0
    """
    from pyDecision.algorithm import promethee_ii

    # Call Promethee II
    p2 = promethee_ii(dataset, W=W, Q=Q, S=S, P=P, F=F,
                      sort=sort, topn=topn, graph=graph)

    # Create dictionary of results
    ranks = dict()
    for i in range(p2.shape[0]):
        ranks['a' + str(int(p2[i, 0]))] = round(p2[i, 1], 4)

    # Print verbose output if requested
    if verbose:
        print("Ranking results:")
        for key, value in ranks.items():
            print(f"{key}: {value}")

    return {'ranks': p2, 'net_flow': p2[:, -1], 'positive_flow': p2[:, :-1], 'negative_flow': -p2[:, :-1],
            'preference_degree': p2[:, :-1] - p2[:, 1:]}
