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

        if type(event) != dict:
            event = {i: event for i in indices}
        if type(dim) != dict:
            dim = {i: dim for i in indices}
        if type(optional) != dict:
            optional = {i: optional for i in indices}

        return {i: self.evar(name+f"[{i}]".replace("(", "").replace(")", ""), event=event[i], dim=dim[i], optional=optional[i]) for i in indices}