'''
Name: FelooPy
Version: 0.1.11
Contributors: Keivan Tafakkori
Date: 21 November 2022
License: MIT. (For more details please refer to LICENSE.txt file).
Copyright (c) 2022 Keivan Tafakkori & FELOOP (https://ktafakkori.github.io/)
'''


from infix import make_infix
import itertools as it

@make_infix('or','sub')
def isle(x,y):
    return x<=y

@make_infix('or','sub')
def le(x,y):
    return x<=y

@make_infix('or','sub')
def l(x,y):
    return x<=y

@make_infix('or','sub')
def isge(x,y):
    return x>=y

@make_infix('or','sub')
def ge(x,y):
    return x>=y

@make_infix('or','sub')
def g(x,y):
    return x>=y

@make_infix('or','sub')
def ise(x,y):
    return x == y

@make_infix('or','sub')
def e(x,y):
    return x == y

@make_infix('or','sub')
def ll(x,y):
    return x-y

@make_infix('or','sub')
def gg(x,y):
    return y-x

@make_infix('or','sub')
def ee(x,y):
    x = y
    return  x

def sets(*args):
    return it.product(*args)