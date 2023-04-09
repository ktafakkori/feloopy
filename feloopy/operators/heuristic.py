import itertools as it
from infix import make_infix
import math as mt

@make_infix('or', 'sub')
def l(x, y):
    return x-y

@make_infix('or', 'sub')
def g(x, y):
    return y-x