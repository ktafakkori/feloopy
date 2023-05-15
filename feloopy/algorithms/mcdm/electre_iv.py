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


def mcdm_electre_iv(dataset, P, Q, V, graph=False, verbose=False):
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
        - 'mcdm_D': the descending ranking of alternatives.
        - 'mcdm_A': the ascending ranking of alternatives.
        - 'mcdm_P': the partial ranking of alternatives.
    """
    from pyDecision.algorithm import electre_iv

    credibility, mcdm_D, mcdm_A, mcdm_N, mcdm_P = electre_iv(
        dataset, P=P, Q=Q, V=V, graph=graph)

    if verbose:
        print("Credibility matrix:")
        print(np.round(credibility, decimals=4))
        print("Descending ranking of alternatives:")
        for i, alt in enumerate(mcdm_D):
            print(f"{i+1}. {alt}")
        print("Ascending ranking of alternatives:")
        for i, alt in enumerate(mcdm_A):
            print(f"{i+1}. {alt}")
        print("Partial ranking of alternatives:")
        for i, alt in enumerate(mcdm_P):
            print(f"a{i+1}. {alt}")

    return {
        'credibility': np.round(credibility, decimals=4),
        'mcdm_D': mcdm_D,
        'mcdm_A': mcdm_A,
        'mcdm_P': mcdm_P
    }
