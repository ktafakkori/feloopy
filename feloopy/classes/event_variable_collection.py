"""
EventVariableCollection Module

This module defines a class, `EventVariableCollectionClass`, that provides methods to create collections of event (interval) variables with specific names and indices.
These variables represent events with characteristics such as size, start, and end, and are useful in constraint programming.

Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
See the file LICENSE file for licensing details.
"""

from typing import List, Optional, Any

class EventVariableCollection:
    """Placeholder class for event variable collections."""

class EventVariableCollectionClass:
    """
    Class that provides methods to create collections of event (event) variables.
    """

    def cevar(
        self,
        name: str,
        indices: List[Any],
        event: Optional[Any] = [None, None, None],
        dim: Optional[Any] = 0,
        optional: Optional[Any] = False
    ) -> EventVariableCollection:
        """
        Creates a dictionary of event (event) variables with specific names and indices.

        Parameters
        ----------
        name : str
            Base name for the variables.
        indices : List[Any]
            Indices for the variables.
        event : Optional[Any]
            [size, start, end]. Defaults to [None, None, None].
        dim : Optional[Any]
            Dimensions for the variables. Defaults to 0.
        optional : Optional[Any]
            Optional flag. Defaults to False.

        Returns
        -------
        EventVariableCollection
            A dictionary where each key is an index from 'indices' and the corresponding value is an event variable with the name derived from 'name' and the index.
        """
        if type(event) != dict:
            event = {i: event for i in indices}
        if type(dim) != dict:
            dim = {i: dim for i in indices}
        if type(optional) != dict:
            optional = {i: optional for i in indices}

        return {i: self.evar(name+f"[{i}]".replace("(", "").replace(")", ""), event=event[i], dim=dim[i], optional=optional[i]) for i in indices}