# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.



import timeit
from tabulate import tabulate as tb
import numpy as np


def generate_solution(model_object, fitness_function, total_features, objectives_directions, objective_number, number_of_times, show_plots,show_log):

    if number_of_times == 1:

        time_solve_begin = timeit.default_timer()
        x, y, status = model_object.solve(fitness_function)
        time_solve_end = timeit.default_timer()
        return x, y, time_solve_begin, time_solve_end, status

    else:

        Multiplier = {'max': 1, 'min': -1}
        directions = Multiplier[objectives_directions[objective_number]]
        time_solve_begin = []
        time_solve_end = []
        bestreward = [-directions*np.inf]
        best_reward_found = -directions*np.inf
        for i in range(number_of_times):
            time_solve_begin.append(timeit.default_timer())
            best_agent, best_reward, status = model_object.solve(
                fitness_function)
            time_solve_end.append(timeit.default_timer())
            Result = [best_agent, best_reward]
            Result[1] = np.asarray(Result[1])
            Result[1] = Result[1].item()
            bestreward.append(best_reward)
            if directions*(Result[1]) >= directions*(best_reward_found):
                best_agent_found = Result[0]
                best_reward_found = Result[1]
        bestreward.pop(0)

        if show_log:
            print()
            hour = []
            min = []
            sec = []
            ave = []
            for i in range(number_of_times):
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

            print("~~~~~~~\nTIME INFO\n~~~~~~~")
            print(tb({
                "cpt (ave)": [np.average(ave), "%02d:%02d:%02d" % (np.average(hour), np.average(min), np.average(sec))],
                "cpt (std)": [np.std(ave), "%02d:%02d:%02d" % (np.std(hour), np.std(min), np.std(sec))],
                "unit": ["micro sec", "h:m:s"]
            }, headers="keys", tablefmt="github"))
            print()

            print("~~~~~~~\nOBJ INFO\n~~~~~~~")
            print(tb({
                "obj": [np.max(bestreward), np.average(bestreward), np.std(bestreward), np.min(bestreward)],
                "unit": ["max", "average", "standard deviation", "min"]
            }, headers="keys", tablefmt="github"))
            print("~~~~~~~")

        best_agent = best_agent_found
        best_reward = best_reward_found

    return best_agent, best_reward, np.average(time_solve_begin), np.average(time_solve_end), status
