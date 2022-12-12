'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

def GenerateSolution(ModelObject, Fitness, Times):

    if Times == 1:
        
        return  ModelObject.solve(Fitness)