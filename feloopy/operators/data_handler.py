# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import numpy as np
import pandas as pd
import itertools as it
import numpy as np
import pandas as pd
import polars as pl

try:
    from ..extras.operators.data_handler import *
except:

    class FileManager:
        pass


class DataToolkit(FileManager):

    def __init__(self, key=None, memorize=True):
        
        self.data = dict()
        self.history = dict()
        self.seed= key
        self.random = np.random.default_rng(key)
        self.criteria_directions = dict()
        self.tstart = self.vstart = self.start
        self.lfe = self.load_from_excel
        self.memorize=memorize
        self.gaussian = self.normal
        
        self.store = self.__keep

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
    
    def __keep(self, name, value, neglect=False):
        if self.memorize and neglect==False:
            self.data[name]=value
            return self.data[name]
        elif neglect:
            return value
        else:
            return value
    
    ## Sets
     
    def _convert_to_set(self, input_set):
        if isinstance(input_set, set):
            return input_set
        elif isinstance(input_set, range):
            return set(input_set)
        elif isinstance(input_set, list):
            return set(input_set)
        else:
            raise TypeError("Unsupported set type")

    def set(
        self,
        name,
        bound=None,
        step=1,
        callback=None,
        to_list=False,
        to_range=False,
        named_indices=False,
        size=None,
        init=None,
        axis=0,
        neglect=False):
        
        if size is not None:
            if to_range:
                result = range(size)
            else:
                result = set(range(size))
        elif init is not None:
            
            if type(init)==int:
                if to_range:
                    result = range(init)
                else:
                    result = set(range(init))
            elif type(init)==np.ndarray:
                if to_range:
                    result = range(np.shape(init)[axis])
                else:
                    result = set(range(np.shape(init)[axis]))

            elif type(init)==list:
                if to_range:
                    result = range(len(list))
                else:
                    result = set(range(len(list)))
            else:
                try:
                    result = set(init)
                except:
                    result = init 
        else:   
            if callback:
                named_indices = False
            if to_range:
                result = range(bound[0], bound[1] + 1, step)
            elif named_indices:
                result = {f"{name.lower()}{i}" for i in range(bound[0], bound[1] + 1, step) if not callback or callback(i)}
            else:
                if callback:
                    result =  set(item for item in range(bound[0], bound[1] + 1, step) if callback(item))
                else:
                    result =  set(range(bound[0], bound[1] + 1, step))
        if to_list:
            result = list(result)
        
        return self.__keep(name, result, neglect)
    

    def alias(self, name, init, neglect=False):
        result=init
        return self.__keep(name, result, neglect)

    def union(self, name, *sets, neglect=False):
        converted_sets = [self._convert_to_set(s) for s in sets]
        result=  set().union(*converted_sets)
        return self.__keep(name, result, neglect)

    def intersection(self, name, *sets, neglect=False):
        converted_sets = [self._convert_to_set(s) for s in sets]
        result = set().intersection(*converted_sets)
        return self.__keep(name, result, neglect)

    def difference(self,name, *sets, neglect=False):
        converted_sets = [self._convert_to_set(s) for s in sets]
        result = converted_sets[0]
        for s in converted_sets[1:]:
            result = result.difference(s)
        return self.__keep(name, result, neglect)

    def symmetric_difference(self,name, *sets, neglect=False):
        converted_sets = [self._convert_to_set(s) for s in sets]
        result = converted_sets[0]
        for s in converted_sets[1:]:
            result = result.symmetric_difference(s)
        return self.__keep(name, result, neglect)

    ## Parameters

    def _sample_list_or_array(self, name, init, size, replace=False, sort_result=False, return_indices=False, axis=None):
        if isinstance(init, (list, range)):
            init = np.array(init)

        if axis is None:
            sampled_indices = self.random.choice(init.size, size=size, replace=replace)
        else:
            axis = np.atleast_1d(axis)
            axis_size = init.shape[axis[0]] if len(axis) == 1 else np.prod([init.shape[i] for i in axis])
            sampled_indices = self.random.choice(axis_size, size=size, replace=replace)

        if return_indices:
            if sort_result:
                sampled_indices.sort()
            self.data[name] = sampled_indices
        else:
            sampled_data = init.flat[sampled_indices] if axis is None else np.take(init, sampled_indices, axis=axis)
            if sort_result:
                sampled_data.sort()
            self.data[name] = sampled_data

        return self.data[name]

    def _sample_pandas_dataframe(self, name, init, size, replace=False, sort_result=False, return_indices=False, axis=None):
        axis = 0 if axis is None else axis 

        if axis not in [0, 1]:
            raise ValueError("Invalid axis for Pandas DataFrame sampling. Supported axes: 0 (rows), 1 (columns)")

        sampled_indices = self.random.choice(init.shape[axis], size=size, replace=replace)

        if return_indices:
            self.data[name] = sampled_indices
        else:
            if axis == 0:
                sampled_data = init.iloc[sampled_indices, :]
            else:
                sampled_data = init.iloc[:, sampled_indices]

            if sort_result:
                sampled_data = sampled_data.sort_index(axis=axis)

            self.data[name] = sampled_data

        return self.data[name]
       
    def zeros(self, name, dim=0, neglect=False):
        dim = self.__fix_dims(dim)
        if dim == 0:
            result = np.zeros(1)
        else:
            result = np.zeros(tuple(len(i) for i in dim))
        return self.__keep(name, result, neglect)

    def ones(self, name, dim=0, neglect=False):
        dim = self.__fix_dims(dim)
        if dim == 0:
            result = np.ones(1)
        else:
            result = np.ones(tuple(len(i) for i in dim))
        return self.__keep(name, result, neglect)

    def uniformint(self, name, dim=0, bound=[1, 10], result=None, neglect=False):
        dim = self.__fix_dims(dim)
        if dim == 0:
            result = self.random.integers(low=bound[0], high=bound[1] + 1)
        else:
            result = self.random.integers(low=bound[0], high=bound[1] + 1, size=[len(i) for i in dim])
        return self.__keep(name, result, neglect)
    
    def bernoulli(self, name, dim=0, p=0.5, result=None, neglect=False):
        dim = self.__fix_dims(dim)
        if dim == 0:
            result = self.random.choice([0, 1], p=[1-p, p])
        else:
            result = self.random.choice([0, 1], p=[1-p, p], size=[len(i) for i in dim])
        return self.__keep(name, result, neglect)
    
    def binomial(self, name, dim=0, n=None, p=None, result=None, neglect=False):
        dim = self.__fix_dims(dim, is_range=False)
        if dim == 0:
            result = self.random.binomial(n, p)
        else:
            result = self.random.binomial(n, p, size=tuple(len(s) for s in dim))
        return self.__keep(name, result, neglect)

    def poisson(self, name, dim=0, lam=1, result=None, neglect=False):
        dim = self.__fix_dims(dim, is_range=False)
        if dim == 0:
            result = self.random.poisson(lam)
        else:
            result = self.random.poisson(lam, size=tuple(len(s) for s in dim))
        return self.__keep(name, result, neglect)

    def geometric(self, name, dim=0, p=None, result=None, neglect=False):
        dim = self.__fix_dims(dim, is_range=False)
        if dim == 0:
            result = self.random.geometric(p)
        else:
            result = self.random.geometric(p, size=tuple(len(s) for s in dim))
        return self.__keep(name, result, neglect)

    def negative_binomial(self, name, dim=0, r=None, p=None, result=None, neglect=False):
        dim = self.__fix_dims(dim, is_range=False)
        if dim == 0:
            result = self.random.negative_binomial(r, p)
        else:
            result = self.random.negative_binomial(r, p, size=tuple(len(s) for s in dim))
        return self.__keep(name, result, neglect)

    def hypergeometric(self, name, dim=0, N=None, m=None, n=None, result=None, neglect=False):
        nbad = m
        ngood = N - m
        nsamples = n

        dim = self.__fix_dims(dim, is_range=False)
        if dim == 0:
            result = self.random.hypergeometric(ngood, nbad, nsamples)
        else:
            result = self.random.hypergeometric(ngood, nbad, nsamples, size=tuple(len(s) for s in dim))
        return self.__keep(name, result, neglect)

    def uniform(self, name, dim=0, bound=[0, 1], result=None, neglect=False):
        dim = self.__fix_dims(dim)
        if dim == 0:
            result = self.random.uniform(low=bound[0], high=bound[1])
        else:
            result = self.random.uniform(low=bound[0], high=bound[1], size=[len(i) for i in dim])
        return self.__keep(name, result, neglect)

    def weight(self, name, dim=0, bound=[0, 1], result=None, neglect=False):
        dim = self.__fix_dims(dim)
        if dim == 0:
            data = self.random.uniform(low=bound[0], high=bound[1])
            result = data / data.sum() if data.sum() != 0 else data
        else:
            data = self.random.uniform(low=bound[0], high=bound[1], size=[len(i) for i in dim])
            result = data / data.sum(axis=-1, keepdims=True) if data.sum() != 0 else data
        return self.__keep(name, result, neglect)

    def normal(self, name, dim=0, mu=0, sigma=1, result=None, neglect=False):
        dim = self.__fix_dims(dim)
        if dim == 0:
            result = self.random.normal(mu, sigma)
        else:
            result = self.random.normal(mu, sigma, size=[len(i) for i in dim])
        return self.__keep(name, result, neglect)

    def standard_normal(self, name, dim=0, result=None, neglect=False):
        dim = self.__fix_dims(dim)
        if dim == 0:
            result = self.random.normal(0, 1)
        else:
            result = self.random.normal(0, 1, size=[len(i) for i in dim])
        return self.__keep(name, result, neglect)

    def exponential(self, name, dim=0, lam=1.0, result=None, neglect=False):
        dim = self.__fix_dims(dim, is_range=False)
        if dim == 0:
            result = self.random.exponential(scale=1/lam)
        else:
            result = self.random.exponential(scale=1/lam, size=[len(i) for i in dim])
        return self.__keep(name, result, neglect)

    def gamma(self, name, dim=0, alpha=1, lam=1, result=None, neglect=False):
        dim = self.__fix_dims(dim, is_range=False)
        if dim == 0:
            result = self.random.gamma(shape=alpha, scale=1/lam)
        else:
            result = self.random.gamma(shape=alpha, scale=1/lam, size=[len(i) for i in dim])
        return self.__keep(name, result, neglect)

    def erlang(self, name, dim=0, alpha=1, lam=1, result=None, neglect=False):
        alpha = int(alpha)
        dim = self.__fix_dims(dim, is_range=False)
        if dim == 0:
            result = self.random.gamma(shape=alpha, scale=1/lam)
        else:
            result = self.random.gamma(shape=alpha, scale=1/lam, size=[len(i) for i in dim])
        return self.__keep(name, result, neglect)

    def beta(self, name, dim=0, a=1, b=1, result=None, neglect=False):
        dim = self.__fix_dims(dim, is_range=False)
        if dim == 0:
            result = self.random.beta(a, b, size=None)
        else:
            result = self.random.beta(a, b, size=[len(i) for i in dim])
        return self.__keep(name, result, neglect)

    def weibull(self, name, dim=0, alpha=None, beta=None, result=None, neglect=False):
        dim = self.__fix_dims(dim, is_range=False)
        if dim == 0:
            result = alpha * self.random.weibull(a=beta)
        else:
            result = alpha * self.random.weibull(a=beta, size=[len(i) for i in dim])
        return self.__keep(name, result, neglect)

    def cauchy(self, name, dim=0, alpha=None, beta=None, result=None, neglect=False):
        dim = self.__fix_dims(dim, is_range=False)
        if dim == 0:
            result = self.random.standard_cauchy()
        else:
            result = self.random.standard_cauchy(size=[len(i) for i in dim])
        return self.__keep(name, result, neglect)

    def dirichlet(self, name, dim=0, k=None, alpha=None, result=None, neglect=False):
        dim = self.__fix_dims(dim, is_range=False)
        if alpha is None:
            if k is not None:
                alpha = np.ones(k)
            elif isinstance(dim, list):
                alpha = np.ones(len(dim[-1]))
        if dim == 0 or len(dim) == 1:
            result = self.random.dirichlet(alpha)
        else:
            result = self.random.dirichlet(alpha, size=[len(i) for i in dim])
        return self.__keep(name, result, neglect)


    def start(self, name, value, direction=None):
        self.criteria_directions[name] = direction
        self.data[name] = [value]

    def update(self, names: list, criteria: list, values: list, compared_with: list):
        xcounter = 0
        for name in names:
            counter = 0
            for criterion in criteria:
                if self.criteria_directions[criterion] == "max":
                    if compared_with[counter] >= self.data[criterion][-1]:
                        self.data[name] = values[xcounter]
                        self.data[criterion].append(compared_with[counter])
                elif self.criteria_directions[criterion] == "min":
                    if compared_with[counter] <= self.data[criterion][-1]:
                        self.data[name] = values[xcounter]
                        self.data[criterion].append(compared_with[counter])
                else:
                    self.data[name] = values[xcounter]
                    self.data[criterion].append(compared_with[counter])
                counter += 1
            xcounter += 1


    def sample(self, name, init, size, replace=False, sort_result=False, return_indices=False, axis=None, neglect=False):

        type_is= type(init)
        
        if type_is ==set:
            init = list(init)
            
        if isinstance(init, (list, set,range, np.ndarray)):
            sample =  self._sample_list_or_array(name, init, size, replace, sort_result, return_indices, axis)
        elif isinstance(init, pd.DataFrame):
            sample = self._sample_pandas_dataframe(name, init, size, replace, sort_result, return_indices, axis)
        else:
            raise ValueError("Unsupported data type for sampling. Supported types: set, list, range, numpy.ndarray, pandas.DataFrame")

        self.__keep(name, sample, neglect)
        
        if type_is ==set:
            return set(sample)
        elif type_is in [list, range]:
            return list(sample)
        elif return_indices:
            return set(sample)
        else:
            return sample

    def load_from_excel(
        self, name: str, dim: list, labels: list, appearance: list, file_name: str, neglect=False
    ):
        
        dim = self.__fix_dims(dim, is_range=True)

        if len(appearance) == 2:
            if (
                (appearance[0] == 1 and appearance[1] == 1)
                or (appearance[0] == 1 and appearance[1] == 0)
                or (appearance[0] == 0 and appearance[1] == 0)
                or (appearance[0] == 0 and appearance[1] == 1)
            ):
                result = pd.read_excel(
                    file_name, index_col=0, sheet_name=name
                ).to_numpy()
            else:
                parameter = pd.read_excel(
                    file_name,
                    header=[i for i in range(appearance[1])],
                    index_col=[i for i in range(appearance[0])],
                    sheet_name=name,
                )
                created_par = np.zeros(shape=([len(i) for i in dim]))
                for keys in it.product(*dim):
                    try:
                        created_par[keys] = parameter.loc[
                            tuple(
                                [labels[i] + str(keys[i]) for i in range(appearance[0])]
                            ),
                            tuple(
                                [
                                    labels[i] + str(keys[i])
                                    for i in range(appearance[0], len(labels))
                                ]
                            ),
                        ]
                    except:
                        created_par[keys] = None
                result = created_par
        else:
            par = pd.read_excel(file_name, index_col=0, sheet_name=name).to_numpy()
            result = par.reshape(
                par.shape[0],
            )
        
        if dim==0:
            result=result[0][0]
        
        elif len(dim)==1:
            result=np.reshape(result,[len(dim[0]),])
        
        else:
            pass

        return self.__keep(name, result, neglect)


data_toolkit = data_utils = data_manager = DataToolkit
