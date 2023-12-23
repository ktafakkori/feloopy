"""
Linearization Module

This module defines a class, `LinearizationClass`, that facilitates the linearization of mathematical models.

Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
See the file LICENSE file for licensing details.
"""

from .multidim_variable import MultidimVariable
from .special_constraint import Expression
from typing import List, Optional, Tuple, Callable, Union
import numpy as np
import math as mt

class LinearizationClass:
    

    def lin_piecewise(self, slopes: List[float], intercepts: List[float], breakpoints: List[float]) -> Expression:
        """
        Implements a piecewise linear function in the context of mathematical programming.

        Parameters:
            slopes (List[float]): A list of slopes for each piece of the function.
            intercepts (List[float]): A list of intercepts for each piece of the function.
            breakpoints (List[float]): A list of breakpoints that define the domain of each piece of the function.

        Returns:
            Expression: The piecewise linear function represented as a sum of linear functions, each multiplied by a binary variable.

        Note:
            The function is represented as a sum of linear functions, each multiplied by a binary variable that indicates whether that piece of the function is active. The constraints ensure that only one piece is active at any point in the domain.
        """
        try:
            self.features['indicators'].append(self.features['indicators'][-1] + 1)
        except:
            self.features['indicators'] = [0]

        x = self.pvar(f"indicatorr{self.features['indicators'][-1]}", range(len(breakpoints)))
        y = self.bvar(f"indicatorr{self.features['indicators'][-1]}", range(len(breakpoints)))

        for i in range(len(breakpoints) - 1):
            self.con((breakpoints[i+1] - breakpoints[i]) * y[i] <= x[i])
            self.con(x[i] <= (breakpoints[i+1] - breakpoints[i]) * y[i+1])

        self.con(sum(y[i] for i in range(len(breakpoints))) == 1)

        return sum((slopes[i] * x[i] + intercepts[i]) * y[i] for i in range(len(breakpoints)))

    def lin_approx(self, f: Callable, x: MultidimVariable, x_range: Tuple[float, float], num_breakpoints: int) -> Expression:
        """
        Implements a piecewise linear approximation of a non-linear function in the context of mathematical programming.

        Parameters:
            f (Callable): The non-linear function to be approximated.
            x (MultidimVariable): The variable of the non-linear function.
            x_range (Tuple[float, float]): A tuple of two numbers representing the minimum and maximum values of x.
            num_breakpoints (int): The number of breakpoints to use in the approximation.

        Returns:
            Expression: The piecewise linear approximation of the non-linear function.
        """
        breakpoints = np.linspace(x_range[0], x_range[1], num_breakpoints)
        slopes = [(f(breakpoints[i+1]) - f(breakpoints[i])) / (breakpoints[i+1] - breakpoints[i]) for i in range(len(breakpoints)-1)]
        intercepts = [f(breakpoints[i]) - slopes[i] * breakpoints[i] for i in range(len(breakpoints)-1)]
        
        return self.lin_piecewise(slopes, intercepts, breakpoints)

    def lin_abs_in_obj(self, expr: Expression, method: int = 0, dir_obj: Optional[str] = None) -> Expression:
        """
        Linearizes an │a│ expression inside the objective function.

        Parameters:
            expr (Expression): The absolute value expression to be linearized.
            method (int): The method to use for linearization.
                - method 0: Uses +2 pvars and +1 constraint (for min and max).
                - method 1: Uses +1 pvar and +2 constraints (+1 bvar for max) (for min or max, requires user input).
                - method 2: Uses +1 pvar and +1 constraint (only for min, does not require user input).
            dir_obj (str): The direction of the objective function. Required for method 1 when linearizing for max.

        Returns:
            Expression: The linearized expression.

        Note:
            The linearization is performed based on the chosen method and the direction of the objective function.
        """
        if method == 0:
            try:
                self.features['abs_obj_linearizers'].append(self.features['abs_obj_linearizers'][-1] + 1)
                self.features['abs_obj_linearizers'].append(self.features['abs_obj_linearizers'][-1] + 1)
            except:
                self.features['abs_obj_linearizers'] = [0, 1]
            z1 = self.pvar(f"abs_obj_linearizer{self.features['abs_obj_linearizers'][-1]}")
            z2 = self.pvar(f"abs_obj_linearizer{self.features['abs_obj_linearizers'][-2]}")
            self.con(expr == z1 - z2)
            return z1 + z2

        if method == 1:
            if dir_obj == 'min':
                try:
                    self.features['abs_obj_linearizers'].append(self.features['abs_obj_linearizers'][-1] + 1)
                except:
                    self.features['abs_obj_linearizers'] = [0]
                z = self.pvar(f"abs_obj_linearizer{self.features['abs_obj_linearizers'][-1]}")
                self.scon_abs_leq(expr, z)
                return z
            elif dir_obj == 'max':
                try:
                    self.features['abs_obj_linearizers'].append(self.features['abs_obj_linearizers'][-1] + 1)
                except:
                    self.features['abs_obj_linearizers'] = [0]
                z = self.pvar(f"abs_obj_linearizer{self.features['abs_obj_linearizers'][-1]}")
                self.scon_abs_geq(expr, z)
                return z

        if method == 2:
            try:
                self.features['abs_obj_linearizers'].append(self.features['abs_obj_linearizers'][-1] + 1)
            except:
                self.features['abs_obj_linearizers'] = [0]
            z = self.pvar(f"abs_obj_linearizer{self.features['abs_obj_linearizers'][-1]}")
            self.con(expr + z >= 0)
            return expr + 2 * z

    def lin_max(self, input_list: List[Expression], type_max: str, ub_max: Union[float, None] = None) -> Expression:
        """
        Linearizes the max function.

        Parameters:
            input_list (List[Expression]): The list of expressions to be linearized.
            type_max (str): The type of variable to use for linearization.
            ub_max (Union[float, None]): The upper bound for the linearized expression (optional).

        Returns:
            Expression: The linearized expression.

        Note:
            The linearization is performed based on the type of variable chosen for linearization and the upper bound, if provided.
        """
        if self.features['solution_method'] == 'exact':
            try:
                self.features['max_linearizers'].append(self.features['max_linearizers'][-1] + 1)
            except:
                self.features['max_linearizers'] = [0]

            if type_max == 'bvar':
                z = self.bvar(f"max_linearizer{self.features['max_linearizers'][-1]}")
            elif type_max == 'ivar':
                z = self.ivar(f"max_linearizer{self.features['max_linearizers'][-1]}")
            elif type_max == 'pvar':
                z = self.pvar(f"max_linearizer{self.features['max_linearizers'][-1]}")
            elif type_max == 'fvar':
                z = self.fvar(f"max_linearizer{self.features['max_linearizers'][-1]}")

            for item in input_list:
                self.con(z >= item)
            if ub_max is not None:
                self.con(z <= ub_max)
            return z

    def lin_min(self, input_list: List[Expression], type_min: str, lb_min: Union[float, None] = None) -> Expression:
        """
        Linearizes the min function.

        Parameters:
            input_list (List[Expression]): The list of expressions to be linearized.
            type_min (str): The type of variable to use for linearization.
            lb_min (Union[float, None]): The lower bound for the linearized expression (optional).

        Returns:
            Expression: The linearized expression.

        Note:
            The linearization is performed based on the type of variable chosen for linearization and the lower bound, if provided.
        """
        try:
            self.features['min_linearizers'].append(self.features['min_linearizers'][-1] + 1)
        except:
            self.features['min_linearizers'] = [0]

        if type_min == 'bvar':
            z = self.bvar(f"min_linearizer{self.features['min_linearizers'][-1]}")
        elif type_min == 'ivar':
            z = self.ivar(f"min_linearizer{self.features['min_linearizers'][-1]}")
        elif type_min == 'pvar':
            z = self.pvar(f"min_linearizer{self.features['min_linearizers'][-1]}")
        elif type_min == 'fvar':
            z = self.fvar(f"min_linearizer{self.features['min_linearizers'][-1]}")

        for item in input_list:
            self.con(z <= item)
        if lb_min is not None:
            self.con(z >= lb_min)
        return z

    def lin_prod_bb(self, binary1: MultidimVariable, binary2: MultidimVariable) -> MultidimVariable:
        """
        Linearizes a Binary * Binary product.

        Returns:
            MultidimVariable: The linearized expression.

        Note:
            The linearization requires +3 constraints and +1 positive variable.
        """
        try:
            self.features['bb_linearizers'].append(self.features['bb_linearizers'][-1] + 1)
        except:
            self.features['bb_linearizers'] = [0]

        z = self.pvar(f"bb_linearizer{self.features['bb_linearizers'][-1]}")
        self.con(z <= binary1)
        self.con(z <= binary2)
        self.con(z >= binary1 + binary2 - 1)
        return z
    
    def lin_prod_bp(self, binary: MultidimVariable, positive: MultidimVariable, ub_positive: float = 1e9) -> MultidimVariable:
        """
        Linearizes a Binary * Positive product.

        Returns:
            MultidimVariable: The linearized expression.

        Note:
            The linearization requires +3 constraints and +1 positive variable.
        """
        try:
            self.features['bp_linearizers'].append(self.features['bp_linearizers'][-1] + 1)
        except:
            self.features['bp_linearizers'] = [0]

        z = self.pvar(f"bp_linearizer{self.features['bp_linearizers'][-1]}")
        self.con(z <= positive)
        self.con(z <= binary * ub_positive)
        self.con(z >= positive - ub_positive * (1 - binary))
        return z

    def lin_prod_bi(self, binary: MultidimVariable, integer: MultidimVariable, ub_integer: float = 1e9) -> MultidimVariable:
        """
        Linearizes a Binary * Integer product.

        Returns:
            MultidimVariable: The linearized expression.

        Note:
            The linearization requires +3 constraints and +1 positive variable.
        """
        try:
            self.features['bi_linearizers'].append(self.features['bi_linearizers'][-1] + 1)
        except:
            self.features['bi_linearizers'] = [0]

        z = self.pvar(f"bi_linearizer{self.features['bi_linearizers'][-1]}")
        self.con(z <= integer)
        self.con(z <= binary * ub_integer)
        self.con(z >= integer - ub_integer * (1 - binary))
        return z

    def lin_prod_ip(self, integer: MultidimVariable, positive: MultidimVariable, ub_integer: int, ub_positive: float) -> MultidimVariable:
        """
        Linearizes an Integer * Positive product.

        Returns:
            MultidimVariable: The linearized expression.

        Note:
            The linearization requires +1 + 3 * (mt.ceil(mt.log2(ub_integer + 1))) constraints, +
            (mt.ceil(mt.log2(ub_integer + 1))) positive variables, and +
            (mt.ceil(mt.log2(ub_integer + 1))) binary variables.
        """
        try:
            self.features['ip_linearizers'].append(self.features['ip_linearizers'][-1] + 1)
        except:
            self.features['ip_linearizers'] = [0]

        z = self.pvar(f"ip_linearizer{self.features['ip_linearizers'][-1]}", [range(mt.ceil(mt.log2(ub_integer + 1)))])
        x = self.bvar(f"ip_binary_convert{self.features['ip_linearizers'][-1]}", [range(mt.ceil(mt.log2(ub_integer + 1)))])
        
        self.con(integer == sum(2**i * x[i] for i in range(mt.ceil(mt.log2(ub_integer + 1)))))

        for i in range(mt.ceil(mt.log2(ub_integer + 1))):
            self.con(z[i] <= positive)
            self.con(z[i] <= x[i] * ub_positive)
            self.con(z[i] >= positive - ub_positive * (1 - x[i]))

        return sum(2**i * z[i] for i in range(mt.ceil(mt.log2(ub_integer + 1))))

    def lin_prod_ii(self, integer1: MultidimVariable, integer2: MultidimVariable, ub_integer1: int, ub_integer2: int) -> MultidimVariable:
        """
        Linearizes an Integer * Integer product.

        Returns:
            MultidimVariable: The linearized expression.

        Note:
            The linearization requires +1 + 3 * (mt.ceil(mt.log2(ub_integer + 1))) constraints, +
            (mt.ceil(mt.log2(ub_integer + 1))) positive variables, and +
            (mt.ceil(mt.log2(ub_integer + 1))) binary variables.
        """

        try:
            self.features['ii_linearizers'].append(self.features['ii_linearizers'][-1] + 1)
        except:
            self.features['ii_linearizers'] = [0]

        z = self.pvar(f"ii_linearizer{self.features['ii_linearizers'][-1]}", [range(mt.ceil(mt.log2(ub_integer1 + 1)))])
        x = self.bvar(f"ii_binary_convert{self.features['ii_linearizers'][-1]}", [range(mt.ceil(mt.log2(ub_integer1 + 1)))])

        self.con(integer1 == sum(2**i * x[i] for i in range(mt.ceil(mt.log2(ub_integer1 + 1)))))

        for i in range(mt.ceil(mt.log2(ub_integer1 + 1))):
            self.con(z[i] <= integer2)
            self.con(z[i] <= x[i] * ub_integer2)
            self.con(z[i] >= integer2 - ub_integer2 * (1 - x[i]))

        return sum(2**i * z[i] for i in range(mt.ceil(mt.log2(ub_integer1 + 1))))