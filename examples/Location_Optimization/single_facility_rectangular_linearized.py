from feloopy import *

#Environment
m = model('exact', 'sflp_rec', 'ortools') 

#Data
coords = np.array([[0, 0], [3, 16], [18, 2], [8, 18], [20, 2]]) # Coordinates of existing facilities
w = np.array([5,22,41,60,34]) # distance * per distance cost

#Sets
I = m.set(len(coords)) # Number of existing facilities
J = m.set(2) # Coordinates of new facility

#Decision variables
x = m.pvar('x', [J]) 
r = m.pvar('r', [J,I])
s = m.pvar('s', [J,I])

#Objective
m.obj(sum(w[i]*(r[j,i]+s[j,i]) for i,j in sets(I,J)))

for i in I:
    for j in J:
        m.con(x[j] - r[j,i] + s[j,i] == coords[i][j]) 

#Solve
m.sol(['min'], 'scip')

m.dis_obj()
m.dis_variable(x[0],x[1])


