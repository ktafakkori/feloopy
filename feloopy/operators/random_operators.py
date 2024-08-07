# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import numpy as np

def create_random_number_generator(key):
    """ Creates a random number generator with a fixed special seed.
    """
    return np.random.default_rng(key)
