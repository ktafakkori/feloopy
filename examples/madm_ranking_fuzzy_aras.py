from feloopy import *

m = madm('fuzzy_aras','ahp_model', 'pydecision') 

m.add_fdm([
    [ (  3,   6,   9), (  5,   8,   9), (  5,   7,   9) ],   #a0
    [ (  5,   7,   9), (  3,   7,   9), (  3,   5,   7) ],   #a1
    [ (  5,   8,   9), (  3,   5,   7), (  1,   2,   3) ],   #a2
    [ (  1,   2,   4), (  1,   4,   7), (  1,   2,   5) ]    #a3
    ])

m.add_fwv([[ (  0.1,   0.2,   0.3), (  0.7,   0.8,   0.9), (  0.3,   0.5,   0.8) ]])

m.sol(['max', 'max', 'min'])

m.report(show_tensors=False)