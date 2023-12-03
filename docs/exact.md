# Exact Optimization

This section of the documentation provides an overview of the elements in `feloopy` that enable you to work with exact optimization algorithms in Python.

## Defining Variables 

### `fvar` method

`fvar` method is used to create and return a free variable.

#### Alternatives

`free_variable` | `real_variable` | `float_variable` | `add_free_variable` | `add_real_variable` | `add_float_variable` | `add_fvar` 

#### Parameters

- **`name` (str):** Name.

- **`dim` (list, optional):** Dimensions. Default is `0`.

- **`bound` (list, optional):** Lower and upper bounds. Default is `[None, None]`.

#### Returns

- **`variable`:** A free variable.

### `pvar` method

`pvar` method is used to create and return a positive variable.

#### Alternatives

`positive_variable` | `add_positive_variable` | `add_pvar` 

#### Parameters

- **`name` (str):** Name.
- **`dim` (list, optional):** Dimensions. Default is `0`.
- **`bound` (list, optional):** Bounds. Default is `[0, None]`.

#### Returns

- **`variable`:** A positive variable.

### `ivar` method

`ivar` method is used to create and return an integer variable.

#### Alternatives

`integer_variable` | `add_integer_variable` | `add_ivar` 

#### Parameters

- **`name` (str):** Name.
- **`dim` (list, optional):** Dimensions. Default is `0`.
- **`bound` (list, optional):** Bounds. Default is `[0, None]`.

#### Returns

- **`variable`:** An integer variable.

### `bvar` method

`bvar` method is used to create and return a binary variable.

#### Alternatives

`binary_variable` | `boolean_variable` | `indicator_variable` | `add_binary_variable` | `add_boolean_variable` | `add_indicator_Variable` | `add_bvar` 

#### Parameters

- **`name` (str):** Name.
- **`dim` (list, optional):** Dimensions. Default is `0`.
- **`bound` (list, optional):** Bounds. Default is `[0, 1]`.

#### Returns

- **`variable`:** A binary variable.