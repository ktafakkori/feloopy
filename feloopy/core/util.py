'''
Name: FelooPy
Version: 0.1.11
Contributors: Keivan Tafakkori
Date: 21 November 2022
License: MIT. (For more details please refer to LICENSE.txt file).
Copyright (c) 2022 Keivan Tafakkori & FELOOP (https://ktafakkori.github.io/)
'''


import pandas as pd
import itertools as it
import numpy as np

def load_data(path,shape,row_dim,col_dim,index_names,sheet_name):
    parameter = pd.read_excel(path, header=[i for i in range(col_dim)], index_col=[i for i in range(row_dim)], sheet_name=sheet_name)
    created_par = np.zeros(shape=([len(i) for i in shape]))
    for keys in it.product(*shape):
        try:
            created_par[keys] = parameter.loc[tuple([index_names[i]+str(keys[i]) for i in range(row_dim)]),tuple([index_names[i]+str(keys[i]) for i in range(row_dim,len(index_names))])]
        except:
            created_par[keys] = None
    return created_par