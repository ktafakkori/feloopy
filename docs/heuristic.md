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
- `levy`: Levy flight version
- `bio-inspired`: 13 bio-inspired algorithms
- `evolution-inspired`: 8 evolution-inspired algorithms

## 1989 Algorithms

- Src: [MA mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/evolutionary_based/MA.py)

- Ref: Moscato, P., 1989. On evolution, search, optimization, genetic algorithms and martial arts: Towards memetic algorithms. Caltech concurrent computation program, C3P Report, 826, p.1989.

- Config:

    ```python
        {
            "epoch": "(int): maximum number of iterations, default = 10000",
            "pop_size": "(int): number of population size, default = 100",
            "pc": "(float): cross-over probability, default = 0.85",
            "pm": "(float): mutation probability, default = 0.15",
            "p_local": "(float): Probability of local search for each agent, default=0.5",
            "max_local_gens": "(int): number of local search agent will be created during local search mechanism, default=10",
            "bits_per_param": "(int): number of bits to decode a real number to 0-1 bitstring, default=4"
        }
    ```

## 1994 Algorithms

### `orig-ga`

- Evolution-inspired

- Src: [GA mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/evolutionary_based/GA.py)

- Ref: Whitley, D., 1994. A genetic algorithm tutorial. Statistics and computing, 4(2), pp.65-85.

- Config:

    ```python
    { 
        "epoch": "(int): maximum number of iterations, default = 10000", 
        "pop_size": "(int) number of population size, default = 100", 
        "pc": "(float): cross-over probability, default = 0.95", 
        "pm": "(float): mutation probability, default = 0.025", 
        "selection": "(str): Optional, can be ['roulette', 'tournament', 'random'], default = 'tournament'", 
        "k_way": "(float): Optional, set it when use 'tournament' selection, default = 0.2", 
        "crossover": "(str): Optional, can be ['one_point', 'multi_points', 'uniform', 'arithmetic'], default = 'uniform'",
        "mutation_multipoints": "(bool): Optional, True or False, effect on mutation process, default = False",
        "mutation": "(str): Optional, can be ['flip', 'swap'] for multipoints and can be ['flip', 'swap', 'scramble', 'inversion'] for one-point, default='flip'" 
    }
    ```

### `single-ga`

- Evolution-inspired

- Src: [GA mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/evolutionary_based/GA.py)

- Ref: Whitley, D., 1994. A genetic algorithm tutorial. Statistics and computing, 4(2), pp.65-85.

- Config:

    ```python
    { 
        "epoch": "(int): maximum number of iterations, default = 10000", 
        "pop_size": "(int) number of population size, default = 100", 
        "pc": "(float) cross-over probability, default = 0.95", 
        "pm": "(float) mutation probability, default = 0.8", 
        "selection": "(str) Optional, can be ['roulette', 'tournament', 'random'], default = 'tournament'", 
        "crossover": "(str) Optional, can be ['one_point', 'multi_points', 'uniform', 'arithmetic'], default = 'uniform'", 
        "mutation": "(str) Optional, can be ['flip', 'swap', 'scramble', 'inversion'], default = 'flip'", 
        "k_way": "(float) Optional, set it when use 'tournament' selection, default = 0.2" 
    }
    ```

### `elite-single-ga`

- Evolution-inspired

- Src: [GA mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/evolutionary_based/GA.py)

- Ref: Whitley, D., 1994. A genetic algorithm tutorial. Statistics and computing, 4(2), pp.65-85.

- Config:

    ```python
    { 
        "epoch": "(int): maximum number of iterations, default = 10000", 
        "pop_size": "(int) number of population size, default = 100", 
        "pc": "(float): [0.7, 0.95], cross-over probability, default = 0.95", 
        "pm": "(float): [0.01, 0.2], mutation probability, default = 0.025", 
        "selection": "(str): Optional, can be ['roulette', 'tournament', 'random'], default = 'tournament'", 
        "crossover": "(str): Optional, can be ['one_point', 'multi_points', 'uniform', 'arithmetic'], default = 'uniform'", 
        "mutation": "(str): Optional, can be ['flip', 'swap', 'scramble', 'inversion'] for one-point", 
        "k_way": "(float): Optional, set it when use 'tournament' selection, default = 0.2", 
        "elite_best": "(float/int): Optional, can be float (percentage of the best in elite group), or int (the number of best elite), default = 0.1", 
        "elite_worst": "(float/int): Optional, can be float (percentage of the worst in elite group), or int (the number of worst elite), default = 0.3", 
        "strategy": "(int): Optional, can be 0 or 1. If = 0, the selection is select parents from (elite_worst + non_elite_group). Else, the selection will select dad from elite_worst and mom from non_elite_group." 
    }
    ```

### `multi-ga`

- Bio-inspired

- Src: [MultiGA mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/evolutionary_based/GA.py)

- Ref: Whitley, D., 1994. A genetic algorithm tutorial. Statistics and computing, 4(2), pp.65-85.

- Config:

    ```python
    { 
        "epoch": "(int): maximum number of iterations, default = 10000", 
        "pop_size": "(int) number of population size, default = 100", 
        "pc": "(float): cross-over probability, default = 0.95", 
        "pm": "(float): mutation probability, default = 0.025", 
        "selection": "(str): Optional, can be ['roulette', 'tournament', 'random'], default = 'tournament'", 
        "crossover": "(str): Optional, can be ['one_point', 'multi_points', 'uniform', 'arithmetic'], default = 'uniform'", 
        "mutation": "(str): Optional, can be ['flip', 'swap'] for multipoints", 
        "k_way": "(float): Optional, set it when use 'tournament' selection, default = 0.2" 
    }
    ```

### `elite-multi-ga`

- Evolution-inspired

- Src: [Elite Multi-GA mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/evolutionary_based/EliteMultiGA.py)

- Ref: Whitley, D. (1994). A genetic algorithm tutorial. Statistics and computing, 4(2), pp.65-85.

- Config:

    ```python
    { 
        "epoch": "(int): maximum number of iterations, default = 10000", 
        "pop_size": "(int): number of population size, default = 100", 
        "pc": "(float): [0.7, 0.95], cross-over probability, default = 0.95", 
        "pm": "(float): [0.01, 0.2], mutation probability, default = 0.025", 
        "selection": "(str): Optional, can be ['roulette', 'tournament', 'random'], default = 'tournament'", 
        "k_way": "(float): Optional, set it when use 'tournament' selection, default = 0.2", 
        "crossover": "(str): Optional, can be ['one_point', 'multi_points', 'uniform', 'arithmetic'], default = 'uniform'", 
        "mutation": "(str): Optional, can be ['flip', 'swap'] for multipoints", 
        "elite_best": "(float/int): Optional, can be float (percentage of the best in elite group), or int (the number of best elite), default = 0.1", 
        "elite_worst": "(float/int): Optional, can be float (percentage of the worst in elite group), or int (the number of worst elite), default = 0.3", 
        "strategy": "(int): Optional, can be 0 or 1. If = 0, the selection is select parents from (elite_worst + non_elite_group). Else, the selection will select dad from elite_worst and mom from non_elite_group." 
    }
    ```

## 1999 Algorithms

### `orig-ep`, `levy-ep`

- Evolution-inspired

- Src: [EP mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/evolutionary_based/EP.py)

- Ref: Yao, X., Liu, Y. and Lin, G., 1999. Evolutionary programming made faster. IEEE Transactions on Evolutionary computation, 3(2), pp.82-102.

- Config:

    ```python
    { 
        "epoch": "(int): maximum number of iterations, default = 10000", 
        "pop_size": "(int) number of population size (miu in the paper), default = 100", 
        "bout_size": "(float): percentage of child agents implement tournament selection", 
    }
    ```

## 2001 Algorithms

### `cma-es`, `simp-cma-es`

- Evolution-inspired

- Src: [CMA-ES mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/evolutionary_based/ES.py)

- Ref: Hansen, N., & Ostermeier, A. (2001). Completely derandomized self-adaptation in evolution strategies. Evolutionary computation, 9(2), 159-195.

- Config:

    ```python
    { 
        "epoch": "(int): maximum number of iterations, default = 10000", 
        "pop_size": "(int) number of population size (miu in the paper), default = 100" 
    }
    ```

## 2002 Algorithms

### `orig-es`, `levy-es`

- Evolution-based

- Src: [ES mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/evolutionary_based/ES.py)

- Ref: Beyer, H.G. and Schwefel, H.P., 2002. Evolution strategies–a comprehensive introduction. Natural computing, 1(1), pp.3-52.

- Config:

    ```python
    { 
        "epoch": "(int): maximum number of iterations, default = 10000",
        "pop_size": "(int) number of population size, default = 100",
        "lamda": "(float) Percentage of child agents, evolving in the next generation, default=0.75" 
    }
    ```

## 2005 Algorithms

### `sa-de`

- Evolution-inspired

- Src: [SADE mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/evolutionary_based/DE.py)

- Ref: Qin, A. K., & Suganthan, P. N. (2005). Self-adaptive differential evolution algorithm for numerical optimization. 2005 IEEE Congress on Evolutionary Computation. IEEE. doi: 10.1109/CEC.2005.1554904

- Config:

    ```python
    {
        'epoch': "max iterations (int), default = 10000",
        'pop_size': "population size (int), default = 100",
    }
    ```

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

### `sap-de`

- Evolution-inspired

- Src: [SAPDE mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/evolutionary_based/DE.py)

- Ref: Teo, J. (2006). Exploring dynamic self-adaptive populations in differential evolution. Soft Comput, 10(8), 673–686. doi: 10.1007/s00500-005-0537-1

- Config:

    ```python
    {
        'epoch': "maximum number of iterations (int), default = 10000",
        'pop_size': "number of population size (int), default = 100",
        'branch': "gaussian (absolute) or uniform (relative) method (str)",
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

## 2009 Algorithms

### `ja-de`

- Evolution-inspired

- Src: [JADE mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/evolutionary_based/DE.py)

- Ref: Zhang, J., & Sanderson, A. C. (2009). JADE: Adaptive Differential Evolution With Optional External Archive. IEEE Transactions on Evolutionary Computation, 13(5), 945–958. doi: 10.1109/TEVC.2009.2014613

- Config:

    ```python
    {
        'epoch': "maximum number of iterations (int), default = 10000",
        'pop_size': "number of population size (int), default = 100",
        'miu_f': "initial adaptive f (float), default = 0.5",
        'miu_cr': "initial adaptive cr (float), default = 0.5",
        'pt': "The percent of top best agents (float) (p in the paper), default = 0.1",
        'ap': "The Adaptation Parameter control value of f and cr (float) (c in the paper), default = 0.1",
    }
    ```

## 2012 Algorithms

### `orig-fpa`

- Evolution-inspired

- Src: [OriginalFPA mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/evolutionary_based/FPA.py)

- Ref: Yang, X.S., 2012, September. Flower pollination algorithm for global optimization. In International
conference on unconventional computing and natural computation (pp. 240-249). Springer, Berlin, Heidelberg.

- Config:

    ```python
    { 
        "epoch": "(int): maximum number of iterations, default = 10000", 
        "pop_size": "(int): number of population size, default = 100", 
        "p_s": "(float): switch probability, default = 0.8", 
        "levy_multiplier": "(float): multiplier factor of Levy-flight trajectory, default = 0.2" 
    }
    ```

## 2013 Algorithms

### `sha-de`

- Evolution-inspired

- Src: [SHADE mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/evolutionary_based/SHADE.py)

- Ref: Tanabe, R. and Fukunaga, A., 2013, June. Success-history based parameter adaptation for
differential evolution. In 2013 IEEE congress on evolutionary computation (pp. 71-78). IEEE.

- Config:

    ```python
    { 
        "epoch": "(int): maximum number of iterations, default = 750",
        "pop_size": "(int): number of population size, default = 100",
        "miu_f": "(float): initial weighting factor, default = 0.5",
        "miu_cr": "(float): initial cross-over probability, default = 0.5",
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

### `orig-cro`

- Evolution-based

- Src: [CRO mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/evolutionary_based/CRO.py)

- Ref: Salcedo-Sanz, S., Del Ser, J., Landa-Torres, I., Gil-López, S. and Portilla-Figueras, J.A., 2014.
    The coral reefs optimization algorithm: a novel metaheuristic for efficiently solving optimization problems. The Scientific World Journal, 2014.
  
- Config:
  
  ```python
  {
        'epoch': "maximum number of iterations, default = 10000",
        'pop_size': "number of population size, default = 100",
        'po': "the rate between free/occupied at the beginning",
        'Fb': "BroadcastSpawner/ExistingCorals rate",
        'Fa': "fraction of corals duplicates its self and tries to settle in a different part of the reef",
        'Fd': "fraction of the worse health corals in reef will be applied depredation",
        'Pd': "the maximum of probability of depredation",
        'GCR': "probability for mutation process",
        'gamma_min': "factor for mutation process",
        'gamma_max': "factor for mutation process",
        'n_trials': "number of attempts for a larva to set in the reef",
    }
    ```

### `o-cro`

- Evolution-based

- Src: [OCRO mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/evolutionary_based/CRO.py)

- Ref: Nguyen, T., Nguyen, T., Nguyen, B. M., & Nguyen, G. (2019). Efficient Time-Series Forecasting Using Neural Network and Opposition-Based Coral Reefs Optimization. International Journal of Computational Intelligence Systems, 12(2), 1144–1161. doi: 10.2991/ijcis.d.190930.003

- Config:

    ```python
    {
        'epoch': "maximum number of iterations, default = 10000",
        'pop_size': "number of population size, default = 100",
        'po': "the rate between free/occupied at the beginning, no default value specified",
        'Fb': "BroadcastSpawner/ExistingCorals rate, no default value specified",
        'Fa': "fraction of corals duplicates its self and tries to settle in a different part of the reef, no default value specified",
        'Fd': "fraction of the worse health corals in reef will be applied depredation, no default value specified",
        'Pd': "Probability of depredation, no default value specified",
        'GCR': "probability for mutation process, no default value specified",
        'gamma_min': "[0.01, 0.1] factor for mutation process",
        'gamma_max': "[0.1, 0.5] factor for mutation process",
        'n_trials': "number of attempts for a larva to set in the reef, no default value specified",
        'restart_count': "reset the whole population after global best solution is not improved after restart_count times, no default value specified"
    }
    ```

### `l-sha-de`

- Bio-inspired

- Src: [L_SHADE mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/evolutionary_based/SHADE.py)

- Ref: Tanabe, R. and Fukunaga, A.S., 2014, July. Improving the search performance of SHADE using linear population size reduction. In 2014 IEEE congress on evolutionary computation (CEC) (pp. 1658-1665). IEEE.

- Config:

    ```python
    { 
        "epoch": "(int): maximum number of iterations, default = 750",
        "pop_size": "(int): number of population size, default = 100", 
        "miu_f": "(float): initial weighting factor, default = 0.5", 
        "miu_cr": "(float): initial cross-over probability, default = 0.5",
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

### `base-de`

- Evolution-inspired

- Src: [DE mealpy](https://github.com/thieu1995/mealpy/blob/master/mealpy/evolutionary_based/DE.py)

- Ref: Mohamed, A. W., Hadi, A. A., & Jambi, K. M. (2018). Novel mutation strategy for enhancing SHADE and LSHADE algorithms for global Numerical Optimization. Swarm and Evolutionary Computation, 50. doi: 10.1016/j.swevo.2018.10.006

- Config:

    ```python
    {        
        'epoch': "maximum number of iterations, default = 10000",
        'pop_size': "number of population size, default = 100",
        'wf': "weighting factor (float) [0.5, 0.95], default = 0.8",
        'cr': "crossover rate (float) [0.5, 0.95], default = 0.9",
        'strategy': """variant version of DE algorithm (int) [0, 5], there are lots of variant versions of DE algorithm, including:
            + 0: DE/current-to-rand/1/bin
            + 1: DE/best/1/bin
            + 2: DE/best/2/bin
            + 3: DE/rand/2/bin
            + 4: DE/current-to-best/1/bin
            + 5: DE/current-to-rand/1/bin"""
    }
    ```

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
- Src: https://github.com/thieu1995/mealpy/blob/master/mealpy/evolutionary_based/DE.py
- stic paradigm for global optimization. Engineering Applications of Artificial Intelligence, 90, 103541. doi: 10.1016/j.engappai.2020.103541

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
