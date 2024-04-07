import numpy as np

def binary_similarity(a, b):
    if type(a) ==type(None)  or type(b) ==type(None):
        return None
    else:
        dot_product = np.dot(a, b)
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)
        similarity = dot_product / (norm_a * norm_b)
        return similarity

def continuous_similarity(a, b):
    if type(a) ==type(None)  or type(b) ==type(None):
        return None
    else:
        dot_product = np.dot(a, b)
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)
        similarity = dot_product / (norm_a * norm_b)
        return similarity

def compute_similarity(variables, control_scenario_id):
    control_index = control_scenario_id
    control = variables[control_index]
    similarities = []

    for i, var in enumerate(variables):
        similarity = {}

        for key, value in var.items():
            control_value = control[key]


            if isinstance(value, np.ndarray):
                if np.array_equal(control_value, value):
                    similarity[key] = 1.0
                elif value.dtype == bool: 
                    # binary variable
                    similarity[key] = binary_similarity(control_value, value)
                else:  
                    # continuous variable
                    similarity[key] = continuous_similarity(control_value, value)
            else:  
                    # scalar value
                    similarity[key] = continuous_similarity(control_value, value)
                
        similarities.append(similarity)

    return similarities
