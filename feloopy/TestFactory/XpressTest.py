'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

from ModelFactory import XpressModelGenerator
from VariableFactory import XpressVariableGenerator
from SolutionFactory import XpressSolutionGenerator
from GetFactory import XpressGetter

m = XpressModelGenerator.GenerateModel()

I = range(2)
J = range(4)

x1 = XpressVariableGenerator.GenerateVariable(m, 'bvar', 'x1', b = [0,1])
#print(x1)

x2 = XpressVariableGenerator.GenerateVariable(m, 'bvar', 'x2', b = [0,1], dim=[I,J])
#print(x2)

x3 = XpressVariableGenerator.GenerateVariable(m, 'pvar', 'x3', b = [0,None])
#print(x3)

x4 = XpressVariableGenerator.GenerateVariable(m, 'pvar', 'x4', b = [0,None], dim=[I,J])
#print(x4)

x5 = XpressVariableGenerator.GenerateVariable(m, 'ivar', 'x5', b = [0,None])
#print(x5)

x6 = XpressVariableGenerator.GenerateVariable(m, 'ivar', 'x6', b = [0,None], dim=[I,J])
#print(x6)

x7 = XpressVariableGenerator.GenerateVariable(m, 'fvar', 'x7', b = [None,None])
#print(x7)

x8 = XpressVariableGenerator.GenerateVariable(m, 'fvar', 'x8', b = [None,None],  dim=[I,J])
#print(x8)

Solution = XpressSolutionGenerator.GenerateSolution(m, [x3], [x3>=2], ['min'], 'xpress', 0)
print(Solution)

print(XpressGetter.Get(m, Solution, 'variable', x3))
#print(XpressGetter.Get(m, Solution, 'objective'))
#print(XpressGetter.Get(m, Solution, 'status'))
print(XpressGetter.Get(m, Solution, 'time'))