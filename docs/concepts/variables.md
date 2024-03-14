# Variables

Variables play a critical role in obtaining the best possible real/virtual world solutions or designs based on a decision environment, given the sets and parameters. While similar to parameters, variables encompass the values that need to be determined (preferably optimally) by a machine with a given or learnable feasible and logical policy and using search algorithms. Variables are either encoded-decoded directly (e.g., in exact optimization algorithms) or indirectly (e.g., in heuristic optimization algorithms). They can also be defined as tensors (e.g., in convex programming) or a special logical constraint (e.g., in constraint programming).

In this section, continuing the definition of [sets](sets.md), and [parameters](parameters.md), the way that variables are defined using FelooPy is described.

## Generating a variable

In FelooPy, variables are encapsulated within the `model` class, which offers intuitive methods for their creation.

## Multi-dimensional variables

The `model` class provides user-friendly methods for defining various types of multi-dimensional variables in FelooPy:

- Binary variable: Denoted as $y$ or $y_{ij}$.
- Integer variable: Denoted as $w$ or $w_{ij}$.
- Positive variable: Denoted as $x$ or $x_{ij}$.
- Free variable: Denoted as $z$ or $z_{ij}$.
- Sequence variable (vector): Denoted as $\mathbf{p}$.
- Event variable: Denoted as $c$ or $c_{ij}$.
- Random variable: Denoted as $\epsilon$ or $\epsilon_{ij}$.

| function | range                                                       |
| -------- | ----------------------------------------------------------- |
| `bvar`   | $\lbrace 0,1 \rbrace$                                       |
| `ivar`   | $\lbrace 0,1,2,... \rbrace$                                 |
| `pvar`   | $[0, \infty)$                                               |
| `fvar`   | $(-\infty, \infty)$                                         |
| `svar`   | $[\lbrace 0,1,2,... \rbrace,\lbrace 0,1,2,... \rbrace,...]$ |
| `evar`   | $[[0, \infty),[0, \infty)]$                                 |
| `rvar`   | $(-\infty, \infty)$                                         |

(Note: The range is defined for each index at each dimension.)

Here's an example demonstrating the definition of multi-dimensional variables in FelooPy:

```py
--8<-- "./concepts/variables.py:multidimensional"
```

## Tensor variables

Tensor variables are essential for handling complex decision environments in convex programming. The model class offers methods to define the following tensor variables:

- Binary tensor: Denoted as $\mathbf{y}$ or $\mathbf{Y}$.
- Integer tensor: Denoted as $\mathbf{w}$ or $\mathbf{W}$.
- Positive tensor: Denoted as $\mathbf{x}$ or $\mathbf{X}$.
- Free tensor: Denoted as $\mathbf{z}$ or $\mathbf{Z}$.
- Random tensor: Denoted as $\mathbf{\epsilon}$ or $\mathbf{E}$.

| function | range                       |
| -------- | --------------------------- |
| `btvar`  | $\lbrace 0,1 \rbrace$       |
| `itvar`  | $\lbrace 0,1,2,... \rbrace$ |
| `ptvar`  | $[0, \infty)$               |
| `ftvar`  | $(-\infty, \infty)$         |
| `rtvar`  | $(-\infty, \infty)$         |

(Note: The range is defined for each element at each axis of the specified shape.)

Here's an example illustrating the definition of tensor variables in FelooPy:

```py
--8<-- "./concepts/variables.py:tensor"
```

## Collection variables

Collection variables simplify the management of multiple variables with varying dimensions or bounds but sharing the same feature or meaning.

### A collection of multidimensional variables

The `model` class provides functions to define collections of multi-dimensional variables:

| function | range                                                       |
| -------- | ----------------------------------------------------------- |
| `cbvar`  | $\lbrace 0,1 \rbrace$                                       |
| `civar`  | $\lbrace 0,1,2,... \rbrace$                                 |
| `cpvar`  | $[0, \infty)$                                               |
| `cfvar`  | $(-\infty, \infty)$                                         |
| `csvar`  | $[\lbrace 0,1,2,... \rbrace,\lbrace 0,1,2,... \rbrace,...]$ |
| `cevar`  | $[[0, \infty),[0, \infty)]$                                 |
| `crvar`  | $(-\infty, \infty)$                                         |

(Note: The range is defined for each index at each dimension for each collection member.)

Here's an example showcasing the definition of multi-dimensional collection variables:

```py
--8<-- "./concepts/variables.py:multidimensionalcoll"
```

### A collection of tensor variables

Similarly, the `model` class offers functions to define collections of tensor variables:

| function | range                       |
| -------- | --------------------------- |
| `cbtvar` | $\lbrace 0,1 \rbrace$       |
| `citvar` | $\lbrace 0,1,2,... \rbrace$ |
| `cptvar` | $[0, \infty)$               |
| `cftvar` | $(-\infty, \infty)$         |
| `crtvar` | $(-\infty, \infty)$         |

(Note: The range is defined for each element at each axis of the specified shape for each collection member.)

Here's an example illustrating the definition of tensor collection variables in FelooPy:

```py
--8<-- "./concepts/variables.py:tensorcoll"
```

By leveraging these comprehensive variable definitions, FelooPy enables users to model diverse decision environments effectively and easily.