from feloopy import *
import os

I = range(4)
M = range(4)
T = range(2)
J = range(3)

data_file = os.path.join(sys.path[0], "data.xlsx")

par_h = data(data_file, [I,M,T,J], 2,2,['i','m','t','j'],"h") 

par_p = data(data_file, [I,T,J], 1,2,['i','t','j'],"p")