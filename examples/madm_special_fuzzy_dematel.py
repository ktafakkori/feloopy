from feloopy import *

m = madm('fuzzy_dematel','fuzzy_dematel_model', 'pydecision')

m.add_fcim([
    #          g1              g2                g3                  g4
    [  (  0,   0, 1/4),  (  0, 1/4, 1/2),  (1/4, 1/2, 3/4),  (  0,   0, 1/4)  ],   #g1
    [  (1/2, 3/4,   1),  (  0,   0, 1/4),  (3/4,   1,   1),  (3/4,   1,   1)  ],   #g2
    [  (1/2, 3/4,   1),  (1/4, 1/2, 3/4),  (  0,   0, 1/4),  (  0, 1/4, 1/2)  ],   #g3
    [  (3/4,   1,   1),  (  0, 1/4, 1/2),  (1/4, 1/2, 3/4),  (  0,   0, 1/4)  ]    #g4
    ])

m.sol(show_graph=False)

m.report(show_tensors=False)