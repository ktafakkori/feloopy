In modeling a meaningful relationship between elements of various sets in a decision environment, we usually need some indicators, metrics, features, and attributes, given to or collected by the experts as “parameters”. In statistics, however, parameters are referred to as independent and dependent "variables". In both mathematical/statistical modeling, the aim is to increase the accuracy of the solution. In statistics, the accuracy of a decision (e.g., the value of the regressors) depends on statistical measures, while in mathematics and especially operations research, accuracy depends on some expert-defined metrics to match the expectations of a real/virtual world.

This section outlines the process of defining parameters within any decision environment. Continuing the definition of [sets](./sets.md), it is necessary to have instantiated a data toolkit, as follows:

```py
--8<-- "./concepts/parameters.py:parameterenvironment"
```

Again, if you have already defined the above commands in your code, there is no need to replicate them.

!!! note

    The argument `key` (any non-negative integer) is used for the generation of arbitrary random data that remains the same across multiple runs of your decision environment on different machines and operating systems. You may share the key with others to let them reproduce the results.

## Generating a parameter

In the real world, instances of a dataset are almost always collected and not generated. However, to heuristically simulate the data, to have a virtual twin of the real-world systems, we might be interested in using some arbitrary values that follow heuristically identified, observed, or detected by scientists throughout the years.

`data_toolkit` provides some easy-to-use methods based on [`numpy`](https://numpy.org/doc/stable/reference/random/generator.html#distributions), as follows:


| function               | range                                                                        |
| ---------------------- | ---------------------------------------------------------------------------- |
| `zeros`                | $\lbrace 0 \rbrace$                                                          |
| `ones`                 | $\lbrace 1 \rbrace$                                                          |
| `bernoulli`            | $\lbrace 0,1 \rbrace$                                                        |
| `binomial`             | $\lbrace 0,1,2,...,n \rbrace$                                                |
| `poisson`              | $\lbrace 0,1,2,... \rbrace$                                                  |
| `geometric`            | $\lbrace 1,2,... \rbrace$                                                    |
| `negative_binomial`    | $\lbrace r,r+1,r+2,... \rbrace$                                              |
| `hypergeometric`       | $\lbrace i: \max (0,n+m-N) \leqslant i \leqslant \min (m,n) \rbrace$         |
| `uniformint`           | $\lbrace a=0,2,...,b=n \rbrace$ (special case: $a=1$)                        |
| `uniform`              | $[a,b]$                                                                      |
| `normal` or `gaussian` | $(-\infty, \infty)$ (in 99.7% of cases $(\mu -3\sigma, \mu +3\sigma)$)       |
| `standard_normal`      | $(-\infty, \infty)$ (in 99.7% of cases $( -3, +3)$)                          |
| `exponential`          | $[0, \infty)$                                                                |
| `gamma`                | $[0, \infty)$                                                                |
| `erlang`               | $[0, \infty)$                                                                |
| `beta`                 | $(0,1)$                                                                      |
| `dirichlet`            | $[0,1]$ where $\sum_{i=1}^{k} x_i =1$ and $\alpha=[\alpha_1,...,\alpha_{k}]$ |
| `weight`               | $[0,1]$ where $\sum_{i=1}^{k} x_i =1$ (coefficients of a convex combination)                                       |
| `weibull`              | $(0,\infty)$                                                                 |
| `cauchy`               | $(-\infty, \infty)$                                                          |

An all-in-one example of using these functions is provided as follows:

```py
--8<-- "./concepts/parameters.py:generatingparameters"
```

Notably, as the names of all these parameters is `"a"` the generated values are replaced, till the last line of the code.

## Sampling a parameter

Some parameters might just be samples of a `set`, `list`, numpy `np.ndarray`, or pandas `pd.DataFrame`. In these cases, the following codes might be used:

### From a `set`


=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./concepts/parameters.py:samplingaset"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./concepts/parameters.txt:samplingaset"
    ```

### From a `list`

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./concepts/parameters.py:samplingalist"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./concepts/parameters.txt:samplingalist"
    ```


### From a `numpy` array

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./concepts/parameters.py:samplinganarray"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./concepts/parameters.txt:samplinganarray"
    ```

### From a `pandas` DataFrame

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./concepts/parameters.py:samplingpandas"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./concepts/parameters.txt:samplingpandas"
    ```

## Storing a parameter

Users might prefer storing some custom defined parameters using `data_toolkit`.

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./concepts/parameters.py:storingaparameter"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./concepts/parameters.txt:storingaparameter"
    ```

## Loading a parameter

FelooPy also enables users to load their structured datasets from Excel files! A sample code for each case is provided as follows:

### Loading a scalar

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./concepts/parameters.py:loadingaparameter1"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./concepts/parameters.txt:loadingaparameter1"
    ```

### Loading a vector


=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./concepts/parameters.py:loadingaparameter2"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./concepts/parameters.txt:loadingaparameter2"
    ```

### Loading a matrix


=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./concepts/parameters.py:loadingaparameter3"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./concepts/parameters.txt:loadingaparameter3"
    ```

### Loading a tensor


#### Header rows from top

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./concepts/parameters.py:loadingaparameter4"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./concepts/parameters.txt:loadingaparameter4"
    ```

#### Header columns from left

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./concepts/parameters.py:loadingaparameter5"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./concepts/parameters.txt:loadingaparameter5"
    ```