from feloopy import *

m = madm('macbeth','macbeth_model', 'pydecision')

m.add_dm([
        [6, 8, 4, 7],   
        [9, 3, 4, 6],   
        [4, 9, 7, 3],   
        [8, 2, 5, 8],   
        [4, 9, 2, 3],   
        [7, 5, 9, 9],   
        [9, 6, 3, 1],   
        [3, 5, 7, 6],   
        [5, 3, 8, 5],  
        [4, 6, 3, 8],  
        ])

m.add_wv( [0.25, 0.25, 0.25, 0.25])

m.sol( ['max', 'max', 'max', 'max'],show_graph=False)

m.report(show_tensors=False)