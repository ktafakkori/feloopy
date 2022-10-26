
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