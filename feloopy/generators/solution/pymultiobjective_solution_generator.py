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
import timeit


def generate_solution(solver_name, AlgOptions, Fitness, ToTalVariableCounter, ObjectivesDirections, ObjectiveBeingOptimized, number_of_times, show_plots, save_plots):

    ObjectivesDirections = [-1 if direction ==
                            'max' else 1 for direction in ObjectivesDirections]

    def f1(X): return ObjectivesDirections[0]*Fitness(np.array(X))[0]
    def f2(X): return ObjectivesDirections[1]*Fitness(np.array(X))[1]
    def f3(X): return ObjectivesDirections[2]*Fitness(np.array(X))[2]
    def f4(X): return ObjectivesDirections[3]*Fitness(np.array(X))[3]
    def f5(X): return ObjectivesDirections[4]*Fitness(np.array(X))[4]
    def f6(X): return ObjectivesDirections[5]*Fitness(np.array(X))[5]

    my_list_of_functions = [f1, f2, f3, f4, f5, f6]

    parameters = dict()

    parameters['verbose'] = False

    for key in AlgOptions:

        if key == 'epoch':
            parameters['generations'] = AlgOptions[key]

        elif key == 'show_log':
            parameters['verbose'] = AlgOptions[key]

        else:
            parameters[key] = AlgOptions[key]

    parameters['min_values'] = (0,)*ToTalVariableCounter[1]

    parameters['max_values'] = (1,)*ToTalVariableCounter[1]

    list_of_functions = []
    list_of_directions = ObjectivesDirections

    for i in range(len(ObjectivesDirections)):

        list_of_functions.append(my_list_of_functions[i])

    match solver_name:

        case "nsga-iii":

            from pyMultiobjective.algorithm import non_dominated_sorting_genetic_algorithm_III
            solver = non_dominated_sorting_genetic_algorithm_III

        case "nsga-ii":

            from pyMultiobjective.algorithm import non_dominated_sorting_genetic_algorithm_II
            solver = non_dominated_sorting_genetic_algorithm_II

        case "c-nsga-ii":

            from pyMultiobjective.algorithm import clustered_non_dominated_sorting_genetic_algorithm_II
            solver = clustered_non_dominated_sorting_genetic_algorithm_II

        case "ctaea":

            from pyMultiobjective.algorithm import constrained_two_archive_evolutionary_algorithm
            solver = constrained_two_archive_evolutionary_algorithm

        case "grea":

            from pyMultiobjective.algorithm import grid_based_evolutionary_algorithm
            solver = grid_based_evolutionary_algorithm

        case "ibea-fc":

            from pyMultiobjective.algorithm import indicator_based_evolutionary_algorithm_fc
            solver = indicator_based_evolutionary_algorithm_fc

        case "moead":

            from pyMultiobjective.algorithm import multiobjective_evolutionary_algorithm_based_on_decomposition
            solver = multiobjective_evolutionary_algorithm_based_on_decomposition

        case "naemo":

            from pyMultiobjective.algorithm import neighborhood_sensitive_archived_evolutionary_many_objective_optimization
            solver = neighborhood_sensitive_archived_evolutionary_many_objective_optimization

        case "omopso":

            from pyMultiobjective.algorithm import optimized_multiobjective_particle_swarm_optimization
            solver = optimized_multiobjective_particle_swarm_optimization

        case "paes":

            from pyMultiobjective.algorithm import pareto_archived_evolution_strategy
            solver = pareto_archived_evolution_strategy

        case  "rvea":

            from pyMultiobjective.algorithm import reference_vector_guided_evolutionary_algorithm
            solver = reference_vector_guided_evolutionary_algorithm

        case "spea-ii":

            from pyMultiobjective.algorithm import strength_pareto_evolutionary_algorithm_2
            solver = strength_pareto_evolutionary_algorithm_2

        case "smpso":

            from pyMultiobjective.algorithm import speed_constrained_multiobjective_particle_swarm_optimization
            solver = speed_constrained_multiobjective_particle_swarm_optimization

        case "u-nsga-iii":

            from pyMultiobjective.algorithm import unified_non_dominated_sorting_genetic_algorithm_III
            solver = unified_non_dominated_sorting_genetic_algorithm_III

    time_solve_begin = timeit.default_timer()
    sol = solver(list_of_functions=list_of_functions, **parameters)
    time_solve_end = timeit.default_timer()

    if show_plots:

        from pyMultiobjective.util import graphs

        # Plot Solution - Scatter Plot
        parameters = {
            'min_values': (0,)*ToTalVariableCounter[1],
            'max_values': (1,)*ToTalVariableCounter[1],
            'step': (AlgOptions.get('step', 0.1),)*ToTalVariableCounter[1],
            'solution': sol,
            'show_pf': True,
            'show_pts': True,
            'show_sol': True,
            'pf_min': True if AlgOptions.get('pareto_dir', 'min') == 'min' else False,
            # Input a custom Pareto Front(numpy array where each column is an Objective Function)
            'custom_pf': [],
            'view': 'browser'
        }
        graphs.plot_mooa_function(
            list_of_functions=list_of_functions, **parameters)

        # Plot Solution - Parallel Plot
        parameters = {
            'min_values': (0,)*ToTalVariableCounter[1],
            'max_values': (1,)*ToTalVariableCounter[1],
            'step': (AlgOptions.get('step', 0.1),)*ToTalVariableCounter[1],
            'solution': sol,
            'show_pf': True,
            'pf_min': True if AlgOptions.get('pareto_dir', 'min') == 'min' else False,
            # Input a custom Pareto Front(numpy array where each column is an Objective Function)
            'custom_pf': [],
            'view': 'browser'
        }
        graphs.parallel_plot(list_of_functions=list_of_functions, **parameters)

        # Plot Solution - Andrews Plot
        parameters = {
            'min_values': (0,)*ToTalVariableCounter[1],
            'max_values': (1,)*ToTalVariableCounter[1],
            'step': (AlgOptions.get('step', 0.1),)*ToTalVariableCounter[1],
            'solution': sol,
            'normalize': True,
            'size_x': 15,
            'size_y': 15,
            'show_pf': True,
            'pf_min': True if AlgOptions.get('pareto_dir', 'min') == 'min' else False,
            # Input a custom Pareto Front(numpy array where each column is an Objective Function)
            'custom_pf': []
        }
        graphs.andrews_plot(list_of_functions=list_of_functions, **parameters)

    return sol[:, :ToTalVariableCounter[1]], list_of_directions*sol[:, ToTalVariableCounter[1]:], np.average(time_solve_begin), np.average(time_solve_end)
