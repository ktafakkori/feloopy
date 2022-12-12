'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

from ModelFactory import GekkoModelGenerator
from VariableFactory import GekkoVariableGenerator
from SolutionFactory import GekkoSolutionGenerator
from GetFactory import GekkoGetter

m = GekkoModelGenerator.GenerateModel()

I = range(2)
J = range(4)

x1 = GekkoVariableGenerator.GenerateVariable(m, 'bvar', 'x', b = [0,1])
#print(x1)

x2 = GekkoVariableGenerator.GenerateVariable(m, 'bvar', 'x', b = [0,1], dim=[I,J])
#print(x2)

x3 = GekkoVariableGenerator.GenerateVariable(m, 'pvar', 'x', b = [0,None])
#print(x3)

x4 = GekkoVariableGenerator.GenerateVariable(m, 'pvar', 'x', b = [0,None], dim=[I,J])
#print(x4)

x5 = GekkoVariableGenerator.GenerateVariable(m, 'ivar', 'x', b = [0,None])
#print(x5)

x6 = GekkoVariableGenerator.GenerateVariable(m, 'ivar', 'x', b = [0,None], dim=[I,J])
#print(x6)

x7 = GekkoVariableGenerator.GenerateVariable(m, 'fvar', 'x', b = [None,None])
#print(x7)

x8 = GekkoVariableGenerator.GenerateVariable(m, 'fvar', 'x', b = [None,None],  dim=[I,J])
#print(x8)

Solution = GekkoSolutionGenerator.GenerateSolution(m, [x3], [x3>=2], ['min'], 'apopt', 0)
print(Solution)

print(GekkoGetter.Get(m, Solution, 'variable', x3))
print(GekkoGetter.Get(m, Solution, 'objective'))
print(GekkoGetter.Get(m, Solution, 'status'))
print(GekkoGetter.Get(m, Solution, 'time'))
