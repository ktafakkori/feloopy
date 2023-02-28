from feloopy import *

I = range(4)
M = range(4)
T = range(2)
J = range(3)

par_h = load_from_excel("data.xlsx", [I,M,T,J], 2,2,['i','m','t','j'],"h") 

par_p = load_from_excel("data.xlsx", [I,T,J], 1,2,['i','t','j'],"p")
