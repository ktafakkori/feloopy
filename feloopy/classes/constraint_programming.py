
"""
ConstraintProgramming Module

This module defines a class, `ConstraintProgrammingClass`, that is used in constraint programming.

Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
See the file LICENSE file for licensing details.
"""

from .event_variable import EventVariable
from .special_constraint import Expression
from typing import Optional, Union
import numpy as np
import math as mt

class ConstraintFeature:
    pass

class ConstraintProgrammingClass:
    
    def cp_get_event_start(self, event_variable: EventVariable, absent_value: Optional[ConstraintFeature] = None) -> ConstraintFeature:
        """
        Returns the start time of an event_variable.

        Parameters
        ----------
        event_variable : EventVariable
            The event variable whose start time is to be returned.
        absent_value : Optional[ConstraintFeature], optional
            The value to be returned if the event_variable is absent in the solution. The default is None.

        Returns
        -------
        ConstraintFeature
            The start time of the event_variable or the absent_value if the event_variable is absent in the solution.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.start_of(event_variable, absent_value)

        elif self.features['interface_name'] == 'ortools_cp':
            return event_variable.StartExpr()

    def cp_get_event_end(self, event_variable: EventVariable, absent_value: Optional[ConstraintFeature] = None) -> ConstraintFeature:
        """
        Returns the end time of an event_variable.

        If the event_variable is absent in the solution, the absent_value is returned. 
        The default absent_value is 0.

        Parameters:
        event_variable: The event variable whose end time is to be returned.
        absent_value: The value to be returned if the event_variable is absent in the solution.

        Returns:
        The end time of the event_variable or the absent_value if the event_variable is absent in the solution.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.end_of(event_variable, absent_value)
        elif self.features['interface_name'] == 'ortools_cp':
            return event_variable.EndExpr()
    
    def cp_get_event_length(self, event_variable: EventVariable, absent_value: Optional[ConstraintFeature] = None) -> ConstraintFeature:
        """
        Returns the length of an event_variable.

        If the event_variable is absent in the solution, the absent_value is returned. 
        The default absent_value is 0.

        Parameters:
        event_variable: The event variable whose length is to be returned.
        absent_value: The value to be returned if the event_variable is absent in the solution.

        Returns:
        The length of the event_variable or the absent_value if the event_variable is absent in the solution.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.length_of(event_variable, absent_value)
        elif self.features['interface_name'] == 'ortools_cp':
            return event_variable.EndExpr() - event_variable.StartExpr()

    def cp_get_event_size(self, event_variable: EventVariable, absent_value: Optional[ConstraintFeature] = None) -> ConstraintFeature:
        """
        Returns the size of an event_variable.

        If the event_variable is absent in the solution, the absent_value is returned. 
        The default absent_value is 0.

        Parameters:
        event_variable: The event variable whose size is to be returned.
        absent_value: The value to be returned if the event_variable is absent in the solution.

        Returns:
        The size of the event_variable or the absent_value if the event_variable is absent in the solution.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.size_of(event_variable, absent_value)
        elif self.features['interface_name'] == 'ortools_cp':
            return event_variable.SizeExpr()

    def cp_get_presence(self, event_variable: EventVariable) -> int:
        """
        Returns the presence (1) or absence (0) of an event_variable. 

        This method can be used to check whether the event_variable is present in the solution.

        Parameters:
        event_variable: The event variable whose presence is to be checked.

        Returns:
        1 if the event_variable is present in the solution, 0 otherwise.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.presence_of(event_variable)
        elif self.features['interface_name'] == 'ortools_cp':
            return event_variable.IsPresent().Value()
        
    def cp_event_start_exactly_before_start(
        self, first_event, second_event, delay: Union[int, float] = 0
    ) -> Expression:
        """
        Returns a boolean expression that checks if the start time of the first event 'first_event'
        plus a specified delay equals the start time of the second event 'second_event'.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.start_at_start(first_event, second_event, delay)
        elif self.features['interface_name'] == 'ortools_cp':
            return first_event.StartExpr() + delay == second_event.StartExpr()

    def cp_event_start_exactly_before_end(
        self, first_event, second_event, delay: Union[int, float] = 0
    ) -> Expression:
        """
        Returns a boolean expression that checks if the start time of the first event 'first_event'
        plus a specified delay equals the end time of the second event 'second_event'.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.start_at_end(first_event, second_event, delay)
        elif self.features['interface_name'] == 'ortools_cp':
            return first_event.StartExpr() + delay == second_event.EndExpr()

    def cp_event_end_exactly_before_start(
        self, first_event, second_event, delay: Union[int, float] = 0
    ) -> Expression:
        """
        Returns a boolean expression that checks if the end time of the first event 'first_event'
        plus a specified delay equals the start time of the second event 'second_event'.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.end_at_start(first_event, second_event, delay)
        elif self.features['interface_name'] == 'ortools_cp':
            return first_event.EndExpr() + delay == second_event.StartExpr()

    def cp_event_end_exactly_before_end(
        self, first_event, second_event, delay: Union[int, float] = 0
    ) -> Expression:
        """
        Returns a boolean expression that checks if the end time of the first event 'first_event'
        plus a specified delay equals the end time of the second event 'second_event'.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.end_at_end(first_event, second_event, delay)
        elif self.features['interface_name'] == 'ortools_cp':
            return first_event.EndExpr() + delay == second_event.EndExpr()

    def cp_event_start_before_start(
        self, first_event, second_event, delay: Union[int, float] = 0
    ) -> Expression:
        """
        Returns a boolean expression that checks if the start time of the first event 'first_event'
        plus a specified delay is less than or equal to the start time of the second event 'second_event'.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.start_before_start(first_event, second_event, delay)
        elif self.features['interface_name'] == 'ortools_cp':
            return first_event.StartExpr() + delay <= second_event.StartExpr()

    def cp_event_start_before_end(
        self, first_event, second_event, delay: Union[int, float] = 0
    ) -> Expression:
        """
        Returns a boolean expression that checks if the start time of the first event 'first_event'
        plus a specified delay is less than or equal to the end time of the second event 'second_event'.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.start_before_end(first_event, second_event, delay)
        elif self.features['interface_name'] == 'ortools_cp':
            return first_event.StartExpr() + delay <= second_event.EndExpr()

    def cp_event_end_before_start(self, event_one, event_two, delay=0):
        """
        Returns a boolean expression that checks if the end time of event 'event_one' 
        plus a specified delay is less than or equal to the start time of event 'event_two'.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.end_before_start(event_one, event_two, delay)
        if self.features['interface_name'] == 'ortools_cp':
            return event_one.EndExpr() + delay <= event_two.StartExpr()

    def cp_event_end_before_end(self, event_one, event_two, delay=0):
        """
        Returns a boolean expression that checks if the end time of event 'event_one' 
        plus a specified delay is less than or equal to the end time of event 'event_two'.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.end_before_end(event_one, event_two, delay)
        elif self.features['interface_name'] == 'ortools_cp':
            return event_one.EndExpr() + delay <= event_two.EndExpr()
    
    def cp_forbid_event_start(self, event, function):
        """
        Forbids an event from starting during specified regions.

        Parameters:
        - event (EventVar): The event variable.
        - function (function): The function that specifies forbidden regions.

        Returns:
        - Expression: A boolean expression representing the forbidden start constraint.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.forbid_start(event, function)

        if self.features['interface_name'] == 'ortools_cp':
            forbidden_domains = function(event)
            for domain in forbidden_domains:
                self.model.Add(event.StartExpr() < domain[0])
                self.model.Add(event.StartExpr() > domain[1])

    def cp_forbid_event_end(self, event, function):
        """
        Forbids an event from ending during specified regions.

        Parameters:
        - event (EventVar): The event variable.
        - function (function): The function that specifies forbidden regions.

        Returns:
        - Expression: A boolean expression representing the forbidden end constraint.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.forbid_end(event, function)

        if self.features['interface_name'] == 'ortools_cp':
            forbidden_domains = function(event)
            for domain in forbidden_domains:
                self.model.Add(event.EndExpr() < domain[0])
                self.model.Add(event.EndExpr() > domain[1])
            
    def cp_forbid_event_overlap(self, event_variables, transition_matrix=None):
        """
        Forbids overlapping of event variables.

        Parameters:
        - event_variables (list of EventVar): The list of event variables.
        - transition_matrix (list of list of bool, optional): Transition matrix. Defaults to None.

        Returns:
        - Expression: A boolean expression representing the forbidden overlap constraint.
        """
        if self.features['interface_name'] == 'cplex_cp':
            if transition_matrix is None:
                return self.model.no_overlap(event_variables)
            else:
                return self.model.no_overlap(event_variables, transition_matrix)

        if self.features['interface_name'] == 'ortools_cp':
            return self.model.AddNoOverlap(event_variables)
        
    def cp_forbid_event_extent(self, event, function):
        """
        Forbids an event from overlapping with specified regions.

        Parameters:
        - event (EventVar): The event variable.
        - function (function): The function that specifies forbidden regions.

        Returns:
        - Expression: A boolean expression representing the forbidden extent constraint.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.forbid_extent(event, function)

        if self.features['interface_name'] == 'ortools_cp':
            forbidden_domains = function(event)
            for domain in forbidden_domains:
                self.model.Add(event.EndExpr() < domain[0])
                self.model.Add(event.StartExpr() > domain[1])
            
    def cp_event_overlap_length(self, event1, event2, absent_value=None):
        """
        Returns the length of the overlap of two events.

        Parameters:
        - event1 (EventVar): The first event variable.
        - event2 (EventVar): The second event variable.
        - absent_value: Value to use when there is no overlap. Defaults to None.

        Returns:
        - Expression: The length of the overlap.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.overlap_length(event1, event2, absent_value)

        if self.features['interface_name'] == 'ortools_cp':
            overlap_start = self.model.NewIntVar(0, self.model.Horizon(), "")
            overlap_end = self.model.NewIntVar(0, self.model.Horizon(), "")
            self.model.Add(overlap_start <= event1.EndExpr())
            self.model.Add(overlap_end >= event1.StartExpr())
            return overlap_end - overlap_start

    def cp_start_eval(self, event, function, absent_value=None):
        """
        Evaluate the given segmented function at the start of the provided event variable.

        :param event: The event variable.
        :param function: The segmented function to be evaluated.
        :param absent_value: The value to be used if the function is absent.
        :return: The evaluation result.
        """

        if self.features['interface_name'] == 'cplex_cp':
            return self.model.start_eval(event, function, absent_value)

        if self.features['interface_name'] == 'ortools_cp':
            return function(event.StartExpr().Value())

    def cp_end_eval(self, event, function, absent_value=None):
        """
        Evaluate the given segmented function at the end of the provided event variable.

        :param event: The event variable.
        :param function: The segmented function to be evaluated.
        :param absent_value: The value to be used if the function is absent.
        :return: The evaluation result.
        """

        if self.features['interface_name'] == 'cplex_cp':
            return self.model.end_eval(event, function, absent_value)

        if self.features['interface_name'] == 'ortools_cp':
            return function(event.EndExpr().Value())

    def cp_size_eval(self, event, function, absent_value=None):
        """
        Evaluate the given segmented function on the size of the provided event variable.

        :param event: The event variable.
        :param function: The segmented function to be evaluated.
        :param absent_value: The value to be used if the function is absent.
        :return: The evaluation result.
        """

        if self.features['interface_name'] == 'cplex_cp':
            return self.model.size_eval(event, function, absent_value)

        if self.features['interface_name'] == 'ortools_cp':
            return function(event.SizeExpr().Value())

    def cp_length_eval(self, event, function, absent_value=None):
        """
        Evaluate the given segmented function on the length of the provided event variable.

        :param event: The event variable.
        :param function: The segmented function to be evaluated.
        :param absent_value: The value to be used if the function is absent.
        :return: The evaluation result.
        """

        if self.features['interface_name'] == 'cplex_cp':
            return self.model.length_eval(event, function, absent_value)

        if self.features['interface_name'] == 'ortools_cp':
            return function(event.SizeExpr().Value())

    def cp_span(self, event, function, absent_value=None):
        """
        Force that one event variable must exactly cover a set of event variables.

        :param event: The main event variable.
        :param function: A function providing a set of event variables.
        :param absent_value: The value to be used if the function is absent.
        """

        if self.features['interface_name'] == 'cplex_cp':
            return self.model.span(event, function, absent_value)

        if self.features['interface_name'] == 'ortools_cp':
            intervals = function(event)
            for i in intervals:
                self.model.Add(event.StartExpr() <= i.StartExpr())
                self.model.Add(event.EndExpr() >= i.EndExpr())

    def cp_always_equal(self, state_function, input1, input2):
        """
        Create an equality constraint between two expressions.

        :param state_function: The state function.
        :param input1: The first expression.
        :param input2: The second expression.
        """

        if self.features['interface_name'] == 'cplex_cp':
            return self.model.always_equal(state_function, input1, input2)

        if self.features['interface_name'] == 'ortools_cp':
            return self.model.Add(input1 == input2)

    def cp_alternative(self, event, array, cardinality=None):
        """
        Create an alternative constraint between event variables.

        :param event: The main event variable.
        :param array: An array of event variables.
        :param cardinality: The cardinality of the alternative constraint.
        """

        if self.features['interface_name'] == 'cplex_cp':
            return self.model.alternative(event, array, cardinality)

        if self.features['interface_name'] == 'ortools_cp':
            self.model.Add(sum([self.model.NewBoolVar('') for _ in array]) == 1)

    def cp_all_dist_above(self, exprs, value):
        """
        Ensure that all expressions are greater than or equal to the specified value.

        :param exprs: List of expressions to be constrained.
        :param value: The threshold value.
        """

        if self.features['interface_name'] == 'cplex_cp':
            return self.model.all_min_distance(exprs, value)

        if self.features['interface_name'] == 'ortools_cp':
            for expr in exprs:
                self.model.Add(expr >= value)

    def cp_if_then(self, input1, input2):
        """
        Return input2 if input1 is true.

        :param input1: Boolean expression.
        :param input2: Value to be returned if input1 is true.
        :return: input2 if input1 is true, else None.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.if_then(input1, input2)

        if self.features['interface_name'] == 'ortools_cp':
            if input1:
                return input2

    def cp_synchronize(self, event, array):
        """
        Synchronize an event variable with a set of event variables.

        :param event: Event variable to be synchronized.
        :param array: Set of event variables to synchronize with.
        """
        return self.model.synchronize(event, array)

    def cp_control_resource(self, *args, function='pulse'):
        
        """
        Create and return a dynamic resource usage control function.

        :param args: Additional arguments required for the specified control function.
        :param function: Type of control function to create ('pulse', 'step', 'start', 'end').
        :return: The created control function.
        """
        
        if function == 'pulse':
            return self.model.pulse(*args)
        if function == 'step':
            return self.model.step(*args)
        if function == 'start':
            return self.model.step_at_start(*args)
        if function == 'end':
            return self.model.step_at_end(*args)

    def cp_circuit(self, nodes):
        """
        Create a circuit constraint.

        The circuit constraint ensures that there is a Hamiltonian circuit on the nodes.

        :param nodes: List of nodes forming the circuit.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.circuit(nodes)

        if self.features['interface_name'] == 'ortools_cp':
            return self.model.AddCircuit(nodes)

    def cp_allowed_assignments(self, variables, tuples):
        """
        Create an allowed assignments constraint.

        The allowed assignments constraint ensures that the values assigned to the variables are in the list of tuples.

        :param variables: List of variables to be constrained.
        :param tuples: List of allowed value assignments.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.allowed_assignments(variables, tuples)

        if self.features['interface_name'] == 'ortools_cp':
            return self.model.AddAllowedAssignments(variables, tuples)

    def cp_inverse(self, variables, inverse_variables):
        """
        Create an inverse constraint.

        The inverse constraint ensures that if variables[i] = j then inverse_variables[j] = i and vice versa.

        :param variables: List of variables to be constrained.
        :param inverse_variables: List of variables forming the inverse relationship.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.inverse(variables, inverse_variables)

        if self.features['interface_name'] == 'ortools_cp':
            return self.model.AddInverse(variables, inverse_variables)

    def cp_logical_and(self, expr1, expr2):
        """
        Create a logical AND constraint.

        :param expr1: First boolean expression.
        :param expr2: Second boolean expression.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.logical_and(expr1, expr2)

        if self.features['interface_name'] == 'ortools_cp':
            return self.model.AddBoolAnd([expr1, expr2])

    def cp_logical_or(self, expr1, expr2):
        """
        Create a logical OR constraint.

        :param expr1: First boolean expression.
        :param expr2: Second boolean expression.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.logical_or(expr1, expr2)
            
        if self.features['interface_name'] == 'ortools_cp':
            return self.model.AddBoolOr([expr1, expr2])

    def cp_logical_not(self, expr):
        """
        Create a logical NOT constraint.

        :param expr: Boolean expression to be negated.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.logical_not(expr)
            
        if self.features['interface_name'] == 'ortools_cp':
            return self.model.Not(expr)

    def cp_less_than(self, expr1, expr2):
        """
        Create a less than constraint.

        :param expr1: First expression.
        :param expr2: Second expression.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.less_than(expr1, expr2)
            
        if self.features['interface_name'] == 'ortools_cp':
            return self.model.Add(expr1 < expr2)

    def cp_greater_than(self, expr1, expr2):
        """
        Create a greater than constraint.

        :param expr1: First expression.
        :param expr2: Second expression.
        """
        if self.features['interface_name'] == 'cplex_cp':
            return self.model.greater_than(expr1, expr2)
            
        if self.features['interface_name'] == 'ortools_cp':
            return self.model.Add(expr1 > expr2)
        
    def cp_add_exactly_one(self, variable_list):

        if self.features['interface_name'] == 'ortools_cp':
            return self.model.AddExactlyOne(variable_list)

    def cp_add_at_least_one(self, variable_list):

        if self.features['interface_name'] == 'ortools_cp':
            return self.model.AddAtLeastOne(variable_list)

    def cp_add_all_different(self, expressions):

        if self.features['interface_name'] == 'cplex_cp':
            return self.model.all_diff(expressions)
        if self.features['interface_name'] == 'ortools_cp':
            return self.model.AddAllDifferent(expressions)