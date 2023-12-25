# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


import math as mt

def product(iterable):
    return mt.prod(iterable)

def count_variable(variable_dim, total_count, special_count):
    total_count[0] += 1
    special_count[0] += 1
    count = 1 if variable_dim == 0 else product(len(dims) for dims in variable_dim)
    special_count[1] += count
    total_count[1] += count
    return total_count, special_count

def update_variable_features(name, variable_dim, variable_bound, variable_counter_type, features):

    if features['solution_method'] == 'exact':
        features['total_variable_counter'], features[variable_counter_type] = count_variable(variable_dim, features['total_variable_counter'], features[variable_counter_type])

    elif features['solution_method'] == 'heuristic' and features['agent_status'] == 'idle':

        start_counter = features['total_variable_counter'][1]

        if variable_counter_type == 'sequential_variable_counter':

            changed = True

            variable_counter_type = 'integer_variable_counter'
        
        else:
            changed =False
        
        features['total_variable_counter'], features[variable_counter_type] = count_variable(variable_dim, features['total_variable_counter'], features[variable_counter_type])
        end_counter = features['total_variable_counter'][1]

        features['variable_spread'][name] = [start_counter, end_counter]
        variable_type_mapping = {
            'free_variable_counter': 'fvar',
            'binary_variable_counter': 'bvar',
            'integer_variable_counter': 'ivar',
            'positive_variable_counter': 'pvar',
            'sequential_variable_counter': 'svar'
        }
        
        if changed:

            variable_counter_type = 'sequential_variable_counter'

        features['variable_type'][name] = variable_type_mapping[variable_counter_type]
        features['variable_bound'][name] = variable_bound
        features['variable_dim'][name] = variable_dim

    return features