# Heuristic optimization

In this documentation section, the elements that let you work with heuristic optimization algorithms using `feloopy` in Python are defined.

## Defining Variables 

### `fvar` method

`fvar` method is used to create and return a free variable.

#### Parameters

- **`name` (str):** Name.

- **`dim` (list, optional):** Dimensions. Default is `0`.

- **`bound` (list):** Lower and upper bounds.

#### Returns

- **`variable`:** A free variable.