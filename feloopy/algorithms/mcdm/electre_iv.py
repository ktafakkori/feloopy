import numpy as np


def rank_electre_iv(dataset, P, Q, V, graph=False, verbose=False):
    """
    Ranks alternatives using the ELECTRE IV method.

    Parameters
    ----------
    dataset : numpy.ndarray
        The decision matrix with shape (n_alternatives, n_criteria).
    P : list of float
        The weights of the criteria with respect to which minimization is enforced.
    Q : list of float
        The weights of the criteria with respect to which maximization is enforced.
    V : list of float
        The veto thresholds for each criterion.
    graph : bool, optional
        Whether to show the graph. Default is False.
    verbose : bool, optional
        Whether to print additional information. Default is False.

    Returns
    -------
    dict
        A dictionary containing the following keys:
        - 'credibility': the credibility matrix.
        - 'rank_D': the descending ranking of alternatives.
        - 'rank_A': the ascending ranking of alternatives.
        - 'rank_P': the partial ranking of alternatives.
    """
    from pyDecision.algorithm import electre_iv

    credibility, rank_D, rank_A, rank_N, rank_P = electre_iv(
        dataset, P=P, Q=Q, V=V, graph=graph)

    if verbose:
        print("Credibility matrix:")
        print(np.round(credibility, decimals=4))
        print("Descending ranking of alternatives:")
        for i, alt in enumerate(rank_D):
            print(f"{i+1}. {alt}")
        print("Ascending ranking of alternatives:")
        for i, alt in enumerate(rank_A):
            print(f"{i+1}. {alt}")
        print("Partial ranking of alternatives:")
        for i, alt in enumerate(rank_P):
            print(f"a{i+1}. {alt}")

    return {
        'credibility': np.round(credibility, decimals=4),
        'rank_D': rank_D,
        'rank_A': rank_A,
        'rank_P': rank_P
    }


dataset = np.array([
    [15, 80, 60, 30, 60, 50, 60, 70],  # a1
    [25,  0, 40, 30, 40, 40, 50, 140],  # a2
    [25,  0, 50, 30, 40, 40, 50, 140],  # a3
    [25,  0, 50, 30, 50, 40, 70, 140],  # a4
    [25,  0, 50, 30, 50, 40, 50, 140],  # a5
    [15, 20, 50, 30, 50, 60, 60, 100],  # a6
    [15, 80, 50, 50, 40, 90, 60, 100],  # a7
])
P = [20, 20, 20, 20, 20, 20, 20, 20]
Q = [10, 10, 10, 10, 10, 10, 10, 10]
V = [100, 100, 100, 100, 100, 100, 100, 100]

result = rank_electre_iv(dataset, P, Q, V, graph=True, verbose=True)
print(result)
