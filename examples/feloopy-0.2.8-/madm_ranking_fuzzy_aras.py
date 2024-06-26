# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

# Example credit: https://github.com/Valdecy/pyDecision

from feloopy import *

m = madm('fuzzy_aras','ahp_model', 'pydecision') 

m.add_fdm([
    [ (  3,   6,   9), (  5,   8,   9), (  5,   7,   9) ],   
    [ (  5,   7,   9), (  3,   7,   9), (  3,   5,   7) ],   
    [ (  5,   8,   9), (  3,   5,   7), (  1,   2,   3) ],   
    [ (  1,   2,   4), (  1,   4,   7), (  1,   2,   5) ]    
    ])

m.add_fwv([[ (  0.1,   0.2,   0.3), (  0.7,   0.8,   0.9), (  0.3,   0.5,   0.8) ]])

m.sol(['max', 'max', 'min'],show_log=False)

m.report(show_tensors=False)