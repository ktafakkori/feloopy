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

        if not isinstance(shape, dict):
            shape = {i: shape for i in indices}

        return {
            i: self.rtvar(
                name + f"[{i}]".replace("(", "").replace(")", ""),
                shape=shape[i]
            ) for i in indices
        }
