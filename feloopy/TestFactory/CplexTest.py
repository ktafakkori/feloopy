'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

from ModelFactory import CplexModelGenerator
from VariableFactory import CplexVariableGenerator
from SolutionFactory import CplexSolutionGenerator
from GetFactory import CplexGetter

m = CplexModelGenerator.GenerateModel()

I = range(2)
J = range(4)

x1 = CplexVariableGenerator.GenerateVariable(m, 'bvar', 'x', b = [0,1])
#print(x1)

x2 = CplexVariableGenerator.GenerateVariable(m, 'bvar', 'x', b = [0,1], dim=[I,J])
#print(x2)

x3 = CplexVariableGenerator.GenerateVariable(m, 'pvar', 'x', b = [0,None])
#print(x3)

x4 = CplexVariableGenerator.GenerateVariable(m, 'pvar', 'x', b = [0,None], dim=[I,J])
#print(x4)

x5 = CplexVariableGenerator.GenerateVariable(m, 'ivar', 'x', b = [0,None])
#print(x5)

x6 = CplexVariableGenerator.GenerateVariable(m, 'ivar', 'x', b = [0,None], dim=[I,J])
#print(x6)

x7 = CplexVariableGenerator.GenerateVariable(m, 'fvar', 'x', b = [None,None])
#print(x7)

x8 = CplexVariableGenerator.GenerateVariable(m, 'fvar', 'x', b = [None,None],  dim=[I,J])
#print(x8)

Solution = CplexSolutionGenerator.GenerateSolution(m, [x3+1, x3], [x3>=2], ['min','min'], 'cplex', 1)
print(Solution)


print(CplexGetter.Get(m, Solution, 'variable', x3))
print(CplexGetter.Get(m, Solution, 'objective'))
print(CplexGetter.Get(m, Solution, 'status'))
print(CplexGetter.Get(m, Solution, 'time'))