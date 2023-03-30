from feloopy import *

def rep(X):

    #Environment
    m = model('heuristic', 'sflp_minkowski', 'feloopy', X) 

    #Data
    coords = np.array([[0, 0], [3, 16], [18, 2], [8, 18], [20, 2]]) # Coordinates of existing facilities
    w = np.array([5,22,41,60,34]) # distance * per distance cost
    p = 10**9

    #Sets
    I = m.set(len(coords)) # Number of existing facilities
    J = m.set(2) # Coordinates of new facility

    #Decision variables
    x = m.pvar('x', [J], [0,100]) 

    #Objective
    m.obj( sum( w[i] * ((x[:,0] - coords[i][0])**p + (x[:,1] - coords[i][1])**p )**(1/p) for i in I))

    #Solve
    m.sol(['min'], 'GA')

    return m[X]

m = implement(rep)
m.sol()
#Report
m.dis_obj()
print(m.get_variable(['x']))