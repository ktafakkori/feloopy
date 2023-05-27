'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

import math as mt

product = mt.prod


def extract_slopes_intercepts(func_str, num_breakpoints, x_range):
    # Evaluate the input function string
    func = eval("lambda x: " + func_str)

    # Calculate the breakpoints based on the range and number of desired breakpoints
    breakpoints = [x_range[0] + i/(num_breakpoints-1) *
                   (x_range[1] - x_range[0]) for i in range(num_breakpoints)]

    # Initialize lists to store slopes and intercepts
    slopes = []
    intercepts = []

    # Calculate the slope and intercept for each breakpoint
    for i in range(num_breakpoints):
        if i == 0:
            x1 = breakpoints[i]
            x2 = breakpoints[i+1]
            slope = (func(x2) - func(x1)) / (x2 - x1)
            intercept = func(x1) - slope * x1
        elif i == num_breakpoints-1:
            x1 = breakpoints[i-1]
            x2 = breakpoints[i]
            slope = (func(x2) - func(x1)) / (x2 - x1)
            intercept = func(x2) - slope * x2
        else:
            x1 = breakpoints[i-1]
            x2 = breakpoints[i]
            slope = (func(x2) - func(x1)) / (x2 - x1)
            intercept = func(x1) - slope * x1
        slopes.append(slope)
        intercepts.append(intercept)

    return breakpoints, slopes, intercepts
