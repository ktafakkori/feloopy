import numpy as np

class GWO:

    # [CLASS] [ANNOTATION]
    F: int
    S: int
    T: int
    D: list
    R: int
    PIE: np.ndarray
    Best: np.ndarray

    def __init__(self,  F: int, D: list, S: int, T: int):
        '''
        Grey Wolf Optimizer (GWO) (Official version)
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        Date
        ~~~~
        2014

        Parameters
        ~~~~~~~~~~
        * F (int): Numer of features, dimensions, or decision variables; e.g., 1, 2, ...
        * D (list): Directions of objectives; e.g., ['max', 'min', ...]
        * S (int): Number of iterations, states, or sequences; e.g., 10, 1000, ...
        * T (int): Number of search agents, or population members, e.g., 10, 50, ... 

        Reference 
        ~~~~~~~~~ 
        @article{Mirjalili2014Mar,
            author = {Mirjalili, Seyedali and Mirjalili, Seyed Mohammad and Lewis, Andrew},
            title = {{Grey Wolf Optimizer}},
            journal = {Advances in Engineering Software},
            volume = {69},
            pages = {46--61},
            year = {2014},
            publisher = {Elsevier},
            doi = {10.1016/j.advengsoft.2013.12.007}
        }

        Link
        ~~~~
        https://doi.org/10.1016/j.advengsoft.2013.12.007
        '''


        # [CLASS] [ATTRIBUTES]
        self.R = len(D)
        self.F = F
        self.S = S
        self.T = T
        self.D = np.asarray([1 if item == 'max' else -1 for item in D])

    # [CLASS] [METHOD]
    def solve(self, evaluate):

        # [AGENT] [INITIALIZE]
        self.PIE = np.random.rand(self.T, self.F+self.R)
        self.PIE[:, self.F:] = np.tile(np.array([-np.inf*d for d in self.D]), (self.T, 1))

        # [PARAM] [INITIALIZE]
        Alpha, Beta, Delta = np.copy(self.PIE[-1]), np.copy(self.PIE[-2]), np.copy(self.PIE[-3])

        for s in range(0, self.S):

            # [AGENT] [EVALUATE]
            self.PIE = evaluate(self.PIE)

            # [PARAM] [UPDATE]
            for i in range(0, self.T):

                if self.D ==1:

                    if self.PIE[i, self.F] > Alpha[self.F]: Alpha = np.copy(self.PIE[i])
                    if self.PIE[i, self.F] < Alpha[self.F] and self.PIE[i, self.F] > Beta[self.F]: Beta = np.copy(self.PIE[i])
                    if self.PIE[i, self.F] < Alpha[self.F] and self.PIE[i, self.F] < Beta[self.F] and self.PIE[i, self.F] > Delta[self.F]: Delta = np.copy(self.PIE[i])

                else:
                    if self.PIE[i, self.F] < Alpha[self.F]: Alpha = np.copy(self.PIE[i])
                    if self.PIE[i, self.F] > Alpha[self.F] and self.PIE[i, self.F] < Beta[self.F]: Beta = np.copy(self.PIE[i])
                    if self.PIE[i, self.F] > Alpha[self.F] and self.PIE[i, self.F] > Beta[self.F] and self.PIE[i, self.F] < Delta[self.F]: Delta = np.copy(self.PIE[i])

            # [BEST] [UPDATE]
            self.Best = Alpha

            # [PARAM] [GENERATION]
            A = 2*(1 - s/self.S)*(2*np.random.rand(self.T, self.F, 3)-1)
            C = 2*np.random.rand(self.T, self.F, 3)

            # [AGENT] [UPDATE]
            self.PIE[:, :-1] = np.clip((A[:, :, 0] - abs(C[:, :, 0] * Alpha[:-1] - self.PIE[:, :-1]))/3 + (A[:, :, 1] - abs(C[:, :, 1] * Beta[:-1] - self.PIE[:, :-1]))/3 + (A[:, :, 2] - abs(C[:, :, 2] * Delta[:-1] - self.PIE[:, :-1]))/3, 0, 1)
        
        return self.Best[:-1],self.Best[-1]