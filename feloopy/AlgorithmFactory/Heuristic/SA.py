import numpy as np

class SA:

    # [CLASS] [ANNOTATION]
    F: int
    S: int
    T: int
    D: list
    R: int
    PIE: np.ndarray
    Best: np.ndarray

    Cc = int
    Mt = int

    def __init__(self, F: int, D: list, S: int, T: int, Cc: int, Mt: int):
        
        '''
        Simulated Annealing (SA) (Official version)
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
        @article{Kirkpatrick1983May,
            author = {Kirkpatrick, S. and Gelatt, Jr., C. D. and Vecchi, M. P.},
            title = {{Optimization by Simulated Annealing}},
            journal = {Science},
            volume = {220},
            number = {4598},
            pages = {671--680},
            year = {1983},
            publisher = {American Association for the Advancement of Science},
            doi = {10.1126/science.220.4598.671}
        }

        Link
        ~~~~
        https://doi.org/10.1126/science.220.4598.671
        '''

        # [CLASS] [ATTRIBUTES]

        self.R = len(D)
        self.F = F
        self.S = S
        self.T = T
        self.D = np.asarray([1 if item == 'max' else -1 for item in D])

        self.Cc = Cc
        self.Mt = Mt

    # [CLASS] [METHOD]
    def solve(self, evaluate):

        # [AGENT] [INITIALIZE]
        self.PIE = np.random.rand(self.T, self.F+self.R)
        self.PIE[:, self.F:] = np.tile(np.array([-np.inf*d for d in self.D]), (self.T, 1))

        # [PARAM] [INITIALIZE]
        self.Best = self.PIE[-1]

        # [NEW AGENT] [CLONE]
        NEWPIE = np.copy(self.PIE)

        for s in range(0, self.S):

            # [PARAM] [UPDATE]
            temp = ((self.S-s)/self.S)*self.Mt

            for c in range(0, self.Cc):

                # [NEW AGENT] [EVALUATE]
                NEWPIE = evaluate(NEWPIE)

                # [AGENT] [UPDATE]

                #self.PIE[np.where((NEWPIE[:, self.F] > self.PIE[:, self.F]) | (np.random.rand() < np.exp(-abs(self.PIE[:, self.F]-NEWPIE[:, self.F])/temp)))] = NEWPIE[np.where((NEWPIE[:, self.F] > self.PIE[:, self.F]) | (np.random.rand() < np.exp(-abs(self.PIE[:, self.F]-NEWPIE[:, self.F])/temp)))]
                
                self.PIE = np.where((NEWPIE[:, self.F] > self.PIE[:, self.F]) | (np.random.rand() < np.exp(-abs(self.PIE[:, self.F]-NEWPIE[:, self.F])/temp)), NEWPIE, self.PIE)

                # [BEST] [UPDATE]
                self.Best = self.PIE[0] if self.D[0]*self.PIE[:,-1][0] > self.D[0]*self.Best[-1] else self.Best

                # [NEW AGENT] [Neighborhood Search]
                NEWPIE[:, 0:self.F] = np.clip(self.PIE[:, 0:self.F] + 2*np.random.rand(self.F)-1,0,1)

        return self.Best[:-1],self.Best[-1]