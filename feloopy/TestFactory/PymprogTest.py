'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

from ModelFactory import PymprogModelGenerator
from VariableFactory import PymprogVariableGenerator
from SolutionFactory import PymprogSolutionGenerator
from GetFactory import PymprogGetter

m = PymprogModelGenerator.GenerateModel()

I = range(2)
J = range(4)

x1 = PymprogVariableGenerator.GenerateVariable(m, 'bvar', 'x1', b = [0,1])
#print(x1)

x2 = PymprogVariableGenerator.GenerateVariable(m, 'bvar', 'x2', b = [0,1], dim=[I,J])
#print(x2)

x3 = PymprogVariableGenerator.GenerateVariable(m, 'pvar', 'x3', b = [0,None])
#print(x3)

x4 = PymprogVariableGenerator.GenerateVariable(m, 'pvar', 'x4', b = [0,None], dim=[I,J])
#print(x4)

x5 = PymprogVariableGenerator.GenerateVariable(m, 'ivar', 'x5', b = [0,None])
#print(x5)

x6 = PymprogVariableGenerator.GenerateVariable(m, 'ivar', 'x6', b = [0,None], dim=[I,J])
#print(x6)

x7 = PymprogVariableGenerator.GenerateVariable(m, 'fvar', 'x7', b = [None,None])
#print(x7)

x8 = PymprogVariableGenerator.GenerateVariable(m, 'fvar', 'x8', b = [None,None],  dim=[I,J])
#print(x8)

Solution = PymprogSolutionGenerator.GenerateSolution(m, [x3], [x3>=2], ['min'], 'glpk', 0)
print(Solution)

print(PymprogGetter.Get(m, Solution, 'variable', x3))
print(PymprogGetter.Get(m, Solution, 'objective'))
print(PymprogGetter.Get(m, Solution, 'status'))
print(PymprogGetter.Get(m, Solution, 'time'))