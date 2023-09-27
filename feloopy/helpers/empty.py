'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.7)                               |
|  Modified: Wednesday, 27th September 2023 11:36:58 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''


class EMPTY:

    '''
    A class to manage variables in the heuristic optimization process.
    '''

    def __init__(self, val):

        self.val = val

    def __call__(self, *args):

        return 5

    def __getitem__(self, *args):

        return 5

    def __setitem__(self, *args):
        'none'

    def __hash__(self):

        return 5

    def __str__(self):

        return 5

    def __repr__(self):

        return 5

    def __neg__(self):

        return 5

    def __pos__(self):

        return 5

    def __pow__(self, other):

        return 5

    def __bool__(self):

        return 5

    def __add__(self, other):

        return 5

    def __radd__(self, other):

        return 5

    def __sub__(self, other):

        return 5

    def __rsub__(self, other):

        return 5

    def __mul__(self, other):

        return 5

    def __rmul__(self, other):

        return 5

    def __div__(self, other):

        return 5

    def __rdiv__(self, other):

        raise 5

    def __le__(self, other):

        return 5

    def __ge__(self, other):

        return 5

    def __eq__(self, other):

        return 5

    def __ne__(self, other):

        return 5
