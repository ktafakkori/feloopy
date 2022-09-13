import feloopy.interfaces.pyomo_int as pyomo
import feloopy.interfaces.gekko_int as gekko
import feloopy.interfaces.ortools_int as ortools
import feloopy.interfaces.pulp_int as pulp

def test_pyomo():

    m = pyomo.interface(direction="max")
    x = m.pvar('x')
    y = m.ivar('y')

    m.obj(2*x+5*y)
    m.con(5*x+3*y <= 10)
    m.con(2*x+7*y <= 9)

    m.solve('glpk')
    m.display(x, y)


def test_gekko():

    m = gekko.interface(direction="max")
    x = m.pvar('x')
    y = m.ivar('y')

    m.obj(2*x+5*y)
    m.con(5*x+3*y <= 10)
    m.con(2*x+7*y <= 9)

    m.solve('apopt')
    m.display(x, y)


def test_ortools():
    m = ortools.interface(direction="max")
    x = m.pvar('x')
    y = m.ivar('y')

    m.obj(2*x+5*y)
    m.con(5*x+3*y <= 10)
    m.con(2*x+7*y <= 9)

    m.solve('glpk')
    m.display(x, y)


def test_pulp():

    m = pulp.interface(direction="max")
    x = m.pvar('x')
    y = m.ivar('y')

    m.obj(2*x+5*y)
    m.con(5*x+3*y <= 10)
    m.con(2*x+7*y <= 9)

    m.solve('glpk')
    m.display(x, y)
