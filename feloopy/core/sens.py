'''
FelooPy version 0.1.1
Release: 26 October 2022
'''

'''
MIT License

Copyright (c) 2022 Keivan Tafakkori & FELOOP (https://ktafakkori.github.io/)

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

   1. Redistributions of source code must retain the above copyright notice, this list of
      conditions and the following disclaimer.

   2. Redistributions in binary form must reproduce the above copyright notice, this list
      of conditions and the following disclaimer in the documentation and/or other materials
      provided with the distribution.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
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

