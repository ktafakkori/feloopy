from feloopy import *

m = madm('electre_i_v','electre_i_v_model', 'pydecision')

m.add_dm([
            [15,  9, 6, 10],   
            [10,  5, 7,  8],   
            [22, 12, 1, 14],   
            [31, 10, 6, 18],  
            [ 8,  9, 0,  9]   
            ])

m.add_vt([2, 2, 2, 2])
m.add_wv([7, 3, 5, 6])

m.sol(show_graph=False)

m.report(show_tensors=False)
