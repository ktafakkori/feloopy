# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

# Example credit: https://github.com/Valdecy/pyDecision

from feloopy import *

m = madm('multimoora','multimoora_model', 'pydecision')

m.add_dm([
        [33.95, 23.78, 11.45, 39.97, 29.44, 167.10,  3.852 ],   
        [38.90,  4.17,  6.32,  0.01,  4.29, 132.52, 25.184 ],   
        [37.59,  9.36,  8.23,  4.35, 10.22, 136.71, 10.845 ],   
        [30.44, 37.59, 13.91, 74.08, 45.10, 198.34,  2.186 ],   
        [36.21, 14.79,  9.17, 17.77, 17.06, 148.30,  6.610 ],   
        [37.80,  8.55,  7.97,  2.35,  9.25, 134.83, 11.935 ]    
        ])

m.sol(['min', 'min', 'min', 'min', 'max', 'min', 'max'],show_graph=False)

m.report(show_tensors=False)