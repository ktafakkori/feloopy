'''
Name: FelooPy
Version: 0.1.11
Contributors: Keivan Tafakkori
Date: 21 November 2022
License: MIT. (For more details please refer to LICENSE.txt file).
Copyright (c) 2022 Keivan Tafakkori & FELOOP (https://ktafakkori.github.io/)
'''


def get_ga_options(input):
    algorithm_param = {'max_num_iteration': input.get('S'),
                        'population_size': input.get('T'),
                        'mutation_probability': input.get('Mu'),
                        'elit_ratio': input.get('El', 0.01),
                        'crossover_probability': input.get('Cr'),
                        'crossover_type': input.get('Cr_type', 'uniform'),
                        'parents_portion': input.get('Pp', 0.3),
                        'max_iteration_without_improv': None}
    return algorithm_param               

option_get = {
    'ga': get_ga_options
}