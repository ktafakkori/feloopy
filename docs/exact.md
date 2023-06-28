# Exact optimization

In this documentation section, the elements that let you work with exact optimization algorithms using `feloopy` in Python are defined.

## Variable creation methods

### `fvar`

creates a free variable (continuous, real-valued) with a specified name, dimensions, and bounds.

### Parameters:

- `name`: String representing the free variable's name.
- `dim`: List of sets or integers for dimensions (default is 0, a scalar variable).
- `bound`: Optional list of [lower_bound, upper_bound] (no bounds by default).

### Returns:

The generated free variable.

### Example Usage:

```python
# Create a free variable named 'x' with two dimensions, and no bounds
# my_variable = my_instance.fvar('x', [2, 2])
```


