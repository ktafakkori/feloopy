import warnings
import sys

def mkarr_h(size, func, params={}, idx=[]):
    if len(size) > 0:
        dim = size[0]
        res = []
        for tidx in range(dim):
            res.append(mkarr_h(size[1:], func, params=params, idx=idx + [tidx]))
        return res
    else:
        return func(idx, **params)
    
def mkarr(size, func, params={}):
    if type(size) is int:
        size = [size]
    elif type(size) is tuple:
        size = list(size)
    elif type(size) is list:
        size = size
    else:
        warnings.warn('Input "size" should be an integer or a tuple.')
    return np.array(mkarr_h(size, func, params=params))