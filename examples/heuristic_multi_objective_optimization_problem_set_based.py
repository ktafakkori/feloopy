from feloopy import *

def instance(X):
    m = representor_model('heuristic','my_model','pymoo',X)
    x = m.pvar('x', bound= [-1000,1000])
    m.obj(x[...,0]**2)
    m.obj((x[...,0]-2)**2)
    m.sol(['min','min'], 'ns-ga-ii', {'n_gen':100}, 'all')
    
    return m[X]

m = implement(instance)
m.solve(show_log=True)
m.report(sys_info=True, dec_info=True, all_metrics=True)