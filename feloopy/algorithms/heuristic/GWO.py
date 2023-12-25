# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import warnings as wn
import numpy as np

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
            self.pi = np.random.rand(self.t, self.single_objective_tot)
            self.pi[:, self.reward_col] = - np.inf * self.d
            self.pi[:, self.status_col] = 0
            self.bad_status = -1
            self.best_index = -1*(1+self.d[0])//2
        self.best = self.pi[-1].copy()
        self.alpha, self.beta, self.delta = np.copy(self.pi[-1]), np.copy(self.pi[-2]), np.copy(self.pi[-3])

    def update(self):

        self.pi = self.evaluate(self.pi)
        if self.r == 0:
            self.pi = self.pi[np.argsort(self.pi[:, self.reward_col[0]])]
            if self.d[0]*self.pi[self.best_index][-1] > self.d[0]*self.best[-1]: 
                self.best = self.pi[self.best_index].copy()
            self.alpha = self.pi[self.best_index].copy()
            self.beta  = self.pi[self.best_index-1*self.d[0]].copy()
            self.delta = self.pi[self.best_index-2*self.d[0]].copy()

    def vary(self):

        a = 2*(1 - self.it_no/self.it)*(2*np.random.rand(self.t, self.f, 3)-1)
        c = 2*np.random.rand(self.t, self.f, 3)
        self.pi[:, :self.f] = np.clip((self.alpha[:self.f] - a[:, :, 0] * np.abs(c[:, :, 0] * self.alpha[:self.f] - self.pi[:, :self.f]))/3 + (self.beta[:self.f] - a[:, :, 1] * np.abs(c[:, :, 1] * self.beta[:self.f] - self.pi[:, :self.f]))/3 + (self.delta[:self.f] - a[:, :, 2] * np.abs(c[:, :, 2] * self.delta[:self.f] - self.pi[:, :self.f]))/3, 0, 1)

    def report(self):

        if self.r == 0:
            return self.best[self.features_cols[0]:self.features_cols[1]], self.best[self.reward_col[0]], self.best[self.status_col]
