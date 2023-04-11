
from .count_operators import *

def update_variable_features(name, variable_dim, variable_bound, variable_counter_type, features):
    """ For hierarchical updating the features of the problem.
    """
    match features['solution_method']:

        case 'exact':

            features['total_variable_counter'], features['variable_counter_type'] = count_variable(
                variable_dim, features['total_variable_counter'], features[variable_counter_type])

        case 'heuristic':

            if features['agent_status'] == 'idle':

                features['variable_spread'][name] = [
                    features['total_variable_counter'][1], 0]
                features['total_variable_counter'], features[variable_counter_type] = count_variable(
                    variable_dim, features['total_variable_counter'], features[variable_counter_type])
                features['variable_spread'][name][1] = features['total_variable_counter'][1]
                if variable_counter_type == 'free_variable_counter':
                    features['variable_type'][name] = 'fvar'
                if variable_counter_type == 'binary_variable_counter':
                    features['variable_type'][name] = 'bvar'
                if variable_counter_type == 'integer_variable_counter':
                    features['variable_type'][name] = 'ivar'
                if variable_counter_type == 'positive_variable_counter':
                    features['variable_type'][name] = 'pvar'
                features['variable_bound'][name] = variable_bound
                features['variable_dim'][name] = variable_dim

    return features