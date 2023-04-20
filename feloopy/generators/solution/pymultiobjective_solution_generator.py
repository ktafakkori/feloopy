import numpy as np
import timeit



def generate_solution(solver_name, AlgOptions, Fitness, ToTalVariableCounter, ObjectivesDirections, ObjectiveBeingOptimized, number_of_times, show_plots, save_plots):

        parameters = dict()

        for key in AlgOptions:
 
            if key=='epoch':
                parameters['generations'] = AlgOptions[key] 
            elif key=='show_log':
                parameters['verbose'] = AlgOptions[key] 
            else:
                parameters[key] = AlgOptions[key]

        parameters['min_values'] = (0,)*ToTalVariableCounter[1]

        parameters['max_values'] = (1,)*ToTalVariableCounter[1]

        list_of_functions = []
        list_of_directions = []

        for i in range(len(ObjectivesDirections)):

            if ObjectivesDirections[1]=='max':

                list_of_directions.append(-1)

                def res(X): 
                 
                    return -1*Fitness(np.array(X))[i]
            
            else:

                list_of_directions.append(1)

                def res(X): 
                 
                    return Fitness(np.array(X))[i]
                
            list_of_functions.append(res)

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
        sol = solver(list_of_functions = list_of_functions, **parameters)
        time_solve_end = timeit.default_timer()


        if show_plots:

            from pyMultiobjective.util import graphs

            # Plot Solution - Scatter Plot
            parameters = {
                'min_values': (0,)*ToTalVariableCounter[1],
                'max_values': (1,)*ToTalVariableCounter[1],
                'step': (AlgOptions.get('step',0.1),)*ToTalVariableCounter[1],
                'solution': sol, 
                'show_pf': True,
                'show_pts': True,
                'show_sol': True,
                'pf_min': True if AlgOptions.get('pareto_dir','min')=='min' else False,
                'custom_pf': [], # Input a custom Pareto Front(numpy array where each column is an Objective Function)
                'view': 'browser'
            }
            graphs.plot_mooa_function(list_of_functions = list_of_functions, **parameters)

            # Plot Solution - Parallel Plot
            parameters = {
                'min_values': (0,)*ToTalVariableCounter[1],
                'max_values': (1,)*ToTalVariableCounter[1],
                'step': (AlgOptions.get('step',0.1),)*ToTalVariableCounter[1],
                'solution': sol, 
                'show_pf': True,
                'pf_min': True if AlgOptions.get('pareto_dir','min')=='min' else False,
                'custom_pf': [], # Input a custom Pareto Front(numpy array where each column is an Objective Function)
                'view': 'browser'
            }
            graphs.parallel_plot(list_of_functions = list_of_functions, **parameters)

            # Plot Solution - Andrews Plot
            parameters = {
                'min_values': (0,)*ToTalVariableCounter[1],
                'max_values': (1,)*ToTalVariableCounter[1],
                'step': (AlgOptions.get('step',0.1),)*ToTalVariableCounter[1],
                'solution': sol, 
                'normalize': True,
                'size_x': 15,
                'size_y': 15,
                'show_pf': True, 
                'pf_min': True if AlgOptions.get('pareto_dir','min')=='min' else False,
                'custom_pf': [] # Input a custom Pareto Front(numpy array where each column is an Objective Function)
            }
            graphs.andrews_plot(list_of_functions = list_of_functions, **parameters)

        return sol[:,:ToTalVariableCounter[1]], list_of_directions*sol[:,ToTalVariableCounter[1]:], np.average(time_solve_begin), np.average(time_solve_end)