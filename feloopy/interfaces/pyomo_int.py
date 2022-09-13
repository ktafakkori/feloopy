import pyomo.environ as pyomo_in
import itertools as it
import timeit
import os


def begin(name):
    timer = [timeit.default_timer(), name]
    return timer


def end(timer):
    start = timer[0]
    end = timeit.default_timer()
    diff = end-start
    sec = round((end - start), 3) % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    print(timer[1], "CPT=", (end-start)*10**6, "(μs)",
          "%02d:%02d:%02d" % (hour, min, sec), "(h:m:s)")
    return diff


class pyeo:
    def __init__(self, name="your model", direction="min", interface="none"):
        self.name = name
        self.direction = direction
        self.interface = interface

    def modify(self, _name, _direction):
        self.name = _name
        self.direction = _direction

class pyomo_op(pyeo):

    def __init__(self, name="your model", direction="min", interface="none"):
        self.pyomo_model = pyomo_in.ConcreteModel()
        self.pyomo_model.constraint = pyomo_in.ConstraintList()
        self.name = name
        self.direction = direction
        self.interface = interface
        super().__init__(name, direction, interface)

    def pvar(self, var_name, dim=0):
        self.dim = dim
        if self.dim == 0:
            self.pyomo_model.add_component(var_name, pyomo_in.Var(
                initialize=0, domain=pyomo_in.NonNegativeReals))
        else:
            self.pyomo_model.add_component(var_name, pyomo_in.Var(
                [i for i in it.product(*dim)], domain=pyomo_in.NonNegativeReals))
        return self.pyomo_model.component(var_name)

    def ivar(self, var_name, dim=0):
        self.dim = dim
        if self.dim == 0:
            self.pyomo_model.add_component(
                var_name, pyomo_in.Var(domain=pyomo_in.NonNegativeIntegers))
        else:
            self.pyomo_model.add_component(var_name, pyomo_in.Var(
                [i for i in it.product(*dim)], domain=pyomo_in.NonNegativeIntegers))
        return self.pyomo_model.component(var_name)

    def bvar(self, var_name, dim=0):
        self.dim = dim
        if self.dim == 0:
            self.pyomo_model.add_component(
                var_name, pyomo_in.Var(domain=pyomo_in.Binary))
        else:
            self.pyomo_model.add_component(var_name, pyomo_in.Var(
                [i for i in it.product(*dim)], domain=pyomo_in.Binary))
        return self.pyomo_model.component(var_name)

    def fvar(self, var_name, dim=0):
        self.dim = dim
        if self.dim == 0:
            self.pyomo_model.add_component(
                var_name, pyomo_in.Var(domain=pyomo_in.Binary))
        else:
            self.pyomo_model.add_component(var_name, pyomo_in.Var(
                [i for i in it.product(*dim)], domain=pyomo_in.Binary))
        return self.pyomo_model.component(var_name)

    def obj(self, expr, dim=0):
        self.expr = expr
        self.dim = dim
        if self.direction == "min":
            self.pyomo_model.OBJ = pyomo_in.Objective(
                expr=expr, sense=pyomo_in.minimize)
        else:
            self.pyomo_model.OBJ = pyomo_in.Objective(
                expr=expr, sense=pyomo_in.maximize)

    def con(self, expr):
        self.expr = expr
        self.pyomo_model.constraint.add(expr=expr)

    def solve(self, solver, online=False, email='enter_your_email', showmodel=False, solvemodel=True, showresult=False):
        self.solver = solver
        self.showmodel = showmodel
        self.online = online
        self.solvemodel = solvemodel
        self.showresult = showresult
        self.email=email
        if self.showmodel:
            print("Model:", self.pyomo_model)
        if self.online:
            if self.solvemodel:
                os.environ['NEOS_EMAIL'] = self.email
                solver_manager = pyomo_in.SolverManagerFactory('neos')
                timer = begin("Pyomo solved '%s' with %s solver through NEOS |" % (
                    self.name, self.solver))
                self.results = solver_manager.solve(
                    self.pyomo_model, solver=self.solver)
                timer = end(timer)
        else:
            if solvemodel:
                solver_manager = pyomo_in.SolverFactory(self.solver)
                timer = begin("Pyomo solved '%s' with %s solver |" %
                              (self.name, self.solver))
                self.results = solver_manager.solve(self.pyomo_model)
                timer = end(timer)
                self.obj = pyomo_in.value(self.pyomo_model.OBJ)
        self.status = self.results.solver.termination_condition
        if showresult:
            print(self.status)
            print(self.results)
            pyomo_in.display(self.pyomo_model)

    def display(self, *args):
        for i in args:
            print(str(i)+":", pyomo_in.value(i))
        print("obj:", self.obj)

    def get_var(self, var):
        return pyomo_in.value(var)

    def get_obj(self):
        return self.obj

    def available_solvers(self):
        os.system("pyomo help --solvers")
