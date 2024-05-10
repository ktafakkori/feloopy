# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

from .configurator import *

import numpy as np
import timeit
from tabulate import tabulate as tb
import pygad

def generate_solution(model_object, fitness_function, total_features, objectives_directions, objective_number, number_of_times, show_plots, save_plots,show_log, solver_options):

    coeffs = get_coeffs("pygad", objectives_directions)
    
    def new_fitness_function(ga_instance, sol, solution_idx):
        result = fitness_function(sol)*coeffs
        return result
    
    initial_configs = get_config("pygad", "ga")
    supported_configs_specific = initial_configs.keys()
    supported_configs_standard = initial_configs.values()
    config = {}
    for key in solver_options.keys():
        if key in initial_configs.keys():
            config[key] = solver_options[key]
        elif key in initial_configs.values():
            correct_key = next((k for k, v in initial_configs.items() if v == key), None)
            config[correct_key] = solver_options[key]
    if "gene_space" not in config.keys(): config["gene_space"] = [{'low': 0, 'high': 1} for i in range(total_features[1])]
    if "num_genes" not in config.keys(): config["num_genes"] = total_features[1]
    if "num_generations" not in config.keys(): config["num_generations"] = 100
    if "num_parents_mating" not in config.keys(): config["num_parents_mating"] = config["sol_per_pop"] // 2
    
    ga_instance = pygad.GA(fitness_func=new_fitness_function,**config)
    
    if number_of_times == 1:
        
        time_solve_begin = timeit.default_timer()
        ga_instance.run()
        time_solve_end = timeit.default_timer()
        if len(objectives_directions)==1:
            best_agent, best_reward, solution_idx = ga_instance.best_solution(ga_instance.last_generation_fitness)
            best_reward=best_reward*coeffs
            best_reward=best_reward[0]
        else:
            best_reward = np.array(ga_instance.self.best_solutions_fitness)
            best_reward=best_reward*coeffs
    
            
        
    else:

        Multiplier = {'max': 1, 'min': -1}
        directions = Multiplier[objectives_directions[objective_number]]
        time_solve_begin = []
        time_solve_end = []
        bestreward = [-directions*np.inf]
        best_reward_found = -directions*np.inf

        for i in range(number_of_times):
            time_solve_begin.append(timeit.default_timer())
            ga_instance.run()
            time_solve_end.append(timeit.default_timer())
            best_agent, best_reward, solution_idx = ga_instance.best_solution()
            Result = [best_agent, best_reward[0]]
            Result[1] = np.asarray(Result[1])
            Result[1] = Result[1].item()
            bestreward.append(best_reward[0])
            if directions*(Result[1]) >= directions*(best_reward_found):
                best_agent_found = Result[0]
                best_reward_found = Result[1]
        bestreward.pop(0)

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

        if show_log:
            print()
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

    print(best_agent, best_reward, time_solve_begin, time_solve_end)
    return best_agent, best_reward, time_solve_begin, time_solve_end