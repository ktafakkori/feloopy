'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.8)                               |
|  Modified: Wednesday, 27th September 2023 08:28:04 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''

import numpy as np
import warnings as wn

wn.filterwarnings("ignore")


class GA:

    def __init__(self, f: int, d: list, s: int, t: int, cr: float, mu: float, sfl: float, sfu: float, **kwargs):

        self.d = np.asarray([1 if item == 'max' else -1 for item in d])
        self.r = 0 if len(d) == 1 else len(d)
        self.f = f
        self.s = s
        self.t = t
        self.cr = cr
        self.mu = mu
        self.features_cols = [0, self.f]
        self.status_col = [-2]
        self.reward_col = [-1]
        self.single_objective_tot = self.f + 1 + 1
        self.survival_of_the_fittest_lb = sfl
        self.survival_of_the_fittest_ub = sfu
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
            self.pie = np.random.rand(self.t, self.single_objective_tot)
            self.pie[:, self.reward_col] = - np.inf * self.d
            self.pie[:, self.status_col] = 0
            self.best_index = -1*(1+self.d[0])//2
            self.bad_status = -1
        self.best = self.pie[-1].copy()

    def update(self):

        self.pie = self.evaluate(self.pie)
        if self.r == 0:
            self.pie = self.pie[np.argsort(self.pie[:, self.reward_col[0]])]
            if self.d[0]*self.pie[self.best_index][self.reward_col[0]] > self.d[0]*self.best[self.reward_col[0]]:
                self.best = self.pie[self.best_index].copy()
            cut = int(np.random.uniform(self.survival_of_the_fittest_lb,self.survival_of_the_fittest_ub)*self.t)
            if self.d[0] == 1:
                self.pie[:cut] = self.pie[np.random.choice(self.t, cut)]
            else:
                self.pie[cut:] = self.pie[np.random.choice(self.t, self.t-cut)]

    def vary(self):

        pool = np.asarray([np.array([t, np.random.randint(0, self.t)]) if np.random.rand(
        ) < self.cr else np.array([t, t]) for t in range(0, self.t)], dtype=np.int64)
        self.pie[:, self.features_cols[0]:self.features_cols[1]] = np.where(np.random.randint(0, 2, size=(self.t, self.f)) == 1, self.pie[pool.T[1], self.features_cols[0]:self.features_cols[1]] + np.random.uniform(-1, 1, size=(
            self.t, self.f))*(self.pie[pool.T[1], self.features_cols[0]:self.features_cols[1]]-self.pie[pool.T[0], self.features_cols[0]:self.features_cols[1]]), self.pie[pool.T[0], self.features_cols[0]:self.features_cols[1]])
        self.pie[:, self.features_cols[0]:self.features_cols[1]] = np.where((np.random.rand(
            self.t, self.f) < self.mu), 1-self.pie[:, self.features_cols[0]:self.features_cols[1]], self.pie[:, self.features_cols[0]:self.features_cols[1]])
        self.pie[:, self.features_cols[0]:self.features_cols[1]] = np.clip(
            self.pie[:, self.features_cols[0]:self.features_cols[1]], 0, 1)

    def report(self):

        if self.r == 0:
            return self.best[self.features_cols[0]:self.features_cols[1]], self.best[self.reward_col[0]], self.best[self.status_col]
