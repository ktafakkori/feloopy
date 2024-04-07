"""
EventVariable Module

This module defines a class, `EventVariableClass`, that provides methods to create event (interval) variables.
These variables represent events with characteristics such as size, start, and end, and are useful in constraint programming.

Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
See the file LICENSE file for licensing details.
"""

from typing import List, Optional
from itertools import product as sets 
from ..operators.update_operators import update_variable_features

class EventVariable:
    """Placeholder class for event variables."""

class EventVariableClass:
    """
    Class that provides methods to create event variables.
    """

    def evar(
        self,
        name: str,
        event: List[Optional[float]] = [None, None, None],
        dim: List[int] = 0,
        optional: bool = False
    ) -> EventVariable:
        """
        Creates and returns an event (interval) variable.

        Parameters
        ----------
        name : str
            Name of this variable.
        event : List[Optional[float]], optional
            [size, start, end]. Default: [None, None, None].
        dim : List[int], optional
            Dimensions of this variable. Default: 0.
        optional : bool, optional
            Flag indicating whether the variable is optional. Default: False.

        Returns
        -------
        EventVariable
            An event (interval) variable.
        """

        self.features = update_variable_features(name, dim, None, 'event_variable_counter', self.features)

        if len(event) == 1:
            event = [event[0], None, None]

        if dim == 0:

            if self.features['interface_name'] == 'cplex_cp':
                self.features['variables'][("evar", name)] = self.model.interval_var(start=event[1], size=event[0], end=event[2], name=name, optional=optional)
                self.features['dimensions'][name] = dim
                return self.features['variables'][("evar", name)]
                
            elif self.features['interface_name'] == 'ortools_cp':
                self.features['variables'][("evar", name)] = self.model.NewOptionalIntervalVar(start=event[1], size=event[0], end=event[2], name=name, is_present=optional)
                self.features['dimensions'][name] = dim
                return self.features['variables'][("evar", name)]
        else:

            if self.features['interface_name'] == 'cplex_cp':

                if len(dim) == 1:
                    self.features['variables'][("evar", name)] = {key: self.model.interval_var(start=event[1], size=event[0], end=event[2], name=f"{name}{key}", optional=optional) for key in dim[0]}
                    self.features['dimensions'][name] = dim
                    return self.features['variables'][("evar", name)] 
                    
                else:
                    self.features['variables'][("evar", name)]  = {key: self.model.interval_var(start=event[1], size=event[0], end=event[2], name=f"{name}{key}", optional=optional) for key in sets(*dim)}
                    self.features['dimensions'][name] = dim
                    return  self.features['variables'][("evar", name)] 

            elif self.features['interface_name'] == 'ortools_cp':

                if len(dim) == 1:
                    self.features['variables'][("evar", name)] = {key: self.model.NewOptionalIntervalVar(start=event[1], size=event[0], end=event[2], name=f"{name}{key}", is_present=optional) for key in dim[0]}
                    self.features['dimensions'][name] = dim
                    return self.features['variables'][("evar", name)]
                    
                else:
                    self.features['variables'][("evar", name)]  = {key: self.model.NewOptionalIntervalVar(start=event[1], size=event[0], end=event[2], name=f"{name}{key}", is_present=optional) for key in sets(*dim)}
                    self.features['dimensions'][name] = dim
                    return self.features['variables'][("evar", name)]
