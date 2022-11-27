'''
Name: FelooPy
Version: 0.1.11
Contributors: Keivan Tafakkori
Date: 21 November 2022
License: MIT. (For more details please refer to LICENSE.txt file).
Copyright (c) 2022 Keivan Tafakkori & FELOOP (https://ktafakkori.github.io/)
'''


from tabulate import tabulate as tb 
import numpy as np
from .sol import *

def benchmark_exact(data, criterion):
    if criterion == 'cpt':
        time_solve_end = data[1]
        time_solve_begin = data[0]
        hour = round((time_solve_end - time_solve_begin), 3) % (24 * 3600) // 3600
        min = round((time_solve_end - time_solve_begin), 3) % (24 * 3600) % 3600 // 60
        sec = round((time_solve_end - time_solve_begin), 3) % (24 * 3600) % 3600 % 60
        print()
        print("BENCHMARK: TIME \n --------")
        print(tb({
            "cpt": [round((time_solve_end-time_solve_begin)*10**6), "%02d:%02d:%02d" % (hour, min, sec)],
            "unit": ["micro sec", "h:m:s"]
        }, headers="keys", tablefmt="github"))
        print()

def benchmark_heuristic(model, data, criterion):
    if criterion[0] == 'cpt' or 'obj':
        time_solve_begin = []
        time_solve_end = []
        bestreward = [np.inf]
        bestallreward = np.inf
        for i in range(criterion[1]):
            Result, Chronometer = implementor[data[0]](data[1],data[2])
            time_solve_begin.append(Chronometer[0])
            time_solve_end.append(Chronometer[1])
            Result[1] = np.asarray(Result[1])
            Result[1] = Result[1].item()
            bestreward.append(model.best_function)
            if Result[1] <= bestallreward:
                bestagent = Result[0]
                bestallreward = Result[1]
        bestreward.pop(0)
        bestreward = -np.asarray(bestreward) if data[2] == 'max' else np.asarray(bestreward)
        bestallreward = -bestallreward if data[2] == 'max' else bestallreward

        print()
        hour = []
        min = []
        sec = []
        ave = []
        for i in range(criterion[1]):
            tothour = round((time_solve_end[i] - time_solve_begin[i]), 3) % (24 * 3600) // 3600
            totmin = round((time_solve_end[i] - time_solve_begin[i]),3) % (24 * 3600) % 3600 // 60
            totsec = round((time_solve_end[i] - time_solve_begin[i]),3) % (24 * 3600) % 3600 % 60
            hour.append(tothour)
            min.append(totmin)
            sec.append(totsec)
            ave.append(round((time_solve_end[i]-time_solve_begin[i])*10**6))

        print("BENCHMARK: TIME \n --------")
        print(tb({
            "cpt (ave)": [np.average(ave), "%02d:%02d:%02d" % (np.average(hour), np.average(min), np.average(sec))],
            "cpt (std)": [np.std(ave), "%02d:%02d:%02d" % (np.std(hour), np.std(min), np.std(sec))],
            "unit": ["micro sec", "h:m:s"]
        }, headers="keys", tablefmt="github"))
        print()
        
        print("BENCHMARK: OBJ \n --------")
        print(tb({
            "obj": [np.max(bestreward), np.average(bestreward), np.std(bestreward), np.min(bestreward)],
            "unit": ["max", "average", "standard deviation", "min"]
        }, headers="keys", tablefmt="github"))
        print()

benchmark_int = {
    'gekko': benchmark_exact,
    'ortools': benchmark_exact,
    'pulp': benchmark_exact,
    'pyomo': benchmark_exact,
    'cplex': benchmark_exact,
    'gurobi': benchmark_exact,
    'xpress': benchmark_exact,
    'ga' : benchmark_heuristic
}