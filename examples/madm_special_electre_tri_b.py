from feloopy import *

m = madm('electre_tri_b','electre_tri_b_model', 'pydecision')

m.add_dm([
        [75, 67, 85, 82, 90],   
        [28, 35, 70, 90, 95],   
        [98, 90, 70, 90, 95],   
        [29, 30, 30, 30, 35],   
        [12, 11, 12, 50, 75],   
        [44, 90, 30, 70, 35],   
        [45, 60, 55, 68, 60]    
        ])

m.add_qt([ 10,  10,  10,  10,  10,  10,  10,  10])
m.add_pt([ 20,  20,  20,  20,  20,  20,  20,  20])
m.add_vt([100, 100, 100, 100, 100, 100, 100, 100])
m.add_wv([ 1,  1,  1,  1,  1])
m.add_bt([[50, 48, 55, 55, 60], [70, 75, 80, 75, 85]])

m.sol(show_graph=False)

m.report(show_tensors=False)