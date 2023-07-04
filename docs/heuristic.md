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

- `orig`: original version (based on reference)
- `base`: developed version (improved implementation)
- `bio-inspired`: 13 bio-inspired algorithms from 2008-2023
- `evolution-inspired`: 8 evolution-inspired algorithms from 

## 2006 Algorithms

### `orig-iwo`

- Bio-inspired

- Src: [IWO mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/bio_based/IWO.py)

- Ref: Mehrabian, A. R., & Lucas, C. (2006). A novel numerical optimization algorithm inspired from weed colonization. Ecological Informatics, 1(4), 355–366. doi: 10.1016/j.ecoinf.2006.07.003

- Config: 

    ```python
    {
        "epoch": "(int): maximum number of iterations, default = 10000"
        "pop_size": "(int) number of population size, default = 100"
        "seed_min": "(int) Number of Seeds (min)"
        "seed_max": "(int) Number of seeds (max)"
        "exponent": "(int) Variance Reduction Exponent"
        "sigma_start": "(float) The initial value of standard deviation"
        "sigma_end": "(float) The final value of standard deviation"
    }
    ```

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

## 2014 Algorithms

### `orig-sos`

- Bio-inspired 

- Src: [SOS mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/bio_based/SOS.py)

- Ref: Cheng, M.-Y., & Prayogo, D. (2014). Symbiotic Organisms Search: A new metaheuristic optimization algorithm. Computers & Structures, 139. doi: 10.1016/j.compstruc.2014.03.007

- Config:

    ```python
    {
        'epoch': "maximum number of iterations, default = 10000",
        'pop_size': "number of population size, default = 100",
    }
    ```

### `orig-cro`, `o-cro`

- Evolution-based

- Src: [CRO mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/evolutionary_based/CRO.py)

- Ref: Salcedo-Sanz, S., Del Ser, J., Landa-Torres, I., Gil-López, S., & Portilla-Figueras, J. A. (2014). The Coral Reefs Optimization Algorithm: A Novel Metaheuristic for Efficiently Solving Optimization Problems. Scientific World Journal, 2014. doi: 10.1155/2014/739768

- Config:

    ```python
    {
        'epoch': "maximum number of iterations, default = 10000",
        'pop_size': "number of population size, default = 100",
        'po': "the rate between free/occupied at the beginning, no default value specified",
        'Fb': "BroadcastSpawner/ExistingCorals rate, no default value specified",
        'Fa': "fraction of corals duplicates its self and tries to settle in a different part of the reef, no default value specified",
        'Fd': "fraction of the worse health corals in reef will be applied depredation, no default value specified",
        'Pd': "the maximum of probability of depredation, no default value specified",
        'GCR': "probability for mutation process, no default value specified",
        'gamma_min': "factor for mutation process, no default value specified",
        'gamma_max': "factor for mutation process, no default value specified",
        'n_trials': "number of attempts for a larva to set in the reef, no default value specified"
    }
    ```

## 2016 Algorithms

### `orig-vcs`, `base-vcs`

- Bio-inspired

- Src: [VCS mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/bio_based/VCS.py)

- Ref: Li, M. D., Zhao, H., Weng, X. W., & Han, T. (2016). A novel nature-inspired algorithm for optimization: Virus colony search. Advances in Engineering Software, 92, 65–88. doi: 10.1016/j.advengsoft.2015.11.004

- Config: 

    ```python
    {
        'epoch': "maximum number of iterations, default = 10000",
        'pop_size': "number of population size, default = 100",
        'lamda': "Number of the best will keep, default = 0.5",
        'sigma': "Weight factor, default = 1.5"
    }
    ```

## 2017 Algorithms


### `orig-sbo`, `base-sbo`

- Bio-inspired

- Src: [SBO mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/bio_based/SBO.py)

- Ref: Samareh Moosavi, S. H., & Khatibi Bardsiri, V. (2017). Satin bowerbird optimizer: A new optimization algorithm to optimize ANFIS for software development effort estimation. Engineering Applications of Artificial Intelligence, 60, 1–15. doi: 10.1016/j.engappai.2017.01.006

- Config: 

    ```python
    {
        'epoch': "maximum number of iterations, default = 10000",
        'pop_size': "number of population size, default = 100",
        'alpha': "the greatest step size, default=0.94",
        'p_m': "mutation probability, default=0.05",
        'psw': "proportion of space width (z in the paper), default=0.02",
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
        'p_c': "crossover probability (float) [0,1], default = 0.9"
        'p_m': "initial mutation probability (float) [0,1], default = 0.01",
        'n_best': "elites survived (int) [2, pop_size/2], default = 2",
        'alpha': "similarity factor (float) [0,1], default = 0.98", 
        'beta': "initial proportional factor (float) [0,1], default = 0.9", 
        'gamma': "similar to cooling factor of a cooling schedule in the simulated annealing (float) [0,1], default = 0.9",
    }
    ```

## 2019 Algorithms

### `orig-soa`, `base-soa`

- Bio-inspired

- Ref: Dhiman, G., & Kumar, V. (2019). Seagull optimization algorithm: Theory and its applications for large-scale industrial engineering problems. Knowledge-Based Systems, 165, 169–196. doi: 10.1016/j.knosys.2018.11.024

- Config:

    ```python
    {
        'epoch': "maximum number of iterations, default = 1000",
        'pop_size': "number of population size, default = 100",
        'fc': "freequency of employing variable A (A linear decreased from fc to 0), default = 2"
    }

    ```

### `orig-who`

- Bio-inspired

- Src: [WHO mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/bio_based/WHO.py)

- Ref: Amali, D. and Dinakaran, M., 2019. Wildebeest herd optimization: a new global optimization algorithm inspired by wildebeest herding behaviour. Journal of Intelligent & Fuzzy Systems, 37(6), pp.8063-8076.

- Config:

    ```python
    {
        'epoch': "maximum number of iterations, default = 10000",
        'pop_size': "number of population size, default = 100",
        'n_explore_step': "number of exploration step, default = 3",
        'n_exploit_step': "number of exploitation step, default = 3",
        'eta': "learning rate, default = 0.15",
        'p_hi': "the probability of wildebeest move to another position based on herd instinct, default = 0.9",
        'local_alpha': "control local movement (alpha 1), no default value specified",
        'local_beta': "control local movement (beta 1), no default value specified",
        'global_alpha': "control global movement (alpha 2), no default value specified",
        'global_beta': "control global movement (beta 2), no default value specified",
        'delta_w': "dist to worst, no default value specified",
        'delta_c': "dist to best, no default value specified"
    }
    ```

### `orig-tpo`

- Bio-inspired

- Ref: Halim, A. H., & Ismail, I. (2019). Tree Physiology Optimization in Benchmark Function and Traveling Salesman Problem. Journal of Intelligent Systems, 28(5), 849–871. doi: 10.1515/jisys-2017-0156

- Config:
    ```python
    {
        'epoch': "maximum number of iterations, default = 10000",
        'pop_size': "number of population size, default = 100",
        'alpha': "Absorption constant for tree root elongation, default=0.3",
        'beta': "Diversification factor of tree shoot, default=50.",
        'theta': "Factor to reduce randomization, Theta = Power law to reduce randomization as iteration increases, default=0.9"
    }
    ```

## 2020 Algorithms

### `orig-sma`, `base-sma`

- Bio-inspired

- Src: [SMA mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/bio_based/SMA.py)

- Ref: Li, S., Chen, H., Wang, M., Heidari, A. A., & Mirjalili, S. (2020). Slime mould algorithm: A new method for stochastic optimization. Future Generation Computer Systems, 111, 300–323. doi: 10.1016/j.future.2020.03.055

- Config:

    ```python
    {
        'epoch': "maximum number of iterations, default = 1000",
        'pop_size': "number of population size, default = 100",
        'p_t': "probability threshold (z in the paper), default = 0.03",
    }
    ```

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

### `orig-tsa`

- Bio-inspired

- Src: [TSA mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/bio_based/TSA.py)

- Ref: Kaur, S., Awasthi, L. K., Sangal, A. L., & Dhiman, G. (2020). Tunicate Swarm Algorithm: A new bio-inspired based metaheuristic paradigm for global optimization. Engineering Applications of Artificial Intelligence, 90, 103541. doi: 10.1016/j.engappai.2020.103541

- Config:

    ```python
    {
        'epoch': "max iterations (int), default = 10000",
        'pop_size': "population size (int), default = 100",
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