# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


import numpy as np
import timeit
from tabulate import tabulate as tb
from mealpy.utils.visualize import *
from mealpy import FloatVar

def generate_solution(model_object, fitness_function, total_features, objectives_directions, objective_number, number_of_times, show_plots, save_plots,show_log, solver_options):

    problem = {
        "obj_func": fitness_function,
        "bounds": FloatVar(lb=(0, )* total_features[1], ub=(1, )*total_features[1]),
        "minmax": objectives_directions[objective_number],
        "log_to": "console" if show_log else None,
        "save_population": False,
    }
    if solver_options.get("mode", None)!=None:

        termination={
            "mode": solver_options.get("mode", "MG"), 
            "quantity": solver_options.get("quantity", 100)}

    else:
        termination=None
        
    if number_of_times == 1:
        
        if solver_options.get("process_mode")!=None:
            solver_inputs = {'problem': problem, 'mode': solver_options.get("process_mode"), 'n_workers': solver_options.get("n_workers")}
        else:
            solver_inputs = {'problem': problem}

        if termination!=None:
            time_solve_begin = timeit.default_timer()
            g_best = model_object.solve(**solver_inputs, termination=termination)
            time_solve_end = timeit.default_timer()
            best_agent, best_reward = g_best.solution, g_best.target.fitness
        else:
            time_solve_begin = timeit.default_timer()
            g_best = model_object.solve(**solver_inputs)
            time_solve_end = timeit.default_timer()
            best_agent, best_reward = g_best.solution, g_best.target.fitness
        
        if show_plots:
            
            export_convergence_chart(model_object.history.list_global_best_fit, title='Global Best fitness_function')
            export_convergence_chart(model_object.history.list_current_best_fit, title='Local Best fitness_function')
            export_convergence_chart(model_object.history.list_epoch_time, title='Runtime chart', y_label="Second")
            export_explore_exploit_chart([model_object.history.list_exploration, model_object.history.list_exploitation])
            export_diversity_chart([model_object.history.list_diversity], list_legends=[''])

            if save_plots:

                model_object.history.save_global_best_fitness_chart(filename="results/gbfc")
                model_object.history.save_local_best_fitness_chart(filename="results/lbfc")
                model_object.history.save_runtime_chart(filename="results/rtc")
                model_object.history.save_exploration_exploitation_chart(filename="results/eec")
                model_object.history.save_diversity_chart(filename="results/dc")

    else:

        Multiplier = {'max': 1, 'min': -1}
        directions = Multiplier[objectives_directions[objective_number]]
        time_solve_begin = []
        time_solve_end = []
        bestreward = [-directions*np.inf]
        best_reward_found = -directions*np.inf

        for i in range(number_of_times):
            time_solve_begin.append(timeit.default_timer())
            g_best = model_object.solve(**solver_inputs)
            time_solve_end.append(timeit.default_timer())
            best_agent, best_reward = g_best.solution, g_best.target.fitness
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
            print("~~~~~~~")

            print("~~~~~~~\nOBJ INFO\n~~~~~~~")
            print(tb({
                "obj": [np.max(bestreward), np.average(bestreward), np.std(bestreward), np.min(bestreward)],
                "unit": ["max", "average", "standard deviation", "min"]
            }, headers="keys", tablefmt="github"))
            print("~~~~~~~")

        best_agent = best_agent_found
        best_reward = best_reward_found

    return best_agent, best_reward, time_solve_begin, time_solve_end
