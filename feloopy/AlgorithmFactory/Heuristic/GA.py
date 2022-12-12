import numpy as np

class GA:

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
        Genetic Algorithm (GA) (Classic version modified)
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        Date
        ~~~~
        1975

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

    # [CLASS] [METHOD]
    def solve(self, evaluate):

        # [AGENT] [INITIALIZE]
        self.PIE = np.random.rand(self.T, self.F+self.R)
        self.PIE[:, self.F:] = np.tile(np.array([-np.inf*d for d in self.D]), (self.T, 1))

        for s in range(0, self.S):
            
            # [AGENT] [EVALUATE]
            self.PIE = evaluate(self.PIE)
            
            # [AGENT] [SORT]
            self.PIE = self.PIE[np.argsort(self.PIE[:, self.F])]

            # [BEST] [UPDATE]
            self.Best = self.PIE[-1*(1+self.D[0])//2]

            # [AGENT] [SELECT] [ROULETTE WHEEL]
            self.PIE = self.PIE[[np.random.choice(self.T, p=(1+self.D[0])//2*(self.PIE[:, self.F]/np.sum(self.PIE[:, self.F])) + (-1+self.D[0])//2* ((self.PIE[:, self.F]/np.sum(self.PIE[:, self.F]))-1)) for t in range(0,self.T)]]

            # [AGENT] [CROSS]
            POOL = np.asarray([np.random.randint(0,self.T,2) if np.random.rand() < self.Cr else np.array([t,t]) for t in range(0,self.T)])
            self.PIE[:,:-1] = np.where((np.less.outer(np.array([np.random.randint(0,self.F) for t in range(0,self.T)]),np.arange(self.F))),self.PIE[POOL.T[0],:-1],self.PIE[POOL.T[1],:-1])
     
            # [AGENT] [MUTATE]
            self.PIE[:,:-1] = np.where((np.random.rand(self.T,self.F) < self.Mu), 1-self.PIE[:,:-1], self.PIE[:,:-1])

        return self.Best[:-1],self.Best[-1]