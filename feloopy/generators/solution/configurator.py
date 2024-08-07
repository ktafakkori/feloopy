# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

##TODO 

import numpy as np
def get_coeffs(interface, directions):
    if interface in ["pygad"]:
        max_indicator = 1
        min_indicator = -1
    else:
        max_indicator = -1
        min_indicator = 1
    
    return np.array([max_indicator if directions[objective_number]!='min' else min_indicator for objective_number in range(len(directions))])

def get_additional_info(interface,inputi, dicti):
    try:
        result=dicti[inputi][interface]
    except:
        result=""
    return result

def get_config(interface, solver, verbose=False):
    
    config = {}
    
    additional_info = \
        {
        "type_selection" :
            {"pygad": 
                """
                'sss'          steady-state selection
                'rws'          roulette wheel selection
                'sus'          stochastic universal selection
                'rank'         rank selection
                'random'       random selection
                'tournament'   tournament selection (parameter "K_tournament=3" might be needed)
                """    
            },
            
        "type_crossover" :
            {"pygad": 
                """
                'single_point' single-point crossover
                'two_points'   two-point crossover
                'uniform'      uniform crossover
                'scattered'    scattered crossover
                """,
                
             "pymoo":
                """
                'single_point' single-point crossover
                'two_points'   two-points crossover
                
                
                """,                
            },
        "type_mutation" :
            {"pygad": 
                """
                'random'       random mutation (parameter "mutation_by_replacement=True" is optional that means replace the feature by a randomly generated value if true or add with a random value if false, "random_mutation_min_val" or "random_mutation_max_val" are also needed for this addition)
                'swap'         swap mutation
                'inversion'    inversion mutation
                'scramble'     scramble mutation
                'adaptive'     adaptive mutation
                """    
            },
            
        "prob_crossover" :
            {
            "pygad":
                """
                activates if less than
                """
                
            },
            
        "prob_mutation" :
            {
            "pygad":
                """
                activates if less than
                """
                
            },

        "exit_criterion" :
            {
            "pygad":
                """
                'reach_{value}'  if the fitness is >= value
                'saturate_{int}' if the fitness saturates for a given number of consecutive epochs.
            
                """,
                
            "pymoo":
                
                """
                'nfe_{value}' if number of function evaluations is ==
                
                """
            } 
                      
        }
        
    descriptions = {
        "key"                :  "Key for reproducibility",
        "num_epochs"         :  "Number of epochs. [an integer>=1]",
        "num_agents"         :  "Number of search agents. [an integer>=1]",
        "num_best_agents"    : "Number of best search agents to keep. [an integer>=1]",
        "num_parents"        :  "Number of agents to be selected as parents. [an integer>=1]",
        "init_agents"        :  "Initial state of the search agents. [a 2D numpy array]",
        "init_range"         :  "Range of initialized search agents. [list]",
        "type_feature"       :  "Type of each/all features [int, float, or numpy.int/uint/float(8-64)] or [list, tuple, or a numpy.ndarray]",
        "limit_features"     :  "Specify continuous [range] or discrete [list] of possible values that each feature takes. [range or list of ranges] or [list or list of list] or dict [{low:0 high:2 step:1}]",
        "type_selection"     :  "How to select eligible search agents after evaluation?" + get_additional_info(interface,"type_selection", additional_info),
        "type_crossover"     :  "How to variate search agents collaboratively in a crossover?" + get_additional_info(interface,"type_crossover", additional_info),
        "type_mutation"      :  "How to variate search agents sigularly in a mutation?" + get_additional_info(interface,"type_mutation", additional_info),
        "prob_crossover"     :  "Probability of selecting a search agent for a crossover [0,1]" + get_additional_info(interface,"prob_crossover", additional_info),
        "store_epoch_best"   : "To store the best popoulation member in each epoch",    
        "store_epoch_agents" : "To store all popoulation members in each epoch",
        "store_epoch_obj"    : "To store the objective function (or Pareto front) in each epoch",
        "exit_criterion"     : "Criterion to exit search process" + get_additional_info(interface,"exit_criterion", additional_info),
        "parallel"           : "Number of threads/processes to use for parallel computing ['thread', int] or ['process', int]",
        "verbose"            : "To show a progress log",
    }
     
    if interface=="pygad":
        
        config["num_generations"] = "num_epochs"
        config["num_parents_mating"] = "num_parents"
        config["initial_population"] = "init_agents"
        config["sol_per_pop"] = "num_agents"
        config["gene_type"] = "type_feature"
        config["init_range_low"] = "init_range"
        config["init_range_high"] = "init_range"
        config["parent_selection_type"] = "type_selection"
        config["crossover_type"] = "type_crossover"
        config["keep_elitism"] = "num_best_agents"
        config["crossover_probability"] = "prob_crossover"
        config["mutation_type"] = "type_mutation"
        config["save_best_solutions"] = "store_epoch_best"
        config["save_solutions"] = "store_epoch_agents"
        config["stop_criteria"] = "exit_criterion"
        config["parallel_processing"] = "parallel"
        config["random_seed"] = "key"

    if interface=="pymoo":

        config["pop_size"] = "num_agents"
        config["n_gen"] = "num_epochs"
        config["seed"] = "key"
        config["verbose"] = "verbose"
        
        
    if verbose:
        print("{")
        for ky in descriptions.keys():
            print(ky +": "+descriptions[ky] + ",")
        print("}")
    return config

def fix_config(interface,solver,options):
    initial_configs = get_config(interface, solver)
    supported_configs_specific = initial_configs.keys()
    supported_configs_standard = initial_configs.values()
    config = {}
    for key in options.keys():
        if key in initial_configs.keys():
            config[key] = options[key]
        elif key in initial_configs.values():
            correct_key = next((k for k, v in initial_configs.items() if v == key), None)
            config[correct_key] = options[key]
    return config
            
print(get_config('pymoo', 'ga', verbose=False))