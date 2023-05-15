

import numpy as np


def consistency_validation(rc, threshold=0.1, verbose=True):
    if (rc > threshold):
        result = 'inconsistent'
        if verbose:
            print('Status: inconsistent')
    else:
        result = 'inconsistent'
        if verbose:
            print('Status: consistent')
    return result


def weight_ahp(dataset, weight_derivation='geometric', verbose=True):
    """
    AHP

    """

    from pyDecision.algorithm import ahp_method
    weights, rc = ahp_method(dataset, wd=weight_derivation)
    if verbose:
        print("~~~~~~~~~~")
        print("AHP Method")
        print("~~~~~~~~~~")
        for i in range(0, weights.shape[0]):
            print('w(g'+str(i+1)+'): ', round(weights[i], 4))
        print('RC: ' + str(round(rc, 4)))
        print("----------")
        consistency_validation(rc)
        print("----------")

    return [weights, rc]


def score_electre_i_s(dataset: np.ndarray, Q: list, P: list, V: list, W: list,
                      lambda_value: float, graph: bool = False) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    This function implements the Electre I_s MCDM algorithm to evaluate a dataset based on decision weights.

    :param dataset: A numpy array representing the dataset to be evaluated.
    :param Q: A list of weights for the quantitative criteria.
    :param P: A list of weights for the qualitative criteria.
    :param V: A list of weights for the veto thresholds.
    :param W: A list of weights for the criteria weights.
    :param lambda_value: A float representing the value of the lambda threshold.
    :param graph: A boolean indicating whether to plot the kernel after evaluation (default False).
    :return: A tuple containing the global concordance matrix, discordance matrix, and credibility matrix.
    """

    from pyDecision.algorithm import electre_i_s

    global_concordance, discordance, kernel, credibility, dominated = electre_i_s(dataset, Q=Q, P=P, V=V, W=W,
                                                                                  graph=graph, lambda_value=lambda_value)
    return np.round(global_concordance, decimals=2), np.round(discordance, decimals=2), np.round(credibility, decimals=2)


def rank_promethee_vi(dataset, W_lower, W_upper, Q, S, P, F, sort=True, topn=10, iterations=1000, graph=False, verbose=False):
    """
    Rank alternatives using Promethee VI algorithm.

    Parameters:
    -----------
    dataset : numpy.ndarray
        A 2D numpy array of shape (n, m) where n is the number of alternatives and m is the number of criteria.
    W_lower : numpy.ndarray
        A 1D numpy array of shape (m,) containing the lower bounds of the weight range for each criterion.
    W_upper : numpy.ndarray
        A 1D numpy array of shape (m,) containing the upper bounds of the weight range for each criterion.
    Q : list
        A list of length m containing the preference threshold for each criterion.
    S : list
        A list of length m containing the indifference threshold for each criterion.
    P : list
        A list of length m containing the preference function parameter for each criterion.
    F : list
        A list of length m containing the preference function type for each criterion. ('t1' = Usual; 't2' = U-Shape; 't3' = V-Shape; 't4' = Level; 't5' = V-Shape with Indifference; 't6' = Gaussian; 't7' = C-Form)
    sort : bool, optional
        Whether to sort the results in descending order. Default is True.
    topn : int
        The number of top alternatives to return. Default is 10.
    iterations : int, optional
        The number of iterations to run the algorithm. Default is 1000.
    graph : bool, optional
        Whether to plot the average difference between two consecutive iterations. Default is False.
    verbose : bool, optional
        Whether to print the ranking results. Default is False.

    Returns:
    --------
    numpy.ndarray
        A 2D numpy array of shape (n, 2) containing the alternative IDs and their corresponding rankings.
    """

    from pyDecision.algorithm import promethee_vi

    p6_minus, p6, p6_plus = promethee_vi(dataset, W_lower=W_lower, W_upper=W_upper,
                                         Q=Q, S=S, P=P, F=F, sort=sort, topn=topn, iterations=iterations, graph=graph)

    rankings = p6
    if verbose:

        print('Rank - Minus(Lower)')
        for i in range(0, p6_minus.shape[0]):
            print('a'+str(int(p6_minus[i, 0])) +
                  ': '+str(round(p6_minus[i, 1], 3)))

        print('Rank (Favorable)')
        for i in range(0, p6.shape[0]):
            print('a'+str(int(p6[i, 0]))+': '+str(round(p6[i, 1], 3)))

        print('Rank - Plus(Upper)')
        for i in range(0, p6_plus.shape[0]):
            print('a'+str(int(p6_plus[i, 0])) +
                  ': '+str(round(p6_plus[i, 1], 3)))

    return rankings


def rank_electre_ii(dataset, W, c_minus, c_zero, c_plus, d_minus, d_plus, verbose=False, show_plot=False):
    """
    Rank alternatives using the ELECTRE II method.

    Parameters
    ----------
    dataset : numpy.ndarray
        A 2D numpy array of shape (n, m) where n is the number of alternatives and m is the number of criteria.
    W : list
        A list of length m containing the weight for each criterion.
    c_minus : float
        The concordance threshold for the 'less important' category.
    c_zero : float
        The concordance threshold for the 'indifference' category.
    c_plus : float
        The concordance threshold for the 'important' category.
    d_minus : float
        The discordance threshold for the 'less important' category.
    d_plus : float
        The discordance threshold for the 'important' category.
    verbose : bool, optional
        Whether to print the ranking results. Default is False.
    show_plot : bool, optional
        Whether to plot the average difference between two consecutive iterations. Default is False.

    Returns
    -------
    numpy.ndarray
        A 2D numpy array of shape (n, 2) containing the alternative IDs and their corresponding rankings.
    """
    from pyDecision.algorithm import electre_ii

    # Call Electre II Function
    concordance, discordance, dominance_s, dominance_w, rank_D, rank_A, rank_N, rank_P = electre_ii(
        dataset, W, c_minus, c_zero, c_plus, d_minus, d_plus, graph=show_plot)

    # Rank - Descending
    rank_D = np.array(rank_D)
    rank_D[:, 1] = rank_D[:, 1].astype(np.float)
    rank_D = rank_D[rank_D[:, 1].argsort()[::-1]]

    # Rank - Ascending
    rank_A = np.array(rank_A)
    rank_A[:, 1] = rank_A[:, 1].astype(np.float)
    rank_A = rank_A[rank_A[:, 1].argsort()]

    # Rank - Partial
    rank_P = np.array(rank_P)
    rank_P = np.concatenate((np.array(
        [['a'+str(i+1), np.nan] for i in range(dataset.shape[0])]), rank_P), axis=1)
    for i in range(rank_P.shape[0]):
        rank_P[i, 1] = np.nanmean(rank_P[i, 1:].astype(np.float))

    # Combine ranks and sort by descending order
    ranks = np.concatenate(
        (rank_D[:, :2], rank_A[:, 1:2], rank_P[:, :2]), axis=0)
    ranks = ranks[ranks[:, 1].argsort()[::-1]]

    if verbose:
        print("Rankings:")
        print("---------")
        for i in range(ranks.shape[0]):
            print(f"{i+1}. {ranks[i, 0]} - {ranks[i, 1]:.3f}")

    return ranks


# Parameters
c_minus = 0.65
c_zero = 0.75
c_plus = 0.85

d_minus = 0.25
d_plus = 0.50

W = [0.0780, 0.1180, 0.1570, 0.3140, 0.2350, 0.0390, 0.0590]

# Dataset
dataset = np.array([
    [1, 2, 1, 5, 2, 2, 4],  # a1
    [3, 5, 3, 5, 3, 3, 3],  # a2
    [3, 5, 3, 5, 3, 2, 2],  # a3
    [1, 2, 2, 5, 1, 1, 1],  # a4
    [1, 1, 3, 5, 4, 1, 5]  # a6
])

# Call rank_electre_ii function
ranks = rank_electre_ii(dataset, W, c_minus, c_zero,
                        c_plus, d_minus, d_plus, verbose=True, show_plot=True)
