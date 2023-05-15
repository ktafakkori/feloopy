'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-15
 # @ Modified: 2023-05-15
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''


def mcdm_fuzzy_vikor(dataset, weights, criterion_type, strategy_coefficient=0.5, show_graph=False):
    """
    Calculate the scores of alternatives using Fuzzy VIKOR method.

    Args:
    - dataset (list): List of alternative evaluations. Each alternative evaluation is a list of tuples,
                      where each tuple contains the ratings for each criterion.
    - weights (list): List of weights for each criterion. Each weight is a tuple containing the weights for each rating.
    - criterion_type (list): List of criterion types, either 'max' or 'min' for each criterion.
    - strategy_coefficient (float, optional): The strategy coefficient used to calculate the Q values.
    - show_graph (bool, optional): Whether to display a graph for each output.

    Returns:
    - result (dict): A dictionary containing the following keys:
        - s (list): Scores of each alternative.
        - r (list): Ranks of each alternative.
        - q (list): Q values of each alternative.
        - c_solution (list): Final solution using the Fuzzy VIKOR method.

    Example:
    >>> dataset = [
    ...     [(3, 6, 9), (5, 8, 9), (5, 7, 9)],
    ...     [(5, 7, 9), (3, 7, 9), (3, 5, 7)],
    ...     [(5, 8, 9), (3, 5, 7), (1, 2, 3)],
    ...     [(1, 2, 4), (1, 4, 7), (1, 2, 5)]
    ... ]
    >>> weights = [
    ...     [(0.1, 0.2, 0.3), (0.7, 0.8, 0.9), (0.3, 0.5, 0.8)]
    ... ]
    >>> criterion_type = ['max', 'max', 'min']
    >>> result = score_fuzzy_vikor(dataset, weights, criterion_type, strategy_coefficient=0.5, show_graph=True)
    """

    # Required Libraries
    from pyDecision.algorithm import fuzzy_vikor_method, ranking

    # Call Fuzzy VIKOR
    s, r, q, c_solution = fuzzy_vikor_method(
        dataset, weights, criterion_type, strategy_coefficient=strategy_coefficient, graph=show_graph)

    # Graph Solutions
    if show_graph:
        print("----- Scores -----")
        ranking(s)
        print("------------------")
        print("----- Ranks -----")
        ranking(r)
        print("------------------")
        print("----- Q Values -----")
        ranking(q)
        print("------------------")
        print("----- Final Solution -----")
        ranking(c_solution)

    # Return the results in a dictionary
    return {
        's': s,
        'r': r,
        'q': q,
        'c_solution': c_solution
    }