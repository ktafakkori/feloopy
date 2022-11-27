'''
Name: FelooPy
Version: 0.1.11
Contributors: Keivan Tafakkori
Date: 21 November 2022
License: MIT. (For more details please refer to LICENSE.txt file).
Copyright (c) 2022 Keivan Tafakkori & FELOOP (https://ktafakkori.github.io/)
'''


import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate as tb

def variate(input, rangeofchange, stepofchange):
    param = []
    original = np.asarray(input)
    diff = rangeofchange[1]-rangeofchange[0]
    percentage = []
    for i in range(diff//stepofchange+1):
        percentage.append(rangeofchange[0])
        param.append(original*(1+rangeofchange[0]/100))
        rangeofchange[0] = rangeofchange[0]+stepofchange
    return param, percentage

def sensitivity(modelfunc, input, rangeofchange, stepofchange=1, table=True, plot=False):
    param, percentage = variate(input, rangeofchange, stepofchange)
    objvals = []
    for member in param:
        param = member
        m = modelfunc(param)
        objvals.append(m.get_obj())
    
    x = percentage
    y = objvals

    if table:
        print()
        print("SENSITIVITY ANALYSIS \n --------")
        print(
            tb({
                "% change": x,
                "objective value": y
            },
                headers="keys", tablefmt="github"))
        print()

    if plot:
        plt.rcParams['figure.dpi'] = 1200
        default_x_ticks = range(len(x))
        plt.xlabel('% Change', size=12)
        plt.ylabel('Objective value', size=12)
        plt.plot(default_x_ticks, y)
        plt.scatter(default_x_ticks, y)
        plt.xticks(default_x_ticks, x)
        plt.show()

