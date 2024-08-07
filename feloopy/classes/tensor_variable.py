"""
TensorVariable Module

This module defines a class, `TensorVariableClass`, that facilitates the creation of various types
of tensor variables, such as free float-valued, positive float-valued, positive integer-valued, 
binary-valued, and random float-valued tensor variables. These tensor variables are used for 
matrix/tensor-wise operations in the specified mathematical models.

Supported tensor variables:

    - ftvar
    - ptvar
    - itvar
    - btvar
    - rtvar

Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
See the file LICENSE file for licensing details.
"""

from typing import List, Union, Optional
from ..operators.fix_operators import fix_dims
from ..operators.update_operators import update_variable_features

class TensorVariable:
    """Placeholder class for tensor variables."""

class TensorVariableClass:
    """Class that provides methods to create tensor variables."""

    def ftvar(
        self,
        name: str,
        shape: Optional[Union[int, List[Union[int, range]]]] = 0,
        bound: Optional[List[float]] = [None, None]
    ) -> TensorVariable:
        """
        Create a free float-valued tensor variable.

        Parameters
        ----------
        name : str
            The name of the tensor variable.
        shape : Optional[Union[int, List[Union[int, range]]]], optional
            The shape of the tensor variable, represented as a list containing integers or ranges. Default is 0.
        bound : Optional[List[float]], optional
            The lower and upper bounds of the tensor variable. Default is [None, None].

        Returns
        -------
        TensorVariable
            A tensor variable that accepts matrix/tensor-wise operations.
        """
        dim = fix_dims(shape)
        self.features = update_variable_features(name, dim, bound or [None, None], 'free_variable_counter', self.features)
        
        if self.features['solution_method'] == 'exact':
            from ..generators import variable_generator
            self.features['variables'][("ftvar", name)] = variable_generator.generate_variable(
                self.features['interface_name'], self.model, 'ftvar', name, bound, dim
            )
            self.features['dimensions'][name] = dim
            return self.features['variables'][("ftvar", name)]

        raise ValueError(f"Error: TensorVariable '{name}' cannot be created.")
    
    def ptvar(
        self,
        name: str,
        shape: Optional[Union[int, List[Union[int, range]]]] = 0,
        bound: Optional[List[float]] = [0, None]
    ) -> TensorVariable:
        """
        Create a positive float-valued tensor variable.

        Parameters
        ----------
        name : str
            The name of the tensor variable.
        shape : Optional[Union[int, List[Union[int, range]]]], optional
            The shape of the tensor variable, represented as a list containing integers or ranges. Default is 0.
        bound : Optional[List[float]], optional
            The lower and upper bounds of the tensor variable. Default is [0, None].

        Returns
        -------
        TensorVariable
            A tensor variable that accepts matrix/tensor-wise operations.
        """
        dim = fix_dims(shape)
        self.features = update_variable_features(name, dim, bound or [0, None], 'positive_variable_counter', self.features)

        if self.features['solution_method'] == 'exact':
            from ..generators import variable_generator

            self.features['variables'][("ptvar", name)] = variable_generator.generate_variable(
                self.features['interface_name'], self.model, 'ptvar', name, bound, dim
            )
            self.features['dimensions'][name] = dim

            if self.features['interface_name'] in ['rsome_ro', 'rsome_dro', 'cvxpy']:
                self.con(self.features['variables'][("ptvar", name)] >= 0)

                if bound and bound[1] is not None:
                    self.con(self.features['variables'][("ptvar", name)] <= bound[1])

            return self.features['variables'][("ptvar", name)]
    
        raise ValueError(f"Error: TensorVariable '{name}' cannot be created.")
    
    def itvar(
        self,
        name: str,
        shape: Optional[Union[int, List[Union[int, range]]]] = 0,
        bound: Optional[List[float]] = [0, None]
    ) -> TensorVariable:
        """
        Create a positive integer-valued tensor variable.

        Parameters
        ----------
        name : str
            The name of the tensor variable.
        shape : Optional[Union[int, List[Union[int, range]]]], optional
            The shape of the tensor variable, represented as a list containing integers or ranges. Default is 0.
        bound : Optional[List[float]], optional
            The lower and upper bounds of the tensor variable. Default is [0, None].

        Returns
        -------
        TensorVariable
            A tensor variable that accepts matrix/tensor-wise operations.
        """

        dim = fix_dims(shape)
        self.features = update_variable_features(name, dim, bound or [0, None], 'integer_variable_counter', self.features)

        if self.features['solution_method'] == 'exact':
            from ..generators import variable_generator

            self.features['variables'][("itvar", name)] = variable_generator.generate_variable(
                self.features['interface_name'], self.model, 'itvar', name, bound, dim
            )
            self.features['dimensions'][name] = dim
            return self.features['variables'][("itvar", name)]

        raise ValueError(f"Error: TensorVariable '{name}' cannot be created.")
    
    def btvar(
        self,
        name: str,
        shape: Optional[Union[int, List[Union[int, range]]]] = 0,
        bound: Optional[List[float]] = [0, 1]
    ) -> TensorVariable:
        """
        Create a binary-valued tensor variable.

        Parameters
        ----------
        name : str
            The name of the tensor variable.
        shape : Optional[Union[int, List[Union[int, range]]]], optional
            The shape of the tensor variable, represented as a list containing integers or ranges. Default is 0.
        bound : Optional[List[float]], optional
            The lower and upper bounds of the tensor variable. Default is [0, 1].

        Returns
        -------
        TensorVariable
            A tensor variable that accepts matrix/tensor-wise operations.
        """

        dim = fix_dims(shape)
        self.features = update_variable_features(name, dim, bound or [0, 1], 'binary_variable_counter', self.features)

        if self.features['solution_method'] == 'exact':
            from ..generators import variable_generator

            self.features['variables'][("btvar", name)] = variable_generator.generate_variable(
                self.features['interface_name'], self.model, 'btvar', name, bound, dim
            )
            self.features['dimensions'][name] = dim
            return self.features['variables'][("btvar", name)]

        raise ValueError(f"Error: TensorVariable '{name}' cannot be created.")

    def rtvar(
        self,
        name: str,
        shape: Optional[Union[int, List[Union[int, range]]]] = 0
    ) -> TensorVariable:
        """
        Create a random float-valued tensor variable.

        Parameters
        ----------
        name : str
            The name of the tensor variable.
        shape : Optional[Union[int, List[Union[int, range]]]], optional
            The shape of the tensor variable, represented as a list containing integers or ranges. Default is 0.

        Returns
        -------
        TensorVariable
            A tensor variable that accepts matrix/tensor-wise operations.
        """

        dim = fix_dims(shape)
   
        if self.features['solution_method'] == 'exact':
   
            from ..generators import variable_generator
            return variable_generator.generate_variable(
                self.features['interface_name'], self.model, 'rtvar', name, [None, None], dim
            )

        raise ValueError(f"Error: TensorVariable '{name}' cannot be created.")
