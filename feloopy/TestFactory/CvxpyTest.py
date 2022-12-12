'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

from ModelFactory import CvxpyModelGenerator
from VariableFactory import CvxpyVariableGenerator
from SolutionFactory import CvxpySolutionGenerator
from GetFactory import CvxpyGetter

m = CvxpyModelGenerator.GenerateModel()

I = range(2)
J = range(4)

x1 = CvxpyVariableGenerator.GenerateVariable(m, 'bvar', 'x', b = [0,1])
#print(x1)

x2 = CvxpyVariableGenerator.GenerateVariable(m, 'bvar', 'x', b = [0,1], dim=[I,J])
#print(x2)

x3 = CvxpyVariableGenerator.GenerateVariable(m, 'pvar', 'x', b = [0,None])
#print(x3)

x4 = CvxpyVariableGenerator.GenerateVariable(m, 'pvar', 'x', b = [0,None], dim=[I,J])
#print(x4)

x5 = CvxpyVariableGenerator.GenerateVariable(m, 'ivar', 'x', b = [0,None])
#print(x5)

x6 = CvxpyVariableGenerator.GenerateVariable(m, 'ivar', 'x', b = [0,None], dim=[I,J])
#print(x6)

x7 = CvxpyVariableGenerator.GenerateVariable(m, 'fvar', 'x', b = [None,None])
#print(x7)

x8 = CvxpyVariableGenerator.GenerateVariable(m, 'fvar', 'x', b = [None,None],  dim=[I,J])
#print(x8)

Solution = CvxpySolutionGenerator.GenerateSolution(m, [x3], [x3>=2], ['min'], 'cplex', 0)
print(Solution)

print(CvxpyGetter.Get(m, Solution, 'variable', x3))
#print(CvxpyGetter.Get(m, Solution, 'objective'))
#print(CvxpyGetter.Get(m, Solution, 'status'))
print(CvxpyGetter.Get(m, Solution, 'time'))