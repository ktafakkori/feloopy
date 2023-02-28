import itertools as it
from infix import make_infix
import math as mt

@make_infix('or', 'sub')
def ll(x, y):
    return x-y

@make_infix('or', 'sub')
def gg(x, y):
    return y-x

@make_infix('or', 'sub')
def ee(x, y):
    x = y
    return x

def sets(*args):
    return it.product(*args)