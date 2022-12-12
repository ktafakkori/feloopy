'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

from ModelFactory import GurobiModelGenerator
from VariableFactory import GurobiVariableGenerator
from SolutionFactory import GurobiSolutionGenerator
from GetFactory import GurobiGetter

m = GurobiModelGenerator.GenerateModel()

I = range(2)
J = range(4)

x1 = GurobiVariableGenerator.GenerateVariable(m, 'bvar', 'x', b = [0,1])
print(x1)

x2 = GurobiVariableGenerator.GenerateVariable(m, 'bvar', 'x', b = [0,1], dim=[I,J])
print(x2)

x3 = GurobiVariableGenerator.GenerateVariable(m, 'pvar', 'x', b = [0,None])
#print(x3)

x4 = GurobiVariableGenerator.GenerateVariable(m, 'pvar', 'x', b = [0,None], dim=[I,J])
#print(x4)

x5 = GurobiVariableGenerator.GenerateVariable(m, 'ivar', 'x', b = [0,None])
#print(x5)

x6 = GurobiVariableGenerator.GenerateVariable(m, 'ivar', 'x', b = [0,None], dim=[I,J])
#print(x6)

x7 = GurobiVariableGenerator.GenerateVariable(m, 'fvar', 'x', b = [None,None])
#print(x7)

x8 = GurobiVariableGenerator.GenerateVariable(m, 'fvar', 'x', b = [None,None],  dim=[I,J])
#print(x8)

Solution = GurobiSolutionGenerator.GenerateSolution(m, [x3], [x3>=2], ['min'], 'gurobi', 0)
print(Solution)

print(GurobiGetter.Get(m, Solution, 'variable', x3))
print(GurobiGetter.Get(m, Solution, 'objective'))
print(GurobiGetter.Get(m, Solution, 'status'))
print(GurobiGetter.Get(m, Solution, 'time'))

