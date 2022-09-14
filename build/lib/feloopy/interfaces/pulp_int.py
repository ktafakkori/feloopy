import pulp as pulp_in
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
    def __init__(self, name="your_model", direction="min", interface="none"):
        self.name = name
        self.direction = direction
        self.interface = interface

    def modify(self, _name, _direction):
        self.name = _name
        self.direction = _direction


class interface(pyeo):
    def __init__(self, name="your_model", direction="min", interface="none"):
        self.name = name
        self.direction = direction
        self.interface = interface
        if self.direction == "min":
            self.pulp_model = pulp_in.LpProblem(name, pulp_in.LpMinimize)
        else:
            self.pulp_model = pulp_in.LpProblem(name, pulp_in.LpMaximize)
        super().__init__(name, direction, interface)

    def pvar(self, var_name, dim=0):
        self.dim = dim
        if self.dim == 0:
            return pulp_in.LpVariable(var_name, 0, None, pulp_in.LpContinuous)
        else:
            return {key: pulp_in.LpVariable(f"{var_name}{key}", 0, None, pulp_in.LpContinuous) for key in it.product(*dim)}

    def ivar(self, var_name, dim=0):
        self.dim = dim
        if self.dim == 0:
            return pulp_in.LpVariable(var_name, 0, None, pulp_in.LpInteger)
        else:
            return {key: pulp_in.LpVariable(f"{var_name}{key}", 0, None, pulp_in.LpInteger) for key in it.product(*dim)}

    def bvar(self, var_name, dim=0):
        self.dim = dim
        if self.dim == 0:
            return pulp_in.LpVariable(var_name, 0, 1, pulp_in.LpBinary)
        else:
            return {key: pulp_in.LpVariable(f"{var_name}{key}", 0, 1, pulp_in.LpBinary) for key in it.product(*dim)}

    def fvar(self, var_name, dim=0):
        self.dim = dim
        if self.dim == 0:
            return pulp_in.LpVariable(var_name, None, None, pulp_in.LpContinuous)
        else:
            return {key: pulp_in.LpVariable(f"{var_name}{key}", None, None, pulp_in.LpContinuous) for key in it.product(*dim)}

    def obj(self, expr, dim=0):
        self.expr = expr
        self.dim = dim
        self.pulp_model += self.expr

    def con(self, expr):
        self.expr = expr
        self.pulp_model += self.expr

    def solve(self, solver, online=True, showmodel=False, solvemodel=True, showresult=False):
        self.showmodel = showmodel
        self.online = online
        self.solvemodel = solvemodel
        self.showresult = showresult
        self.solver = solver
        if solver == 'glpk':
            self.solver = pulp_in.GLPK_CMD()
        if solver == 'pyglpk':
            self.solver = pulp_in.PYGLPK()
        if solver == 'cplex_cmd':
            self.solver = pulp_in.CPLEX_CMD()
        if solver == 'cplex':
            self.solver = pulp_in.CPLEX_PY()
        if solver == 'gurobi':
            self.solver = pulp_in.GUROBI()
        if solver == 'gurobi_cmd':
            self.solver = pulp_in.GUROBI()
        if solver == 'mosek':
            self.solver = pulp_in.MOSEK()
        if solver == 'xpress':
            self.solver = pulp_in.XPRESS()
        if solver == 'cbc':
            self.solver = pulp_in.PULP_CBC_CMD()
        if solver == 'coin_cmd':
            self.solver = pulp_in.COIN_CMD()
        if solver == 'coinmp_dll':
            self.solver = pulp_in.COINMP_DLL()
        if solver == 'choco_cmd':
            self.solver = pulp_in.CHOCO_CMD()
        if solver == 'mipcl_cmd':
            self.solver = pulp_in.MIPCL_CMD()
        if solver == 'scip':
            self.solver = pulp_in.SCIP_CMD()

        if self.showmodel:
            print("Model:", self.pulp_model)
        if solvemodel:
            timer = begin("PuLP solved '%s' with %s solver |" %
                          (self.name, self.solver))
            self.result = self.pulp_model.solve(solver=self.solver)
            timer = end(timer)
        self.status = pulp_in.LpStatus[self.result]
        if showresult:
            print("Status --- \n", self.status)
            print("Objective --- \n", pulp_in.value(self.pulp_model.objective))
            print("Decision --- \n", [(variables.name, variables.varValue)
                  for variables in self.pulp_model.variables() if variables.varValue != 0])

    def display(self, *args):
        for i in args:
            print(str(i)+":", i.varValue)
        print("obj:", pulp_in.value(self.pulp_model.objective))

    def get_var(self, var):
        return var.value

    def get_obj(self):
        return -self.gekko_model.options.objfcnval

    def available_solvers(self):
        print(pulp_in.listSolvers())
