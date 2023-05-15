'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-15
 # @ Modified: 2023-05-15
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

from pyDecision.algorithm import vikor_method, ranking
import numpy as np


def rank_vikor(weights, criterion_type, dataset, strategy_coefficient=0.5, graph=False, verbose=False):
    """
    This function takes in the weights, criterion_type, and dataset and returns the results of the VIKOR algorithm as a dictionary.

    Args:
    weights (numpy.ndarray): A 2D array of weights for each criterion.
    criterion_type (list): A list of strings where each string is either 'min' or 'max' indicating whether the corresponding criterion is to be minimized or maximized.
    dataset (numpy.ndarray): A 2D array of data where each row represents a decision alternative and each column represents a criterion.
    strategy_coefficient (float, optional): A float value between 0 and 1 that determines the level of optimism/pessimism for the decision maker. Default is 0.5.
    graph (bool, optional): A boolean value that determines whether to plot the ranking graphs. Default is False.
    verbose (bool, optional): A boolean value that determines whether to print the intermediate steps. Default is False.

    Returns:
    dict: A dictionary with keys representing the name of the output and values the value of the outputs. The keys are 's', 'r', 'q', and 'c_solution' representing the values of the s-criterion, r-criterion, q-criterion, and the final solution, respectively.
    """
    from pyDecision.algorithm import vikor_method, ranking

    s, r, q, c_solution = vikor_method(
        dataset, weights, criterion_type, strategy_coefficient=strategy_coefficient, graph=graph)

    if verbose:
        print('-'*40)
        print('VIKOR Results')
        print('-'*40)
        print(f"S-criterion: {s}")
        print(f"R-criterion: {r}")
        print(f"Q-criterion: {q}")
        print(f"Final solution: {c_solution}")
        print('-'*40)

    results = {'s': s, 'r': r, 'q':   q, 'c_solution': c_solution}

    if graph:
        ranking(s)
        ranking(r)
        ranking(q)
        ranking(c_solution)

    return results
