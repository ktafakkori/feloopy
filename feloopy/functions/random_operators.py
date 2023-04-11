import numpy as np

def create_random_number_generator(key):
    """ For creating a random number generator with a fixed special seed.
    """
    return np.random.default_rng(key)