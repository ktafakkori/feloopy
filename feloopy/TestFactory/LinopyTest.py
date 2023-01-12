'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

from ModelFactory import LinopyModelGenerator
from VariableFactory import LinopyVariableGenerator
from SolutionFactory import LinopySolutionGenerator
from GetFactory import LinopyGetter

m = LinopyModelGenerator.GenerateModel()

I = range(2)
J = range(4)

x1 = LinopyVariableGenerator.GenerateVariable(m, 'bvar', 'x1', b = [0,1])
#print(x1)

x2 = LinopyVariableGenerator.GenerateVariable(m, 'bvar', 'x2', b = [0,1], dim=[I,J])
#print(x2)

x3 = LinopyVariableGenerator.GenerateVariable(m, 'pvar', 'x3', b = [0,None])
#print(x3)

x4 = LinopyVariableGenerator.GenerateVariable(m, 'pvar', 'x4', b = [0,None], dim=[I,J])
#print(x4)

x5 = LinopyVariableGenerator.GenerateVariable(m, 'ivar', 'x5', b = [0,None])
#print(x5)

x6 = LinopyVariableGenerator.GenerateVariable(m, 'ivar', 'x6', b = [0,None], dim=[I,J])
#print(x6)

x7 = LinopyVariableGenerator.GenerateVariable(m, 'fvar', 'x7', b = [None,None])
#print(x7)

x8 = LinopyVariableGenerator.GenerateVariable(m, 'fvar', 'x8', b = [None,None],  dim=[I,J])
#print(x8)

Solution = LinopySolutionGenerator.GenerateSolution(m, [x3], [x3>=2], ['min'], 'cplex', 0)
print(Solution)

print(LinopyGetter.Get(m, Solution, 'variable', x3))
print(LinopyGetter.Get(m, Solution, 'objective'))
print(LinopyGetter.Get(m, Solution, 'status'))
print(LinopyGetter.Get(m, Solution, 'time'))