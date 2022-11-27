'''
Name: FelooPy
Version: 0.1.11
Contributors: Keivan Tafakkori
Date: 21 November 2022
License: MIT. (For more details please refer to LICENSE.txt file).
Copyright (c) 2022 Keivan Tafakkori & FELOOP (https://ktafakkori.github.io/)
'''


from feloopy.core import *
from feloopy.exact import *
from feloopy.heuristic import *

import math as mt
import pandas as pd


class empty:

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


class feloopy:

    def __init__(self, name, interface_name, agent=None, notactive=[True, dict()], vectorized=False):

        self.Agent = agent
        self.NotActive = notactive
        self.Vectorized = vectorized

        self.ModelName = name

        self.InterfaceName = interface_name

        if len(notactive[1]) == 0:
            self.ModelObject = model_maker[interface_name]()

        self.ObjectiveExpression = []

        self.ConstraintExpression = []

        self.Pvar_grp = 0
        self.Pvar_tot = 0
        self.Bvar_grp = 0
        self.Bvar_tot = 0
        self.Ivar_grp = 0
        self.Ivar_tot = 0
        self.Fvar_grp = 0
        self.Fvar_tot = 0
        self.TotVar_grp = 0
        self.TotVar_tot = 0
        self.Obj_tot = 0
        self.Con_tot = 0

        self.VarLength = dict()
        self.VarType = dict()
        self.VarBound = dict()
        self.VarDim = dict()
        self.VarName = []

    def __getitem__(self, indicator):
        if indicator[0]:
            return self
        else:
            return self.Result

    def pvar(self, var_name, dim=0, b=[0, 1]):
        if self.NotActive[0]:
            self.VarName.append(var_name)
            self.VarType[var_name] = 'pvar'
            self.VarBound[var_name] = b
            self.VarDim[var_name] = dim
            self.Pvar_grp += 1
            self.TotVar_grp += 1
            self.Pvar_tot += mt.prod(len(dims)
                                     for dims in dim) if dim != 0 else 1
            TotVar_old = self.TotVar_tot
            self.TotVar_tot += mt.prod(len(dims)
                                       for dims in dim) if dim != 0 else 1
            self.VarLength[var_name] = [TotVar_old, self.TotVar_tot]
            if self.InterfaceName not in {'ga'}:
                pass
            else:
                return empty(0)

        if type(self.Agent) == type(None):
            if b[1] == 1:
                b = [0, None]
            return pvar_maker[self.InterfaceName](self.ModelObject, var_name, b, dim)
        else:
            return pvar_maker[self.InterfaceName](var_name, self.Agent, self.NotActive[1][var_name], dim, b, self.Vectorized)

    def bvar(self, var_name, dim=0, b=[0, 1]):
        if self.NotActive[0]:
            self.VarName.append(var_name)
            self.VarType[var_name] = 'bvar'
            self.VarBound[var_name] = b
            self.VarDim[var_name] = dim
            self.Bvar_grp += 1
            self.TotVar_grp += 1
            self.Bvar_tot += mt.prod(len(dims)
                                     for dims in dim) if dim != 0 else 1
            TotVar_old = self.TotVar_tot
            self.TotVar_tot += mt.prod(len(dims)
                                       for dims in dim) if dim != 0 else 1
            self.VarLength[var_name] = [TotVar_old, self.TotVar_tot]
            if self.InterfaceName not in {'ga'}:
                pass
            else:
                return empty(0)

        if type(self.Agent) == type(None):
            return bvar_maker[self.InterfaceName](self.ModelObject, var_name, b, dim)
        else:
            return bvar_maker[self.InterfaceName](var_name, self.Agent, self.NotActive[1][var_name], dim, b, self.Vectorized)

    def ivar(self, var_name, dim=0, b=[0, 1]):
        if self.NotActive[0]:
            self.VarName.append(var_name)
            self.VarType[var_name] = 'ivar'
            self.VarBound[var_name] = b
            self.VarDim[var_name] = dim
            self.Ivar_grp += 1
            self.TotVar_grp += 1
            self.Ivar_tot += mt.prod(len(dims)
                                     for dims in dim) if dim != 0 else 1
            TotVar_old = self.TotVar_tot
            self.TotVar_tot += mt.prod(len(dims)
                                       for dims in dim) if dim != 0 else 1
            self.VarLength[var_name] = [TotVar_old, self.TotVar_tot]
            if self.InterfaceName not in {'ga'}:
                pass
            else:
                return empty(0)

        if type(self.Agent) == type(None):
            if b[1] == 1:
                b = [0, None]
            return ivar_maker[self.InterfaceName](self.ModelObject, var_name, b, dim)
        else:
            return ivar_maker[self.InterfaceName](var_name, self.Agent, self.NotActive[1][var_name], dim, b, self.Vectorized)

    def fvar(self, var_name, dim=0, b=[0, 1]):
        if self.NotActive[0]:
            self.VarName.append(var_name)
            self.VarType[var_name] = 'fvar'
            self.VarBound[var_name] = b
            self.VarDim[var_name] = dim
            self.Fvar_grp += 1
            self.TotVar_grp += 1
            self.Fvar_tot += mt.prod(len(dims)
                                     for dims in dim) if dim != 0 else 1
            TotVar_old = self.TotVar_tot
            self.TotVar_tot += mt.prod(len(dims)
                                       for dims in dim) if dim != 0 else 1
            self.VarLength[var_name] = [TotVar_old, self.TotVar_tot]
            if self.InterfaceName not in {'ga'}:
                pass
            else:
                return empty(0)

        if self.Agent == None:
            if b[1] == 1 or b[0] == 0:
                b = [None, None]
            return fvar_maker[self.InterfaceName](self.ModelObject, var_name, b, dim)
        else:

            return fvar_maker[self.InterfaceName](var_name, self.Agent, self.NotActive[1][var_name], dim, b, self.Vectorized)

    def obj(self, expr):
        self.Obj_tot += 1
        self.ObjectiveExpression.append(expr)

    def con(self, expr):
        self.Con_tot += 1
        self.ConstraintExpression.append(expr)

    def sol(self, dir, solvername, algoptions=None, objectivenumber=0, email=None):
        if type(self.Agent) == type(None) or self.NotActive:
            self.SolverName = solvername
            self.Direction = dir
            self.AlgOptions = algoptions
        if type(self.Agent) == type(None):
            self.Result, self.Chronometer = solver[self.InterfaceName](
                self.ModelObject, self.ObjectiveExpression, self.ConstraintExpression, dir, solvername, objectivenumber, algoptions, email)
            return self.Result
        else:
            self.Result = solver[self.InterfaceName](
                self.ObjectiveExpression, self.ConstraintExpression, dir, objectivenumber=0)

    def dis(self, *args,  showstatus=True, showobj=True):
        return show[self.InterfaceName](*args, modelobject=self.ModelObject, result=self.Result, showstatus=showstatus, showobj=showobj)

    def get(self, input):
        return variable_getter[self.InterfaceName](self.ModelObject, input)

    def get_stat(self):
        return status_getter[self.InterfaceName](self.ModelObject, self.Result)

    def get_obj(self):
        return objective_getter[self.InterfaceName](self.ModelObject, self.Result)

    def inf(self):
        return table(self.ModelName, self.InterfaceName, self.SolverName, self.Direction, self.Pvar_grp, self.Pvar_tot, self.Bvar_grp, self.Bvar_tot, self.Ivar_grp, self.Ivar_tot, self.Fvar_grp, self.Fvar_tot, self.TotVar_grp, self.TotVar_tot, self.Obj_tot, self.Con_tot)

    def ben(self, factor):
        return benchmark_int[self.InterfaceName](self.Chronometer, factor)

    def ava(self):
        return ava_solver[self.InterfaceName](self.InterfaceName)

    def dat(path, shape, row_dim, col_dim, index_names, sheet_name):
        parameter = pd.read_excel(path, header=[i for i in range(col_dim)], index_col=[
                                  i for i in range(row_dim)], sheet_name=sheet_name)
        created_par = np.zeros(shape=([len(i) for i in shape]))
        for keys in it.product(*shape):
            try:
                created_par[keys] = parameter.loc[tuple([index_names[i]+str(keys[i]) for i in range(
                    row_dim)]), tuple([index_names[i]+str(keys[i]) for i in range(row_dim, len(index_names))])]
            except:
                created_par[keys] = None
        return created_par


class implement:

    def __init__(self, model, timesimplemented=1, verbose=True):

        self.timesimplemented = timesimplemented
        self.usermodel = model
        self.fakemodel = self.seemodel()
        self.TotVar_tot = self.fakemodel.TotVar_tot
        self.ModelName = self.fakemodel.ModelName
        self.InterfaceName = self.fakemodel.InterfaceName
        self.SolverName = self.fakemodel.SolverName
        self.VarName = self.fakemodel.VarName
        self.VarLength = self.fakemodel.VarLength
        self.VarType = self.fakemodel.VarType
        self.VarBound = self.fakemodel.VarBound
        self.VarDim = self.fakemodel.VarDim
        self.Obj_tot = self.fakemodel.Obj_tot
        self.Con_tot = self.fakemodel.Con_tot
        self.Direction = self.fakemodel.Direction
        self.AlgOptions = self.fakemodel.AlgOptions
        self.Pvar_grp = self.fakemodel.Pvar_grp
        self.Pvar_tot = self.fakemodel.Pvar_tot
        self.Bvar_grp = self.fakemodel.Bvar_grp
        self.Bvar_tot = self.fakemodel.Bvar_tot
        self.Ivar_grp = self.fakemodel.Ivar_grp
        self.Ivar_tot = self.fakemodel.Ivar_tot
        self.Fvar_grp = self.fakemodel.Fvar_grp
        self.Fvar_tot = self.fakemodel.Fvar_tot
        self.TotVar_grp = self.fakemodel.TotVar_grp
        self.status = 'Not solved'
        self.result = None

        self.ModelObject = model_maker[self.InterfaceName](
            self.initiatemodel, self.TotVar_tot,  option_get[self.InterfaceName](self.AlgOptions))

    def sol(self):
        self.Result, self.Chronometer = implementor[self.InterfaceName](
            self.ModelObject, self.Direction)
        self.BestAgent = self.Result[0]
        self.BestObj = self.Result[1]

    def initiatemodel(self, x):
        return self.usermodel(x, [False, self.VarLength])

    def seemodel(self):
        return self.usermodel(0, [True, {0: 1}])

    def dis(self, *args, showstatus=True, showobj=True):
        data = [self.BestAgent, self.BestObj, self.Direction, self.VarBound,
                self.VarDim, showstatus, showobj, self.VarLength, self.VarType]
        return show[self.InterfaceName](*args, data=data)

    def inf(self):
        return table(self.ModelName, self.InterfaceName, self.SolverName, self.Direction, self.Pvar_grp, self.Pvar_tot, self.Bvar_grp, self.Bvar_tot, self.Ivar_grp, self.Ivar_tot, self.Fvar_grp, self.Fvar_tot, self.TotVar_grp, self.TotVar_tot, self.Obj_tot, self.Con_tot)

    def ben(self, factor):
        return benchmark_int[self.InterfaceName](self.ModelObject, [self.InterfaceName, self.ModelObject, self.Direction], factor)
