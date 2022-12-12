'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

from ModelFactory import PicosModelGenerator
from VariableFactory import PicosVariableGenerator
from SolutionFactory import PicosSolutionGenerator
from GetFactory import PicosGetter

m = PicosModelGenerator.GenerateModel()

I = range(2)
J = range(4)

x1 = PicosVariableGenerator.GenerateVariable(m, 'bvar', 'x1', b = [0,1])
#print(x1)

x2 = PicosVariableGenerator.GenerateVariable(m, 'bvar', 'x2', b = [0,1], dim=[I,J])
#print(x2)

x3 = PicosVariableGenerator.GenerateVariable(m, 'pvar', 'x3', b = [0,None])
#print(x3)

x4 = PicosVariableGenerator.GenerateVariable(m, 'pvar', 'x4', b = [0,None], dim=[I,J])
#print(x4)

x5 = PicosVariableGenerator.GenerateVariable(m, 'ivar', 'x5', b = [0,None])
#print(x5)

x6 = PicosVariableGenerator.GenerateVariable(m, 'ivar', 'x6', b = [0,None], dim=[I,J])
#print(x6)

x7 = PicosVariableGenerator.GenerateVariable(m, 'fvar', 'x7', b = [None,None])
#print(x7)

x8 = PicosVariableGenerator.GenerateVariable(m, 'fvar', 'x8', b = [None,None],  dim=[I,J])
#print(x8)

Solution = PicosSolutionGenerator.GenerateSolution(m, [x3], [x3>=2], ['min'], 'cplex', 0)
print(Solution)

print(PicosGetter.Get(m, Solution, 'variable', x3))
print(PicosGetter.Get(m, Solution, 'objective'))
print(PicosGetter.Get(m, Solution, 'status'))
print(PicosGetter.Get(m, Solution, 'time'))
