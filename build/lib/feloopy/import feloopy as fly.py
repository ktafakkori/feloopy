from feloopy import *

def model(val):
    m = feloopy('milp', 'ortools')
    x = m.pvar('x',[range(2)])
    y = m.ivar('y',[range(2)])
    m.obj(2*val*x[0]+5*y[0])
    m.con(5*x[0] + 5*val*y[0] |l| 10)
    m.sol('max','scip')
    return m

val= 1
sensitivity(model, val, [-5,5], stepofchange=1, table=True, plot=True)

def instance(agent,active):
    m = feloopy('milp', 'ga', agent, active)
    x = m.pvar('x', [range(1)], b=[0,10])
    y = m.ivar('y', [range(1)], b=[0,10])
    m.obj(2*x[0]+5*y[0])
    m.con(5*x[0] + 5*y[0] |ll| 10)
    m.sol('max','ga',{'T': 10, 'S': 1000, 'Mu': 0.1, 'Cr': 0.5})
    return m[active]

m = implement(instance)
m.inf()
m.sol()
m.dis(['x',(0,)],['y',(0,)])
m.ben(['cpt',1])


