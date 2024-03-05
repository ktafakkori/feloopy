"""
SpecialConstraint Module

This module defines a class, `SpecialConstraintClass`, that facilitates the creation of special constraints with an explainable logic.

Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
See the file LICENSE file for licensing details.
"""

from .multidim_variable import MultidimVariable
from typing import List, Optional, Any

class Expression:
    pass

class SpecialConstraintClass:
    
    def con_exactly_one_one(self, binary_variables: List[MultidimVariable]):
        """
        Adds a constraint to the model ensuring exactly one variable in the list of binary variables is equal to 1.

        Parameters:
            binary_variables (List[MultidimVariable]): List of binary variables.
        """
        self.con(sum(binary_variables) == 1)
    
    def con_max_one_one(self, binary_variables: List[MultidimVariable]):
        """
        Adds a constraint to the model ensuring at most one variable in the list of binary variables is equal to 1.

        Parameters:
            binary_variables (List[MultidimVariable]): List of binary variables.
        """
        self.con(sum(binary_variables) <= 1)

    def con_min_one_one(self, binary_variables: List[MultidimVariable]):
        """
        Adds a constraint to the model ensuring at least one variable in the list of binary variables is equal to 1.

        Parameters:
            binary_variables (List[MultidimVariable]): List of binary variables.
        """
        self.con(sum(binary_variables) >= 1)
    
    def con_exactly_m_one(self, binary_variables: List[MultidimVariable], m: int):
        """
        Adds a constraint to the model ensuring exactly 'm' variables in the list of binary variables are equal to 1.

        Parameters:
            binary_variables (List[MultidimVariable]): List of binary variables.
            m (int): The exact number of variables that should be equal to 1.
        """
        self.con(sum(binary_variables) == m)

    def con_max_m_one(self, binary_variables: List[MultidimVariable], m: int):
        """
        Adds a constraint to the model ensuring at most 'm' variables in the list of binary variables are equal to 1.

        Parameters:
            binary_variables (List[MultidimVariable]): List of binary variables.
            m (int): The maximum number of variables that should be equal to 1.
        """
        self.con(sum(binary_variables) <= m)
    
    def con_min_m_one(self, binary_variables: List[MultidimVariable], m: int):
        """
        Adds a constraint to the model ensuring that at least 'm' variables in the list of binary variables are equal to 1.

        Parameters:
            binary_variables (List[MultidimVariable]): List of binary variables.
            m (int): The minimum number of variables that should be equal to 1.
        """
        self.con(sum(binary_variables) >= m)

    def con_only_one_of_the_values(self, variable: MultidimVariable, list_of_values: List[Any]):
        """
        Adds a constraint to the model ensuring that the variable can only take one value from the list of values.

        Parameters:
            variable (MultidimVariable): The variable that should take a value from the list.
            list_of_values (List[Any]): List of potential values for the variable.
        """
        try:
            for i in range(len(list_of_values)):
                self.features['indicators'].append(self.features['indicators'][-1] + 1)
        except:
            self.features['indicators'] = []
            for i in range(len(list_of_values)):
                self.features['indicators'].append(i)
        
        z = self.bvar(f"indicator{self.features['indicators'][-1]}", [range(len(list_of_values))])
        self.con(variable == sum(list_of_values[i] * z[i] for i in range(len(list_of_values))))
        self.con(sum(z[i] for i in range(len(list_of_values))) == 1)
        
    def con_only_one_of_the_values_or_zero(self, variable: MultidimVariable, list_of_values: List[Any]):
        """
        Adds a constraint to the model ensuring that the variable can either take one value from the list of values or be zero.

        Parameters:
            variable (MultidimVariable): The variable that should take a value from the list or be zero.
            list_of_values (List[Any]): List of potential values for the variable.
        """
        try:
            for i in range(len(list_of_values)):
                self.features['indicators'].append(self.features['indicators'][-1] + 1)
        except:
            self.features['indicators'] = []
            for i in range(len(list_of_values)):
                self.features['indicators'].append(i)
        
        z = self.bvar(f"indicator{self.features['indicators'][-1]}", [range(len(list_of_values))])
        self.con(variable == sum(list_of_values[i] * z[i] for i in range(len(list_of_values))))
        self.con(sum(z[i] for i in range(len(list_of_values))) <= 1)

    def con_this_depends_on_that(self, this: MultidimVariable, that: MultidimVariable):
        """
        Adds a constraint to the model ensuring that the 'this' variable should be less than or equal to the 'that' variable.

        Parameters:
            this (MultidimVariable): The dependent variable.
            that (MultidimVariable): The variable that 'this' is dependent on.
        """
        self.con(this <= that)

    def con_this_indeed_that(self, this: MultidimVariable, that: MultidimVariable):
        """
        Adds a constraint to the model ensuring that the 'this' variable should be equal to or less than the 'that' variable.

        Parameters:
            this (MultidimVariable): The dependent variable.
            that (MultidimVariable): The variable that 'this' depends on.
        """
        self.con(this <= that)

    def con_soft_indicator_leq(self, indicator: MultidimVariable, expr: Expression, rhs: float, big_m: float = 1e9) -> None:
        """
        Adds a soft constraint to the model. Relaxes the constraint expr <= rhs by allowing it to be false. 
        The indicator variable decides whether the constraint should be enforced (1) or not (0).

        Parameters:
            indicator (MultidimVariable): The binary variable indicating whether the constraint should be enforced or not.
            expr (Expression): The left-hand side of the constraint.
            rhs (float): The right-hand side of the constraint.
            big_m (float): A large positive number used for relaxation. Default is 1e9.
        """
        self.con(expr <= rhs + (1 - indicator) * big_m)
    
    def con_soft_indicator_geq(self, indicator: MultidimVariable, expr: Expression, rhs: float, big_m: float = 1e9) -> None:
        """
        Adds a soft constraint to the model. Relaxes the constraint expr >= rhs by allowing it to be false. 
        The indicator variable decides whether the constraint should be enforced (1) or not (0).

        Parameters:
            indicator (MultidimVariable): The binary variable indicating whether the constraint should be enforced or not.
            expr (Expression): The left-hand side of the constraint.
            rhs (float): The right-hand side of the constraint.
            big_m (float): A large positive number used for relaxation. Default is 1e9.
        """
        self.con(expr >= rhs - (1 - indicator) * big_m)

    def con_this_or_that(
        self,
        this: Expression,
        rhs_this: float,
        that: Expression,
        rhs_that: float,
        big_m: float = 1e9
    ) -> None:
        """
        Adds two constraints and one indicator variable to the model. The constraints ensure that either 'this' is less than or equal to 'rhs_this' or 'that' is less than or equal to 'rhs_that'.
        Note: Variables can also be expressions.

        Parameters:
            this (Expression): The first variable or expression.
            rhs_this (float): The upper limit for the 'this' variable or expression.
            that (Expression): The second variable or expression.
            rhs_that (float): The upper limit for the 'that' variable or expression.
            big_m (float): A large positive number used for relaxation. Default is 1e9.
        """
        try:
            self.features['indicators'].append(self.features['indicators'][-1] + 1)
        except:
            self.features['indicators'] = [0]

        z = self.bvar(f"indicator{self.features['indicators'][-1]}")

        self.con(this <= rhs_this + z * big_m)
        self.con(that <= rhs_that + (1 - z) * big_m)
        
    def con_if_then(
        self,
        this: Expression,
        rhs_this: float,
        that: Expression,
        rhs_that: float,
        big_m: float = 1e9,
        epsilon: float = 1e-9
    ) -> None:
        """
        Adds two constraints and one indicator variable to the model. If 'this' is less than or equal to 'rhs_this', then 'that' should be less than or equal to 'rhs_that'.
        Note: Variables can also be expressions.

        Parameters:
            this (Expression): The condition variable or expression.
            rhs_this (float): The upper limit for the 'this' variable or expression.
            that (Expression): The dependent variable or expression.
            rhs_that (float): The upper limit for the 'that' variable or expression.
            big_m (float): A large positive number used for relaxation. Default is 1e9.
            epsilon (float): A small positive number to ensure strict inequality. Default is 1e-9.
        """
        try:
            self.features['indicators'].append(self.features['indicators'][-1] + 1)
        except:
            self.features['indicators'] = [0]
        z = self.bvar(f"indicator{self.features['indicators'][-1]}")
        self.con(this >= rhs_this + epsilon - z * big_m)
        self.con(that <= rhs_that + (1 - z) * big_m)

    def con_leq_viol(self, expr: Expression, rhs: float = 0) -> MultidimVariable:
        """
        Adds a constraint to the model that represents the amount of violation for soft constraints of type less than or equal to (<=).

        Parameters:
            expr (Expression): The expression that should be less than or equal to 'rhs'.
            rhs (float): The right-hand side of the constraint. Default is 0.

        Returns:
            MultidimVariable: The variable representing the amount of violation.
        """
        try:
            self.features['indicators'].append(self.features['indicators'][-1] + 1)
        except:
            self.features['indicators'] = [0]
        z = self.pvar(f"indicator{self.features['indicators'][-1]}")
        self.con(expr <= rhs + z)
        return z

    def con_geq_viol(self, expr: Expression, rhs: float = 0) -> MultidimVariable:
        """
        Adds a constraint to the model that represents the amount of violation for soft constraints of type greater than or equal to (>=).

        Parameters:
            expr (Expression): The expression that should be greater than or equal to 'rhs'.
            rhs (float): The right-hand side of the constraint. Default is 0.

        Returns:
            MultidimVariable: The variable representing the amount of violation.
        """
        try:
            self.features['indicators'].append(self.features['indicators'][-1] + 1)
        except:
            self.features['indicators'] = [0]
        z = self.pvar(f"indicator{self.features['indicators'][-1]}")
        self.con(expr >= rhs - z)
        return z

    def con_eq_viol(self, expr: Expression, rhs: float = 0) -> MultidimVariable:
        """
        Adds two constraints to the model that represent the amount of violation for soft constraints of type equal to (==).

        Parameters:
            expr (Expression): The expression that should be equal to 'rhs'.
            rhs (float): The right-hand side of the constraint. Default is 0.

        Returns:
            MultidimVariable: The variable representing the amount of violation.
        """
        try:
            self.features['indicators'].append(self.features['indicators'][-1] + 1)
        except:
            self.features['indicators'] = [0]
        z = self.pvar(f"indicator{self.features['indicators'][-1]}")
        self.con(expr <= rhs + z)
        self.con(expr >= rhs - z)
        return z

    def con_leq_slack(self, expr: Expression, rhs: float = 0) -> MultidimVariable:
        """
        Adds a slack variable to the model for a less than or equal to (<=) constraint. The slack variable represents the difference between the left-hand side expression and the right-hand side.

        Parameters:
            expr (Expression): The expression that should be less than or equal to 'rhs'.
            rhs (float): The right-hand side of the constraint. Default is 0.

        Returns:
            MultidimVariable: The slack variable.
        """
        try:
            self.features['indicators'].append(self.features['indicators'][-1] + 1)
        except:
            self.features['indicators'] = [0]
        z = self.pvar(f"indicator{self.features['indicators'][-1]}")
        self.con(expr + z == rhs)
        return z

    def con_geq_surplus(self, expr: Expression, rhs: float = 0) -> MultidimVariable:
        """
        Adds a surplus variable to the model for a greater than or equal to (>=) constraint. The surplus variable represents the difference between the left-hand side expression and the right-hand side.

        Parameters:
            expr (Expression): The expression that should be greater than or equal to 'rhs'.
            rhs (float): The right-hand side of the constraint. Default is 0.

        Returns:
            MultidimVariable: The surplus variable.
        """
        try:
            self.features['indicators'].append(self.features['indicators'][-1] + 1)
        except:
            self.features['indicators'] = [0]
        z = self.pvar(f"indicator{self.features['indicators'][-1]}")
        self.con(expr - z == rhs)
        return z

    def con_expr_in_bound(self, expr: Expression, lb: Optional[float] = None, ub: Optional[float] = None, name: Optional[str] = None):
        """
        Creates upper and/or lower bounds on the given variable in the optimization model.

        Parameters:
            expr (Expression): The variable expression.
            lb (float, optional): Lower bound. Default is None.
            ub (float, optional): Upper bound. Default is None.
            name (str, optional): name for the constraint. Default is None.
        """
        if lb is not None:
            self.con(expr >= lb, name=name)
        if ub is not None:
            self.con(expr <= ub, name=name)

    def con_abs_leq(self, expr: Expression, rhs: float):
        """
        Linearizes a constraint like │a│ <= b.

        Parameters:
            expr (Expression): The expression inside the absolute value.
            rhs (float): The right-hand side of the constraint.
        """
        self.con(expr >= -rhs)
        self.con(expr <= rhs)
        
    def con_abs_geq(self, expr: Expression, rhs: float, big_m: float = 1e9):
        """
        Linearizes a constraint like │a│ >= b.

        Parameters:
            expr (Expression): The expression inside the absolute value.
            rhs (float): The right-hand side of the constraint.
            big_m (float): A large positive number used for relaxation. Default is 1e9.
        """
        try:
            self.features['abs_geq_linearizers'].append(
                self.features['abs_geq_linearizers'][-1] + 1)
        except:
            self.features['abs_geq_linearizers'] = [0]

        z = self.bvar(
            f"abs_geq_linearizer{self.features['abs_geq_linearizers'][-1]}")
        
        self.con_this_or_that(expr >= rhs - z * big_m, expr <= -1 * rhs + (1 - z) * big_m)
