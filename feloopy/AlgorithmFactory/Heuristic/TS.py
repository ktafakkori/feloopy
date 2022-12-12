import numpy as np

class TS:

    # [CLASS] [ANNOTATION]
    F: int
    S: int
    T: int
    D: list
    R: int
    PIE: np.ndarray
    Best: np.ndarray

    C: int

    def __init__(self, D=['max'], F=2, S=5, T=1, C=10):

        '''
        Tabu Search (TS) (Official version)
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        Date
        ~~~~
        1983

        Parameters
        ~~~~~~~~~~
        * F (int): Numer of features, dimensions, or decision variables [1,+inf)
        * D (list): Directions of objectives; e.g., ['max', 'min', ...]
        * S (int): Number of iterations, states, or sequences [1,+inf)
        * T (int): Number of search agents, or population members [2,+inf)
        * Cc (float): Number of cooling cycles [1,+inf)
        * Mt (float): Maximum temperature [100,+inf)

        Reference 
        ~~~~~~~~~ 
        @article{Glover1986Jan,
            author = {Glover, Fred},
            title = {{Future paths for integer programming and links to artificial intelligence}},
            journal = {Computers {\&} Operations Research},
            volume = {13},
            number = {5},
            pages = {533--549},
            year = {1986},
            month = jan,
            issn = {0305-0548},
            publisher = {Pergamon},
            doi = {10.1016/0305-0548(86)90048-1}
        }

        Link
        ~~~~
        https://doi.org/10.1016/0305-0548(86)90048-1
        '''

        # [CLASS] [ATTRIBUTES]

        self.R = len(D)
        self.F = F
        self.S = S
        self.T = T
        self.D = np.asarray([1 if item == 'max' else -1 for item in D])

        self.C = C

    def solve(self, evaluate):

        # [AGENT] [INITIALIZE]
        self.PIE = np.random.rand(self.T, self.F+self.R)
        self.PIE[:, self.F:] = np.tile(np.array([-np.inf*d for d in self.D]), (self.T, 1))

        # [PARAM] [INITIALIZE]
        self.Best = np.copy(self.PIE[:])
        T = []

        # [CLASS] [METHOD]
        for s in range(0, self.S):
            
            # [AGENT] [EVALUATE]
            self.PIE = evaluate(self.PIE)

            # [BEST] [UPDATE]
            if not self.PIE[:].tolist() in T and self.PIE[:,-1]>self.Best[:,-1]: 
                self.Best = np.copy(self.PIE)
            
            # [PARAM] [UPDATE]
            T.append(self.Best.tolist()[0])
            if len(T)>self.C: T.pop(0)

            # [AGENT] [Neighborhood Search]
            self.PIE[:, :-1] = np.clip(self.Best[:,:-1] + 2*np.random.rand(self.F)-1,0, 1)

  
        return self.Best[:,:-1][0],self.Best[:,-1][0]