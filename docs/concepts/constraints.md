# Constraints

Constraints are critical elements of decision environments based on mathematical programming. They can be inequalities or equalities with six different senses: less than or equal $\leqslant$, less than $<$, greater than or equal $\geqslant$, greater than $>$, equal $=$ or inequal $\ne$. Your mathematical expression (or function), in a standard form, is positioned on the left, (i.e., left-hand-side), and a threshold, resource, capacity, or satisfaction level is positioned on the right (i.e., right-hand-side). While their existence varies, it is more probable to see them in the context of modeling real-world decision environments rather than virtual ones. Soft constraints offer flexibility, permitting adjustments of their thresholds, while hard constraints impose strict limitations and sometimes lead to infeasibility.

# Defining constraints

Consider the following constraint:

$$ \sum_{i \in I} p_{ij} x_{i} \geqslant v_{j}, \quad \forall j \in J$$


FelooPy supports defining constraints in 7 different ways as follows:

```py
--8<-- "./concepts/constraints.py:constraintdefintion"
```