# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

from feloopy import *
import numpy as np

solution_method = 'heuristic'
interface = 'feloopy'

coords = np.array([[0, 0], [3, 16], [18, 2], [8, 18], [20, 2]])
w = np.array([5, 22, 41, 60, 34])

def instance(X):
    m = representor_model(solution_method, 'Rectangular distance', interface, X)
    I = range(len(coords))
    J = range(2)
    x = m.pvar('x', [J], [0, 100])
    m.obj(sum(w[i] * (((x[:, 0] - coords[i][0])**2) + ((x[:, 1] - coords[i][1])**2))**0.5 for i in I))
    m.sol(['min'], 'ga')
    return m[X]

m = implement(instance)
m.sol()
m.report()

def instance(X):
    m = representor_model(solution_method, 'Euclidean distance', interface, X)
    I = range(len(coords))
    J = range(2)
    x = m.pvar('x', [J], [0, 100])
    m.obj(sum(w[i] * (((x[:, 0] - coords[i][0])**2) + ((x[:, 1] - coords[i][1])**2))**0.5 for i in I))
    m.sol(['min'], 'ga')
    return m[X]

m = implement(instance)
m.sol()
m.report()

def instance(X):
    m = representor_model(solution_method, 'Squared Euclidean distance', interface, X)
    I = range(len(coords))
    J = range(2)
    x = m.pvar('x', [J], [0, 100])
    m.obj(sum(w[i] * ((x[:, 0] - coords[i][0])**2) for i in I) + sum(w[i] * ((x[:, 1] - coords[i][1])**2) for i in I))
    m.sol(['min'], 'ga')
    return m[X]

m = implement(instance)
m.sol()
m.report()

def instance(X):
    m = representor_model(solution_method, 'Minkowski distance', interface, X)
    I = range(len(coords))
    J = range(2)
    x = m.pvar('x', [J], [0, 100])
    p = 50
    m.obj(sum(w[i] * ((x[:,0] - coords[i][0])**p + (x[:,1] - coords[i][1])**p )**(1/p) for i in I))
    m.sol(['min'], 'ga')
    return m[X]

m = implement(instance)
m.sol()
m.report()
