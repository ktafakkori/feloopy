from feloopy import *

m = madm('entropy','entropy_model', 'pydecision')

m.add_dm([
        [0.22, 0.28, 0.24],
        [0.33, 0.32, 0.33],
        [0.44, 0.40, 0.43]
        ]
        )

m.sol(['min', 'min', 'min'])

m.report(show_tensors=False)