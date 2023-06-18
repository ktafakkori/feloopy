from feloopy import *

#Environment
m = target_model('exact', 'advertising problem', 'pulp', key=0)

#Dataset
c = [50, 100]
v = [28, 24]
p = np.array([[7,  2] , [2, 12]])

#Sets
I = range(len(c)) #Set of ads
J = range(len(v)) #Set of viewer types

#Variables
x = m.pvar('x', [I])

#Objective
m.obj(sum(c[i]*x[i] for i in I))

#Constraints
for j in J:
    m.con(sum(p[i,j]*x[i] for i in I) >= v[j])
    
#Solve
m.sol(['min'], 'glpk')

# Display
m.report()