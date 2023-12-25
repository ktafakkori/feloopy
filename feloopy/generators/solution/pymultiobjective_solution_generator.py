# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import numpy as np
import timeit


def generate_solution(solver_name, AlgOptions, Fitness, ToTalVariableCounter, ObjectivesDirections, ObjectiveBeingOptimized, number_of_times, show_plots, save_plots,show_log):

    ObjectivesDirections = [-1 if direction =='max' else 1 for direction in ObjectivesDirections]

    def f1(X): return ObjectivesDirections[0]*Fitness(np.array(X))[0]
    def f2(X): return ObjectivesDirections[1]*Fitness(np.array(X))[1]
    def f3(X): return ObjectivesDirections[2]*Fitness(np.array(X))[2]
    def f4(X): return ObjectivesDirections[3]*Fitness(np.array(X))[3]
    def f5(X): return ObjectivesDirections[4]*Fitness(np.array(X))[4]
    def f6(X): return ObjectivesDirections[5]*Fitness(np.array(X))[5]

    my_list_of_functions = [f1, f2, f3, f4, f5, f6]

    parameters = dict()
    parameters['verbose'] = show_log

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

        case "c-ns-ga-ii":

            from pyMultiobjective.algorithm import clustered_non_dominated_sorting_genetic_algorithm_II
            solver = clustered_non_dominated_sorting_genetic_algorithm_II

        case "cta-ea":

            from pyMultiobjective.algorithm import constrained_two_archive_evolutionary_algorithm
            solver = constrained_two_archive_evolutionary_algorithm

        case "gr-ea":

            from pyMultiobjective.algorithm import grid_based_evolutionary_algorithm
            solver = grid_based_evolutionary_algorithm

        case "est-hv":

            from pyMultiobjective.algorithm import hypervolume_estimation_mooa
            solver = hypervolume_estimation_mooa

        case "ea-fc":

            from pyMultiobjective.algorithm import indicator_based_evolutionary_algorithm_fc
            solver = indicator_based_evolutionary_algorithm_fc

        case "ea-hv":

            from pyMultiobjective.algorithm import indicator_based_evolutionary_algorithm_hv
            solver = indicator_based_evolutionary_algorithm_hv

        case "ea-d":

            from pyMultiobjective.algorithm import multiobjective_evolutionary_algorithm_based_on_decomposition
            solver = multiobjective_evolutionary_algorithm_based_on_decomposition

        case "na-ea":

            from pyMultiobjective.algorithm import neighborhood_sensitive_archived_evolutionary_many_objective_optimization
            solver = neighborhood_sensitive_archived_evolutionary_many_objective_optimization

        case "ns-ga-ii":

            from pyMultiobjective.algorithm import non_dominated_sorting_genetic_algorithm_II
            solver = non_dominated_sorting_genetic_algorithm_II

        case "ns-ga-iii":

            from pyMultiobjective.algorithm import non_dominated_sorting_genetic_algorithm_III
            solver = non_dominated_sorting_genetic_algorithm_III

        case "modi-pso":

            from pyMultiobjective.algorithm import optimized_multiobjective_particle_swarm_optimization
            solver = optimized_multiobjective_particle_swarm_optimization

        case "pa-es":

            from pyMultiobjective.algorithm import pareto_archived_evolution_strategy
            solver = pareto_archived_evolution_strategy

        case  "rv-ea":

            from pyMultiobjective.algorithm import reference_vector_guided_evolutionary_algorithm
            solver = reference_vector_guided_evolutionary_algorithm

        case "sm-pso":

            from pyMultiobjective.algorithm import speed_constrained_multiobjective_particle_swarm_optimization
            solver = speed_constrained_multiobjective_particle_swarm_optimization

        case "sms-ea":

            from pyMultiobjective.algorithm import s_metric_selection_evolutionary_multiobjective_optimization_algorithm
            solver = s_metric_selection_evolutionary_multiobjective_optimization_algorithm

        case "sp-ea-ii":

            from pyMultiobjective.algorithm import strength_pareto_evolutionary_algorithm_2
            solver = strength_pareto_evolutionary_algorithm_2

        case "u-ns-ga-iii":

            from pyMultiobjective.algorithm import unified_non_dominated_sorting_genetic_algorithm_III
            solver = unified_non_dominated_sorting_genetic_algorithm_III

    time_solve_begin = timeit.default_timer()
    sol = solver(list_of_functions=list_of_functions, **parameters)
    time_solve_end = timeit.default_timer()

    return sol[:, :ToTalVariableCounter[1]], list_of_directions*sol[:, ToTalVariableCounter[1]:], time_solve_begin, time_solve_end
