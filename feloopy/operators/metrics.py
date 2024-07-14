import numpy as np

def cosine_similarity(a, b):
    try:
        if a is None or b is None:
            return 'n/a'
        dot_product = np.dot(a, b)
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)
        return dot_product / (norm_a * norm_b) if norm_a * norm_b != 0 else 'n/a'
    except Exception as e:
        return 'n/a'

def jaccard_similarity(a, b):
    try:
        if a is None or b is None:
            return 'n/a'
        set_a = set(a)
        set_b = set(b)
        intersection = len(set_a & set_b)
        union = len(set_a | set_b)
        return intersection / union if union != 0 else 'n/a'
    except Exception as e:
        return 'n/a'

def scalar_similarity(a, b):
    try:
        if a is None or b is None:
            return 'n/a'
        if a == b:
            return 1.0
        else:
            return 1 - abs(a - b) / (abs(a) + abs(b) + 1e-10) 
    except Exception as e:
        return 'n/a'

def compute_similarity(variables, control_scenario_id):
    control_index = control_scenario_id
    control = variables[control_index]
    similarity_scores = []

    for i, var in enumerate(variables):
        similarity = {}

        for key, value in var.items():
            control_value = control.get(key)

            try:
                if value is None or control_value is None:
                    similarity[key] = 'n/a'
                    continue

                if isinstance(value, np.ndarray) or isinstance(value, list) or isinstance(value, range):
                    control_value = np.array(control_value)
                    value = np.array(value)
                    if np.array_equal(control_value, value):
                        similarity[key] = 1.0
                    elif value.dtype == bool:
                        similarity[key] = jaccard_similarity(control_value, value)
                    else:
                        similarity[key] = cosine_similarity(control_value, value)
                elif isinstance(value, dict):
                    dict_similarities = []
                    for sub_key, sub_value in value.items():
                        control_sub_value = control_value.get(sub_key)
                        if sub_value is None or control_sub_value is None:
                            dict_similarities.append('n/a')
                        elif isinstance(sub_value, np.ndarray) or isinstance(sub_value, list) or isinstance(sub_value, range):
                            control_sub_value = np.array(control_sub_value)
                            sub_value = np.array(sub_value)
                            if np.array_equal(control_sub_value, sub_value):
                                dict_similarities.append(1.0)
                            elif sub_value.dtype == bool:
                                dict_similarities.append(jaccard_similarity(control_sub_value, sub_value))
                            else:
                                dict_similarities.append(cosine_similarity(control_sub_value, sub_value))
                        else:
                            dict_similarities.append(scalar_similarity(control_sub_value, sub_value))
                    dict_similarities = [s for s in dict_similarities if s != 'n/a']
                    similarity[key] = np.mean(dict_similarities) if dict_similarities else 'n/a'
                else:
                    similarity[key] = scalar_similarity(control_value, value)
            except Exception as e:
                similarity[key] = 'n/a'

        similarity_scores.append(similarity)

    return similarity_scores
