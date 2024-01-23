# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import numpy as np
import pandas as pd
import itertools as it

try:
    from ..extras.operators.data_handler import *
except:
    class FileManager:
        pass

class DataToolkit(FileManager):

    def __init__(self, key=None):
        self.data = dict()
        self.history = dict()
        self.random = np.random.default_rng(key)
        self.criteria_directions = dict()
        self.tstart =self.vstart = self.start
        self.lfe = self.load_from_excel
        
    def __fix_dims(self, dim, is_range=True):
        if dim == 0:
            pass
        elif not isinstance(dim, set):
            if len(dim) >= 1:
                if not isinstance(dim[0], set):
                    if is_range:
                        dim = [range(d) if not isinstance(d, range) else d for d in dim]
                    else:
                        dim = [len(d) if not isinstance(d, int) else d for d in dim]
        return dim

    def alias(self, name, input):        
        if type(input) == str: self.data[name] = self.data[input]
        else: self.data[name] = input
        return self.data[name]

    def set(self, index='', bound=None, step=1, to_list=False):
        if index == '':
            if not to_list: created_set = set(range(bound[0], bound[1] + 1, step))
            else: created_set = list(range(bound[0], bound[1] + 1, step))
        else:
            if bound is not None:
                if not to_list: created_set = set(f'{index}{i}' for i in range(bound[0], bound[1] + 1, step))
                else: created_set = list([f'{index}{i}' for i in range(bound[0], bound[1] + 1, step)])
            elif index:
                if not to_list: created_set = set(f'{index}{i}' for i in range(0, len(index), step))
                else: created_set = list([f'{index}{i}' for i in range(0, len(index), step)])        
        if index != '': self.data[index] = created_set
        return created_set

    def start(self, name, value, direction=None):
        self.criteria_directions[name] = direction
        self.data[name] = [value]

    def update(self, names: list, criteria: list, values: list, compared_with: list):
        xcounter = 0
        for name in names:
            counter = 0
            for criterion in criteria:
                if self.criteria_directions[criterion] == 'max':
                    if compared_with[counter] >= self.data[criterion][-1]:
                        self.data[name] = values[xcounter]
                        self.data[criterion].append(compared_with[counter])
                elif self.criteria_directions[criterion] == 'min':
                    if compared_with[counter] <= self.data[criterion][-1]:
                        self.data[name] = values[xcounter]
                        self.data[criterion].append(compared_with[counter])
                else:
                    self.data[name] = values[xcounter]
                    self.data[criterion].append(compared_with[counter])
                counter += 1
            xcounter += 1
   
    def zeros(self, name, dim=0):
        dim = self.__fix_dims(dim)
        if dim == 0: self.data[name] = np.zeros(1)
        else: self.data[name] = np.zeros(tuple(len(i) for i in dim))
        return self.data[name]

    def ones(self, name, dim=0):
        dim = self.__fix_dims(dim)
        if dim == 0: self.data[name] = np.ones(1)
        else: self.data[name] = np.ones(tuple(len(i) for i in dim))
        return self.data[name]

    def uniform(self, name, dim=0, bound=[0, 1]):
        dim = self.__fix_dims(dim)
        if dim == 0:self.data[name] = self.random.uniform(low=bound[0], high=bound[1])
        else: self.data[name] = self.random.uniform(low=bound[0], high=bound[1], size=[len(i) for i in dim])
        return self.data[name]

    def normal(self, name, dim=0, mu=0, sigma=1):
        dim = self.__fix_dims(dim)
        if dim == 0: self.data[name] = self.random.normal(mu, sigma)
        else: self.data[name] = self.random.normal(mu, sigma, size=[len(i) for i in dim])
        return self.data[name]

    def uniformint(self, name, dim=0, bound=[0, 10]):
        dim = self.__fix_dims(dim)
        if dim == 0: self.data[name] = self.random.integers(low=bound[0], high=bound[1] + 1)
        else: self.data[name] = self.random.integers(low=bound[0], high=bound[1] + 1, size=[len(i) for i in dim])
        return self.data[name]

    def dirichlet(self, name, dim=0, alpha=None):
        dim = self.__fix_dims(dim, is_range=False)
        if dim ==0: self.data[name] = self.random.dirichlet(alpha)
        else: self.data[name] = self.random.dirichlet(alpha,size=dim)
        return self.data[name]

    def exponential(self, name, dim=0, scale=1.0):
        dim = self.__fix_dims(dim, is_range=False)
        if dim == 0: self.data[name] = self.random.exponential(scale)
        else: self.data[name] = self.random.exponential(scale, size=dim)
        return self.data[name]

    def poisson(self, name, dim=0, lam=1):
        dim = self.__fix_dims(dim, is_range=False)
        if dim == 0: self.data[name] = self.random.poisson(lam)
        else: self.data[name] = self.random.poisson(lam, size=dim)
        return self.data[name]

    def gamma(self, name, dim=0, shape=1, scale=1):
        dim = self.__fix_dims(dim, is_range=False)
        if dim == 0: self.data[name] = self.random.gamma(shape, scale)
        else: self.data[name] = self.random.gamma(shape=shape, scale=scale, size=dim)
        return self.data[name]

    def weibull(self, name, dim=0, shape=None, scale=None):
        dim = self.__fix_dims(dim, is_range=False)
        if dim == 0: self.data[name] = self.random.weibull(shape=shape, scale=scale)
        else: self.data[name] = self.random.weibull(shape=shape, scale=scale, size=dim)
        return self.data[name]

    def binomial(self, name, dim=0, n=None, p=None):
        dim = self.__fix_dims(dim, is_range=False)
        if dim == 0: self.data[name] = self.random.binomial(n, p)
        else: self.data[name] = self.random.binomial(n, p, size=dim)
        return self.data[name]

    def geometric(self, name, dim=0, p=None):
        dim = self.__fix_dims(dim, is_range=False)
        if dim == 0: self.data[name] = self.random.geometric(p)
        else: self.data[name] = self.random.geometric(p, size=dim)
        return self.data[name]

    def uniformlist(self, name, dim=0, index_range=[0, 1], from_set=range(0), repetition=False, sorted=True):
        dim = self.__fix_dims(dim)
        if dim == 0:
            if sorted: self.data[name] = np.sort(self.random.choice(from_set, self.random.integers(index_range[0], index_range[1] + 1), replace=repetition))
            else: self.data[name] = self.random.choice(from_set, self.random.integers(index_range[0], index_range[1] + 1), replace=repetition) 
        else:
            if sorted: self.data[name] = [np.sort(self.random.choice(from_set, self.random.integers(index_range[0], index_range[1] + 1), replace=repetition)) for i in dim[0]]
            else: self.data[name] = [self.random.choice(from_set, self.random.integers(index_range[0], index_range[1] + 1), replace=repetition) for i in dim[0]]
        return self.data[name]

    def load_from_excel(self, name: str, dim: list, labels: list, appearance: list, file_name: str):

        if len(appearance) == 2:
            if (appearance[0] == 1 and appearance[1] == 1) or (appearance[0] == 1 and appearance[1] == 0) or (appearance[0] == 0 and appearance[1] == 0) or (appearance[0] == 0 and appearance[1] == 1):
                result = pd.read_excel(file_name, index_col=0, sheet_name=name).to_numpy()
            else:
                parameter = pd.read_excel(file_name, header=[i for i in range(appearance[1])], index_col=[i for i in range(appearance[0])], sheet_name=name)
                created_par = np.zeros(shape=([len(i) for i in dim]))
                for keys in it.product(*dim):
                    try:
                        created_par[keys] = parameter.loc[tuple([labels[i]+str(keys[i]) for i in range(appearance[0])]), tuple([labels[i]+str(keys[i]) for i in range(appearance[0], len(labels))])]
                    except:
                        created_par[keys] = None
                result = created_par
        else:
            par = pd.read_excel(file_name, index_col=0,sheet_name=name).to_numpy()
            result= par.reshape(par.shape[0],)
        self.data[name] = result    
        return self.data[name]
    
data_toolkit = data_utils = data_manager = DataToolkit