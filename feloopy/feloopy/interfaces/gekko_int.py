import gekko as gekko_in
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


class gekko_op(pyeo):
    def __init__(self, name="your model", direction="min", interface="none"):
        self.gekko_model = gekko_in.GEKKO(remote=False)
        self.name = name
        self.direction = direction
        self.interface = interface

        super().__init__(name, direction, interface)

    def pvar(self, var_name, dim=0):
        self.dim = dim
        if self.dim == 0:
            return self.gekko_model.Var(lb=0, ub=None, integer=False)
        else:
            return {key: self.gekko_model.Var(lb=0, ub=None, integer=False) for key in it.product(*dim)}

    def ivar(self, var_name, dim=0):
        self.dim = dim
        if self.dim == 0:
            return self.gekko_model.Var(lb=0, ub=None, integer=True)
        else:
            return {key: self.gekko_model.Var(lb=0, ub=None, integer=True) for key in it.product(*dim)}

    def bvar(self, var_name, dim=0):
        self.dim = dim
        if self.dim == 0:
            return self.gekko_model.Var(lb=0, ub=1, integer=True)
        else:
            return {key: self.gekko_model.Var(lb=0, ub=1, integer=True) for key in it.product(*dim)}

    def fvar(self, var_name, dim=0):
        self.dim = dim
        if self.dim == 0:
            return self.gekko_model.Var()
        else:
            return {key: self.gekko_model.Var.Var() for key in it.product(*dim)}

    def obj(self, expr, dim=0):
        self.expr = expr
        self.dim = dim
        if self.direction == "min":
            self.gekko_model.Minimize(self.expr)
        else:
            self.gekko_model.Maximize(self.expr)

    def con(self, expr):
        self.expr = expr
        self.gekko_model.Equation(self.expr)

    def solve(self, solver, online=False, showmodel=False, solvemodel=True, showresult=False):
        self.solver = 1 if solver == "apopt" else 2 if solver == "bpopt" else 3 if solver == "ipopt" else None
        self.solvername = "apopt" if solver == "apopt" else "bpopt" if solver == "bpopt" else "ipopt" if solver == "ipopt" else "default"
        self.showmodel = showmodel
        self.online = online
        self.solvemodel = solvemodel
        self.showresult = showresult
        if self.showmodel:
            print("Model:", self.gekko_model)
        if self.online:
            gekko_in.GEKKO(remote=True)
            if self.solvemodel:
                timer = begin("Gekko solved '%s' with %s solver |" %
                              (self.name, self.solvername))
                self.gekko_model.solve(disp=False)
                timer = end(timer)
        else:
            if solvemodel:
                self.gekko_model.options.SOLVER = self.solver
                timer = begin("Gekko solved '%s' with %s solver |" %
                              (self.name, self.solvername))
                self.gekko_model.solve(disp=False)
                timer = end(timer)
        self.status = self.gekko_model.options.SOLVESTATUS
        if showresult:
            print(self.status)
            print(self.gekko_model)

    def display(self, *args):
        for i in args:
            print(str(i)+":", i.value)
        print("obj:", -self.gekko_model.options.objfcnval)

    def get_var(self, var):
        return var.value

    def get_obj(self):
        return -self.gekko_model.options.objfcnval

    def available_solvers(self):
        print("Gekko supports: apopt (free), bpopt (free), ipopt (free)")