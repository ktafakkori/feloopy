"""
TensorVariableCollection Module

This module defines a class, `TensorVariableCollectionClass`, that facilitates the creation of collections
of various types of tensor variables, such as free float-valued, positive float-valued, positive integer-valued, 
binary-valued, and random float-valued tensor variables. These tensor variables are used for 
matrix/tensor-wise operations in the specified mathematical models.

Supported tensor variable collections:

    - cftvar
    - cptvar
    - citvar
    - cbtvar
    - crtvar

Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
See the file LICENSE file for licensing details.
"""

from typing import List, Union, Optional, Dict
from ..operators.fix_operators import fix_dims
from ..operators.update_operators import update_variable_features

class TensorVariableCollection:
    """Placeholder class for tensor variable collections."""

class TensorVariableCollectionClass:
    """Class that provides methods to create collections of tensor variables."""
    
    def cftvar(
        self,
        name: str,
        indices: List,
        shape: Union[int, Dict] = 0,
        bound: Union[List[Optional[float]], Dict] = [None, None]
    ) -> TensorVariableCollection:
        """
        Creates a dictionary of free (float) tensor variables with given names and indices.

        Parameters
        ----------
        name : str
            The base name for the variables.
        indices : List
            The indices for the variables.
        shape : Union[int, Dict], optional
            The shapes for the variables. Defaults to 0 for all indices if not provided as a dictionary.
        bound : Union[List[Optional[float]], Dict], optional
            The bounds for the variables. Defaults to [None, None] for all indices if not provided as a dictionary.

        Returns
        -------
        TensorVariableCollection
            A dictionary where each key is an index from 'indices', and the corresponding value is a float tensor variable
            with the name derived from 'name' and the index.
        """
        if not isinstance(bound, dict):
            bound = {i: bound for i in indices}

        if not isinstance(shape, dict):
            shape = {i: shape for i in indices}

        return {
            i: self.ftvar(
                name + f"[{i}]".replace("(", "").replace(")", ""),
                shape=shape[i],
                bound=bound[i]
            ) for i in indices
        }
        
    def cptvar(
        self,
        name: str,
        indices: List,
        shape: Union[int, Dict] = 0,
        bound: Union[List, Dict] = [0, None]
    ) -> TensorVariableCollection:
        """
        This method creates a dictionary of positive tensor variables with given names and indices.

        Parameters
        ----------
        name : str
            The base name for the variables.
        indices : list
            The indices for the variables.
        shape : Union[int, dict], optional
            The shapes for the variables. Defaults to 0 for all indices if not provided as a dictionary.
        bound : Union[list[0, None], dict], optional
            The bounds for the variables. Defaults to [0, None] for all indices if not provided as a dictionary.

        Returns
        -------
        TensorVariableCollection
            A dictionary where each key is an index from 'indices' and the corresponding value is a positive tensor variable with the name derived from 'name' and the index.
        """
        if not isinstance(bound, dict):
            bound = {i: bound for i in indices}

        if not isinstance(shape, dict):
            shape = {i: shape for i in indices}

        return {
            i: self.ptvar(
                name + f"[{i}]".replace("(", "").replace(")", ""),
                shape=shape[i],
                bound=bound[i]
            ) for i in indices
        }
    
    def citvar(
        self,
        name: str,
        indices: List,
        shape: Union[int, Dict] = 0,
        bound: Union[List, Dict] = [0, None]
    ) -> TensorVariableCollection:
        """
        This method creates a dictionary of integer tensor variables with given names and indices.

        Parameters
        ----------
        name : str
            The base name for the variables.
        indices : list
            The indices for the variables.
        shape : Union[int, dict], optional
            The shapes for the variables. Defaults to 0 for all indices if not provided as a dictionary.
        bound : Union[list[0, None], dict], optional
            The bounds for the variables. Defaults to [0, None] for all indices if not provided as a dictionary.

        Returns
        -------
        TensorVariableCollection
            A dictionary where each key is an index from 'indices' and the corresponding value is an integer tensor variable with the name derived from 'name' and the index.
        """
        if not isinstance(bound, dict):
            bound = {i: bound for i in indices}

        if not isinstance(shape, dict):
            shape = {i: shape for i in indices}

        return {
            i: self.itvar(
                name + f"[{i}]".replace("(", "").replace(")", ""),
                shape=shape[i],
                bound=bound[i]
            ) for i in indices
        }
    
    def cbtvar(
        self,
        name: str,
        indices: List,
        shape: Union[int, Dict] = 0,
        bound: Union[List, Dict] = [0, 1]
    ) -> TensorVariableCollection:
        """
        This method creates a dictionary of binary tensor variables with given names and indices.

        Parameters
        ----------
        name : str
            The base name for the variables.
        indices : list
            The indices for the variables.
        shape : Union[int, dict], optional
            The shapes for the variables. Defaults to 0 for all indices if not provided as a dictionary.
        bound : Union[list[0, 1], dict], optional
            The bounds for the variables. Defaults to [0, 1] for all indices if not provided as a dictionary.

        Returns
        -------
        TensorVariableCollection
            A dictionary where each key is an index from 'indices' and the corresponding value is a binary tensor variable with the name derived from 'name' and the index.
        """
        if not isinstance(bound, dict):
            bound = {i: bound for i in indices}

        if not isinstance(shape, dict):
            shape = {i: shape for i in indices}

        return {
            i: self.btvar(
                name + f"[{i}]".replace("(", "").replace(")", ""),
                shape=shape[i],
                bound=bound[i]
            ) for i in indices
        }
    
    def crtvar(
        self,
        name: str,
        indices: List,
        shape: Union[int, Dict] = 0
    ) -> TensorVariableCollection:
        """
        Creates a dictionary of tensor-like random variables with specific names and shapes.

        Parameters
        ----------
        name : str
            Base name for the variables.
        indices : list
            Indices for the variables.
        shape : Union[int, dict], optional
            Shapes for the variables. Defaults to None.

        Returns
        -------
        TensorVariableCollection
            A dictionary where each key is an index from 'indices' and the corresponding value is a tensor-like random variable with the name derived from 'name' and the index, and shape specified by 'shape'.
        """
        if not isinstance(shape, dict):
            shape = {i: shape for i in indices}

        return {
            i: self.rtvar(
                name + f"[{i}]".replace("(", "").replace(")", ""),
                shape=shape[i]
            ) for i in indices
        }
