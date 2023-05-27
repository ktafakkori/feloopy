from sklearn import datasets

from tabulate import tabulate
from sklearn.cluster import KMeans
from scipy.spatial import ConvexHull
from scipy.spatial.distance import cdist
import numpy as np


def metric_pareto_epm(obtained_pareto, ideal_pareto, epsilon):
    """
    Epsilon Metric:
    ---------------
    Checks if the obtained Pareto front is within the specified epsilon distance of the ideal Pareto front. 1 is better.

    Parameters:
    -----------
    obtained_pareto (numpy.ndarray): Numpy array of shape (n, m) representing the obtained Pareto front, where n is the number of solutions and m is the number of objectives.
    ideal_pareto (numpy.ndarray): Numpy array of shape (k, m) representing the ideal Pareto front, where k is the number of points on the front.
    epsilon (float): Threshold distance from the ideal Pareto front that the obtained Pareto front must be within.

    Returns:
    --------
    bool: True or False
    """
    for a in obtained_pareto:
        print(a)
    
    for a in ideal_pareto:
        print(a)

    distances = [np.min([np.linalg.norm(a - r) for r in ideal_pareto]) for a in obtained_pareto]
    if np.max(distances) <= epsilon:
        return 1
    else:
        return 0

def metric_pareto_r2m(obtained_pareto, ideal_pareto):
    """
    R2 Metric:
    ----------
    Measures the proportion of the variation in the objective space that is explained by the obtained Pareto front. Higher values are better.

    Parameters:
    -----------
    obtained_pareto (numpy.ndarray): Numpy array of shape (n, m) representing the obtained Pareto front, where n is the number of solutions and m is the number of objectives.
    ideal_pareto (numpy.ndarray): Numpy array of shape (k, m) representing the ideal Pareto front, where k is the number of points on the front.

    Returns:
    --------
    float: [0,1]
    """
    y_mean = np.mean(ideal_pareto, axis=0)
    ss_tot = np.sum(np.square(ideal_pareto - y_mean))
    ss_res = np.sum(np.square(obtained_pareto - ideal_pareto))
    r2 = 1 - (ss_res / ss_tot)
    return r2


def metric_pareto_frm(obtained_pareto, ideal_pareto):
    """
    F-ratio Metric
    --------------
    Measures the ratio of the average distance between solutions in the obtained_pareto and the average
    distance between solutions on the ideal Pareto front. Higher is better.

    Parameters:
    -----------
    obtained_pareto (numpy.ndarray): Numpy of shape (n, m) representing the Pareto front obtained_pareto, where n is the number of solutions and m is thenumber of objectives.
    ideal_pareto (numpy.ndarray): Numpy array of shape (k, m) representing the ideal Pareto front, where k is the number of points on the front.

    Returns:
    --------
    float: [0,1]
    """
    d_approx = np.mean([np.linalg.norm(a1 - a2) for i, a1 in enumerate(obtained_pareto) for a2 in obtained_pareto[i+1:]])
    d_ideal = np.mean([np.linalg.norm(a1 - a2) for i, a1 in enumerate(ideal_pareto) for a2 in ideal_pareto[i+1:]])
    return d_approx / d_ideal


def metric_pareto_gdm(obtained_pareto, ideal_pareto):
    """
    Generational Distance Metric:
    -----------------------------
    Measures the average distance between the solutions in the obtained Pareto and the ideal Pareto front. Lower values are better.

    Parameters:
    -----------
    obtained_pareto (numpy.ndarray): Numpy array of shape (n, m) representing the Pareto front obtained_pareto, where n is the number of solutions and m is the number of objectives.
    ideal_pareto (numpy.ndarray): Numpy array of shape (k, m) representing the ideal Pareto front, where k is the number of points on the front.

    Returns:
    --------
    float: [0,+inf)
    """

    distances = cdist(obtained_pareto, ideal_pareto)
    return np.mean(np.min(distances, axis=1))


def metric_pareto_gpm(obtained_pareto, ideal_pareto, p):
    """
    Weighted Generational Distance Metric:
    --------------------------------------
    Assigns more weight to solutions that are closer to the ideal Pareto front. Lower values are better.

    Parameters:
    -----------
    obtained_pareto (numpy.ndarray): Numpy array of shape (n, m) representing the Pareto front obtained_pareto, where n is the number of solutions and m is the number of objectives.
    ideal_pareto (numpy.ndarray): Numpy array of shape (k, m) representing the ideal Pareto front, where k is the number of points on the front.
    p (float): A parameter that controls the weighting of solutions that are closer to the ideal Pareto front. A larger value of p assigns more weight to these solutions.

    Returns:
    --------
    float: [0,+inf)
    """

    distances = cdist(obtained_pareto, ideal_pareto)
    return np.mean(np.min(distances, axis=1) ** p) ** (1/p)


def metric_pareto_igd(obtained_pareto, ideal_pareto):
    """

    Inverted Generational Distance:
    -------------------------------
    Measures the average distance between the solutions on the ideal Pareto front and the closest solution in the obtained Pareto. Lower values are better.

    Parameters:
    -----------
    obtained_pareto (numpy.ndarray): Numpy array of shape (n, m) representing the Pareto front obtained_pareto, where n is the number of solutions and m is the number of objectives.
    ideal_pareto (numpy.ndarray): Numpy array of shape (k, m) representing the ideal Pareto front, where k is the number of points on the front.

    Returns:
    --------
    float:  [0,+inf)
    """

    distances = cdist(obtained_pareto, ideal_pareto)
    return np.mean(np.min(distances, axis=0))


def metric_pareto_igdp(obtained_pareto, ideal_pareto, p):
    """
    Weighted Inverted Generational Distance Metric:
    -----------------------------------------------
    Assigns more weight to solutions that are closer to the ideal Pareto front. Lower values are better.

    Parameters:
    -----------
    obtained_pareto (numpy.ndarray): Numpy array of shape (n, m) representing the Pareto front obtained_pareto, where n is the number of solutions and m is the number of objectives.
    ideal_pareto (numpy.ndarray): Numpy array of shape (k, m) representing the ideal Pareto front, where k is the number of points on the front.
    p (float): A parameter that controls the weighting of solutions that are closer to the ideal Pareto front. A larger value of p assigns more weight to these solutions.

    Returns:
    --------
    float: [0,+inf)
    """

    distances = cdist(obtained_pareto, ideal_pareto)
    return np.mean(np.min(distances, axis=0) ** p) ** (1/p)


def metric_pareto_msm(obtained_pareto):
    """
    Maximum Spread Metric:
    ----------------------
    Measures the maximum distance between any two solutions in the obtained_pareto. Higher values are better.

    Parameters:
    -----------
    obtained_pareto (numpy.ndarray): Numpy array containing the Pareto front, where each row represents a solution and each column represents an objective.

    Returns:
    --------
    float: [0,+inf)
    """

    min_values = np.min(obtained_pareto, axis=0)
    max_values = np.max(obtained_pareto, axis=0)
    ranges = max_values - min_values
    max_range = np.max(ranges)
    return max_range


def metric_pareto_spm(obtained_pareto):
    """
    Spacing metric:
    ---------------
    Measures the average distance between each solution in the obtained Pareto and its two nearest neighbors. Higher values are better.

    Parameters:
    -----------
    obtained_pareto (numpy.ndarray): Numpy array of shape (n, m) representing the Pareto front obtained_pareto, where n is the number of solutions and m is the number of objectives.

    Returns:
    --------
    float: [0,+inf)
    """
    distances = []
    for i in range(len(obtained_pareto)):
        d = [np.linalg.norm(obtained_pareto[i]-obtained_pareto[j])
             for j in range(len(obtained_pareto)) if i != j]
        d.sort()
        distances.append(sum(d[:2]))
    spacing = sum(distances) / len(distances)
    return spacing


def metric_pareto_hvm(pareto_front, ideal_pareto):
    """
    Hypervolume Metric:
    -------------------
    Measures the volume of the objective space that is dominated by the obtained Pareto, relative to the volume dominated by the ideal Pareto front. Higher values are better.

    Parameters:
    -----------
    pareto_front (numpy.ndarray): Numpy array of shape (n, m) representing the Pareto front obtained_pareto, where n is the number of solutions and m is the number of objectives.
    ideal_pareto (numpy.ndarray): Numpy array of shape (k, m) representing the ideal Pareto front, where k is the number of points on the front.

    Returns:
    --------
    float: [0, +inf)
    """
    from pyMultiobjective.util import indicators

    parameters = {
        'solution': pareto_front,
        'n_objs': np.shape(pareto_front)[1],
        'ref_point': ideal_pareto,
    }

    return indicators.hv_indicator(**parameters)


def metric_pareto_rsm(obtained_pareto, ideal_pareto):
    """
    Spread Metric:
    -------------- 
    Calculates the average Euclidean distance between each point in the obtained_pareto and its nearest neighbor in the ideal Pareto front. Higher values are better.

    Parameters:
    -----------
    obtained_pareto (list): A list of tuples representing the obtained_pareto of the Pareto front.
    ideal_pareto (list): A list of tuples representing the ideal Pareto front.

    Returns:
    --------
    float: [0, +inf)
    """
    distances = []
    for point in obtained_pareto:
        nearest_neighbor = min(
            [((point[0]-p[0])**2 + (point[1]-p[1])**2)**0.5 for p in ideal_pareto])
        distances.append(nearest_neighbor)
    return sum(distances) / len(distances)


def metric_pareto_kdm(obtained_pareto, ideal_pareto, n_clusters=5):
    """
    Knee Point Distance Metric:
    ---------------------------
    Computes the distances between the centroids and the nearest points on the ideal Pareto and approximated fronts, and uses these distances to find the knee points of the fronts. Then, it computes the KPD as the Euclidean distance between the knee points. Lower values are better.

    Parameters:
        ideal_pareto (np.ndarray): A 2D numpy array containing the objective function values of the ideal_pareto Pareto front.
        obtained_pareto (np.ndarray): A 2D numpy array containing the objective function values of the approximated Pareto front.
        n_clusters (int): The number of clusters to use in the K-means algorithm. Default is 5.

    Returns:
        float:[0, +inf)
    """

    pareto_front = np.vstack((ideal_pareto, obtained_pareto))
    km = KMeans(n_clusters=n_clusters).fit(pareto_front)
    centroids = km.cluster_centers_
    ref_distances = cdist(ideal_pareto, centroids)
    approx_distances = cdist(obtained_pareto, centroids)
    min_ref_distances = np.min(ref_distances, axis=0)
    min_approx_distances = np.min(approx_distances, axis=0)
    ref_knee_point = ideal_pareto[np.argmax(min_ref_distances)]
    approx_knee_point = obtained_pareto[np.argmax(min_approx_distances)]
    kpd = np.linalg.norm(ref_knee_point - approx_knee_point)

    return kpd


def metric_pareto_cvm(obtained_pareto, ideal_pareto):
    """
    Convergence Metric:
    -------------------
    Calculates the average Euclidean distance between each point in the ideal Pareto front and its nearest neighbor in the obtained_pareto. Lower values are better.

    Parameters:
    obtained_pareto (list): A list of tuples representing the obtained_pareto of the Pareto front.
    ideal_pareto (list): A list of tuples representing the ideal Pareto front.

    Returns:
    float: [0,+inf)
    """
    distances = []
    for point in ideal_pareto:
        nearest_neighbor = min(
            [((point[0]-p[0])**2 + (point[1]-p[1])**2)**0.5 for p in obtained_pareto])
        distances.append(nearest_neighbor)
    return sum(distances) / len(distances)


def metric_pareto_mem(ideal_pareto, obtained_pareto):
    """
    Maximum Pareto Front Error Metric:
    ----------------------------------
    Calculates the maximum Pareto front error between the ideal Pareto front and the approximated Pareto front as the maximum of the minimum distances between each point in the approximated Pareto front and its nearest neighbor in the ideal Pareto front.

    Parameters:
        ideal_pareto (np.ndarray): A 2D numpy array containing the objective function values of the ideal_pareto Pareto front.
        obtained_pareto (np.ndarray): A 2D numpy array containing the objective function values of the approximated Pareto front.

    Returns:
        mpe (float): The maximum Pareto front error between the ideal_pareto Pareto front and the approximated Pareto front.
    """

    distances = cdist(ideal_pareto, obtained_pareto)
    mpe = np.max(np.min(distances, axis=0))
    return mpe


def metric_pareto_crm(ideal_pareto, obtained_pareto):
    """
    Coverage Ratio Metric
    ---------------------
    Calculates the Coverage Ratio Metric between the ideal Pareto front and the approximated Pareto front as the percentage of points in the ideal Pareto front that are covered by the approximated Pareto front.

    Parameters:
        ideal_pareto (np.ndarray): A 2D numpy array containing the objective function values of the ideal_pareto Pareto front.
        obtained_pareto (np.ndarray): A 2D numpy array containing theobjective function values of the approximated Pareto front.

    Returns:
        cr (float): A percentage.
    """
    distances = cdist(ideal_pareto, obtained_pareto)
    min_distances = np.min(distances, axis=1)
    cr = 100 * np.sum(min_distances <= 0) / ideal_pareto.shape[0]
    return cr


def metric_pareto_aem(ideal_pareto, obtained_pareto):
    """
    Calculates the additive epsilon indicator (AEI) between the ideal Pareto front and the approximated Pareto front as the sum of the maximum deviations in each objective of the approximated Pareto front from the ideal Pareto front.

    Parameters:
        ideal_pareto (np.ndarray): A 2D numpy array containing the objective function values of the ideal_pareto Pareto front.
        obtained_pareto (np.ndarray): A 2D numpy array containing the objective function values of the approximated Pareto front.

    Returns:
        aei (float): The additive epsilon indicator between the ideal_pareto Pareto front and the approximated Pareto front.
    """
    aei = np.max(np.abs(ideal_pareto - obtained_pareto), axis=0)
    aei = np.sum(aei)
    return aei

def metric_pareto_qvm(obtained_pareto, ideal_pareto):
    """
    Quantity metric:
    ----------------
    Calculates the ratio of the number of solutions in the obtained_pareto that exist in the ideal Pareto front to the total number of solutions in the obtained_pareto.

    Parameters:
    obtained_pareto (list): A list of tuples representing the obtained_pareto of the Pareto front.
    ideal_pareto (list): A list of tuples representing the ideal Pareto front.

    Returns:
    float: [0,1]

    Higher is better.
    """
    count = sum([1 for p in obtained_pareto if p in ideal_pareto])
    return count / len(obtained_pareto)
