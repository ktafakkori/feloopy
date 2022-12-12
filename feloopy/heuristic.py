'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

import numpy as np
import math as mt

from .exact import *

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


class implement:

    def __init__(self, ModelFunction):
        '''
        * ModelFunction (Function): The function that contains the model, its corresponding solve command, and returns its objective, fitness or hypothesis value.
        '''

        self.ModelInfo = ModelFunction(['idle'])

        self.ModelFunction = ModelFunction

        self.InterfaceName = self.ModelInfo.InterfaceName
        self.SolutionMethod = self.ModelInfo.SolutionMethod
        self.ModelName = self.ModelInfo.ModelName
        self.SolverName = self.ModelInfo.SolverName
        self.ModelConstraints = self.ModelInfo.ModelConstraints
        self.ModelObjectives = self.ModelInfo.ModelObjectives
        self.ObjectivesDirections = self.ModelInfo.ObjectivesDirections
        self.PositiveVariableCounter = self.ModelInfo.PositiveVariableCounter
        self.BinaryVariableCounter = self.ModelInfo.BinaryVariableCounter
        self.IntegerVariableCounter = self.ModelInfo.IntegerVariableCounter
        self.FreeVariableCounter = self.ModelInfo.FreeVariableCounter
        self.ToTalVariableCounter = self.ModelInfo.ToTalVariableCounter
        self.ConstraintsCounter = self.ModelInfo.ConstraintsCounter
        self.ObjectivesCounter = self.ModelInfo.ObjectivesCounter
        self.AlgOptions = self.ModelInfo.AlgOptions
        self.VariablesSpread = self.ModelInfo.VariablesSpread
        self.VariablesType = self.ModelInfo.VariablesType
        self.ObjectiveBeingOptimized = self.ModelInfo.ObjectiveBeingOptimized
        self.VariablesBound = self.ModelInfo.VariablesBound
        self.VariablesDim = self.ModelInfo.VariablesDim

        self.status = 'Not solved'
        self.result = None

        self.AgentProperties = [None, None, None, None]

        match self.InterfaceName:

            case 'mealpy':

                from .ModelFactory import MealpyModelGenerator
                self.ModelObject = MealpyModelGenerator.GenerateModel(
                    self.SolverName, self.AlgOptions)

            case 'feloopy':

                from .ModelFactory import FeloopyHeuristicModelGenerator
                self.ModelObject = FeloopyHeuristicModelGenerator.GenerateModel(
                    self.ToTalVariableCounter[1], self.ObjectivesDirections, self.SolverName, self.AlgOptions)

    def sol(self, PenaltyMultiplier=0, Times=1):

        self.PenaltyMultiplier = PenaltyMultiplier

        match self.InterfaceName:

            case 'mealpy':

                from .SolutionFactory import MealpySolutionGenerator
                self.BestAgent, self.BestReward = MealpySolutionGenerator.GenerateSolution(
                    self.ModelObject, self.Fitness, self.ToTalVariableCounter, self.ObjectivesDirections, self.ObjectiveBeingOptimized, Times)

            case 'feloopy':

                from .SolutionFactory import FeloopyHeuristicSolutionGenerator
                self.BestAgent, self.BestReward = FeloopyHeuristicSolutionGenerator.GenerateSolution(
                    self.ModelObject, self.Fitness, Times)

    def Fitness(self, X):

        self.AgentProperties[0] = 'active'
        self.AgentProperties[1] = X
        self.AgentProperties[2] = self.VariablesSpread
        self.AgentProperties[3] = self.PenaltyMultiplier

        return self.ModelFunction(self.AgentProperties)

    def get(self, *args):

        match self.InterfaceName:
            case 'mealpy':
                for i in args:

                    if len(i) >= 2:

                        match self.VariablesType[i[0]]:

                            case 'pvar':

                                if self.VariablesDim[i[0]] == 0:
                                    return (self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))[0]

                                else:
                                    def var(*args):
                                        self.NewAgentProperties = (self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (
                                            self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                        return self.NewAgentProperties[sum(args[k]*mt.prod(len(self.VariablesDim[i[0]][j]) for j in range(k+1, len(self.VariablesDim[i[0]]))) for k in range(len(self.VariablesDim[i[0]])))]

                                    return var(*i[1])

                            case 'fvar':

                                if self.VariablesDim[i[0]] == 0:
                                    return (self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))[0]

                                else:
                                    def var(*args):
                                        self.NewAgentProperties = (self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (
                                            self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                        return self.NewAgentProperties[sum(args[k]*mt.prod(len(self.VariablesDim[i[0]][j]) for j in range(k+1, len(self.VariablesDim[i[0]]))) for k in range(len(self.VariablesDim[i[0]])))]

                                    return var(*i[1])

                            case 'bvar':
                                if self.VariablesDim[i[0]] == 0:
                                    return np.round(self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))[0]

                                else:
                                    def var(*args):
                                        self.NewAgentProperties = np.round(self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (
                                            self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                        return self.NewAgentProperties[sum(args[k]*mt.prod(len(self.VariablesDim[i[0]][j]) for j in range(k+1, len(self.VariablesDim[i[0]]))) for k in range(len(self.VariablesDim[i[0]])))]

                                    return var(*i[1])
                            case 'ivar':
                                if self.VariablesDim[i[0]] == 0:
                                    return np.floor(self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))[0]

                                else:
                                    def var(*args):
                                        self.NewAgentProperties = np.floor(self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (
                                            self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                    
                                        return self.NewAgentProperties[sum(args[k]*mt.prod(len(self.VariablesDim[i[0]][j]) for j in range(k+1, len(self.VariablesDim[i[0]]))) for k in range(len(self.VariablesDim[i[0]])))]

                                    return var(*i[1])

                            case 'svar':

                                return np.argsort(self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]])[i[1]]

                    else:
                        match self.VariablesType[i[0]]:

                            case 'pvar':

                                return (self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))[0]

                            case 'fvar':

                                return (self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))[0]

                            case 'bvar':
                                return np.round(self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))[0]

                            case 'ivar':
                                return np.floor(self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))[0]

                            case 'svar':
                                return np.argsort(self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]])

            case 'feloopy':

  

               for i in args:

                    if len(i) >= 2:

                        match self.VariablesType[i[0]]:

                            case 'pvar':

                                if self.VariablesDim[i[0]] == 0:
                                    return (self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))

                                else:
                                    def var(*args):
                                        self.NewAgentProperties = (self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (
                                            self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                        return self.NewAgentProperties[sum(args[k]*mt.prod(len(self.VariablesDim[i[0]][j]) for j in range(k+1, len(self.VariablesDim[i[0]]))) for k in range(len(self.VariablesDim[i[0]])))]

                                    return var(*i[1])

                            case 'fvar':

                                if self.VariablesDim[i[0]] == 0:
                                    return (self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))

                                else:
                                    def var(*args):
                                        self.NewAgentProperties = (self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (
                                            self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                        return self.NewAgentProperties[sum(args[k]*mt.prod(len(self.VariablesDim[i[0]][j]) for j in range(k+1, len(self.VariablesDim[i[0]]))) for k in range(len(self.VariablesDim[i[0]])))]

                                    return var(*i[1])

                            case 'bvar':
                                if self.VariablesDim[i[0]] == 0:
                                    return np.floor(self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))

                                else:
                                    def var(*args):
                                        self.NewAgentProperties = np.round(self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (
                                            self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                        return self.NewAgentProperties[sum(args[k]*mt.prod(len(self.VariablesDim[i[0]][j]) for j in range(k+1, len(self.VariablesDim[i[0]]))) for k in range(len(self.VariablesDim[i[0]])))]

                                    return var(*i[1])
                            case 'ivar':
                                if self.VariablesDim[i[0]] == 0:
                                    return np.floor(self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))

                                else:
                                    def var(*args):
                                        self.NewAgentProperties = np.floor(self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (
                                            self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                        return self.NewAgentProperties[sum(args[k]*mt.prod(len(self.VariablesDim[i[0]][j]) for j in range(k+1, len(self.VariablesDim[i[0]]))) for k in range(len(self.VariablesDim[i[0]])))]

                                    return var(*i[1])

                            case 'svar':

                                return np.argsort(self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]])[i[1]]

                    else:
                        match self.VariablesType[i[0]]:

                            case 'pvar':

                                return (self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))

                            case 'fvar':

                                return (self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))

                            case 'bvar':
                                return np.round(self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))

                            case 'ivar':
                                return np.floor(self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))

                            case 'svar':
                                return np.argsort(self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]])


    def get_obj(self):
        return self.BestReward

    def dis(self, input):
        print(input[0]+str(input[1])+': ', self.get(input))

    def dis_obj(self):
        print('objective: ', self.BestReward)

    def inf(self):

        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"   FelooPy ({Version}) - Released: {ReleaseDate}         ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()

        print()
        print("PROBLEM FEATURES \n --------")
        A = tb(
            {
                "info": ["model", "interface", "solver", "direction", "method"],
                "detail": [self.ModelName, self.InterfaceName, self.SolverName, self.ObjectivesDirections, self.SolutionMethod],
                "variable": ["positive", "binary", "integer", "free", "tot"],
                "count (cat,tot)": [str(self.PositiveVariableCounter), str(self.BinaryVariableCounter), str(self.IntegerVariableCounter), str(self.FreeVariableCounter), str(self.ToTalVariableCounter)],
                "other": ["objective", "constraint"],
                "count (cat, tot)": [str(self.ObjectivesCounter), str(self.ConstraintsCounter)]
            },
            headers="keys", tablefmt="github"
        )
        print(A)

        return A