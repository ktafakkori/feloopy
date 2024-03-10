This section outlines the process of defining sets within any decision environment. Initially, it's necessary to instantiate a data toolkit, which facilitates dataset manipulation. Notably, sets are integral components of your data. The coding procedure of sets begins as follows:

```py
--8<-- "./concepts/sets.py:setenvironment"
```

## Simple set

You can define a simple set with named indices as follows:

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./concepts/sets.py:simpleset"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./concepts/sets.txt:simpleset"
    ```

This code snippet creates a set I with indices from 0 to 9, where each index is named. Note that the `set` type returned by this code is unordered.

## Recommended set

In some cases, it's advisable to avoid named indices, especially in large-scale decision environments, as they can lead to expensive computations. Here's how to define a set without named indices:


=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./concepts/sets.py:recommendedset"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./concepts/sets.txt:recommendedset"
    ```

## Conditional set

To create a set based on a condition, such as including only even numbers, use the following code:

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./concepts/sets.py:conditionalset"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./concepts/sets.txt:conditionalset"
    ```


## List set

If a `list` type of set is preferable, you can use the following code:

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./concepts/sets.py:setaslist"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./concepts/sets.txt:setaslist"
    ```

## Range set

If a `range` type of a set is preferable, you can use the following code:

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./concepts/sets.py:setasrange"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./concepts/sets.txt:setasrange"
    ```

## Direct set

Direct sets provide a straightforward way to instantiate and store sets with specific elements. These sets are dynamically deduced based on other datasets. Three types of direct sets are outlined below:

### Type 1: From a function

In this example, a direct set is created using the `range` function, representing the integers from 0 to 9.

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./concepts/sets.py:directset1"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./concepts/sets.txt:directset1"
    ```

### Type 2: From an integer

Another type of direct set is illustrated here, where you only use integers to initiate sets.

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./concepts/sets.py:directset2"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./concepts/sets.txt:directset2"
    ```

Note that this is equivalent to using the `size` argument as follows:

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./concepts/sets.py:directset4"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./concepts/sets.txt:directset4"
    ```

### Type 3: From a `numpy` array

In this example, a direct set is created using `numpy`, initializing it with a specific array and axis.

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./concepts/sets.py:directset3"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./concepts/sets.txt:directset3"
    ```

## Alais set

If it is desired to create and store another set J with attributes same as I, you may use the following code: 

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./concepts/sets.py:alaisset1"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./concepts/sets.txt:alaisset1"
    ```

which is equivalent to:

=== ":fontawesome-brands-python: Python"

    ```py
    --8<-- "./concepts/sets.py:alaisset2"
    ```

=== ":material-console: Console"

    ```console
    --8<-- "./concepts/sets.txt:alaisset2"
    ```

After creating a set using one of the above commands you may use the standard [set operations of Python](https://docs.python.org/3/library/stdtypes.html#set) (if the returned type is `set`, by default) or you may use the standard [list operations of Python](https://docs.python.org/3/library/stdtypes.html#lists) (if the returned type is `list`, i.e., `to_list=True`) or you may use the standard [range operations of Python](https://docs.python.org/3/library/stdtypes.html#ranges) (if the returned type is `range`, i.e., `to_range=True`). If you create a set with named indices or a special callback function, returning the created set as a `range` is impossible.

!!! note

    If order is important, you may use `to_range=True` or `to_list=True` arguments.

!!! note

    Complex multi-dimensional sets (e.g., $J = \lbrace (0,1),(1,2),...,(10,10) \rbrace$ or $J = \lbrace (i,k): i \in I \wedge k \in K_i\rbrace$) are always recommended to be constructed by the users, as Python offers flexibility in this regard.