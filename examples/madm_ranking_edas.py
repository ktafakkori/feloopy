from feloopy import *

m = madm('edas','edas_model', 'pydecision')

m.add_dm([
            [250, 16, 12, 5],
            [200, 16, 8 , 3],
            [300, 32, 16, 4],
            [275, 32, 8 , 4],
            [225, 16, 16, 2]    
        ])

m.add_wv([0.35, 0.30, 0.20, 0.15])

m.sol(['min', 'max', 'max', 'max'])

m.report(show_tensors=False)