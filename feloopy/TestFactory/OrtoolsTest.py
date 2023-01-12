'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

from ModelFactory import OrtoolsModelGenerator
from VariableFactory import OrtoolsVariableGenerator
from SolutionFactory import OrtoolsSolutionGenerator
from GetFactory import OrtoolsGetter

m = OrtoolsModelGenerator.GenerateModel()

I = range(2)
J = range(4)

x1 = OrtoolsVariableGenerator.GenerateVariable(m, 'bvar', 'x1', b = [0,1])
#print(x1)

x2 = OrtoolsVariableGenerator.GenerateVariable(m, 'bvar', 'x2', b = [0,1], dim=[I,J])
#print(x2)

x3 = OrtoolsVariableGenerator.GenerateVariable(m, 'pvar', 'x3', b = [0,None])
#print(x3)

x4 = OrtoolsVariableGenerator.GenerateVariable(m, 'pvar', 'x4', b = [0,None], dim=[I,J])
#print(x4)

x5 = OrtoolsVariableGenerator.GenerateVariable(m, 'ivar', 'x5', b = [0,None])
#print(x5)

x6 = OrtoolsVariableGenerator.GenerateVariable(m, 'ivar', 'x6', b = [0,None], dim=[I,J])
#print(x6)

x7 = OrtoolsVariableGenerator.GenerateVariable(m, 'fvar', 'x7', b = [None,None])
#print(x7)

x8 = OrtoolsVariableGenerator.GenerateVariable(m, 'fvar', 'x8', b = [None,None],  dim=[I,J])
#print(x8)

Solution = OrtoolsSolutionGenerator.GenerateSolution(m, [x3], [x3>=2], ['min'], 'scip', 0)
print(Solution)

print(OrtoolsGetter.Get(m, Solution, 'variable', x3))
print(OrtoolsGetter.Get(m, Solution, 'objective'))
print(OrtoolsGetter.Get(m, Solution, 'status'))
print(OrtoolsGetter.Get(m, Solution, 'time'))