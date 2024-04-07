"""
Multi-dimensional variables module

This module facilitates the creation of various types of multi-dimensional variables.

Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
See the file LICENSE file for licensing details.
"""

from typing import List, Optional, Union
import itertools as it
import numpy as np
from ..operators.fix_operators import fix_dims
from ..operators.update_operators import update_variable_features


    
class MultidimVariable:
    """Specifies the variable type."""

class MultidimVariableClass:
    """Class that provides methods to create multi-dimensional variables."""
    
    def fvar(
        self,
        name: str,
        dim: List[int] = 0,
        bound: List[Optional[float]] = [None, None]
    ) -> MultidimVariable:
        
        """
        Creates and returns a free variable.

        Parameters
        ----------
        name : str
            Name.
        dim : List[int], optional
            Dimensions. Default is 0.
        bound : List[Optional[float]], optional
            Lower and upper bounds. Default is [None, None]. Required for heuristic optimization.

        Returns
        -------
        MultidimVariable
            A free variable.
        """

        dim = self.fix_ifneeded(dim)
        self.features = update_variable_features(name, dim, bound, 'free_variable_counter', self.features)

        if self.features['solution_method'] == 'exact':
            from ..generators import variable_generator
            self.features['variables'][("fvar", name)] = variable_generator.generate_variable(
                self.features['interface_name'], self.model, 'fvar', name, bound, dim
            )
            self.features['dimensions'][name] = dim
            return self.features['variables'][("fvar", name)]

        elif self.features['solution_method'] == 'heuristic':
            from ..operators.heuristic_operators import generate_heuristic_variable
            return generate_heuristic_variable(
                self.features, 'fvar', name, dim, bound, self.agent, self.no_agents
            )
        
    def pvar(
        self,
        name: str,
        dim: List[int] = 0,
        bound: List[Optional[float]] = [0, None]
    ) -> MultidimVariable:
        """
        Creates and returns a positive variable.

        Parameters
        ----------
        name : str
            Name of this variable.
        dim : List[int], optional
            Dimensions of this variable. Default: 0.
        bound : List[Optional[float]], optional
            Bounds of this variable. Default: [0, None].

        Returns
        -------
        MultidimVariable
            A positive variable.
        """

        dim = self.fix_ifneeded(dim)
        self.features = update_variable_features(name, dim, bound, 'positive_variable_counter', self.features)

        if self.features['solution_method'] == 'exact':
            from ..generators import variable_generator
            self.features['variables'][("pvar", name)] = variable_generator.generate_variable(
                self.features['interface_name'], self.model, 'pvar', name, bound, dim
            )
            self.features['dimensions'][name] = dim

            if self.features['interface_name'] in ['rsome_ro', 'rsome_dro', 'cvxpy']:
                if dim == 0:
                    self.con(self.features['variables'][("pvar", name)] >= 0)
                    if bound[1] is not None:
                        self.con(self.features['variables'][("pvar", name)] <= bound[1])
                elif len(dim) == 1:
                    for i in dim[0]:
                        self.con(self.features['variables'][("pvar", name)][i] >= 0)
                        if bound[1] is not None:
                            self.con(self.features['variables'][("pvar", name)][i] <= bound[1])
                else:
                    for i in it.product(*tuple(dim)):
                        self.con(self.features['variables'][("pvar", name)][i] >= 0)
                        if bound[1] is not None:
                            self.con(self.features['variables'][("pvar", name)][i] <= bound[1])

            return self.features['variables'][("pvar", name)]

        elif self.features['solution_method'] == 'heuristic':
            from ..operators.heuristic_operators import generate_heuristic_variable
            return generate_heuristic_variable(
                self.features, 'pvar', name, dim, bound, self.agent, self.no_agents
            )
    
    def ivar(
        self,
        name: str,
        dim: List[int] = 0,
        bound: List[Optional[float]] = [0, None]
    ) -> MultidimVariable:
        """
        Creates and returns an integer variable.

        Parameters
        ----------
        name : str
            Name of this variable.
        dim : List[int], optional
            Dimensions of this variable. Default: 0.
        bound : List[Optional[float]], optional
            Bounds of this variable. Default: [0, None].

        Returns
        -------
        MultidimVariable
            An integer variable.
        """

        dim = self.fix_ifneeded(dim)
        self.features = update_variable_features(name, dim, bound, 'integer_variable_counter', self.features)

        if self.features['solution_method'] == 'exact':
            from ..generators import variable_generator
            self.features['variables'][("ivar", name)] = variable_generator.generate_variable(
                self.features['interface_name'], self.model, 'ivar', name, bound, dim
            )
            self.features['dimensions'][name] = dim

            if self.features['interface_name'] in ['rsome_ro', 'rsome_dro', 'cvxpy']:
                if dim == 0:
                    self.con(self.features['variables'][("ivar", name)] >= 0)
                    if bound[1] is not None:
                        self.con(self.features['variables'][("ivar", name)] <= bound[1])
                elif len(dim) == 1:
                    for i in dim[0]:
                        self.con(self.features['variables'][("ivar", name)][i] >= 0)
                        if bound[1] is not None:
                            self.con(self.features['variables'][("ivar", name)][i] <= bound[1])
                else:
                    for i in it.product(*tuple(dim)):
                        self.con(self.features['variables'][("ivar", name)][i] >= 0)
                        if bound[1] is not None:
                            self.con(self.features['variables'][("ivar", name)][i] <= bound[1])

            return self.features['variables'][("ivar", name)]

        elif self.features['solution_method'] == 'heuristic':
            from ..operators.heuristic_operators import generate_heuristic_variable
            return generate_heuristic_variable(
                self.features, 'ivar', name, dim, bound, self.agent, self.no_agents
            )

    def bvar(
        self,
        name: str,
        dim: List[int] = 0,
        bound: List[Optional[float]] = [0, 1]
    ) -> MultidimVariable:
        """
        Creates and returns a binary variable.

        Parameters
        ----------
        name : str
            Name of this variable.
        dim : List[int], optional
            Dimensions of this variable. Default: 0.
        bound : List[Optional[float]], optional
            Bounds of this variable. Default: [0, 1].

        Returns
        -------
        MultidimVariable
            A binary variable.
        """

        dim = self.fix_ifneeded(dim)
        self.features = update_variable_features(name, dim, bound, 'binary_variable_counter', self.features)

        if self.features['solution_method'] == 'exact':
            from ..generators import variable_generator
            self.features['variables'][("bvar", name)] = variable_generator.generate_variable(
                self.features['interface_name'], self.model, 'bvar', name, bound, dim
            )
            self.features['dimensions'][name] = dim

            if self.features['interface_name'] in ['cvxpy']:
                if dim == 0:
                    self.con(self.features['variables'][("bvar", name)] >= 0)
                    self.con(self.features['variables'][("bvar", name)] <= 1)
                elif len(dim) == 1:
                    for i in dim[0]:
                        self.con(self.features['variables'][("bvar", name)][i] >= 0)
                        self.con(self.features['variables'][("bvar", name)][i] <= 1)
                else:
                    for i in it.product(*tuple(dim)):
                        self.con(self.features['variables'][("bvar", name)][i] >= 0)
                        self.con(self.features['variables'][("bvar", name)][i] <= 1)
            return self.features['variables'][("bvar", name)]

        elif self.features['solution_method'] == 'heuristic':
            from ..operators.heuristic_operators import generate_heuristic_variable
            return generate_heuristic_variable(
                self.features, 'bvar', name, dim, bound, self.agent, self.no_agents
            )
            
    def svar(
        self,
        name: str,
        length: int = 1
    ) -> MultidimVariable:
        """
        Creates and returns a sequence variable.

        Parameters
        ----------
        name : str
            Name of this variable.
        length : int, optional
            Length of this variable. Default: 1.

        Returns
        -------
        MultidimVariable
            A sequence variable.
        """

        dim = fix_dims([length])
        self.features = update_variable_features(name, dim, [0, 1], 'sequential_variable_counter', self.features)

        if self.features['solution_method'] == 'heuristic':
            from ..operators.heuristic_operators import generate_heuristic_variable
            return generate_heuristic_variable(
                self.features, 'svar', name, dim, [0, 1], self.agent, self.no_agents
            )
        
    def rvar(
        self,
        name: str,
        dim: List[int] = 0
    ) -> MultidimVariable:
        """
        Creates and returns a random variable.

        Parameters
        ----------
        name : str
            Name of this variable.
        dim : List[int], optional
            Dimensions of this variable. Default: 0.

        Returns
        -------
        MultidimVariable
            A random variable.
        """
        dim = self.fix_ifneeded(dim)
        from ..generators import variable_generator
        return variable_generator.generate_variable(
            self.features['interface_name'], self.model, 'rvar', name, [None, None], dim
        )
        
    def dvar(
        self,
        name: str,
        dim: Union[int, List[Union[int, range]]] = 0
    ) -> np.ndarray:
        """
        Creates and returns a dependent variable.

        Parameters
        ----------
        name : str
            Name of this variable.
        dim : Union[int, List[Union[int, range]]], optional
            Dimensions of this variable. Default: 0.

        Returns
        -------
        np.ndarray
            A dependent variable.

        """
        dim = self.fix_ifneeded(dim)

        if self.no_agents is not None:
            default_pop = self.no_agents
        else:
            default_pop = 100

        if self.features['solution_method'] == 'exact':
            return np.zeros([len(dims) for dims in dim])
        
        elif self.features['solution_method'] == 'heuristic':
            if self.features['agent_status'] == 'idle':
                if self.features['vectorized']:
                    if dim == 0:
                        return 0
                    else:
                        return np.random.rand(*tuple([default_pop] + [len(dims) for dims in dim]))
                else:
                    if dim == 0:
                        return 0
                    else:
                        return np.zeros([len(dims) for dims in dim])
            else:
                if self.features['vectorized']:
                    if dim == 0:
                        return np.zeros(self.features['pop_size'])
                    else:
                        return np.zeros([self.features['pop_size']] + [len(dims) for dims in dim])
                else:
                    if dim == 0:
                        return 0
                    else:
                        return np.zeros([len(dims) for dims in dim])
