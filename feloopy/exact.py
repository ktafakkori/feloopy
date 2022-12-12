'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

import matplotlib.style as style
from tabulate import tabulate as tb
import matplotlib.pyplot as plt
import numpy as np
import itertools as it
from infix import make_infix
import math as mt
import pandas as pd
import os
import sys

prod = mt.prod

@make_infix('or', 'sub')
def isle(x, y):
    return x <= y


@make_infix('or', 'sub')
def le(x, y):
    return x <= y


@make_infix('or', 'sub')
def l(x, y):
    return x <= y


@make_infix('or', 'sub')
def isge(x, y):
    return x >= y


@make_infix('or', 'sub')
def ge(x, y):
    return x >= y


@make_infix('or', 'sub')
def g(x, y):
    return x >= y


@make_infix('or', 'sub')
def ise(x, y):
    return x == y


@make_infix('or', 'sub')
def e(x, y):
    return x == y


@make_infix('or', 'sub')
def ll(x, y):
    return x-y


@make_infix('or', 'sub')
def gg(x, y):
    return y-x


@make_infix('or', 'sub')
def ee(x, y):
    x = y
    return x


def sets(*args):
    return it.product(*args)


Version = 'Version 0.2.0'
ReleaseDate = '11 December 2022'


def UpdateCounter(VarDim, TotCounter, SpecialCounter):
    TotCounter[0] += 1
    SpecialCounter[0] += 1
    SpecialCounter[1] += 1 if VarDim == 0 else prod(len(dims) for dims in VarDim)
    TotCounter[1] += SpecialCounter[1]
    return TotCounter, SpecialCounter


class EMPTY:

    '''
    A class to manage variables in the heuristic optimization process.

    '''

    def __init__(self, val):
        self.val = val

    def __call__(self, *args):
        return 0

    def __getitem__(self, *args):
        return 0

    def __hash__(self):
        return 0

    def __str__(self):
        return 0

    def __repr__(self):
        return 0

    def __neg__(self):
        return 0

    def __pos__(self):
        return 0

    def __bool__(self):
        return 0

    def __add__(self, other):
        return 0

    def __radd__(self, other):
        return 0

    def __sub__(self, other):
        return 0

    def __rsub__(self, other):
        return 0

    def __mul__(self, other):
        return 0

    def __rmul__(self, other):
        return 0

    def __div__(self, other):
        return 0

    def __rdiv__(self, other):
        raise 0

    def __le__(self, other):
        return 0

    def __ge__(self, other):
        return 0

    def __eq__(self, other):
        return 0

    def __ne__(self, other):
        return 0


class model:

    def __init__(self, SolutionMethod: str, ModelName: str, InterfaceName: str, Key=None, AgentProperties=None):
        '''

        Environment Definition
        ~~~~~~~~~~~~~~~~~~~~~~

        * SolutionMethod (String): Determine the solution method of your model (e.g., 'exact' or 'heuristic')
        * ModelName (String): Determine a name for your model (e.g., 'TSP' or 'TravelingSalesManProblem' or 'Trvaeling_Salesman_Problem')
        * InterfaceName (String) : Select the desired exact optimization interface in Python (e.g., 'pulp' or 'pyomo')
        * AgentProperties (List) : (Only for heuristic optimization) Provide a variable name for your agents and consider it as an input for your model function. (e.g., X or Agent) 
        * Key (Integer): Determine a seed for random number generator 
        '''

        self.RNG = np.random.default_rng(Key)

        match SolutionMethod:

            case 'exact':

                self.InterfaceName = InterfaceName
                self.SolutionMethod = SolutionMethod

                self.ModelName = ModelName
                self.SolverName = None

                self.ModelConstraints = []

                self.ModelObjectives = []
                self.ObjectivesDirections = []

                self.PositiveVariableCounter = [0, 0]
                self.BinaryVariableCounter = [0, 0]
                self.IntegerVariableCounter = [0, 0]
                self.FreeVariableCounter = [0, 0]
                self.ToTalVariableCounter = [0, 0]

                self.ConstraintsCounter = [0, 0]
                self.ObjectivesCounter = [0, 0]

                match self.InterfaceName:

                    # 1
                    case 'pulp':

                        from .ModelFactory import PulpModelGenerator
                        self.ModelObject = PulpModelGenerator.GenerateModel()

                    # 2
                    case 'pyomo':

                        from .ModelFactory import PyomoModelGenerator
                        self.ModelObject = PyomoModelGenerator.GenerateModel()

                    # 3
                    case 'ortools':

                        from .ModelFactory import OrtoolsModelGenerator
                        self.ModelObject = OrtoolsModelGenerator.GenerateModel()

                    # 4
                    case 'gekko':

                        from .ModelFactory import GekkoModelGenerator
                        self.ModelObject = GekkoModelGenerator.GenerateModel()

                    # 5
                    case 'picos':

                        from .ModelFactory import PicosModelGenerator
                        self.ModelObject = PicosModelGenerator.GenerateModel()

                    # 6
                    case 'cvxpy':

                        from .ModelFactory import CvxpyModelGenerator
                        self.ModelObject = CvxpyModelGenerator.GenerateModel()

                    # 7
                    case 'cylp':

                        from .ModelFactory import CylpModelGenerator
                        self.ModelObject = CylpModelGenerator.GenerateModel()

                    # 8
                    case 'pymprog':

                        from .ModelFactory import PymprogModelGenerator
                        self.ModelObject = PymprogModelGenerator.GenerateModel()

                    # 9
                    case 'cplex':

                        from .ModelFactory import CplexModelGenerator
                        self.ModelObject = CplexModelGenerator.GenerateModel()

                    # 10
                    case 'gurobi':

                        from .ModelFactory import GurobiModelGenerator
                        self.ModelObject = GurobiModelGenerator.GenerateModel()

                    # 11
                    case 'xpress':

                        from .ModelFactory import XpressModelGenerator
                        self.ModelObject = XpressModelGenerator.GenerateModel()

                    # 12
                    case 'mip':

                        from .ModelFactory import MipModelGenerator
                        self.ModelObject = MipModelGenerator.GenerateModel()

                    # 13
                    case 'linopy':

                        from .ModelFactory import LinopyModelGenerator
                        self.ModelObject = LinopyModelGenerator.GenerateModel()

            case 'heuristic':

                self.InterfaceName = InterfaceName

                match self.InterfaceName:

                    case 'mealpy':

                        self.Vectorized = False

                    case 'feloopy':

                        self.Vectorized = 'FelooPyMethod'

                self.AgentProperties = AgentProperties

                self.SolutionMethod = SolutionMethod

                if self.AgentProperties[0] == 'idle':

                    self.ModelName = ModelName
                    self.SolverName = None

                    self.ModelObjectives = []
                    self.ModelConstraints = []

                    self.ObjectivesDirections = []

                    self.PositiveVariableCounter = [0, 0]
                    self.BinaryVariableCounter = [0, 0]
                    self.IntegerVariableCounter = [0, 0]
                    self.FreeVariableCounter = [0, 0]
                    self.ToTalVariableCounter = [0, 0]

                    self.ConstraintsCounter = [0, 0]
                    self.ObjectivesCounter = [0, 0]

                    self.VariablesSpread = dict()
                    self.VariablesType = dict()
                    self.VariablesBound = dict()
                    self.VariablesDim = dict()

                else:

                    self.ConstraintsViolation = 0
                    self.VariablesSpread = self.AgentProperties[2]
                    self.PenaltyMultiplier = self.AgentProperties[3]

                    self.ModelObjectives = []
                    self.ModelConstraints = []

                    self.AgentProperties = self.AgentProperties[1]
                   

    def __getitem__(self, AgentProperties):
        if AgentProperties[0] == 'idle':
            return self
        else:
            if self.Vectorized != 'FelooPyMethod':
                return self.Result
            else:
                self.AgentProperties[:,-1] = self.Result
                return self.AgentProperties

    def bvar(self, VarName: str, VarDim=0, VarBound=[0, 1]):
        '''

        Binary Variable Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~

        * VarName (String): Determine a name for your variable (e.g., 'x' or 'flow' or 'xy')
        * VarDim (List) : If your variable has indices, determine corresponding sets in a list (e.g., [I] or [I,J] where I=range(2), J=range(3))
        * VarBound (List) : If your variable has a specific bound, determine lb and ub in a list (e.g., [0, None], or [10, 30])

        '''

        match self.SolutionMethod:

            case 'exact':

                self.ToTalVariableCounter, self.BinaryVariableCounter = UpdateCounter(
                    VarDim, self.ToTalVariableCounter, self.BinaryVariableCounter)

                match self.InterfaceName:

                    # 1
                    case 'pulp':

                        from .VariableFactory import PulpVariableGenerator
                        return PulpVariableGenerator.GenerateVariable(self.ModelObject, 'bvar', VarName, VarBound, VarDim)

                    # 2
                    case 'pyomo':

                        from .VariableFactory import PyomoVariableGenerator
                        return PyomoVariableGenerator.GenerateVariable(self.ModelObject, 'bvar', VarName, VarBound, VarDim)

                    # 3
                    case 'ortools':

                        from .VariableFactory import OrtoolsVariableGenerator
                        return OrtoolsVariableGenerator.GenerateVariable(self.ModelObject, 'bvar', VarName, VarBound, VarDim)

                    # 4
                    case 'gekko':

                        from .VariableFactory import GekkoVariableGenerator
                        return GekkoVariableGenerator.GenerateVariable(self.ModelObject, 'bvar', VarName, VarBound, VarDim)

                    # 5
                    case 'picos':

                        from .VariableFactory import PicosVariableGenerator
                        return PicosVariableGenerator.GenerateVariable(self.ModelObject, 'bvar', VarName, VarBound, VarDim)

                    # 6
                    case 'cvxpy':

                        from .VariableFactory import CvxpyVariableGenerator
                        return CvxpyVariableGenerator.GenerateVariable(self.ModelObject, 'bvar', VarName, VarBound, VarDim)

                    # 7
                    case 'cylp':

                        from .VariableFactory import CylpVariableGenerator
                        return CylpVariableGenerator.GenerateVariable(self.ModelObject, 'bvar', VarName, VarBound, VarDim)

                    # 8
                    case 'pymprog':

                        from .VariableFactory import PymprogVariableGenerator
                        return PymprogVariableGenerator.GenerateVariable(self.ModelObject, 'bvar', VarName, VarBound, VarDim)

                    # 9
                    case 'cplex':

                        from .VariableFactory import CplexVariableGenerator
                        return CplexVariableGenerator.GenerateVariable(self.ModelObject, 'bvar', VarName, VarBound, VarDim)

                    # 10
                    case 'gurobi':

                        from .VariableFactory import GurobiVariableGenerator
                        return GurobiVariableGenerator.GenerateVariable(self.ModelObject, 'bvar', VarName, VarBound, VarDim)

                    # 11
                    case 'xpress':

                        from .VariableFactory import XpressVariableGenerator
                        return XpressVariableGenerator.GenerateVariable(self.ModelObject, 'bvar', VarName, VarBound, VarDim)

                    # 12
                    case 'mip':

                        from .VariableFactory import MipVariableGenerator
                        return MipVariableGenerator.GenerateVariable(self.ModelObject, 'bvar', VarName, VarBound, VarDim)

                    # 13
                    case 'linopy':

                        from .VariableFactory import LinopyVariableGenerator
                        return LinopyVariableGenerator.GenerateVariable(self.ModelObject, 'bvar', VarName, VarBound, VarDim)

            case 'heuristic':

                if self.AgentProperties[0] == 'idle':

                    self.VariablesSpread[VarName] = [
                        self.ToTalVariableCounter[1], 0]
                    self.ToTalVariableCounter, self.BinaryVariableCounter = UpdateCounter(
                        VarDim, self.ToTalVariableCounter, self.BinaryVariableCounter)
                    self.VariablesSpread[VarName][1] = self.ToTalVariableCounter[1]
                    self.VariablesType[VarName] = 'bvar'
                    self.VariablesBound[VarName] = VarBound
                    self.VariablesDim[VarName] = VarDim

                    return EMPTY(0)

                else:

                    if self.Vectorized == False:

                        if VarDim == 0:
                            return np.round(VarBound[0] + self.AgentProperties[self.VariablesSpread[VarName][0]:self.VariablesSpread[VarName][1]] * (VarBound[1] - VarBound[0]))
                        else:
                            def var(*args):
                                self.NewAgentProperties = np.round(
                                    VarBound[0] + self.AgentProperties[self.VariablesSpread[VarName][0]:self.VariablesSpread[VarName][1]] * (VarBound[1] - VarBound[0]))
                                return self.NewAgentProperties[sum(args[i]*mt.prod(len(VarDim[j]) for j in range(i+1, len(VarDim))) for i in range(len(VarDim)))]
                            return var

                    if self.Vectorized == 'FelooPyMethod':

                        if VarDim == 0:
                            return np.round(VarBound[0] + self.AgentProperties[:,self.VariablesSpread[VarName][0]:self.VariablesSpread[VarName][1]] * (VarBound[1] - VarBound[0]))
                        else:
                        
                            def var(*args):
                                self.NewAgentProperties = np.round(VarBound[0] + self.AgentProperties[:,self.VariablesSpread[VarName][0]:self.VariablesSpread[VarName][1]] * (VarBound[1] - VarBound[0]))
                                return self.NewAgentProperties[:,sum(args[i]*mt.prod(len(VarDim[j]) for j in range(i+1, len(VarDim))) for i in range(len(VarDim)))]
                            return var

    def set(self, *size):
        return range(*size)

    def card(self, set):
        return len(set)

    def uniform(self, lb, ub, dim=0):
        if dim == 0:
            return self.RNG.uniform(low=lb, high=ub)
        else:
            return self.RNG.uniform(low=lb, high=ub, size=([len(i) for i in dim]))

    def uniformint(self, lb, ub, dim=0):
        if dim == 0:
            return self.RNG.integers(low=lb, high=ub)
        else:
            return self.RNG.integers(low=lb, high=ub+1, size=([len(i) for i in dim]))

    def ivar(self, VarName: str, VarDim=0, VarBound=[0, None]):
        '''

        Integer Variable Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~

        * VarName (String): Determine a name for your variable (e.g., 'x' or 'flow' or 'xy')
        * VarDim (List) : If your variable has indices, determine corresponding sets in a list (e.g., [I] or [I,J] where I=range(2), J=range(3))
        * VarBound (List) : If your variable has a specific bound, determine lb and ub in a list (e.g., [0, None], or [10, 30])

        '''

        match self.SolutionMethod:

            case 'exact':

                self.ToTalVariableCounter, self.IntegerVariableCounter = UpdateCounter(
                    VarDim, self.ToTalVariableCounter, self.IntegerVariableCounter)

                match self.InterfaceName:

                    # 1
                    case 'pulp':

                        from .VariableFactory import PulpVariableGenerator
                        return PulpVariableGenerator.GenerateVariable(self.ModelObject, 'ivar', VarName, VarBound, VarDim)

                    # 2
                    case 'pyomo':

                        from .VariableFactory import PyomoVariableGenerator
                        return PyomoVariableGenerator.GenerateVariable(self.ModelObject, 'ivar', VarName, VarBound, VarDim)

                    # 3
                    case 'ortools':

                        from .VariableFactory import OrtoolsVariableGenerator
                        return OrtoolsVariableGenerator.GenerateVariable(self.ModelObject, 'ivar', VarName, VarBound, VarDim)

                    # 4
                    case 'gekko':

                        from .VariableFactory import GekkoVariableGenerator
                        return GekkoVariableGenerator.GenerateVariable(self.ModelObject, 'ivar', VarName, VarBound, VarDim)

                    # 5
                    case 'picos':

                        from .VariableFactory import PicosVariableGenerator
                        return PicosVariableGenerator.GenerateVariable(self.ModelObject, 'ivar', VarName, VarBound, VarDim)

                    # 6
                    case 'cvxpy':

                        from .VariableFactory import CvxpyVariableGenerator
                        return CvxpyVariableGenerator.GenerateVariable(self.ModelObject, 'ivar', VarName, VarBound, VarDim)

                    # 7
                    case 'cylp':

                        from .VariableFactory import CylpVariableGenerator
                        return CylpVariableGenerator.GenerateVariable(self.ModelObject, 'ivar', VarName, VarBound, VarDim)

                    # 8
                    case 'pymprog':

                        from .VariableFactory import PymprogVariableGenerator
                        return PymprogVariableGenerator.GenerateVariable(self.ModelObject, 'ivar', VarName, VarBound, VarDim)

                    # 9
                    case 'cplex':

                        from .VariableFactory import CplexVariableGenerator
                        return CplexVariableGenerator.GenerateVariable(self.ModelObject, 'ivar', VarName, VarBound, VarDim)

                    # 10
                    case 'gurobi':

                        from .VariableFactory import GurobiVariableGenerator
                        return GurobiVariableGenerator.GenerateVariable(self.ModelObject, 'ivar', VarName, VarBound, VarDim)

                    # 11
                    case 'xpress':

                        from .VariableFactory import XpressVariableGenerator
                        return XpressVariableGenerator.GenerateVariable(self.ModelObject, 'ivar', VarName, VarBound, VarDim)

                    # 12
                    case 'mip':

                        from .VariableFactory import MipVariableGenerator
                        return MipVariableGenerator.GenerateVariable(self.ModelObject, 'ivar', VarName, VarBound, VarDim)

                    # 13
                    case 'linopy':

                        from .VariableFactory import LinopyVariableGenerator
                        return LinopyVariableGenerator.GenerateVariable(self.ModelObject, 'ivar', VarName, VarBound, VarDim)

            case 'heuristic':

                if self.AgentProperties[0] == 'idle':

                    self.VariablesSpread[VarName] = [
                        self.ToTalVariableCounter[1], 0]
                    self.ToTalVariableCounter, self.IntegerVariableCounter = UpdateCounter(
                        VarDim, self.ToTalVariableCounter, self.IntegerVariableCounter)
                    self.VariablesSpread[VarName][1] = self.ToTalVariableCounter[1]
                    self.VariablesType[VarName] = 'ivar'
                    self.VariablesBound[VarName] = VarBound
                    self.VariablesDim[VarName] = VarDim

                    return EMPTY(0)

                else:
                    if self.Vectorized == False:
                        if VarDim == 0:
                            return np.floor(VarBound[0] + self.AgentProperties[self.VariablesSpread[VarName][0]:self.VariablesSpread[VarName][1]] * (VarBound[1] - VarBound[0]))
                        else:
                            def var(*args):
                                self.NewAgentProperties = np.floor(
                                    VarBound[0] + self.AgentProperties[self.VariablesSpread[VarName][0]:self.VariablesSpread[VarName][1]] * (VarBound[1] - VarBound[0]))
                                return self.NewAgentProperties[sum(args[i]*mt.prod(len(VarDim[j]) for j in range(i+1, len(VarDim))) for i in range(len(VarDim)))]
                            return var

                    if self.Vectorized == 'FelooPyMethod':
                        
                        if VarDim == 0:
                            return np.floor(VarBound[0] + self.AgentProperties[:,self.VariablesSpread[VarName][0]:self.VariablesSpread[VarName][1]] * (VarBound[1] - VarBound[0]))
                        else:
                            def var(*args):
                                self.NewAgentProperties = np.floor(VarBound[0] + self.AgentProperties[:,self.VariablesSpread[VarName][0]:self.VariablesSpread[VarName][1]] * (VarBound[1] - VarBound[0]))
                                return self.NewAgentProperties[:,sum(args[i]*mt.prod(len(VarDim[j]) for j in range(i+1, len(VarDim))) for i in range(len(VarDim)))]
                            return var

    def svar(self, VarName: str, VarDim=0):
        '''

        Sequential Variable Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        * VarName (String): Determine a name for your variable (e.g., 'x' or 'flow' or 'xy')
        * VarDim (List) : (Necessary) If your variable has indices, determine corresponding sets in a list (e.g., [I] where I=range(2))

        '''

        match self.SolutionMethod:

            case 'heuristic':

                if self.AgentProperties[0] == 'idle':

                    self.VariablesSpread[VarName] = [
                        self.ToTalVariableCounter[1], 0]
                    self.ToTalVariableCounter, self.IntegerVariableCounter = UpdateCounter(
                        VarDim, self.ToTalVariableCounter, self.IntegerVariableCounter)
                    self.VariablesSpread[VarName][1] = self.ToTalVariableCounter[1]
                    self.VariablesType[VarName] = 'svar'
                    self.VariablesDim[VarName] = VarDim

                    return EMPTY(0)

                else:

                    if self.Vectorized == False:
                        return np.argsort(self.AgentProperties[self.VariablesSpread[VarName][0]:self.VariablesSpread[VarName][1]])

                    if self.Vectorized == 'FelooPyMethod':
                        return np.argsort(self.AgentProperties[:,self.VariablesSpread[VarName][0]:self.VariablesSpread[VarName][1]])

    def pvar(self, VarName: str, VarDim=0, VarBound=[0, None]):
        '''

        Positive Variable Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        * VarName (String): Determine a name for your variable (e.g., 'x' or 'flow' or 'xy')
        * VarDim (List) : If your variable has indices, determine corresponding sets in a list (e.g., [I] or [I,J] where I=range(2), J=range(3))
        * VarBound (List) : If your variable has a specific bound, determine lb and ub in a list (e.g., [0, None], or [10, 30])

        '''

        match self.SolutionMethod:

            case 'exact':

                self.ToTalVariableCounter, self.PositiveVariableCounter = UpdateCounter(
                    VarDim, self.ToTalVariableCounter, self.PositiveVariableCounter)

                match self.InterfaceName:

                    # 1
                    case 'pulp':

                        from .VariableFactory import PulpVariableGenerator
                        return PulpVariableGenerator.GenerateVariable(self.ModelObject, 'pvar', VarName, VarBound, VarDim)

                    # 2
                    case 'pyomo':

                        from .VariableFactory import PyomoVariableGenerator
                        return PyomoVariableGenerator.GenerateVariable(self.ModelObject, 'pvar', VarName, VarBound, VarDim)

                    # 3
                    case 'ortools':

                        from .VariableFactory import OrtoolsVariableGenerator
                        return OrtoolsVariableGenerator.GenerateVariable(self.ModelObject, 'pvar', VarName, VarBound, VarDim)

                    # 4
                    case 'gekko':

                        from .VariableFactory import GekkoVariableGenerator
                        return GekkoVariableGenerator.GenerateVariable(self.ModelObject, 'pvar', VarName, VarBound, VarDim)

                    # 5
                    case 'picos':

                        from .VariableFactory import PicosVariableGenerator
                        return PicosVariableGenerator.GenerateVariable(self.ModelObject, 'pvar', VarName, VarBound, VarDim)

                    # 6
                    case 'cvxpy':

                        from .VariableFactory import CvxpyVariableGenerator
                        return CvxpyVariableGenerator.GenerateVariable(self.ModelObject, 'pvar', VarName, VarBound, VarDim)

                    # 7
                    case 'cylp':

                        from .VariableFactory import CylpVariableGenerator
                        return CylpVariableGenerator.GenerateVariable(self.ModelObject, 'pvar', VarName, VarBound, VarDim)

                    # 8
                    case 'pymprog':

                        from .VariableFactory import PymprogVariableGenerator
                        return PymprogVariableGenerator.GenerateVariable(self.ModelObject, 'pvar', VarName, VarBound, VarDim)

                    # 9
                    case 'cplex':

                        from .VariableFactory import CplexVariableGenerator
                        return CplexVariableGenerator.GenerateVariable(self.ModelObject, 'pvar', VarName, VarBound, VarDim)

                    # 10
                    case 'gurobi':

                        from .VariableFactory import GurobiVariableGenerator
                        return GurobiVariableGenerator.GenerateVariable(self.ModelObject, 'pvar', VarName, VarBound, VarDim)

                    # 11
                    case 'xpress':

                        from .VariableFactory import XpressVariableGenerator
                        return XpressVariableGenerator.GenerateVariable(self.ModelObject, 'pvar', VarName, VarBound, VarDim)

                    # 12
                    case 'mip':

                        from .VariableFactory import MipVariableGenerator
                        return MipVariableGenerator.GenerateVariable(self.ModelObject, 'pvar', VarName, VarBound, VarDim)

                    # 13
                    case 'linopy':

                        from .VariableFactory import LinopyVariableGenerator
                        return LinopyVariableGenerator.GenerateVariable(self.ModelObject, 'pvar', VarName, VarBound, VarDim)

            case 'heuristic':

                if self.AgentProperties[0] == 'idle':

                    self.VariablesSpread[VarName] = [
                        self.ToTalVariableCounter[1], 0]
                    self.ToTalVariableCounter, self.PositiveVariableCounter = UpdateCounter(
                        VarDim, self.ToTalVariableCounter, self.PositiveVariableCounter)
                    self.VariablesSpread[VarName][1] = self.ToTalVariableCounter[1]
                    self.VariablesType[VarName] = 'pvar'
                    self.VariablesBound[VarName] = VarBound
                    self.VariablesDim[VarName] = VarDim

                    return EMPTY(0)

                else:
                    if self.Vectorized == False:

                        if VarDim == 0:
                            return VarBound[0] + self.AgentProperties[self.VariablesSpread[VarName][0]:self.VariablesSpread[VarName][1]] * (VarBound[1] - VarBound[0])
                        else:
                            def var(*args):
                                self.NewAgentProperties = (
                                    VarBound[0] + self.AgentProperties[self.VariablesSpread[VarName][0]:self.VariablesSpread[VarName][1]] * (VarBound[1] - VarBound[0]))
                                return self.NewAgentProperties[sum(args[i]*mt.prod(len(VarDim[j]) for j in range(i+1, len(VarDim))) for i in range(len(VarDim)))]
                            return var
                    if self.Vectorized == 'FelooPyMethod':
                        
                        if VarDim == 0:
                            return VarBound[0] + self.AgentProperties[:,self.VariablesSpread[VarName][0]:self.VariablesSpread[VarName][1]] * (VarBound[1] - VarBound[0])
                        else:
                            def var(*args):
                                self.NewAgentProperties = (VarBound[0] + self.AgentProperties[:,self.VariablesSpread[VarName][0]:self.VariablesSpread[VarName][1]] * (VarBound[1] - VarBound[0]))
                                return self.NewAgentProperties[:,sum(args[i]*mt.prod(len(VarDim[j]) for j in range(i+1, len(VarDim))) for i in range(len(VarDim)))]
                            return var

    def fvar(self, VarName: str, VarDim=0, VarBound=[0, None]):
        
        '''

        Free Variable Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~

        * VarName (String): Determine a name for your variable (e.g., 'x' or 'flow' or 'xy')
        * VarDim (List) : If your variable has indices, determine corresponding sets in a list (e.g., [I] or [I,J] where I=range(2), J=range(3))
        * VarBound (List) : If your variable has a specific bound, determine lb and ub in a list (e.g., [0, None], or [10, 30])

        '''

        match self.SolutionMethod:

            case 'exact':

                self.ToTalVariableCounter, self.FreeVariableCounter = UpdateCounter(
                    VarDim, self.ToTalVariableCounter, self.FreeVariableCounter)

                match self.InterfaceName:

                    # 1
                    case 'pulp':

                        from .VariableFactory import PulpVariableGenerator
                        return PulpVariableGenerator.GenerateVariable(self.ModelObject, 'fvar', VarName, VarBound, VarDim)

                    # 2
                    case 'pyomo':

                        from .VariableFactory import PyomoVariableGenerator
                        return PyomoVariableGenerator.GenerateVariable(self.ModelObject, 'fvar', VarName, VarBound, VarDim)

                    # 3
                    case 'ortools':

                        from .VariableFactory import OrtoolsVariableGenerator
                        return OrtoolsVariableGenerator.GenerateVariable(self.ModelObject, 'fvar', VarName, VarBound, VarDim)

                    # 4
                    case 'gekko':

                        from .VariableFactory import GekkoVariableGenerator
                        return GekkoVariableGenerator.GenerateVariable(self.ModelObject, 'fvar', VarName, VarBound, VarDim)

                    # 5
                    case 'picos':

                        from .VariableFactory import PicosVariableGenerator
                        return PicosVariableGenerator.GenerateVariable(self.ModelObject, 'fvar', VarName, VarBound, VarDim)

                    # 6
                    case 'cvxpy':

                        from .VariableFactory import CvxpyVariableGenerator
                        return CvxpyVariableGenerator.GenerateVariable(self.ModelObject, 'fvar', VarName, VarBound, VarDim)

                    # 7
                    case 'cylp':

                        from .VariableFactory import CylpVariableGenerator
                        return CylpVariableGenerator.GenerateVariable(self.ModelObject, 'fvar', VarName, VarBound, VarDim)

                    # 8
                    case 'pymprog':

                        from .VariableFactory import PymprogVariableGenerator
                        return PymprogVariableGenerator.GenerateVariable(self.ModelObject, 'fvar', VarName, VarBound, VarDim)

                    # 9
                    case 'cplex':

                        from .VariableFactory import CplexVariableGenerator
                        return CplexVariableGenerator.GenerateVariable(self.ModelObject, 'fvar', VarName, VarBound, VarDim)

                    # 10
                    case 'gurobi':

                        from .VariableFactory import GurobiVariableGenerator
                        return GurobiVariableGenerator.GenerateVariable(self.ModelObject, 'fvar', VarName, VarBound, VarDim)

                    # 11
                    case 'xpress':

                        from .VariableFactory import XpressVariableGenerator
                        return XpressVariableGenerator.GenerateVariable(self.ModelObject, 'fvar', VarName, VarBound, VarDim)

                    # 12
                    case 'mip':

                        from .VariableFactory import MipVariableGenerator
                        return MipVariableGenerator.GenerateVariable(self.ModelObject, 'fvar', VarName, VarBound, VarDim)

                    # 13
                    case 'linopy':

                        from .VariableFactory import LinopyVariableGenerator
                        return LinopyVariableGenerator.GenerateVariable(self.ModelObject, 'fvar', VarName, VarBound, VarDim)

            case 'heuristic':

                if self.AgentProperties[0] == 'idle':

                    self.VariablesSpread[VarName] = [
                        self.ToTalVariableCounter[1], 0]
                    self.ToTalVariableCounter, self.FreeVariableCounter = UpdateCounter(
                        VarDim, self.ToTalVariableCounter, self.FreeVariableCounter)
                    self.VariablesSpread[VarName][1] = self.ToTalVariableCounter[1]
                    self.VariablesType[VarName] = 'fvar'
                    self.VariablesBound[VarName] = VarBound
                    self.VariablesDim[VarName] = VarDim

                    return EMPTY(0)

                else:
                    if self.Vectorized == False:
                        if VarDim == 0:
                            return VarBound[0] + self.AgentProperties[self.VariablesSpread[VarName][0]:self.VariablesSpread[VarName][1]] * (VarBound[1] - VarBound[0])
                        else:
                            def var(*args):
                                self.NewAgentProperties = (VarBound[0] + self.AgentProperties[self.VariablesSpread[VarName][0]:self.VariablesSpread[VarName][1]] * (VarBound[1] - VarBound[0]))
                                return self.NewAgentProperties[sum(args[i]*mt.prod(len(VarDim[j]) for j in range(i+1, len(VarDim))) for i in range(len(VarDim)))]
                            return var

                    if self.Vectorized == 'FelooPyMethod':
                        
                        if VarDim == 0:
                            return VarBound[0] + self.AgentProperties[:, self.VariablesSpread[VarName][0]:self.VariablesSpread[VarName][1]] * (VarBound[1] - VarBound[0])
                        else:
                            def var(*args):
                                self.NewAgentProperties = (VarBound[0] + self.AgentProperties[:,self.VariablesSpread[VarName][0]:self.VariablesSpread[VarName][1]] * (VarBound[1] - VarBound[0]))
                                return self.NewAgentProperties[:,sum(args[i]*mt.prod(len(VarDim[j]) for j in range(i+1, len(VarDim))) for i in range(len(VarDim)))]
                            return var

    def con(self, MathematicalExpression):
        '''
        Constraint Definition
        ~~~~~~~~~~~~~~~~~~~~~

        MathematicalExpression: Provide the constraint (equality or inequality) (e.g., x+y<= 10 or x+y |l| 10 (if supported by the interface)) )

        '''
        
        match self.SolutionMethod:

            case 'exact':

                self.ConstraintsCounter[0] += 1

                self.ModelConstraints.append(MathematicalExpression)

                self.ConstraintsCounter[1] = len(self.ModelConstraints)

            case 'heuristic':

                if self.AgentProperties[0] == 'idle':

                    self.ConstraintsCounter[0] += 1

                    self.ModelConstraints.append(0)

                    self.ConstraintsCounter[1] = len(self.ModelConstraints)

                else:

                    self.ModelConstraints.append(MathematicalExpression)

                    self.ConstraintsViolation = np.amax(np.array([0]+self.ModelConstraints, dtype=object))


    def obj(self, MathematicalExpression, Direction=None):
        '''

        Objective Function Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        MathematicalExpression: Provide the objective function (e.g., x+y or sum(c[i,j]*x[i,j] for i,j in sets(I,J)) )

        '''

        match self.SolutionMethod:

            case 'exact':

                self.ObjectivesDirections.append(Direction)

                self.ObjectivesCounter[0] += 1

                self.ModelObjectives.append(MathematicalExpression)

                self.ObjectivesCounter[1] += len(self.ModelObjectives)

            case 'heuristic':

                if self.AgentProperties[0] == 'idle':

                    self.ObjectivesDirections.append(Direction)

                    self.ObjectivesCounter[0] += 1

                    self.ModelObjectives.append(0)

                    self.ObjectivesCounter[1] += len(self.ModelObjectives)

                else:

                    self.ModelObjectives.append(MathematicalExpression)

                    self.FitnessValue = self.ModelObjectives

    def PositiveVariable(self, VarName: str, VarDim=0, VarBound=[0, None]):
        '''

        Positive Variable Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        * VarName (String): Determine a name for your variable (e.g., 'x' or 'flow' or 'xy')
        * VarDim (List) : If your variable has indices, determine corresponding sets in a list (e.g., [I] or [I,J] where I=range(2), J=range(3))
        * VarBound (List) : If your variable has a specific bound, determine lb and ub in a list (e.g., [0, None], or [10, 30])

        '''
        return self.pvar(VarName, VarDim, VarBound)

    def BinaryVariable(self, VarName: str, VarDim=0, VarBound=[0, 1]):
        '''

        Binary Variable Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        * VarName (String): Determine a name for your variable (e.g., 'x' or 'flow' or 'xy')
        * VarDim (List) : If your variable has indices, determine corresponding sets in a list (e.g., [I] or [I,J] where I=range(2), J=range(3))
        * VarBound (List) : If your variable has a specific bound, determine lb and ub in a list (e.g., [0, 1])

        '''

        return self.bvar(VarName, VarDim, VarBound)

    def IntegerVariable(self, VarName: str, VarDim=0, VarBound=[0, None]):
        '''

        Integer Variable Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        * VarName (String): Determine a name for your variable (e.g., 'x' or 'flow' or 'xy')
        * VarDim (List) : If your variable has indices, determine corresponding sets in a list (e.g., [I] or [I,J] where I=range(2), J=range(3))
        * VarBound (List) : If your variable has a specific bound, determine lb and ub in a list (e.g., [0, None], or [10, 30])

        '''

        return self.ivar(VarName, VarDim, VarBound=[0, None])

    def FreeVariable(self, VarName: str, VarDim=0, VarBound=[None, None]):
        '''

        Free Variable Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~

        * VarName (String): Determine a name for your variable (e.g., 'x' or 'flow' or 'xy')
        * VarDim (List) : If your variable has indices, determine corresponding sets in a list (e.g., [I] or [I,J] where I=range(2), J=range(3))
        * VarBound (List) : If your variable has a specific bound, determine lb and ub in a list (e.g., [None, None], or [-10, 30])

        '''

        return self.fvar(VarName, VarDim, VarBound)

    def SequentialVariable(self, VarName: str, VarDim=0):
        '''

        Sequential Variable Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        * VarName (String): Determine a name for your variable (e.g., 'x' or 'flow' or 'xy')
        * VarDim (List) : (Necessary) If your variable has indices, determine corresponding sets in a list (e.g., [I] where I=range(2))

        '''
        return self.svar(VarName, VarDim)

    def Objective(self, MathematicalExpression):
        '''

        Objective Function Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        MathematicalExpression: Provide the objective function (e.g., x+y or sum(c[i,j]*x[i,j] for i,j in sets(I,J)) )

        '''

        self.obj(MathematicalExpression)

    def Constraint(self, MathematicalExpression):
        '''
        Constraint Definition
        ~~~~~~~~~~~~~~~~~~~~~

        MathematicalExpression: Provide the constraint (equality or inequality) (e.g., x+y<= 10 or x+y |l| 10 (if supported by the interface)) )

        '''

        self.con(MathematicalExpression)

    def sol(self, ObjectivesDirections=None, SolverName=None, AlgOptions=dict(), ObjectiveNumber=0, algoptions=None, NEOSEmail=None):
        '''

        Solve Definition
        ~~~~~~~~~~~~~~~~

        * ObjectivesDirections (List) : Provide a list containing the direction of the objectives (e.g., ['max'] or ['max', 'min'])
        * SolverName (String) : Provide a solver name that your desired interface supports (e.g., 'glpk', 'highs' ,'cplex' or 'gurobi')
        * ObjectiveNumber : Provide the number of the objective that is going to be optimized (default is 0)

        '''

        match self.SolutionMethod:

            case 'exact':

                self.ObjectiveBeingOptimized = ObjectiveNumber

                if self.ObjectivesDirections[0] == None:
                    self.ObjectivesDirections = ObjectivesDirections

                self.SolverName = SolverName

                match self.InterfaceName:

                    # 1
                    case 'pulp':

                        from .SolutionFactory import PulpSolutionGenerator
                        self.ModelSolution = PulpSolutionGenerator.GenerateSolution(self.ModelObject, self.ModelObjectives, self.ModelConstraints, self.ObjectivesDirections, SolverName, ObjectiveNumber, AlgOptions, NEOSEmail)

                    # 2
                    case 'pyomo':

                        from .SolutionFactory import PyomoSolutionGenerator
                        self.ModelSolution = PyomoSolutionGenerator.GenerateSolution(self.ModelObject, self.ModelObjectives, self.ModelConstraints, self.ObjectivesDirections, SolverName, ObjectiveNumber, AlgOptions, NEOSEmail)

                    # 3
                    case 'ortools':

                        from .SolutionFactory import OrtoolsSolutionGenerator
                        self.ModelSolution = OrtoolsSolutionGenerator.GenerateSolution(
                            self.ModelObject, self.ModelObjectives, self.ModelConstraints, self.ObjectivesDirections, SolverName, ObjectiveNumber)

                    # 4
                    case 'gekko':

                        from .SolutionFactory import GekkoSolutionGenerator
                        self.ModelSolution = GekkoSolutionGenerator.GenerateSolution(
                            self.ModelObject, self.ModelObjectives, self.ModelConstraints, self.ObjectivesDirections, SolverName, ObjectiveNumber)

                    # 5
                    case 'picos':

                        from .SolutionFactory import PicosSolutionGenerator
                        self.ModelSolution = PicosSolutionGenerator.GenerateSolution(
                            self.ModelObject, self.ModelObjectives, self.ModelConstraints, self.ObjectivesDirections, SolverName, ObjectiveNumber)

                    # 6
                    case 'cvxpy':

                        from .SolutionFactory import CvxpySolutionGenerator
                        self.ModelSolution = CvxpySolutionGenerator.GenerateSolution(
                            self.ModelObject, self.ModelObjectives, self.ModelConstraints, self.ObjectivesDirections, SolverName, ObjectiveNumber)

                    # 7
                    case 'cylp':

                        from .SolutionFactory import CylpSolutionGenerator
                        self.ModelSolution = CylpSolutionGenerator.GenerateSolution(
                            self.ModelObject, self.ModelObjectives, self.ModelConstraints, self.ObjectivesDirections, SolverName, ObjectiveNumber)

                    # 8
                    case 'pymprog':

                        from .SolutionFactory import PymprogSolutionGenerator
                        self.ModelSolution = PymprogSolutionGenerator.GenerateSolution(
                            self.ModelObject, self.ModelObjectives, self.ModelConstraints, self.ObjectivesDirections, SolverName, ObjectiveNumber)

                    # 9
                    case 'cplex':

                        from .SolutionFactory import CplexSolutionGenerator
                        self.ModelSolution = CplexSolutionGenerator.GenerateSolution(
                            self.ModelObject, self.ModelObjectives, self.ModelConstraints, self.ObjectivesDirections, SolverName, ObjectiveNumber)

                    # 10
                    case 'gurobi':

                        from .SolutionFactory import GurobiSolutionGenerator
                        self.ModelSolution = GurobiSolutionGenerator.GenerateSolution(
                            self.ModelObject, self.ModelObjectives, self.ModelConstraints, self.ObjectivesDirections, SolverName, ObjectiveNumber)

                    # 11
                    case 'xpress':

                        from .SolutionFactory import XpressSolutionGenerator
                        self.ModelSolution = XpressSolutionGenerator.GenerateSolution(
                            self.ModelObject, self.ModelObjectives, self.ModelConstraints, self.ObjectivesDirections, SolverName, ObjectiveNumber)

                    # 12
                    case 'mip':

                        from .SolutionFactory import MipSolutionGenerator
                        self.ModelSolution = MipSolutionGenerator.GenerateSolution(
                            self.ModelObject, self.ModelObjectives, self.ModelConstraints, self.ObjectivesDirections, SolverName, ObjectiveNumber)

                    # 13
                    case 'linopy':

                        from .SolutionFactory import LinopySolutionGenerator
                        self.ModelSolution = LinopySolutionGenerator.GenerateSolution(
                            self.ModelObject, self.ModelObjectives, self.ModelConstraints, self.ObjectivesDirections, SolverName, ObjectiveNumber)

            case 'heuristic':

                if self.AgentProperties[0] == 'idle':

                    self.ObjectiveBeingOptimized = ObjectiveNumber

                    if self.ObjectivesDirections[0] == None:
                        self.ObjectivesDirections = ObjectivesDirections

                    self.SolverName = SolverName

                    self.AlgOptions = AlgOptions

                else:

                    self.ObjectiveBeingOptimized = ObjectiveNumber

                    #if self.ObjectivesDirections[0] == None: self.ObjectivesDirections = ObjectivesDirections

                    if ObjectivesDirections[ObjectiveNumber] == 'max':
                        self.Result = self.FitnessValue[ObjectiveNumber] - \
                            self.PenaltyMultiplier * \
                            (self.ConstraintsViolation-0)**2
                    if ObjectivesDirections[ObjectiveNumber] == 'min':
                        self.Result = self.FitnessValue[ObjectiveNumber] + \
                            self.PenaltyMultiplier * \
                            (self.ConstraintsViolation-0)**2

     

    def Solve(self, SolverName=None, ObjectivesDirections=None, ObjectiveNumber=0):
        '''

        Solve Definition
        ~~~~~~~~~~~~~~~~

        * ObjectivesDirections (List) : Provide a list containing the direction of the objectives (e.g., ['max'] or ['max', 'min'])
        * SolverName (String) : Provide a solver name that your desired interface supports (e.g., 'glpk', 'highs' ,'cplex' or 'gurobi')
        * ObjectiveNumber : Provide the number of the objective that is going to be optimized (default is 0)

        '''

        match self.SolutionMethod:

            case 'exact':

                self.sol(ObjectivesDirections, SolverName, ObjectiveNumber)

    def get(self, VariableNameWithIndex):
        '''

        Solution Value Getter 
        ~~~~~~~~~~~~~~~~~~~~~

        * VariableNameWithIndex (Variable Object) : Enter the variable with its corresponding index (e.g., x[0,0])

        '''

        match self.SolutionMethod:

            case 'exact':

                match self.InterfaceName:

                    # 1
                    case 'pulp':

                        from .GetFactory import PulpGetter
                        return PulpGetter.Get(self.ModelObject, self.ModelSolution, 'variable', VariableNameWithIndex)

                    # 2
                    case 'pyomo':

                        from .GetFactory import PyomoGetter
                        return PyomoGetter.Get(self.ModelObject, self.ModelSolution, 'variable', VariableNameWithIndex)

                    # 3
                    case 'ortools':

                        from .GetFactory import OrtoolsGetter
                        return OrtoolsGetter.Get(self.ModelObject, self.ModelSolution, 'variable', VariableNameWithIndex)

                    # 4
                    case 'gekko':

                        from .GetFactory import GekkoGetter
                        return GekkoGetter.Get(self.ModelObject, self.ModelSolution, 'variable', VariableNameWithIndex)

                    # 5
                    case 'picos':

                        from .GetFactory import PicosGetter
                        return PicosGetter.Get(self.ModelObject, self.ModelSolution, 'variable', VariableNameWithIndex)

                    # 6
                    case 'cvxpy':

                        from .GetFactory import CvxpyGetter
                        return CvxpyGetter.Get(self.ModelObject, self.ModelSolution, 'variable', VariableNameWithIndex)

                    # 7
                    case 'cylp':

                        from .GetFactory import CylpGetter
                        return CylpGetter.Get(self.ModelObject, self.ModelSolution, 'variable', VariableNameWithIndex)

                    # 8
                    case 'pymprog':

                        from .GetFactory import PymprogGetter
                        return PymprogGetter.Get(self.ModelObject, self.ModelSolution, 'variable', VariableNameWithIndex)

                    # 9
                    case 'cplex':

                        from .GetFactory import CplexGetter
                        return CplexGetter.Get(self.ModelObject, self.ModelSolution, 'variable', VariableNameWithIndex)

                    # 10
                    case 'gurobi':

                        from .GetFactory import GurobiGetter
                        return GurobiGetter.Get(self.ModelObject, self.ModelSolution, 'variable', VariableNameWithIndex)

                    # 11
                    case 'xpress':

                        from .GetFactory import XpressGetter
                        return XpressGetter.Get(self.ModelObject, self.ModelSolution, 'variable', VariableNameWithIndex)

                    # 12
                    case 'mip':

                        from .GetFactory import MipGetter
                        return MipGetter.Get(self.ModelObject, self.ModelSolution, 'variable', VariableNameWithIndex)

                    # 13
                    case 'linopy':

                        from .GetFactory import LinopyGetter
                        return LinopyGetter.Get(self.ModelObject, self.ModelSolution, 'variable', VariableNameWithIndex)

    def get_obj(self):
        '''

        Solution Getter 
        ~~~~~~~~~~~~~~~

        * This function gets the value of the optimized objective function for you.

        '''

        match self.SolutionMethod:

            case 'exact':

                match self.InterfaceName:

                    # 1
                    case 'pulp':

                        from .GetFactory import PulpGetter
                        return PulpGetter.Get(self.ModelObject, self.ModelSolution, 'objective')

                    # 2
                    case 'pyomo':

                        from .GetFactory import PyomoGetter
                        return PyomoGetter.Get(self.ModelObject, self.ModelSolution, 'objective')

                    # 3
                    case 'ortools':

                        from .GetFactory import OrtoolsGetter
                        return OrtoolsGetter.Get(self.ModelObject, self.ModelSolution, 'objective')

                    # 4
                    case 'gekko':

                        from .GetFactory import GekkoGetter
                        return GekkoGetter.Get(self.ModelObject, self.ModelSolution, 'objective')

                    # 5
                    case 'picos':

                        from .GetFactory import PicosGetter
                        return PicosGetter.Get(self.ModelObject, self.ModelSolution, 'objective')

                    # 6
                    case 'cvxpy':

                        from .GetFactory import CvxpyGetter
                        return CvxpyGetter.Get(self.ModelObject, self.ModelSolution, 'objective')

                    # 7
                    case 'cylp':

                        from .GetFactory import CylpGetter
                        return CylpGetter.Get(self.ModelObject, self.ModelSolution, 'objective')

                    # 8
                    case 'pymprog':

                        from .GetFactory import PymprogGetter
                        return PymprogGetter.Get(self.ModelObject, self.ModelSolution, 'objective')

                    # 9
                    case 'cplex':

                        from .GetFactory import CplexGetter
                        return CplexGetter.Get(self.ModelObject, self.ModelSolution, 'objective')

                    # 10
                    case 'gurobi':

                        from .GetFactory import GurobiGetter
                        return GurobiGetter.Get(self.ModelObject, self.ModelSolution, 'objective')

                    # 11
                    case 'xpress':

                        from .GetFactory import XpressGetter
                        return XpressGetter.Get(self.ModelObject, self.ModelSolution, 'objective')

                    # 12
                    case 'mip':

                        from .GetFactory import MipGetter
                        return MipGetter.Get(self.ModelObject, self.ModelSolution, 'objective')

                    # 13
                    case 'linopy':

                        from .GetFactory import LinopyGetter
                        return LinopyGetter.Get(self.ModelObject, self.ModelSolution, 'objective')

    def get_status(self):
        '''

        Status Getter 
        ~~~~~~~~~~~~~

        * This function gets the status of the optimized model for you.

        '''

        match self.SolutionMethod:

            case 'exact':

                match self.InterfaceName:

                    # 1
                    case 'pulp':

                        from .GetFactory import PulpGetter
                        return PulpGetter.Get(self.ModelObject, self.ModelSolution, 'status')

                    # 2
                    case 'pyomo':

                        from .GetFactory import PyomoGetter
                        return PyomoGetter.Get(self.ModelObject, self.ModelSolution, 'status')

                    # 3
                    case 'ortools':

                        from .GetFactory import OrtoolsGetter
                        return OrtoolsGetter.Get(self.ModelObject, self.ModelSolution, 'status')

                    # 4
                    case 'gekko':

                        from .GetFactory import GekkoGetter
                        return GekkoGetter.Get(self.ModelObject, self.ModelSolution, 'status')

                    # 5
                    case 'picos':

                        from .GetFactory import PicosGetter
                        return PicosGetter.Get(self.ModelObject, self.ModelSolution, 'status')

                    # 6
                    case 'cvxpy':

                        from .GetFactory import CvxpyGetter
                        return CvxpyGetter.Get(self.ModelObject, self.ModelSolution, 'status')

                    # 7
                    case 'cylp':

                        from .GetFactory import CylpGetter
                        return CylpGetter.Get(self.ModelObject, self.ModelSolution, 'status')

                    # 8
                    case 'pymprog':

                        from .GetFactory import PymprogGetter
                        return PymprogGetter.Get(self.ModelObject, self.ModelSolution, 'status')

                    # 9
                    case 'cplex':

                        from .GetFactory import CplexGetter
                        return CplexGetter.Get(self.ModelObject, self.ModelSolution, 'status')

                    # 10
                    case 'gurobi':

                        from .GetFactory import GurobiGetter
                        return GurobiGetter.Get(self.ModelObject, self.ModelSolution, 'status')

                    # 11
                    case 'xpress':

                        from .GetFactory import XpressGetter
                        return XpressGetter.Get(self.ModelObject, self.ModelSolution, 'status')

                    # 12
                    case 'mip':

                        from .GetFactory import MipGetter
                        return MipGetter.Get(self.ModelObject, self.ModelSolution, 'status')

                    # 13
                    case 'linopy':

                        from .GetFactory import LinopyGetter
                        return LinopyGetter.Get(self.ModelObject, self.ModelSolution, 'status')

    def LoadfromExcel(self, DataFile: str, Dimension: list, RowDim: int, ColDim: int, IndexNames: str, SheetName: str, path=None):
        '''
        Multi-Dimensional Excel Parameter Reader 
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        *DataFile: Name of the dataset file (e.g., data.xlsx)
        *Dimension: Dimension of the dataset
        *RowDim: Number of indices that exist in each row from left (e.g., 0, 1, 2, 3...)
        *ColDim: Number of indices that exist in each column from top (e.g., 0, 1, 2, 3...)
        *IndexNames: The string which accompanies index counter (e.g., if row0, row1, ... and col0,col1, then index is ['row','col'])
        *SheetName: Name of the excel sheet in which the corresponding parameter exists.
        *Path: specify directory of the dataset file (if not provided, the dataset file should exist in the same directory as the code.)
        '''
        if path == None:
            data_file = os.path.join(sys.path[0], DataFile)
        else:
            data_file = path

        parameter = pd.read_excel(data_file, header=[i for i in range(ColDim)], index_col=[
            i for i in range(RowDim)], sheet_name=SheetName)

        if (RowDim == 1 and ColDim == 1) or (RowDim == 1 and ColDim == 0) or (RowDim == 0 and ColDim == 0) or (RowDim == 0 and ColDim == 1):

            return parameter.to_numpy()

        else:

            created_par = np.zeros(shape=([len(i) for i in Dimension]))

            for keys in it.product(*Dimension):

                try:

                    created_par[keys] = parameter.loc[tuple([IndexNames[i]+str(keys[i]) for i in range(
                        RowDim)]), tuple([IndexNames[i]+str(keys[i]) for i in range(RowDim, len(IndexNames))])]

                except:

                    created_par[keys] = None

            return created_par

    def get_cpt(self):
        '''

        Chronometer Getter 
        ~~~~~~~~~~~~~~~~~~

        * This function gets the duration of the optimization process for you.

        '''

        match self.SolutionMethod:

            case 'exact':

                match self.InterfaceName:

                    # 1
                    case 'pulp':

                        from .GetFactory import PulpGetter
                        return PulpGetter.Get(self.ModelObject, self.ModelSolution, 'time')

                    # 2
                    case 'pyomo':

                        from .GetFactory import PyomoGetter
                        return PyomoGetter.Get(self.ModelObject, self.ModelSolution, 'time')

                    # 3
                    case 'ortools':

                        from .GetFactory import OrtoolsGetter
                        return OrtoolsGetter.Get(self.ModelObject, self.ModelSolution, 'time')

                    # 4
                    case 'gekko':

                        from .GetFactory import GekkoGetter
                        return GekkoGetter.Get(self.ModelObject, self.ModelSolution, 'time')

                    # 5
                    case 'picos':

                        from .GetFactory import PicosGetter
                        return PicosGetter.Get(self.ModelObject, self.ModelSolution, 'time')

                    # 6
                    case 'cvxpy':

                        from .GetFactory import CvxpyGetter
                        return CvxpyGetter.Get(self.ModelObject, self.ModelSolution, 'time')

                    # 7
                    case 'cylp':

                        from .GetFactory import CylpGetter
                        return CylpGetter.Get(self.ModelObject, self.ModelSolution, 'time')

                    # 8
                    case 'pymprog':

                        from .GetFactory import PymprogGetter
                        return PymprogGetter.Get(self.ModelObject, self.ModelSolution, 'time')

                    # 9
                    case 'cplex':

                        from .GetFactory import CplexGetter
                        return CplexGetter.Get(self.ModelObject, self.ModelSolution, 'time')

                    # 10
                    case 'gurobi':

                        from .GetFactory import GurobiGetter
                        return GurobiGetter.Get(self.ModelObject, self.ModelSolution, 'time')

                    # 11
                    case 'xpress':

                        from .GetFactory import XpressGetter
                        return XpressGetter.Get(self.ModelObject, self.ModelSolution, 'time')

                    # 12
                    case 'mip':

                        from .GetFactory import MipGetter
                        return MipGetter.Get(self.ModelObject, self.ModelSolution, 'time')

                    # 13
                    case 'linopy':

                        from .GetFactory import LinopyGetter
                        return LinopyGetter.Get(self.ModelObject, self.ModelSolution, 'time')

    def dis(self, *VariableswithIndex):

        match self.SolutionMethod:

            case 'exact':

                for i in VariableswithIndex:

                    print(str(i)+'*:', self.get(i))

    def dis_status(self):

        match self.SolutionMethod:

            case 'exact':

                print('status: ', self.get_status())

    def dis_obj(self):

        match self.SolutionMethod:

            case 'exact':

                print('objective: ', self.get_obj())

    def inf(self):

        match self.SolutionMethod:

            case 'exact':

                from tabulate import tabulate as tb

                print()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(
                    f"   FelooPy ({Version}) - Released: {ReleaseDate}         ")
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

    def dis_model(self):

        match self.SolutionMethod:

            case 'exact':

                print('~~~~~~~~~~~~~~~~~~~~~~')
                print('model:', self.ModelName)
                print('~~~~~~~~~~~~~~~~~~~~~~')

                obdirs = 0
                for objective in self.ModelObjectives:
                    print(self.ObjectivesDirections[obdirs], objective)
                    obdirs += 1
                print('s.t.')
                for constraint in self.ModelConstraints:
                    print(constraint)
                print('~~~~~~~~~~~~~~~~~~~~~~')

    def dis_cpt(self):

        hour = round((self.get_cpt()/10**6), 3) % (24 * 3600) // 3600
        min = round((self.get_cpt()/10**6), 3) % (24 * 3600) % 3600 // 60
        sec = round((self.get_cpt()/10**6), 3) % (24 * 3600) % 3600 % 60

        match self.SolutionMethod:

            case 'exact':

                print(f'cpu time [{self.InterfaceName}]: ', self.get_cpt(
                ), '(micro seconds)', "%02d:%02d:%02d" % (hour, min, sec), '(h, m, s)')


def LoadfromExcel(DataFile: str, Dimension: list, RowDim: int, ColDim: int, IndexNames: str, SheetName: str, path=None):
    '''
    Multi-Dimensional Excel Parameter Reader 
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    *DataFile: Name of the dataset file (e.g., data.xlsx)
    *Dimension: Dimension of the dataset
    *RowDim: Number of indices that exist in each row from left (e.g., 0, 1, 2, 3...)
    *ColDim: Number of indices that exist in each column from top (e.g., 0, 1, 2, 3...)
    *IndexNames: The string which accompanies index counter (e.g., if row0, row1, ... and col0,col1, then index is ['row','col'])
    *SheetName: Name of the excel sheet in which the corresponding parameter exists.
    *Path: specify directory of the dataset file (if not provided, the dataset file should exist in the same directory as the code.)
    '''
    if path == None:
        data_file = os.path.join(sys.path[0], DataFile)
    else:
        data_file = path

    parameter = pd.read_excel(data_file, header=[i for i in range(ColDim)], index_col=[
                              i for i in range(RowDim)], sheet_name=SheetName)

    if (RowDim == 1 and ColDim == 1) or (RowDim == 1 and ColDim == 0) or (RowDim == 0 and ColDim == 0) or (RowDim == 0 and ColDim == 1):

        return parameter.to_numpy()

    else:

        created_par = np.zeros(shape=([len(i) for i in Dimension]))

        for keys in it.product(*Dimension):

            try:

                created_par[keys] = parameter.loc[tuple([IndexNames[i]+str(keys[i]) for i in range(
                    RowDim)]), tuple([IndexNames[i]+str(keys[i]) for i in range(RowDim, len(IndexNames))])]

            except:

                created_par[keys] = None

        return created_par


def sensitivity(ModelFunction, ParameterList, Range=[-10, 10], Step=1, Table=True, Plot=False, SavePlot=False, FileName='sensfig.png', PlotStyle='ggplot', Legend=None, XYtitle=['% Change', 'Objective Value'], Sizing=[[8, 6], 80]):
    '''

    Sensitivity Analyser
    ~~~~~~~~~~~~~~~~~~~~

    * ModelFunction (Function): The function that contains the model, its corresponding solve command, and returns its object.
    * ParameterList (List): A list of parameters (e.g., [a], or [a,b])
    * Range (List): A list of two values that specify the range of sensitivity analysis (e.g., [-10, 10] is between -10% and 10%)
    * Step (Integer): A number which specifies the step of change.
    * Table (Boolean): If a table of the results is required = True
    * Plot (Boolean): If a plot of the results is required = True
    * SavePlot (Boolean): If the plot should be saved = True (save directory is where the code is running)
    * FileName (String): The name and format of the file being saved (e.g., fig.png)
    * PlotStyle (String): Provide the style desired (e.g., 'seaborn-dark','seaborn-darkgrid','seaborn-ticks','fivethirtyeight','seaborn-whitegrid','classic','_classic_test','seaborn-talk', 'seaborn-dark-palette', 'seaborn-bright', 'seaborn-pastel', 'grayscale', 'seaborn-notebook', 'ggplot', 'seaborn-colorblind', 'seaborn-muted', 'seaborn', 'seaborn-paper', 'bmh', 'seaborn-white', 'dark_background', 'seaborn-poster', or 'seaborn-deep')
    * Legend (List): Provide the legend Required (e.g., ['a','b'])
    * XYtitle: Specify the x-axis and y-axis title
    * Sizing: Specify the size and dpi of the figure (e.g., [[8,6], 80] )
    '''

    OrigRange = Range.copy()

    ObjVals = [[] for i in ParameterList]

    NewParamValues = ParameterList.copy()

    data = [dict() for i in ParameterList]

    if Plot:
        plt.figure(figsize=(Sizing[0][0], Sizing[0][1]), dpi=Sizing[1])

    for i in range(0, len(ParameterList)):

        OriginalParameterValue = np.asarray(ParameterList[i])

        SensitivityPoints = []
        Percent = []

        Range = OrigRange.copy()

        diff = np.copy(Range[1]-Range[0])

        for j in range(0, diff//Step+1):

            Percent.append(Range[0])

            SensitivityPoints.append(OriginalParameterValue*(1+Range[0]/100))

            Range[0] += Step

        NewParamValues = ParameterList.copy()

        data[i]['points'] = SensitivityPoints

        for SensitivityPointofaParam in SensitivityPoints:

            NewParamValues[i] = SensitivityPointofaParam

            m = ModelFunction(*tuple(NewParamValues))

            ObjVals[i].append(m.get_obj())

        x = Percent
        y = ObjVals[i]

        data[i]['change'] = x
        data[i]['objective'] = y

        if Table:
            print()
            print(f"SENSITIVITY ANALYSIS (PARAM: {i+1})\n --------")
            print(
                tb({
                    "% change": x,
                    "objective value": y
                },
                    headers="keys", tablefmt="github"))
            print()

        if Plot:

            style.use(PlotStyle)

            default_x_ticks = range(len(x))

            plt.xlabel(XYtitle[0], size=12)

            plt.ylabel(XYtitle[1], size=12)

            if Legend == None:
                plt.plot(default_x_ticks, y,
                         label=f"Parameter {i}", linewidth=3.5)
            else:
                plt.plot(default_x_ticks, y, label=Legend[i], linewidth=3.5)

            plt.scatter(default_x_ticks, y)

            plt.xticks(default_x_ticks, x)

    if Plot and len(ParameterList) >= 2:

        plt.legend(loc="upper left")

    if Plot and SavePlot:

        plt.savefig(FileName, dpi=500)

    if Plot:
        plt.show()

    return pd.DataFrame(data)
