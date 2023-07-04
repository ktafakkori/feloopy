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

- Bio-inspired

- Src: [BBO mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/bio_based/BBO.py)

- Ref: Simon, D. (2008). Biogeography-Based Optimization. IEEE Transactions on Evolutionary Computation, 12(6), 702–713. doi: 10.1109/TEVC.2008.919004

- Config: 

    ```python
    {
        'epoch': "max iterations (int), default = 10000",
        'pop_size': "population size (int), default = 100",
        'p_m': "mutation probability (float), default = 0.01",
        'elites': "elites survived (int), default = 2",
    }
    ```
## 2018 Algorithms


### `orig-eoa`

- Bio-inspired

- Src: [EOA mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/bio_based/EOA.py)

- Ref: Wang, G.G., Deb, S. and Coelho, L.D.S., (2018). Earthworm optimisation algorithm: a bio-inspired metaheuristic algorithm for global optimisation problems. International journal of bio-inspired computation, 12(1), pp.1-22. doi: 10.1504/IJBIC.2018.093328

- Config:

    ```python
    {
        'epoch': "max iterations (int), default = 10000",
        'pop_size': "population size (int), default = 100",
        'p_m': "initial mutation probability (float) [0,1], default = 0.01",
        'n_best': "elites survived (int) [2, pop_size/2], default = 2",
        'alpha': "similarity factor (float) [0,1], default = 0.98", 
        'beta': "initial proportional factor (float) [0,1], default = 0.9", 
        'gamma': " similar to cooling factor of a cooling schedule in the simulated annealing (float) [0,1], default = 0.9",
    }
    ```

## 2020 Algorithms

### `orig-bmo`

- Bio-inspired

- Src: [BMO mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/bio_based/BMO.py)

- Ref: Sulaiman, M. H., Mustaffa, Z., Saari, M. M., & Daniyal, H. (2020). Barnacles Mating Optimizer: A new bio-inspired algorithm for solving engineering optimization problems. Engineering Applications of Artificial Intelligence, 87, 103330. doi: 10.1016/j.engappai.2019.103330

- Config: 

    ```python
    {
        'epoch': "max iterations (int), default = 10000",
        'pop_size': "population size (int), default = 100",
        'pl': "barnacle’s threshold (int) [1, pop_size - 1], default =5,
    }
    ```

## 2023 Algorithms

### `orig-bboa`

- Bio-inspired

- Src: [BBOA mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/bio_based/BBOA.py)

- Ref: Prakash, T., Singh, P. P., Singh, V. P., & Singh, S. N. (2023). A Novel Brown-bear Optimization Algorithm for Solving Economic Dispatch Problem. Advanced Control & Optimization Paradigms for Energy System Operation and Management. River Publishers. doi: 10.1201/9781003337003-6

- Config: 

    ```python
    {
        'epoch': "max iterations (int), default = 10000",
        'pop_size': "population size (int), default = 100",
    }
    ```