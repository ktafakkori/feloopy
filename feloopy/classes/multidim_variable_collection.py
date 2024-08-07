"""
MultidimVariableCollection Module

This module defines a class, `MultidimVariableCollectionClass`, that facilitates the creation of various types
of multi-dimensional variables, such as free, positive, integer, binary, sequential, and random variables.
These variables are used for mathematical modeling and optimization purposes.

Supported multi-dimensional variables:

    - cfvar
    - cpvar
    - civar
    - cbvar
    - csvar
    - crvar

Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
See the file LICENSE file for licensing details.
"""

from typing import List, Optional, Union, Any

class MultidimVariableCollection:
    """Placeholder class for multi-dimensional variable collections."""


class MultidimVariableCollectionClass:

    def cfvar(
        self,
        name: str,
        indices: List,
        dim: Optional[Union[int, List[Union[int, range]]]] = 0,
        bound: Optional[List[Optional[float]]] = [None, None]
    ) -> MultidimVariableCollection:

        if not isinstance(bound, dict):
            bound = {i: bound for i in indices}
        if not isinstance(dim, dict):
            dim = {i: dim for i in indices}
        return {i: self.fvar(name + f"[{i}]".replace("(", "").replace(")", ""), dim=dim[i], bound=bound[i]) for i in indices}

    def cpvar(
        self,
        name: str,
        indices: List,
        dim: Optional[Union[int, List[Union[int, range]]]] = 0,
        bound: Optional[List[Optional[float]]] = [0, None]
    ) -> MultidimVariableCollection:

        if not isinstance(bound, dict):
            bound = {i: bound for i in indices}
        if not isinstance(dim, dict):
            dim = {i: dim for i in indices}
        return {i: self.pvar(name + f"[{i}]".replace("(", "").replace(")", ""), dim=dim[i], bound=bound[i]) for i in indices}

    def civar(
        self,
        name: str,
        indices: List[Any],
        dim: Optional[Union[int, List[Union[int, range]]]] = 0,
        bound: Optional[List[Optional[int]]] = [0, None]
    ) -> MultidimVariableCollection:

        if not isinstance(bound, dict):
            bound = {i: bound for i in indices}
        if not isinstance(dim, dict):
            dim = {i: dim for i in indices}
        return {i: self.ivar(name + f"[{i}]".replace("(", "").replace(")", ""), dim=dim[i], bound=bound[i]) for i in indices}

    def cbvar(
        self,
        name: str,
        indices: List[Any],
        dim: Optional[Union[int, List[Union[int, range]]]] = 0,
        bound: Optional[List[Optional[int]]] = [0, 1]
    ) -> MultidimVariableCollection:

        if not isinstance(bound, dict):
            bound = {i: bound for i in indices}
        if not isinstance(dim, dict):
            dim = {i: dim for i in indices}
        return {i: self.bvar(name + f"[{i}]".replace("(", "").replace(")", ""), dim=dim[i], bound=bound[i]) for i in indices}

    def csvar(
        self,
        name: str,
        indices: List[Any],
        length: Optional[Union[int, List[Union[int, range]]]] = 1
    ) -> MultidimVariableCollection:

        if not isinstance(length, dict):
            length = {i: length for i in indices}
        return {i: self.svar(name + f"[{i}]".replace("(", "").replace(")", ""), length=length[i]) for i in indices}

    def crvar(
        self,
        name: str,
        indices: List[Any],
        dim: Optional[Union[int, List[Union[int, range]]]] = 0
    ) -> MultidimVariableCollection:


        if not isinstance(dim, dict):
            dim = {i: dim for i in indices}
        return {i: self.rvar(name + f"[{i}]".replace("(", "").replace(")", ""), dim=dim[i]) for i in indices}
