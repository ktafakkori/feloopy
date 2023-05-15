'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-15
 # @ Modified: 2023-05-15
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''


def mcdm_fuzzy_topsis(weights, criterion_type, dataset, graph=False):
    """
    Ranks alternatives based on Fuzzy TOPSIS method.

    Args:
    weights (list of list): A list of decision matrix with weights for each criterion.
    criterion_type (list of str): A list of 'max' or 'min' values representing the type of optimization for each criterion. 
    dataset (list of list): A list of decision matrix.
    graph (bool, optional): A flag to enable/disable the plot. Default to False.

    Returns:
    dict: A dictionary containing the rank of each alternative.

    """
    from pyDecision.algorithm import fuzzy_topsis_method

    relative_closeness = fuzzy_topsis_method(
        dataset, weights, criterion_type, graph=graph)
    result = {}
    for i in range(0, relative_closeness.shape[0]):
        result['a'+str(i+1)] = round(relative_closeness[i], 4)
    return result
