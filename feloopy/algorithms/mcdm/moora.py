'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-15
 # @ Modified: 2023-05-15
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''


def rank_moora_method(dataset, weights, criterion_type, graph=False):
    """
    Calculates the rank using the MOORA method.

    Parameters:
    -----------
    dataset: array-like, shape(n_samples, n_features)
        Dataset of alternatives
    weights: array-like, shape(n_features,)
        Weights of the criteria
    criterion_type: list, shape(n_features,)
        Type of each criterion. Either "max" or "min".
    graph: bool, optional (default=False)
        Whether to show the ranking graph

    Returns:
    --------
    res: dict
        A dictionary with the rank information

    Example:
    --------
    >>> res = rank_moora_method(dataset, weights, criterion_type, graph=True)
    >>> print(res)
    {'Rank': array([3., 5., 1., 7., 6., 4., 2.]), 'Score': array([0.2435, 0.1919, 0.2679, 0.1222, 0.1483, 0.2142, 0.3915]), 'Weighted Sum': array([0.8396, 0.4116, 1.0367, 0.2767, 0.4462, 0.6516, 0.5838]), 'Normalized Weighted Sum': array([0.6644, 0.3253, 0.8195, 0.219 , 0.353 , 0.5144, 0.4605])}
    """

    # Import necessary libraries
    from pyDecision.algorithm import moora_method

    # Call MOORA Function
    rank = moora_method(dataset, weights, criterion_type, graph=graph)

    # Create dictionary with the outputs
    res = {'Rank': rank[0], 'Score': rank[1],
           'Weighted Sum': rank[2], 'Normalized Weighted Sum': rank[3]}

    return res
