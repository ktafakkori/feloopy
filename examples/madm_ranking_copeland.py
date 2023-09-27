from feloopy import *

m = madm('copeland','copeland_model', 'pydecision')

m.add_dm([
        [7, 9, 9, 5],   
        [8, 7, 8, 7],  
        [9, 6, 8, 9],   
        [6, 7, 8, 6]
        ])

m.sol(['max', 'max', 'max', 'min'])

m.report(show_tensors=False)