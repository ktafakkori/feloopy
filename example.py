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

from feloopy import *

model = feloopy('simple_milp' , 'ortools')

#A positive variable
x = model.pvar('x')

#An integer variable
y = model.ivar('y')

#An objective function
model.obj(2*x+5*y)

#A constraint
model.con(5*x + 3*y |l| 10)

#Another constraint
model.con(2*x + 7*y |l| 9)

#Getting to know the available solvers
model.ava()

#Solving the provided model
model.sol('max', 'scip')

#Getting to know the problem features
model.inf()

model.ben('cpt')

#Displaying objective value, problem status and variables
# model.dis([var1],[var2],...,[varn])

model.dis(x,y)

#Getting objective value, problem status and variables

x = model.get(x)
y = model.get(y)
obj = model.get_obj()
status = model.get_stat()

print(x,y,obj,status)

#Doing a sensitivity analysis

def instance(a):
    model = feloopy('simple_milp' , 'ortools')
    x = model.pvar('x')
    y = model.ivar('y')
    model.obj(2*x+5*y)
    model.con(a[0]*x + 3*y |l| 10)
    model.con(a[1]*x + 7*y |l| 9)
    model.sol('max','scip')
    return model

a = [5,2]

sensitivity(instance, a, [-6,6], stepofchange=1, table=True, plot=True)

#Solving by a heuristic algorithm interface

def instance(agent, active):
    model = feloopy('simple_milp' , 'ga', agent, active)
    x = model.pvar('x')
    y = model.ivar('y')
    model.obj(2*x+5*y)
    model.con(a[0]*x + 3*y |ll| 10)
    model.con(a[1]*x + 7*y |ll| 9)
    model.sol('max','ga',{'T': 10, 'S': 10, 'Mu': 0.1, 'Cr': 0.5  })
    return model[active]

model = implement(instance)

model.sol()

model.inf()

model.dis(['x',(0,)], ['y',(0,)])

model.ben(['cpt',10])