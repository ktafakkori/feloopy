# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

# Example credit: https://xiongpengnus.github.io/rsome/

from feloopy import *

m = target_model('exact', 'max_volume_box', 'rsome_ro')

A_wall = 200
A_floor = 150
alpha, beta = 0.8, 1.5
gamma, delta = 0.8, 1.5

x = m.pvar('x')
y = m.pvar('y')
z = m.pvar('z')
a = m.pvar('a')
b = m.pvar('b')

m.obj(x + y + z)

m.st(m.exponent(x + y) <= a)
m.st(m.exponent(z + y) <= b)
m.st(2 * (a+b) <= A_wall)
m.st(m.exponent(x + z) <= A_floor)
m.st(m.exponent(x - y) <= alpha)
m.st(m.exponent(y - x) <= beta)
m.st(m.exponent(x - z) <= gamma)
m.st(m.exponent(z - x) <= delta)

m.sol(['max'], 'ecos')
m.report()