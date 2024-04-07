def validate_string(label, list_of_allowed_values, input_string, required=False):
    if required and input_string is None:
        raise ValueError(f"Providing '{label}' is required.")
    if input_string is not None and input_string not in list_of_allowed_values:
        raise ValueError(f"Invalid '{label}'. Please choose from: {str(list_of_allowed_values)}.")

def validate_integer(label, min_value=None, max_value=None, input_integer=None, required=False):
    if required and input_integer is None:
        raise ValueError(f"Providing '{label}' is required.")
    if input_integer is not None:
        if not isinstance(input_integer, int):
            raise ValueError(f"Input '{label}' must be an integer.")
        if min_value is not None and input_integer < min_value:
            raise ValueError(f"Input '{label}' must be at least {min_value}.")
        if max_value is not None and input_integer > max_value:
            raise ValueError(f"Input '{label}' must be at most {max_value}.")

def validate_existence(label, input_value, condition=True):
    if condition and input_value is None:
        raise ValueError(f"'{label}' should be provided and cannot be None.")
