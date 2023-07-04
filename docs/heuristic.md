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


## Algorithm Types

`orig`: original version
`base`: developed version

## 2008 Algorithms

### `orig-bbo`, `base-bbo`

- Simon, D. (2008). Biogeography-Based Optimization. IEEE Trans. Evol. Comput., 12(6), 702–713. doi: 10.1109/TEVC.2008.919004

```python
{
    'epoch': "max iterations (int), default = 10000",
    'pop_size': "population size (int), default = 100",
    'p_m': "mutation probability (float), default = 0.01",
    'elites': "elites survived (int), default = 2",
}
```

## 2020 Algorithms

- Sulaiman, M. H., Mustaffa, Z., Saari, M. M., & Daniyal, H. (2020). Barnacles Mating Optimizer: A new bio-inspired algorithm for solving engineering optimization problems. Eng. Appl. Artif. Intell., 87, 103330. doi: 10.1016/j.engappai.2019.103330

```python
{
    'epoch': "max iterations (int), default = 10000",
    'pop_size': "population size (int), default = 100",
    'pl': "barnacle’s threshold, between [1, pop_size - 1], default =5,
}
```

## 2023 Algorithms

### `orig-bboa`

- Prakash, T., Singh, P. P., Singh, V. P., & Singh, S. N. (2023). A Novel Brown-bear Optimization Algorithm for Solving Economic Dispatch Problem. Advanced Control & Optimization Paradigms for Energy System Operation and Management. River Publishers. doi: 10.1201/9781003337003-6

```python
{
    'epoch': "max iterations (int), default = 10000",
    'pop_size': "population size (int), default = 100",
}
```
