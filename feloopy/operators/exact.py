import itertools as it
from infix import make_infix
import math as mt

prod = mt.prod

@make_infix('or', 'sub')
def isle(x, y):
    return x <= y

@make_infix('or', 'sub')
def le(x, y):
    return x <= y

@make_infix('or', 'sub')
def l(x, y):
    return x <= y

@make_infix('or', 'sub')
def isge(x, y):
    return x >= y


@make_infix('or', 'sub')
def ge(x, y):
    return x >= y


@make_infix('or', 'sub')
def g(x, y):
    return x >= y


@make_infix('or', 'sub')
def ise(x, y):
    return x == y

@make_infix('or', 'sub')
def e(x, y):
    return x == y