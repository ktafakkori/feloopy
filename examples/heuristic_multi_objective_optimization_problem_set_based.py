from feloopy import *

def instance(X):
    m = representor_model('heuristic','my_model','pymoo',X)
    x = m.bvar('x', bound= [0,2])
    m.obj(x[...,0]**2)
    m.obj((x[...,0]-2)**2)
    m.sol(['min','min'], 'ns-ga-ii', obj_id='all')
    return m[X]

m = implement(instance)
m.solve(show_log=True)
m.report(sys_info=True, dec_info=True, all_metrics=True)