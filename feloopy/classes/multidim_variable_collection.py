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
    """Class that provides methods to create collections of multi-dimensional variables."""
    
    def cfvar(
        self,
        name: str,
        indices: List,
        dim: Optional[Union[int, List[Union[int, range]]]] = 0,
        bound: Optional[List[Optional[float]]] = [None, None]
    ) -> MultidimVariableCollection:
        """
        Creates a dictionary of free (continuous) variables with specific names and indices.

        Parameters
        ----------
        name : str
            Base name for the variables.
        indices : List
            Indices for the variables.
        dim : Optional[Union[int, List[Union[int, range]]]], optional
            Dimensions for the variables. Defaults to 0 for all indices if not provided as a dictionary.
        bound : Optional[List[Optional[float]]], optional
            Bounds for the variables. Defaults to [None, None] for all indices if not provided as a dictionary.

        Returns
        -------
        MultidimVariableCollection
            A dictionary where each key is an index from 'indices' and the corresponding value is a free (continuous) variable
            with the name derived from 'name' and the index.

        """

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
        """
        Creates a dictionary of positive continuous variables with specific names and indices.

        Parameters
        ----------
        name : str
            Base name for the variables.
        indices : List
            Indices for the variables.
        dim : Optional[Union[int, List[Union[int, range]]]], optional
            Dimensions for the variables. Defaults to 0 for all indices if not provided as a dictionary.
        bound : Optional[List[Optional[float]]], optional
            Bounds for the variables. Defaults to [0, None] for all indices if not provided as a dictionary.

        Returns
        -------
        MultidimVariableCollection
            A dictionary where each key is an index from 'indices' and the corresponding value is a positive continuous variable
            with the name derived from 'name' and the index.

        """

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
        """
        Creates a dictionary of integer variables with specific names and indices.

        Parameters
        ----------
        name : str
            Base name for the variables.
        indices : List[Any]
            Indices for the variables.
        dim : Optional[Union[int, List[Union[int, range]]]], optional
            Dimensions for the variables. Defaults to 0 for all indices if not provided as a dictionary.
        bound : Optional[List[Optional[int]]], optional
            Bounds for the variables. Defaults to [0, None] for all indices if not provided as a dictionary.

        Returns
        -------
        MultidimVariableCollection
            A dictionary where each key is an index from 'indices' and the corresponding value is an integer variable
            with the name derived from 'name' and the index.

        """

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
        """
        Creates a dictionary of binary variables with specific names and indices.

        Parameters
        ----------
        name : str
            Base name for the variables.
        indices : List[Any]
            Indices for the variables.
        dim : Optional[Union[int, List[Union[int, range]]]], optional
            Dimensions for the variables. Defaults to 0 for all indices if not provided as a dictionary.
        bound : Optional[List[Optional[int]]], optional
            Bounds for the variables. Defaults to [0, 1] for all indices if not provided as a dictionary.

        Returns
        -------
        MultidimVariableCollection
            A dictionary where each key is an index from 'indices' and the corresponding value is a binary variable
            with the name derived from 'name' and the index.

        """

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
        """
        Creates a dictionary of sequential variables with specific names and lengths.

        Parameters
        ----------
        name : str
            Base name for the variables.
        indices : List[Any]
            Indices for the variables.
        length : Optional[Union[int, List[Union[int, range]]]], optional
            Lengths for the variables. Defaults to 1 for all indices if not provided as a dictionary.

        Returns
        -------
        MultidimVariableCollection
            A dictionary where each key is an index from 'indices' and the corresponding value is a sequential variable
            with the name derived from 'name' and the index, and length specified by 'length'.

        """

        if not isinstance(length, dict):
            length = {i: length for i in indices}
        return {i: self.svar(name + f"[{i}]".replace("(", "").replace(")", ""), length=length[i]) for i in indices}

    def crvar(
        self,
        name: str,
        indices: List[Any],
        dim: Optional[Union[int, List[Union[int, range]]]] = 0
    ) -> MultidimVariableCollection:
        """
        Creates a dictionary of random variables with specific names and dimensions.

        Parameters
        ----------
        name : str
            Base name for the variables.
        indices : List[Any]
            Indices for the variables.
        dim : Optional[Union[int, List[Union[int, range]]]], optional
            Dimensions for the variables. Defaults to 0 for all indices if not provided as a dictionary.

        Returns
        -------
        MultidimVariableCollection
            A dictionary where each key is an index from 'indices' and the corresponding value is a random variable
            with the name derived from 'name' and the index.

        """

        if not isinstance(dim, dict):
            dim = {i: dim for i in indices}
        return {i: self.rvar(name + f"[{i}]".replace("(", "").replace(")", ""), dim=dim[i]) for i in indices}
