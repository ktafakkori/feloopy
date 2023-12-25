# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


import warnings as wn
import numpy as np

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
            self.pi = np.random.rand(self.t, self.single_objective_tot)
            self.pi[:, self.new_reward_col] = - np.inf * self.d
            self.pi[:, self.old_reward_col] = - np.inf * self.d
            self.pi[:, self.status_col] = 0
            self.bad_status = -1
            self.best_index = -1*(1+self.d[0])//2
        self.best = self.pi[-1].copy()

    def update(self):

        self.pi = self.evaluate(self.pi)

        if self.r == 0:

            self.pi[:, self.old_features_cols[0]:self.old_features_cols[1]] = np.where(np.reshape(self.d[0]*self.pi[:, self.new_reward_col[0]] > self.d[0]*self.pi[:, self.old_reward_col[0]], [self.t, 1]), self.pi[:, self.new_features_cols[0]:self.new_features_cols[1]], self.pi[:, self.old_features_cols[0]:self.old_features_cols[1]])
            self.pi[:, self.old_reward_col[0]] = np.where(self.d[0]*self.pi[:, self.new_reward_col[0]] > self.d[0] * self.pi[:, self.old_reward_col[0]], self.pi[:, self.new_reward_col[0]], self.pi[:, self.old_reward_col[0]])
            self.pi = self.pi[np.argsort(self.pi[:, self.old_reward_col[0]])]
            if self.d[0]*self.pi[self.best_index][self.old_reward_col[0]] > self.d[0]*self.best[self.old_reward_col[0]]: self.best = self.pi[self.best_index].copy()

    def vary(self):

        indices = np.array([np.random.randint(0, self.t, 3) for t in range(self.t)])
        mask = np.random.rand(self.t) < self.cr
        self.pi[mask, :self.f] = np.clip(self.pi[indices[mask, 0], :self.f] + self.mu * (self.pi[indices[mask, 1], :self.f] - self.pi[indices[mask, 2], :self.f]), 0, 1)

    def report(self):

        if self.r == 0:
            return self.best[self.old_features_cols[0]:self.old_features_cols[1]], self.best[self.old_reward_col[0]], self.best[self.status_col]