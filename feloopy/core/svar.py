'''
Name: FelooPy
Version: 0.1.11
Contributors: Keivan Tafakkori
Date: 21 November 2022
License: MIT. (For more details please refer to LICENSE.txt file).
Copyright (c) 2022 Keivan Tafakkori & FELOOP (https://ktafakkori.github.io/)
'''


from .age import *

def add_ga_svar(var_name, agent, VarLength, dim,  b=[0, 1], vectorized=False):
    if vectorized:
        return multiagent(var_name, b[0] + agent[:,VarLength[0]:VarLength[1]] * (b[1] - b[0]), dim, 'svar')
    else:
        return singleagent(var_name, b[0] + agent[:,VarLength[0]:VarLength[1]] * (b[1] - b[0]), dim, 'svar')

svar_maker = {
    "ga": add_ga_svar
}

