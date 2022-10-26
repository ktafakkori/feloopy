'''
FelooPy version 0.1.1
Release: 26 October 2022
'''

'''
MIT License

Copyright (c) 2022 Keivan Tafakkori & FELOOP (https://ktafakkori.github.io/)

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

   1. Redistributions of source code must retain the above copyright notice, this list of
      conditions and the following disclaimer.

   2. Redistributions in binary form must reproduce the above copyright notice, this list
      of conditions and the following disclaimer in the documentation and/or other materials
      provided with the distribution.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
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