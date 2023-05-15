'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-15
 # @ Modified: 2023-05-15
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

from typing import Dict, Optional
import numpy as np


def score_electre_ii(dataset: np.ndarray, W: np.ndarray, c_minus: float, c_zero: float, c_plus: float,
                     d_minus: float, d_plus: float, graph: Optional[bool] = False,
                     verbose: Optional[bool] = False) -> Dict[str, np.ndarray]:
    """
    This function applies the ELECTRE II algorithm on a given decision matrix, weights, and parameters to obtain the
    concordance matrix, discordance matrix, and dominance matrices. It returns the output in the form of a dictionary.

    :param dataset: A numpy array representing the decision matrix with shape (m, n), where m is the number of
                    alternatives and n is the number of criteria.
    :param W: A numpy array representing the weight vector for each criterion.
    :param c_minus: A float representing the preference threshold for the concordance relation.
    :param c_zero: A float representing the indifference threshold for the concordance relation.
    :param c_plus: A float representing the preference threshold for the discordance relation.
    :param d_minus: A float representing the preference threshold for the negative discordance relation.
    :param d_plus: A float representing the preference threshold for the positive discordance relation.
    :param graph: A boolean representing whether or not to plot the graph of the outranking relation. Default is False.
    :param verbose: A boolean representing whether or not to print the output. Default is False.
    :return: A dictionary containing the following keys:
             - 'concordance': The concordance matrix with shape (m, m).
             - 'discordance': The discordance matrix with shape (m, m).
             - 'dominance_s': The strong dominance matrix with shape (m, m).
             - 'dominance_w': The weak dominance matrix with shape (m, m).
    """

    from pyDecision.algorithm import electre_ii

    concordance, discordance, dominance_s, dominance_w, _, _, _, _ = electre_ii(
        dataset, W=W, c_minus=c_minus, c_zero=c_zero, c_plus=c_plus, d_minus=d_minus, d_plus=d_plus, graph=graph)

    output_dict = {'concordance': np.round(concordance, decimals=4),
                   'discordance': np.round(discordance, decimals=4),
                   'dominance_s': np.round(dominance_s, decimals=4),
                   'dominance_w': np.round(dominance_w, decimals=4)}

    if verbose:
        print('Concordance Matrix:\n', output_dict['concordance'])
        print('Discordance Matrix:\n', output_dict['discordance'])
        print('Strong Dominance Matrix:\n', output_dict['dominance_s'])
        print('Weak Dominance Matrix:\n', output_dict['dominance_w'])

    return output_dict
