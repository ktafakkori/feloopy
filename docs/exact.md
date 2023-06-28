# Exact Optimization

This section of the documentation provides an overview of the elements in `feloopy` that enable you to work with exact optimization algorithms in Python.

## Defining Variables 

### `fvar` method

`fvar` method is used to create and return a free variable.

#### Parameters

- **`name` (str):** Name.

- **`dim` (list, optional):** Dimensions. Default is `0`.

- **`bound` (list, optional):** Lower and upper bounds. Default is `[None, None]`.

#### Returns

- **`variable`:** A free variable.
