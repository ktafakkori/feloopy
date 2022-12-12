'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

from ModelFactory import CylpModelGenerator
from VariableFactory import CylpVariableGenerator
from SolutionFactory import CylpSolutionGenerator
from GetFactory import CylpGetter

m = CylpModelGenerator.GenerateModel()

I = range(2)
J = range(4)

x1 = CylpVariableGenerator.GenerateVariable(m, 'bvar', 'x1', b = [0,1])
#print(x1)

x2 = CylpVariableGenerator.GenerateVariable(m, 'bvar', 'x2', b = [0,1], dim=[I,J])
#print(x2)

x3 = CylpVariableGenerator.GenerateVariable(m, 'pvar', 'x3', b = [0,None])
#print(x3)

x4 = CylpVariableGenerator.GenerateVariable(m, 'pvar', 'x4', b = [0,None], dim=[I,J])
#print(x4)

x5 = CylpVariableGenerator.GenerateVariable(m, 'ivar', 'x5', b = [0,None])
#print(x5)

x6 = CylpVariableGenerator.GenerateVariable(m, 'ivar', 'x6', b = [0,None], dim=[I,J])
#print(x6)

x7 = CylpVariableGenerator.GenerateVariable(m, 'fvar', 'x7', b = [None,None])
#print(x7)

x8 = CylpVariableGenerator.GenerateVariable(m, 'fvar', 'x8', b = [None,None],  dim=[I,J])
#print(x8)

Solution = CylpSolutionGenerator.GenerateSolution(m, [x3], [x3>=2], ['min'], 'cbc', 0)
print(Solution)


#print(CylpGetter.Get(m, Solution, 'variable', x3))
#print(CylpGetter.Get(m, Solution, 'objective'))
#print(CylpGetter.Get(m, Solution, 'status'))
print(CylpGetter.Get(m, Solution, 'time'))

