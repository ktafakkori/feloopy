'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.8)                               |
|  Modified: Wednesday, 27th September 2023 08:28:18 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''

import numpy as np
import warnings as wn

wn.filterwarnings("ignore")

class GWO:

    def __init__(self, f: int, d: list, s: int, t: int, **kwargs):

        self.d = np.asarray([1 if item == 'max' else -1 for item in d])
        self.r = 0 if len(d) == 1 else len(d)
        self.f = f
        self.it = s
        self.t = t
        self.features_cols = [0, self.f]
        self.status_col = [-2]
        self.reward_col = [-1]
        self.single_objective_tot = self.f + 1 + 1
        self.solve = self.run

    def run(self, evaluate):

        self.evaluate = evaluate
        self.initialize()
        for self.it_no in range(0, self.it):
            self.update()
            self.vary()
        return self.report()

    def initialize(self):

        if self.r == 0:
            self.pie = np.random.rand(self.t, self.single_objective_tot)
            self.pie[:, self.reward_col] = - np.inf * self.d
            self.pie[:, self.status_col] = 0
            self.bad_status = -1
            self.best_index = -1*(1+self.d[0])//2
        self.alpha, self.beta, self.delta = np.copy(
            self.pie[-1]), np.copy(self.pie[-2]), np.copy(self.pie[-3])
        self.best = self.pie[-1].copy()

    def update(self):

        self.pie = self.evaluate(self.pie)
        if self.r == 0:
            self.pie = self.pie[np.argsort(self.pie[:, self.reward_col[0]])]
            if self.d[0]*self.pie[self.best_index][-1] > self.d[0]*self.best[-1]:
                self.best = self.pie[self.best_index].copy()
            self.alpha = self.pie[:, -1].copy()
            self.beta = self.pie[:, -2].copy()
            self.delta = self.pie[:, -3].copy()

    def vary(self):

        a = 2*(1 - self.it_no/self.it)*(2*np.random.rand(self.t, self.f, 3)-1)
        c = 2*np.random.rand(self.t, self.f, 3)
        self.pie[:, :self.f] = np.clip((self.alpha[:self.f] - a[:, :, 0] * abs(c[:, :, 0] * self.alpha[:self.f] - self.pie[:, :self.f]))/3 + (self.beta[:self.f] - a[:, :, 1] * abs(
            c[:, :, 1] * self.beta[:self.f] - self.pie[:, :self.f]))/3 + (self.delta[:self.f] - a[:, :, 2] * abs(c[:, :, 2] * self.delta[:self.f] - self.pie[:, :self.f]))/3, 0, 1)

    def report(self):

        if self.r == 0:
            return self.best[self.features_cols[0]:self.features_cols[1]], self.best[self.reward_col[0]], self.best[self.status_col]
