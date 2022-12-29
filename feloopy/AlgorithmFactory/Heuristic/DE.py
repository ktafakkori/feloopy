import numpy as np

class DE:
    
    # [CLASS] [ANNOTATION]
    F: int
    S: int
    T: int
    D: list
    R: int
    PIE: np.ndarray
    Best: np.ndarray

    Cr: float
    Mu: float

    def __init__(self, F: int, D: list, S: int, T: int, Cr: float, Mu: float):
 
        '''
        Differential Evolution (DE) (Official version)
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        Date
        ~~~~
        1997

        Parameters
        ~~~~~~~~~~
        * F (int): Numer of features, dimensions, or decision variables [1,+inf)
        * D (list): Directions of objectives; e.g., ['max', 'min', ...]
        * S (int): Number of iterations, states, or sequences [1,+inf)
        * T (int): Number of search agents, or population members [2,+inf)
        * Cr (float): Crossover rate or probability [0,1]
        * Mu (float): Mutation rate or probability [0,1]

        Reference 
        ~~~~~~~~~ 
        @book{Gen1997Jan,
            author = {Gen, Mitsuo and Cheng, Runwei},
            title = {{Genetic Algorithms and Engineering Design}},
            year = {1997},
            publisher = {Wiley},
            address = {Hoboken, NJ, USA}
        }

        Link
        ~~~~
        https://www.wiley.com/en-us/Genetic+Algorithms+and+Engineering+Design+-p-9780471127413
        '''

        # [CLASS] [ATTRIBUTES]

        self.R = len(D)
        self.F = F
        self.S = S
        self.T = T
        self.D = np.asarray([1 if item == 'max' else -1 for item in D])

        self.Mu = Mu
        self.Cr = Cr

    def solve(self, evaluate):

        # [AGENT] [INITIALIZE]
        self.PIE = np.random.rand(self.T, self.F+self.R)
        self.PIE[:, self.F:] = np.tile(np.array([-np.inf*d for d in self.D]), (self.T, 1))

        # [PARAM] [INITIALIZE]
        self.Best = self.PIE[-1]

        # [NEW AGENT] [CLONE]
        NEWPIE = np.copy(self.PIE)

        for s in range(0, self.S):

            # [NEW AGENT] [EVALUATE]
            NEWPIE = evaluate(NEWPIE)

            # [AGENT] [UPDATE]
            self.PIE[np.where(self.D[0]*NEWPIE[:, self.F] > self.D[0]*self.PIE[:, self.F])] = NEWPIE[np.where(self.D[0]*NEWPIE[:, self.F] > self.D[0]*self.PIE[:, self.F])]

            # [AGENT] [SORT]
            self.PIE = self.PIE[np.argsort(self.PIE[:, self.F])]

            # [BEST] [UPDATE]
            self.Best = self.PIE[-1*(1+self.D[0])//2]

            for t in range(0, self.T):

                a, b, c = self.PIE[np.random.randint(0, self.PIE.shape[0], 3)]

                mutant = np.clip(a[:-1] + self.Mu * (b[:-1] - c[:-1]), 0, 1)

                cross_points = np.random.rand(self.F) < self.Cr

                if not np.any(cross_points):
                    cross_points[np.random.randint(0, self.F)] = True

                NEWPIE[t, :-1] = np.where(cross_points, mutant, self.PIE[t, :-1])

        return self.Best[:-1],self.Best[-1]


    def sort(self, old_agent):
        return old_agent[np.argsort(old_agent[:, self.F])]

    def display(self):
        print(self.Best)