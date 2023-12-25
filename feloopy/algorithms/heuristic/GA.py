# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


import warnings as wn
import numpy as np


wn.filterwarnings("ignore")

class GA:

    def __init__(self, f: int, d: list, s: int, t: int, sc: int,cr: float, mu: float, sfl: float, sfu: float, **kwargs):

        self.f = f
        self.d = np.asarray([1 if item == 'max' else -1 for item in d])
        self.s = s
        self.t = t
        self.sc = sc
        self.cr = cr
        self.mu = mu
        self.sfl = sfl
        self.sfu = sfu
        self.r = 0 if len(d) == 1 else len(d)
        self.features_cols = [0, self.f]
        self.status_col = [-2]
        self.reward_col = [-1]
        self.single_objective_tot = self.f + 1 + 1
        self.solve = self.run

    def run(self, evaluate):

        self.evaluate = evaluate
        self.initialize()
        for self.it_no in range(0, self.s):
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

    def update(self):

        self.pi = self.evaluate(self.pi)

        if self.r == 0:
            self.pi = self.pi[np.argsort(self.pi[:, self.reward_col[0]])]
            if self.d[0]*self.pi[self.best_index][self.reward_col[0]] > self.d[0]*self.best[self.reward_col[0]]: self.best = self.pi[self.best_index].copy()
            
            if self.sc == 0:
                #Random
                cut = int(np.random.uniform(self.sfl,self.sfu)*self.t)
                if self.d[0] == 1: self.pi[:self.t-cut] = self.pi[np.random.choice(self.t, self.t-cut)]
                else: self.pi[cut:] = self.pi[np.random.choice(self.t, self.t-cut)]
            
            if self.sc == 1:
                #Tournament
                size = int(np.random.uniform(self.sfl,self.sfu)*self.t)
                tournament_individuals = np.random.choice(self.t, size, replace=False)
                best_individual = np.argmax(self.pi[tournament_individuals, self.reward_col[0]])
                if self.d[0] == 1: self.pi[:self.t-size] = [self.pi[tournament_individuals[best_individual]] for _ in range(self.t-size)]
                else: self.pi[size:] = [self.pi[tournament_individuals[best_individual]] for _ in range(self.t-size)]

    def vary(self):

        pool = np.asarray([np.array([t, np.random.randint(0, self.t)]) if np.random.rand() < self.cr else np.array([t, t]) for t in range(0, self.t)], dtype=np.int64)
        mask = np.random.randint(0, 2, size=(self.t, self.f)) == 1
        self.pi[pool[:,0], self.features_cols[0]:self.features_cols[1]] = mask*self.pi[:, self.features_cols[0]:self.features_cols[1]] + (1-mask)*(self.pi[pool[:,0], self.features_cols[0]:self.features_cols[1]] + np.random.uniform(-1, 1, size=(self.t, self.f))*(self.pi[pool[:,1], self.features_cols[0]:self.features_cols[1]]-self.pi[pool[:,0], self.features_cols[0]:self.features_cols[1]]))
        self.pi[:, self.features_cols[0]:self.features_cols[1]] = np.where((np.random.rand(self.t, self.f) < self.mu), 1-self.pi[:, self.features_cols[0]:self.features_cols[1]], self.pi[:, self.features_cols[0]:self.features_cols[1]])
        self.pi[:, self.features_cols[0]:self.features_cols[1]] = np.clip(self.pi[:, self.features_cols[0]:self.features_cols[1]], 0, 1)

    def report(self):

        if self.r == 0:
            return self.best[self.features_cols[0]:self.features_cols[1]], self.best[self.reward_col[0]], self.best[self.status_col]
