'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.8)                               |
|  Modified: Wednesday, 27th September 2023 08:27:26 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''

import numpy as np
import warnings as wn

wn.filterwarnings("ignore")

class DE:

    def __init__(self, f: int, d: list, s: int, t: int, cr: float, mu: float, **kwargs):

        self.d = np.asarray([1 if item == 'max' else -1 for item in d])
        self.r = 0 if len(d) == 1 else len(d)
        self.f = f
        self.s = s
        self.t = t
        self.cr = cr
        self.mu = mu
        self.new_features_cols = [0, self.f]
        self.old_features_cols = [self.f, 2*self.f]
        self.status_col = [-2]
        self.new_reward_col = [-1]
        self.old_reward_col = [-3] if self.r == 0 else [-3-self.r]
        self.single_objective_tot = self.f + self.f + 1 + 1 + 1
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
            self.pie[:, self.new_reward_col] = - np.inf * self.d
            self.pie[:, self.old_reward_col] = - np.inf * self.d
            self.pie[:, self.status_col] = 0
            self.best_index = -1*(1+self.d[0])//2
            self.bad_status = -1
        self.best = self.pie[-1].copy()

    def update(self):

        self.pie = self.evaluate(self.pie)
        if self.r == 0:
            self.pie[:, self.old_features_cols[0]:self.old_features_cols[1]] = np.where(np.reshape(self.d[0]*self.pie[:, self.new_reward_col[0]] > self.d[0]*self.pie[:, self.old_reward_col[0]], [self.t, 1]), self.pie[:, self.new_features_cols[0]:self.new_features_cols[1]], self.pie[:, self.old_features_cols[0]:self.old_features_cols[1]])
            self.pie[:, self.old_reward_col[0]] = np.where(self.d[0]*self.pie[:, self.new_reward_col[0]] > self.d[0] * self.pie[:, self.old_reward_col[0]], self.pie[:, self.new_reward_col[0]], self.pie[:, self.old_reward_col[0]])
            self.pie = self.pie[np.argsort(
                self.pie[:, self.old_reward_col[0]])]
            if self.d[0]*self.pie[self.best_index][self.old_reward_col[0]] > self.d[0]*self.best[self.old_reward_col[0]]:
                self.best = self.pie[self.best_index].copy()

    def vary(self):

        indices = np.array([np.random.randint(0, self.t, 3) for t in range(self.t)])
        self.pie[:, :self.f] = np.where(np.random.rand(self.f) < self.cr, np.clip(self.pie[indices[:, 0], :self.f] + self.mu * (
            self.pie[indices[:, 1], :self.f] - self.pie[indices[:, 2], :self.f]), 0, 1), self.pie[:, :self.f])

    def report(self):

        if self.r == 0:
            return self.best[self.old_features_cols[0]:self.old_features_cols[1]], self.best[self.old_reward_col[0]], self.best[self.status_col]
