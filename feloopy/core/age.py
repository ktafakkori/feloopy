'''
Name: FelooPy
Version: 0.1.11
Contributors: Keivan Tafakkori
Date: 21 November 2022
License: MIT. (For more details please refer to LICENSE.txt file).
Copyright (c) 2022 Keivan Tafakkori & FELOOP (https://ktafakkori.github.io/)
'''


import numpy as np
import math as mt


class singleagent:
    def __init__(self, var_name, val, dim, type=None):
        self.var_name = var_name
        self.val = val
        self.dim = dim
        self.type = type

    def __call__(self, *args):
        if self.type == 'pvar':
            return self.val[sum(args[i]*mt.prod(len(self.dim[j]) for j in range(i+1, len(self.dim))) for i in range(len(self.dim)))]
        elif self.type == 'svar':
            return np.argsort(self.val[sum(args[i]*mt.prod(len(self.dim[j]) for j in range(i+1, len(self.dim))) for i in range(len(self.dim)))])
        else:
            return np.round(self.val[sum(args[i]*mt.prod(len(self.dim[j]) for j in range(i+1, len(self.dim))) for i in range(len(self.dim)))])

    def __getitem__(self, *args):
        if self.type == 'pvar':
            return self.val[sum(args[i]*mt.prod(len(self.dim[j]) for j in range(i+1, len(self.dim))) for i in range(len(self.dim)))]
        elif self.type == 'svar':
            return np.argsort(self.val[sum(args[i]*mt.prod(len(self.dim[j]) for j in range(i+1, len(self.dim))) for i in range(len(self.dim)))])
        else:
            return np.round(self.val[sum(args[i]*mt.prod(len(self.dim[j]) for j in range(i+1, len(self.dim))) for i in range(len(self.dim)))])


class multiagent:
    def __init__(self, var_name, val, dim, type=None):
        self.var_name = var_name
        self.val = val
        self.dim = dim
        self.type = type

    def __call__(self, *args):
        if self.type == 'pvar':
            return self.val[:, sum(args[i]*mt.prod(len(self.dim[j]) for j in range(i+1, len(self.dim))) for i in range(len(self.dim)))]
        elif self.type == 'svar':
            return np.argsort(self.val[:, sum(args[i]*mt.prod(len(self.dim[j]) for j in range(i+1, len(self.dim))) for i in range(len(self.dim)))])
        else:
            return np.round(self.val[:, sum(args[i]*mt.prod(len(self.dim[j]) for j in range(i+1, len(self.dim))) for i in range(len(self.dim)))])

    def __getitem__(self, *args):
        if self.type == 'pvar':
            return self.val[:, sum(args[i]*mt.prod(len(self.dim[j]) for j in range(i+1, len(self.dim))) for i in range(len(self.dim)))]
        elif self.type == 'svar':
            return np.argsort(self.val[:, sum(args[i]*mt.prod(len(self.dim[j]) for j in range(i+1, len(self.dim))) for i in range(len(self.dim)))])
        else:
            return np.round(self.val[:, sum(args[i]*mt.prod(len(self.dim[j]) for j in range(i+1, len(self.dim))) for i in range(len(self.dim)))])
