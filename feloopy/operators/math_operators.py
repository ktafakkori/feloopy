# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


import math as mt

def extract_slopes_intercepts(func_str, num_breakpoints, x_range):
    # Evaluate the input function string
    func = eval("lambda x: " + func_str)

    # Calculate the breakpoints based on the range and number of desired breakpoints
    breakpoints = [x_range[0] + i/(num_breakpoints-1) * (x_range[1] - x_range[0]) for i in range(num_breakpoints)]

    # Initialize lists to store slopes and intercepts
    slopes = []
    intercepts = []

    # Calculate the slope and intercept for each breakpoint
    for i in range(num_breakpoints - 1):
        x1 = breakpoints[i]
        x2 = breakpoints[i+1]
        slope = (func(x2) - func(x1)) / (x2 - x1)
        intercept = func(x1) - slope * x1
        slopes.append(slope)
        intercepts.append(intercept)

    return breakpoints, slopes, intercepts


import numpy as np


def normalize_array_mean_std(array):
    """
    Normalize a NumPy array between 0 and 1 using mean and standard deviation.

    Parameters:
    - array (numpy.ndarray): The input array to be normalized.

    Returns:
    - numpy.ndarray: The normalized array.

    """
    mean_val = np.mean(array)
    std_val = np.std(array)
    normalized_array = (array - mean_val) / std_val
    return normalized_array


def normalize_array_min_max(array):
    """
    Normalize a NumPy array between 0 and 1 using minimum and maximum values.

    Parameters:
    - array (numpy.ndarray): The input array to be normalized.

    Returns:
    - numpy.ndarray: The normalized array.

    """
    min_val = np.min(array)
    max_val = np.max(array)
    normalized_array = (array - min_val) / (max_val - min_val)
    return normalized_array


def normalize_array_sum(array):
    """
    Normalize a NumPy array by dividing each element by the sum of all elements.

    Parameters:
    - array (numpy.ndarray): The input array to be normalized.

    Returns:
    - numpy.ndarray: The normalized array.

    """
    sum_val = np.sum(array)
    normalized_array = array / sum_val
    return normalized_array
