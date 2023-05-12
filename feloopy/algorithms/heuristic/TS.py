'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

import numpy as np
import warnings as wn

wn.filterwarnings("ignore")


class TS:

    def __init__(self, f: int, d: list, s: int, t: int, c: int,**kwargs):

        self.d = np.asarray([1 if item == 'max' else -1 for item in d])
        self.r = 0 if len(d) == 1 else len(d)
        self.f = f
        self.s = s
        self.t = t
        self.c = c
        self.features_cols = [0, self.f]
        self.status_col = [-2]
        self.reward_col = [-1]
        self.single_objective_tot = self.f + 1 + 1

    def run(self, evaluate):

        self.evaluate = evaluate
        self.initialize()
        for self.it_no in range(0, self.s):
            self.update()
            self.vary()
        return self.report()

    def initialize(self):

        if self.r == 0:
            self.pie = np.random.rand(1, self.single_objective_tot)
            self.pie[:, self.reward_col] = - np.inf * self.d
            self.pie[:, self.status_col] = 0
            self.best_index = -1*(1+self.d[0])//2
            self.bad_status = -1
            self.tabu_list = []
        self.best = self.pie[-1].copy()

    def update(self):

        newpie = self.evaluate(self.pie)
        if self.r == 0:
            if self.d[0]*newpie[self.best_index][self.reward_col[0]] > self.d[0]*self.best[self.reward_col[0]]:
                self.best = newpie[self.best_index].copy()
            if self.it_no == 0:
                self.tabu_list.append(newpie)
                self.pie = newpie.copy()

    def vary(self):

        self.pie[:, :self.f] = np.clip(
            self.pie[:, :self.f] + 2*np.random.rand(self.f)-1, 0, 1)

    def report(self):

        if self.r == 0:
            return self.best[self.features_cols[0]:self.features_cols[1]], self.best[self.reward_col[0]], self.best[self.status_col]
