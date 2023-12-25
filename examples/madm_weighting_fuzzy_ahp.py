# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

# Example credit: https://github.com/Valdecy/pyDecision

from feloopy import *

m = madm('fuzzy_ahp','fuzzy_ahp_model', 'pydecision')

m.add_fcpcm([
    [ (  1,   1,   1), (  4,   5,   6), (  3,   4,   5), (  6,   7,   8) ],   
    [ (1/6, 1/5, 1/4), (  1,   1,   1), (1/3, 1/2, 1/1), (  2,   3,   4) ],   
    [ (1/5, 1/4, 1/3), (  1,   2,   3), (  1,   1,   1), (  2,   3,   4) ],   
    [ (1/8, 1/7, 1/6), (1/4, 1/3, 1/2), (1/4, 1/3, 1/2), (  1,   1,   1) ]    
    ])

m.sol()

m.report(show_tensors=True)