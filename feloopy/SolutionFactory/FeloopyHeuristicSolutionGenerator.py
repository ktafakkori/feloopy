'''
INFO
~~~~
Package Version: 0.2.0
Copyright: (2022) Keivan Tafakkori & FELOOP (http://k.tafakkori.github.io/)
License: MIT (Please Refer to the LICENSE.txt File)
Script Edited by: Keivan Tafakkori (12 December 2022)
'''

import timeit
from tabulate import tabulate as tb
import numpy as np

def GenerateSolution(ModelObject, Fitness, ToTalVariableCounter, ObjectivesDirections, ObjectiveBeingOptimized, Times, Plots):

    if Times == 1:
        
        return  ModelObject.solve(Fitness)

    else:

        Multiplier = {'max': 1, 'min': -1}

        dir = Multiplier[ObjectivesDirections[ObjectiveBeingOptimized]]

        time_solve_begin = []

        time_solve_end = []

        bestreward = [-dir*np.inf]

        bestallreward = -dir*np.inf

        for i in range(Times):

            time_solve_begin.append(timeit.default_timer())

            BestAgent, BestReward = ModelObject.solve(Fitness)

            time_solve_end.append(timeit.default_timer())

            Result = [BestAgent, BestReward]

            Result[1] = np.asarray(Result[1])

            Result[1] = Result[1].item()

            bestreward.append(BestReward)

            if dir*(Result[1]) >= dir*(bestallreward):
                bestagent = Result[0]
                bestallreward = Result[1]

        bestreward.pop(0)

        print()
        hour = []
        min = []
        sec = []
        ave = []
        for i in range(Times):
            tothour = round(
                (time_solve_end[i] - time_solve_begin[i]), 3) % (24 * 3600) // 3600
            totmin = round(
                (time_solve_end[i] - time_solve_begin[i]), 3) % (24 * 3600) % 3600 // 60
            totsec = round(
                (time_solve_end[i] - time_solve_begin[i]), 3) % (24 * 3600) % 3600 % 60
            hour.append(tothour)
            min.append(totmin)
            sec.append(totsec)
            ave.append(round((time_solve_end[i]-time_solve_begin[i])*10**6))

        print("TIME \n --------")
        print(tb({
            "cpt (ave)": [np.average(ave), "%02d:%02d:%02d" % (np.average(hour), np.average(min), np.average(sec))],
            "cpt (std)": [np.std(ave), "%02d:%02d:%02d" % (np.std(hour), np.std(min), np.std(sec))],
            "unit": ["micro sec", "h:m:s"]
        }, headers="keys", tablefmt="github"))
        print()

        print("OBJ \n --------")
        print(tb({
            "obj": [np.max(bestreward), np.average(bestreward), np.std(bestreward), np.min(bestreward)],
            "unit": ["max", "average", "standard deviation", "min"]
        }, headers="keys", tablefmt="github"))
        print()

        BestAgent = bestagent
        BestReward = bestallreward

    return BestAgent, BestReward


