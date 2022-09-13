from ortools.linear_solver import pywraplp as ortools_in
import itertools as it
import timeit


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
        
class ortools_op(pyeo):
    def __init__(self, name="your model", direction="min", interface="none"):
        self.name = name
        self.direction = direction
        self.interface = interface
        self.ortools_model = ortools_in.Solver.CreateSolver('SCIP')

        super().__init__(name, direction, interface)

    def pvar(self, var_name, dim=0):
        self.dim = dim
        if self.dim == 0:
            return self.ortools_model.NumVar(0, self.ortools_model.infinity(), var_name)
        else:
            return {key: self.ortools_model.NumVar(0, self.ortools_model.infinity(), f"{var_name}{key}") for key in it.product(*dim)}

    def ivar(self, var_name, dim=0):
        self.dim = dim
        if self.dim == 0:
            return self.ortools_model.IntVar(0, self.ortools_model.infinity(), var_name)
        else:
            return {key: self.ortools_model.IntVar(0, self.ortools_model.infinity(), f"{var_name}{key}") for key in it.product(*dim)}

    def bvar(self, var_name, dim=0):
        self.dim = dim
        if self.dim == 0:
            return self.ortools_model.BinVar(0, 1, var_name)
        else:
            return {key: self.ortools_model.BinVar(0, 1, f"{var_name}{key}") for key in it.product(*dim)}

    def fvar(self, var_name, dim=0):
        self.dim = dim
        if self.dim == 0:
            return self.ortools_model.NumVar(-self.ortools_model.infinity(), self.ortools_model.infinity(), var_name)
        else:
            return {key: self.ortools_model.NumVar(-self.ortools_model.infinity(), self.ortools_model.infinity(), f"{var_name}{key}") for key in it.product(*dim)}

    def obj(self, expr, dim=0):
        self.expr = expr
        self.dim = dim
        if self.direction == "max":
            self.ortools_model.Maximize(expr)
        else:
            self.ortools_model.Minimize(expr)

    def con(self, expr):
        self.expr = expr
        self.ortools_model.Add(expr)

    def solve(self, solver, online=True, showmodel=False, solvemodel=True, showresult=False):
        self.showmodel = showmodel
        self.online = online
        self.solvemodel = solvemodel
        self.showresult = showresult
        self.solver = solver
        self.ortools_model.CreateSolver(self.solver)
        if self.showmodel:
            "None"
        if solvemodel:
            timer = begin("ORTOOLs solved '%s' with %s solver |" %
                          (self.name, self.solver))

            self.ortools_model.Solve()
            timer = end(timer)
        self.status = ortools_in.Solver
        if showresult:
            print("Status --- \n", self.status)
            print("Objective --- \n",
                  self.ortools_model.Objective().Value())

    def display(self, *args):
        for i in args:
            print(str(i)+":", i.solution_value())
        print("obj:", self.ortools_model.Objective().Value())

    def get_var(self, var):
        return var.solution_value()

    def get_obj(self):
        return self.ortools_model.Objective().Value()

    def available_solvers(self):
        "None"
