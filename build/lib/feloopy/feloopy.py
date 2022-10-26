from feloopy.core import *
from feloopy.exact import *
from feloopy.heuristic import *

import math as mt

class empty:

    def __init__(self, val):
        self.val = val
    def __call__(self, *args):
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

    def __init__(self, name, interface_name, agent = None, notactive = None, vectorized = False):

        self.Agent = agent
        self.NotActive = notactive
        self.Vectorized = vectorized

        self.ModelName = name

        self.InterfaceName = interface_name

        if self.Agent == None: self.ModelObject = model_maker[interface_name]()

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

    def pvar(self, var_name, dim=0, b=[0, 1]):
        if self.Agent == None or self.NotActive:
            self.Pvar_grp += 1
            self.Pvar_tot += mt.prod(len(dims) for dims in dim) if dim !=0 else 1
            if self.NotActive:
                return empty(0)

        if self.Agent == None:
            return pvar_maker[self.InterfaceName](self.ModelObject, var_name, dim)
        else:
            return pvar_maker[self.InterfaceName](var_name, dim, b, self.Agent, self.Vectorized)

    def bvar(self, var_name, dim=0, b=[0,1]):
        if self.Agent == None or self.NotActive:
            self.Bvar_grp += 1
            self.Bvar_tot += mt.prod(len(dims) for dims in dim) if dim !=0 else 1
            if self.NotActive:
                return empty(0)

        if self.Agent == None:
            return bvar_maker[self.InterfaceName](self.ModelObject, var_name, dim)
        else:
            return bvar_maker[self.InterfaceName](var_name, dim, b, self.Agent, self.Vectorized)

    def ivar(self, var_name, dim=0, b=[0,1]):
        if self.Agent == None or self.NotActive:
            self.Ivar_grp += 1
            self.Ivar_tot += mt.prod(len(dims) for dims in dim) if dim !=0 else 1
            if self.NotActive:
                return empty(0)

        if self.Agent == None:
            return ivar_maker[self.InterfaceName](self.ModelObject, var_name, dim)
        else:
            return ivar_maker[self.InterfaceName](var_name, dim, b, self.Agent, self.Vectorized)

    def fvar(self, var_name, dim=0):
        if self.Agent == None or self.NotActive:
            self.Fvar_grp += 1
            self.Fvar_tot += mt.prod(len(dims) for dims in dim) if dim !=0 else 1
            if sellf.NotActive:
                return empty(0)
        if self.Agent == None:
            return fvar_maker[self.InterfaceName](self.ModelObject, var_name, dim)
        else:
            return fvar_maker[self.InterfaceName](var_name, dim, b, self.Agent, self.Vectorized)

    def obj(self, expr):
        self.Obj_tot += 1 
        self.ObjectiveExpression.append(expr)

    def con(self, expr):
        self.Con_tot += 1
        self.ConstraintExpression.append(expr)

    def sol(self, dir, solvername, objectivenumber=0, email=None):
        self.SolverName = solvername
        self.Direction = dir
        if self.Agent == None:
            self.Result, self.Chronometer = solver[self.InterfaceName](
                self.ModelObject, self.ObjectiveExpression, self.ConstraintExpression, dir, solvername, objectivenumber, email)
            return self.Result
        else:
            return solver[self.InterfaceName](objectiveslist, constraintslist, dir, objectivenumber=0)

    def dis(self, *args,  showstatus=True, showobj=True):
        return show[self.InterfaceName](*args, modelobject=self.ModelObject, result=self.Result, showstatus=showstatus, showobj=showobj)

    def get(self, input):
        return variable_getter[self.InterfaceName](input)

    def get_stat(self):
        return status_getter[self.InterfaceName](self.ModelObject,self.Result)

    def get_obj(self):
        return objective_getter[self.InterfaceName](self.ModelObject,self.Result)

    def inf(self):
        return table(self.ModelName, self.InterfaceName, self.SolverName, self.Direction, self.Pvar_grp, self.Pvar_tot, self.Bvar_grp, self.Bvar_tot, self.Ivar_grp, self.Ivar_tot, self.Fvar_grp, self.Fvar_tot, self.TotVar_grp, self.TotVar_tot, self.Obj_tot, self.Con_tot)

    def ben(self, factor):
        return benchmark_int[self.InterfaceName](self.Chronometer, factor)
    
    def ava(self):
        return ava_solver[self.InterfaceName](self.InterfaceName)


m = feloopy('milp', 'ortools')
x = m.pvar('x')
y = m.ivar('y')
m.obj(2*x)
m.con(5*x |e| 10)
m.ava()
m.sol('max','scip')
m.dis(x)