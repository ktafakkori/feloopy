'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

import itertools as it
from infix import make_infix
import math as mt


@make_infix('or', 'sub')
def l(x, y):
    return x-y

@make_infix('or', 'sub')
def g(x, y):
    return y-x
