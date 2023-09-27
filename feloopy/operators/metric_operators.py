'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.7)                               |
|  Modified: Wednesday, 27th September 2023 11:38:03 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''

from sklearn import datasets

from tabulate import tabulate
from sklearn.cluster import KMeans
from scipy.spatial import ConvexHull
from scipy.spatial.distance import cdist
import numpy as np

#Validated
def metric_pareto_spm(obtained_pareto):
    """
    Spacing metric (Lower is better)
    --------------------------------
    Calculates the square root of the average of the squared differences between the minimum distance (dm) and the mean distance (d_mean) for each solution.

    Parameters:
    -----------
    obtained_pareto (numpy.ndarray): Numpy array of shape (n, m) representing the Pareto front obtained_pareto, where n is the number of solutions and m is the number of objectives.

    Returns:
    --------
    float: [0,+inf)
    """

    dm = []
    for i in range(len(obtained_pareto)):
        d = [np.linalg.norm(obtained_pareto[i] - obtained_pareto[j]) for j in range(len(obtained_pareto)) if i != j]
        dm.append(min(d))
    d_mean = np.mean(dm)
    spacing = np.sqrt(np.sum((dm - d_mean) ** 2) / len(dm))
    return spacing

