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


## Defining Algorithms

### `orig-bbo`

- Reference: Simon, D., 2008. Biogeography-based optimization. IEEE transactions on evolutionary computation, 12(6), pp.702-713.

```python
{
    'epoch': "max iterations (int), default = 10000"
    'pop_size': "population size (int), default = 100"
    'p_m': "mutation probability (float), default = 0.01"
    'elites': "elites survived (int), default = 2"
}
```