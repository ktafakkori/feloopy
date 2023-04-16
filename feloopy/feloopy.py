from .classes.empty import *

from .functions.set_operators import *
from .functions.math_operators import *
from .functions.count_operators import *
from .functions.update_operators import *
from .functions.random_operators import *
from .functions.heuristic_operators import *
from .functions.fix_operators import *

import warnings
import itertools as it
import math as mt
import numpy as np
from tabulate import tabulate as tb
import sys

warnings.filterwarnings("ignore")

class Model:

    def __init__(self, solution_method, model_name, interface_name, agent=None, key=None):

        """
        Environment Definition
        ~~~~~~~~~~~~~~~~~~~~~~
        This class is used to define the modeling environment.

        Args:
            solution_method (str): The desired solution (optimization) method.
            model_name (str): The name of this model.
            interface_name (str): The interface name.
            agent (X, optional): If you are using a heuristic optimization method, provide the input of the function here. Defaults to None.
            key (number, optional): The desired key for random number generator. Defaults to None.

        Examples:
            m = Model('exact', 'tsp', 'ortools', None, None)
            m = Model('exact', 'tsp', 'ortools', key=0)
            def instance(X): m = Model('heuristic', 'tsp', 'feloopy', X)
            def instance(X): m = Model('heuristic', 'tsp', 'feloopy', X, 0)
        """

        if solution_method == 'constraint': solution_method = 'exact'

        self.binary_variable = self.add_binary_variable = self.boolean_variable = self.add_boolean_variable = self.bvar
        self.positive_variable = self.add_positive_variable = self.pvar
        self.integer_variable = self.add_integer_variable = self.ivar
        self.free_variable = self.add_free_variable = self.fvar
        self.sequential_variable = self.add_sequential_variable = self.svar
        self.positive_tensor_variable = self.add_positive_tensor_variable = self.ptvar
        self.binary_tensor_variable = self.add_binary_tensor_variable = self.add_boolean_tensor_variable = self.boolean_tensor_variable = self.btvar
        self.integer_tensor_variable = self.add_integer_tensor_variable = self.itvar
        self.free_tensor_variable = self.add_free_tensor_variable = self.ftvar
        self.dependent_variable = self.add_dependent_variable = self.dvar
        self.objective = self.reward = self.hypothesis = self.fitness = self.goal = self.add_objective = self.obj
        self.constraint = self.equation = self.add_constraint = self.add_equation = self.con
        self.solve = self.implement = self.run = self.optimize = self.sol
        self.get_obj = self.get_objective
        self.get_stat = self.get_status
        self.get_var = self.value = self.get = self.get_variable
        self.dis = self.dis_var = self.display = self.show = self.print = self.display_variable = self.dis_variable
        self.status = self.show_status = self.dis_status
        self.objective_value = self.show_objective = self.display_objective = self.dis_obj
        self.random = create_random_number_generator(key)

        match solution_method:

            case 'exact':

                self.features = {
                    'solution_method': 'exact',
                    'model_name': model_name,
                    'interface_name': interface_name,
                    'solver_name': None,
                    'constraints': [],
                    'constraint_labels': [],
                    'objectives': [],
                    'objective_labels': [],
                    'directions': [],
                    'positive_variable_counter': [0, 0],
                    'integer_variable_counter': [0, 0],
                    'binary_variable_counter': [0, 0],
                    'free_variable_counter': [0, 0],
                    'total_variable_counter': [0, 0],
                    'objective_counter': [0, 0],
                    'constraint_counter': [0, 0],
                    'objective_being_optimized': 0,
                }

                from .generators import model_generator
                self.model = model_generator.generate_model(self.features)

            case 'heuristic':

                self.agent = agent

                if self.agent[0] == 'idle':

                    self.features = {
                        'agent_status': 'idle',
                        'solution_method': 'heuristic',
                        'model_name': model_name,
                        'interface_name': interface_name,
                        'solver_name': None,
                        'constraints': [],
                        'constraint_labels': [],
                        'objectives': [],
                        'objective_labels': [],
                        'directions': [],
                        'positive_variable_counter': [0, 0],
                        'integer_variable_counter': [0, 0],
                        'binary_variable_counter': [0, 0],
                        'free_variable_counter': [0, 0],
                        'total_variable_counter': [0, 0],
                        'objective_counter': [0, 0],
                        'constraint_counter': [0, 0],
                        'variable_spread': dict(),
                        'variable_type': dict(),
                        'variable_bound': dict(),
                        'variable_dim': dict(),
                        'pop_size': 1,
                        'penalty_coefficient': 0,
                        'vectorized': None,
                        'objective_being_optimized': 0,
                    }

                else:

                    self.features = {
                        'agent_status': 'active',
                        'solution_method': 'heuristic',
                        'constraints': [],
                        'objectives': [],
                        'objective_counter': [0, 0],
                        'interface_name': interface_name,
                        'variable_spread': self.agent[2],
                        'pop_size': len(self.agent[1]),
                        'penalty_coefficient': self.agent[3],
                        'vectorized': None,
                        'objective_being_optimized': 0,
                        'directions': []
                    }

                    self.agent = self.agent[1].copy()

                match self.features['interface_name']:

                    case 'mealpy': self.features['vectorized'] = False
                    case 'feloopy': self.features['vectorized'] = True

    def __getitem__(self, agent):

        """
        Returns the required model data.

        Args:
            agent (X): If you are using a heuristic optimization method, provide the input of the function here.

        Examples:
            * def instance(X): return m[X]
        """

        if self.features['agent_status'] == 'idle':
            return self
        else:
            if self.features['vectorized']:
                return self.agent
            else:
                return self.response

    def btvar(self, name, variable_dim=0, variable_bound=[0, 1]):

        """
        Binary Tensor Variable Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        To define a binary tensor (N*M) variable.

        Args:
            name (str): What is the name of this variable?
            variable_dim (list, optional): What are the dimensions of this variable? Defaults to 0.
            variable_bound (list, optional): What are the bounds on this variable? Defaults to [0, 1].

        Examples:
            * x = btvar('x')
            * x = btvar('x',[I,J])
            * x = btvar('x',[I,J], [0, 1])
        """

        variable_dim = fix_dims(variable_dim)

        self.features = update_variable_features(name, variable_dim, variable_bound, 'binary_variable_counter', self.features)

        match self.features['solution_method']:

            case 'exact':

                from .generators import variable_generator

                return variable_generator.generate_variable(self.features['interface_name'], self.model, 'btvar', name, variable_bound, variable_dim)

        return self.vars[name]

    def ptvar(self, name, variable_dim=0, variable_bound=[0, None]):

        """
        Positive Tensor Variable Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        To define a positive tensor (N*M) variable.

        Args:
            name (str): What is the name of this variable?
            variable_dim (list, optional): What are the dimensions of this variable? Defaults to 0.
            variable_bound (list, optional): What are the bounds on this variable? Defaults to [0, None].

        Examples:
            * x = ptvar('x')
            * x = ptvar('x',[I,J])
            * x = ptvar('x',[I,J], [0, 100])
        """

        variable_dim = fix_dims(variable_dim)

        self.features = update_variable_features(name, variable_dim, variable_bound, 'positive_variable_counter', self.features)

        match self.features['solution_method']:

            case 'exact':

                from .generators import variable_generator

                return variable_generator.generate_variable(self.features['interface_name'], self.model, 'ptvar', name, variable_bound, variable_dim)

        return self.vars[name]

    def itvar(self, name, variable_dim=0, variable_bound=[0, None]):

        """
        Integer Tensor Variable Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        To define an integer tensor (N*M) variable.

        Args:
            name (str): What is the name of this variable?
            variable_dim (list, optional): What are the dimensions of this variable? Defaults to 0.
            variable_bound (list, optional): What are the bounds on this variable? Defaults to [0, None].

        Examples:
            * x = itvar('x')
            * x = itvar('x',[I,J])
            * x = itvar('x',[I,J], [0, 100])
        """

        variable_dim = fix_dims(variable_dim)

        self.features = update_variable_features(name, variable_dim, variable_bound, 'integer_variable_counter', self.features)

        match self.features['solution_method']:

            case 'exact':

                from .generators import variable_generator

                return variable_generator.generate_variable(self.features['interface_name'], self.model, 'itvar', name, variable_bound, variable_dim)


        return self.vars[name]

    def ftvar(self, name, variable_dim=0, variable_bound=[None, None]):

        """
        Free Tensor Variable Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        To define a free tensor (N*M) variable.

        Args:
            name (str): What is the name of this variable?
            variable_dim (list, optional): What are the dimensions of this variable? Defaults to 0.
            variable_bound (list, optional): What are the bounds on this variable? Defaults to [None, None].

        Examples:
            * x = ftvar('x')
            * x = ftvar('x',[I,J])
            * x = ftvar('x',[I,J], [-100, 100])
        """

        variable_dim = fix_dims(variable_dim)

        self.features = update_variable_features(name, variable_dim, variable_bound, 'free_variable_counter', self.features)

        match self.features['solution_method']:

            case 'exact':

                from .generators import variable_generator

                return variable_generator.generate_variable(self.features['interface_name'], self.model, 'ftvar', name, variable_bound, variable_dim)

        return self.vars[name]

    def bvar(self, name, variable_dim=0, variable_bound=[0, 1]):

        """
        Binary Variable Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        To define a binary variable.

        Args:
            name (str): What is the name of this variable?
            variable_dim (list, optional): What are the dimensions of this variable? Defaults to 0.
            variable_bound (list, optional): What are the bounds on this variable? Defaults to [0, 1].

        Examples:
            * x = bvar('x')
            * x = bvar('x',[I,J])
            * x = bvar('x', [I,J], [0, 1])
        """

        variable_dim = fix_dims(variable_dim)

        self.features = update_variable_features(name, variable_dim, variable_bound, 'binary_variable_counter', self.features)

        match self.features['solution_method']:
            case 'exact':
                from .generators.variable_generator import generate_variable
                return generate_variable(self.features['interface_name'], self.model, 'bvar', name, variable_bound, variable_dim)
            case 'heuristic':
                return generate_heuristic_variable(self.features, 'bvar', name, variable_dim, variable_bound, self.agent)

    def pvar(self, name, variable_dim=0, variable_bound=[0, None]):

        """
        Positive Variable Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        To define a positive variable.

        Args:
            name (str): what is the name of this variable?
            variable_dim (list, optional): what are dimensions of this variable?. Defaults to 0.
            variable_bound (list, optional): what are bounds on this variable?. Defaults to [0, None].

        Examples:
            * x = pvar('x')
            * x = pvar('x',[I,J])
            * x = pvar('x', [I,J], [0, 100])
        """

        variable_dim = fix_dims(variable_dim)

        self.features = update_variable_features(
            name, variable_dim, variable_bound, 'positive_variable_counter', self.features)

        match self.features['solution_method']:
            case 'exact':
                from .generators import variable_generator
                return variable_generator.generate_variable(self.features['interface_name'], self.model, 'pvar', name, variable_bound, variable_dim)
            case 'heuristic':
                return generate_heuristic_variable(self.features, 'pvar', name, variable_dim, variable_bound, self.agent)

    def ivar(self, name, variable_dim=0, variable_bound=[0, None]):

        """
        Integer Variable Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        To define an integer variable.

        Args:
            name (str): what is the name of this variable?
            variable_dim (list, optional): what are dimensions of this variable?. Defaults to 0.
            variable_bound (list, optional): what are bounds on this variable?. Defaults to [0, None].

        Examples:
            * x = ivar('x')
            * x = ivar('x',[I,J])
            * x = ivar('x', [I,J], [0, 100])
        """

        self.features = update_variable_features(
            name, variable_dim, variable_bound, 'integer_variable_counter', self.features)

        match self.features['solution_method']:
            case 'exact':
                from .generators import variable_generator
                return variable_generator.generate_variable(self.features['interface_name'], self.model, 'ivar', name, variable_bound, variable_dim)
            case 'heuristic':
                return generate_heuristic_variable(self.features, 'ivar', name, variable_dim, variable_bound, self.agent)

    def fvar(self, name, variable_dim=0, variable_bound=[None, None]):

        """
        Free Variable Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        To define a free variable.

        Args:
            name (str): what is the name of this variable?
            variable_dim (list, optional): what are dimensions of this variable?. Defaults to 0.
            variable_bound (list, optional): what are bounds on this variable?. Defaults to [None, None].

        Examples:
            * x = fvar('x')
            * x = fvar('x',[I,J])
            * x = fvar('x', [I,J], [0, 100])
        """

        self.features = update_variable_features(
            name, variable_dim, variable_bound, 'free_variable_counter', self.features)

        match self.features['solution_method']:

            case 'exact':

                from .generators import variable_generator

                return variable_generator.generate_variable(self.features['interface_name'], self.model, 'fvar', name, variable_bound, variable_dim)

            case 'heuristic':

                return generate_heuristic_variable(self.features, 'fvar', name, variable_dim, variable_bound, self.agent)

    def dvar(self, name, variable_dim=0):

        """
        Dependent Variable Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        To define a dependent variable.

        Args:
            name (str): what is the name of this variable?
            variable_dim (list, optional): what are dimensions of this variable?. Defaults to 0.

        Examples:
            * x = dvar('x')
            * x = dvar('x',[I,J])
        """

        if self.features['agent_status'] == 'idle':
            if self.features['vectorized']:
                if variable_dim == 0:
                    return 0
                else:
                    return np.random.rand(*tuple([50]+[len(dims) for dims in variable_dim]))
            else:
                if variable_dim == 0:
                    return 0
                else:
                    return np.zeros([len(dims) for dims in variable_dim])

        else:
            if self.features['vectorized']:
                if variable_dim == 0:
                    return np.zeros(self.features['pop_size'])
                else:
                    return np.zeros([self.features['pop_size']]+[len(dims) for dims in variable_dim])
            else:
                if variable_dim == 0:
                    return 0
                else:
                    return np.zeros([len(dims) for dims in variable_dim])

    def svar(self, name, variable_dim=0):

        """
        Sequential Variable Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        To define a sequential variable.

        Args:
            name (str): what is the name of this variable?
            variable_dim (list, optional): what are dimensions of this variable?. Defaults to 0.

        Examples:
            * x = svar('x',[I])

        """

        self.features = update_variable_features(
            name, variable_dim, [0, 1], 'integer_variable_counter', self.features)
        self.features['variable_type'][name] = 'svar'
        return generate_heuristic_variable(self.features, 'fvar', name, variable_dim, [0, 1], self.agent)

    def invar(self, name, variable_dim=0, variable_bound=[None, None, None]):

        """        
        Interval Variable Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        To define an interval variable (which is a constraint) for constraint programming. Can be used inside other constraints.

        Notably: start + size == end.

        Args:
            name: The name of the interval variable.
            variable_dim: The dimension of the interval variable (is ignored).
            variable_bound: [start, size, end] for interval definiton. 
       
        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.interval_var(start=variable_bound[0], size=variable_bound[1], end=variable_bound[2], name=name)

        if self.features['interface_name'] == 'ortools_cp':

            return self.model.NewIntervalVar(start=variable_bound[0], size=variable_bound[1], end=variable_bound[2], name=name)

    def start_of(self, interval, absentValue=None):

        """

        To get the start of an interval variable. If it is absent, then the value of the expression is absentValue (zero by default).

        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.start_of(interval, absentValue)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def end_of(self, interval, absentValue=None):

        """

        To get the end of an interval variable. If it is absent, then the value of the expression is absentValue (zero by default).

        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.end_of(interval, absentValue)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def length_of(self, interval, absentValue=None):

        """

        To get the length (end - start) of an interval variable. If it is absent, then the value of the expression is absentValue (zero by default).

        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.length_of(interval, absentValue)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def size_of(self, interval, absentValue=None):

        """

        To get the size of an interval variable. If it is absent, then the value of the expression is absentValue (zero by default).

        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.size_of(interval, absentValue)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def presence_of(self, interval):

        """

        To get the presence status of an interval variable. If interval is present then the value of the expression is 1; if interval is absent then the value is 0.

        """
        if self.features['interface_name'] == 'cplex_cp':

            return self.model.presence_of(interval)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def start_at_start(self, interval1, interval2, delay=None):

        """
        To constrain the delay between the starts of two interval variables.

        If interval1 and interval2 are present, then interval interval2 must start exactly at start_of(interval1) + delay. 
        
        If interval1 or interval2 is absent, then the constraint is automatically satisfied.

        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.start_at_start(interval1, interval2, delay)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def start_at_end(self, interval1, interval2, delay=None):

        """
        To constrain the delay between the start of one interval variable and end of another one.

        If interval1 and interval2 are present then interval2 must end exactly at start_of(interval1) + delay. 
        
        If interval1 or interval2 is absent then the constraint is automatically satisfied.

        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.start_at_end(interval1, interval2, delay)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def start_before_start(self, interval1, interval2, delay=None):

        """

        To constrain the minimum delay between starts of two interval variables.

        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.start_before_start(interval1, interval2, delay)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def start_before_end(self, interval1, interval2, delay=None):

        """

        To constrain minimum delay between the start of one interval variable and end of another one.

        """


        if self.features['interface_name'] == 'cplex_cp':

            return self.model.start_before_end(interval1, interval2, delay)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def end_at_start(self, interval1, interval2, delay=None):

        """
        To constrain the delay between the end of one interval variable and start of another one.

        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.end_at_start(interval1, interval2, delay)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def end_at_end(self, interval1, interval2, delay=None):

        """

        To constrain the delay between the ends of two interval variables

        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.end_at_end(interval1, interval2, delay)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def end_before_start(self, interval1, interval2, delay=None):

        """

        To constrain minimum delay between the end of one interval variable and start of another one.

        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.end_before_start(interval1, interval2, delay)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def end_before_end(self, interval1, interval2, delay=None):

        """

        To constrain the minimum delay between the ends of two interval variables.

        """


        if self.features['interface_name'] == 'cplex_cp':

            return self.model.end_before_end(interval1, interval2, delay)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def forbid_start(self, interval, function):

        """

        To forbid an interval variable to start during specified regions.

        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.forbid_start(interval, function)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def forbid_end(self, interval, function):

        """

        To forbid an interval variable to end during specified regions.

        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.forbid_end(interval, function)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def forbid_extent(self, interval, function):

        """

        To forbid an interval variable to overlap with specified regions.

        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.forbid_extent(interval, function)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def overlap_length(self, interval1, interval2, absentValue=None):

        """
        To get the length of the overlap of two interval variables.
        """
        
        if self.features['interface_name'] == 'cplex_cp':

            return self.model.overlap_length(interval1, interval2, absentValue)

        if self.features['interface_name'] == 'ortools_cp':

            ""   

    def start_eval(self, interval, function, absentValue=None):

        """
        To evaluate a segmented function at the start of an interval variable
        """
        
        if self.features['interface_name'] == 'cplex_cp':

            return self.model.start_eval(interval, function, absentValue)

        if self.features['interface_name'] == 'ortools_cp':

            ""   

    def end_eval(self, interval, function, absentValue=None):

        """
        To evaluate a segmented function at the end of an interval variable
        """
        
        if self.features['interface_name'] == 'cplex_cp':

            return self.model.end_eval(interval, function, absentValue)

        if self.features['interface_name'] == 'ortools_cp':

            ""   

    def size_eval(self, interval, function, absentValue=None):

        """
        To evaluate a segmented function on the size of an interval variable
        """
        
        if self.features['interface_name'] == 'cplex_cp':

            return self.model.size_eval(interval, function, absentValue)

        if self.features['interface_name'] == 'ortools_cp':

            ""    

    def length_eval(self, interval, function, absentValue=None):

        """
        To evaluate a segmented function on the length of an interval variable
        """
        
        if self.features['interface_name'] == 'cplex_cp':

            return self.model.length_eval(interval, function, absentValue)

        if self.features['interface_name'] == 'ortools_cp':

            ""    

    def span(self, interval, function, absentValue=None):

        """
        To create a span constraint between interval variables.
        """
        
        if self.features['interface_name'] == 'cplex_cp':

            return self.model.span(interval, function, absentValue)

        if self.features['interface_name'] == 'ortools_cp':

            ""    

    def alternative(self, interval, array, cardinality=None):

        """
        To create an alternative constraint between interval variables.
        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.alternative(interval, array, cardinality)

        if self.features['interface_name'] == 'ortools_cp':

            ""       
      
    def set(self, *size):

        """
        Set Definition
        ~~~~~~~~~~~~~~
        To define a set.
        """

        return range(*size)

    def card(self, set):
        """
        Card Definition
        ~~~~~~~~~~~~~~~~
        To measure size of the set, etc.
        """

        return len(set)

    def uniform(self, lb, ub, variable_dim=0):
        """
        Uniform Parameter Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        To generate a real-valued parameter using uniform distribution inside a range.
        """

        if variable_dim == 0:
            return self.random.uniform(low=lb, high=ub)
        else:
            return self.random.uniform(low=lb, high=ub, size=([len(i) for i in variable_dim]))

    def uniformint(self, lb, ub, variable_dim=0):
        """
        Uniform Integer Parameter Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        To generate an integer parameter using uniform distribution inside a range.
        """

        if variable_dim == 0:
            return self.random.integers(low=lb, high=ub)
        else:
            return self.random.integers(low=lb, high=ub+1, size=([len(i) for i in variable_dim]))

    def obj(self, expression, direction=None, label=None):
        """
        Objective Function Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        To define an objective function.

        Args:
            expression (formula): what are the terms of this objective?
            direction (str, optional): what is the direction for optimizing this objective?. Defaults to None.
        """

        match self.features['solution_method']:

            case 'exact':

                self.features['directions'].append(direction)
                self.features['objectives'].append(expression)
                self.features['objective_labels'].append(label)
                self.features['objective_counter'][0] += 1
                self.features['objective_counter'][1] += 1

            case 'heuristic':

                if self.features['agent_status'] == 'idle':

                    self.features['directions'].append(direction)
                    self.features['objectives'].append(expression)
                    self.features['objective_labels'].append(label)
                    self.features['objective_counter'][0] += 1
                    self.features['objective_counter'][1] += 1

                else:
                    self.features['directions'].append(direction)
                    self.features['objective_counter'][0] += 1
                    self.features['objectives'].append(expression)

    def con(self, expression, label=None):
        """
        Constraint Definition
        ~~~~~~~~~~~~~~~~~~~~~
        To define a constraint.

        Args:
            expression (formula): what are the terms of this constraint?
            label (str, optional): what is the label of this constraint?. Defaults to None.
        """

        match self.features['solution_method']:

            case 'exact':

                self.features['constraint_labels'].append(label)
                self.features['constraint_counter'][0] = len(
                    set(self.features['constraint_labels']))
                self.features['constraints'].append(expression)
                self.features['constraint_counter'][1] = len(
                    self.features['constraints'])

            case 'heuristic':

                if self.features['agent_status'] == 'idle':

                    self.features['constraint_labels'].append(label)

                    self.features['constraint_counter'][0] = len(
                        set(self.features['constraint_labels']))

                    self.features['constraints'].append(expression)

                    self.features['constraint_counter'][1] = len(
                        self.features['constraints'])

                else:

                    if self.features['vectorized']:

                        self.features['constraints'].append(
                            np.reshape(expression, [np.shape(self.agent)[0], 1]))

                    else:
                        self.features['constraints'].append(expression)

    def sol(self, directions=None, solver_name=None, solver_options=dict(), objective_id=0, email=None, debug=False, time_limit=None, cpu_threads=None, absolute_gap=None, relative_gap=None, show_log=False, save_log=False, save_model=False, max_iterations=None):
        """
        Solve Command Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~
        To define solver and its settings to solve the problem.

        Args:
            directions (list, optional): please set the optimization directions of the objectives, if not provided before. Defaults to None.
            solver_name (_type_, optional): please set the solver_name. Defaults to None.
            solver_options (dict, optional): please set the solver options using a dictionary with solver specific keys. Defaults to None.
            objective_id (int, optional): please provide the objective id (number) that you wish to optimize. Defaults to 0.
            email (_type_, optional): please provide your email address if you wish to use cloud solvers (e.g., NEOS server). Defaults to None.
            debug (bool, optional): please state if the model should be checked for feasibility or logical bugs. Defaults to False.
            time_limit (seconds, optional): please state if the model should be solved under a specific timelimit. Defaults to None.
            cpu_threads (int, optional): please state if the solver should use a specific number of cpu threads. Defaults to None.
            absolute_gap (value, optional): please state an abolute gap to find the optimal objective value. Defaults to None.
            relative_gap (%, optional): please state a releative gap (%) to find the optimal objective value. Defaults to None.
        """

        self.features['objective_being_optimized'] = objective_id
        self.features['solver_name'] = solver_name
        self.features['solver_options'] = solver_options
        self.features['debug_mode'] = debug
        self.features['time_limit'] = time_limit
        self.features['thread_count'] = cpu_threads
        self.features['absolute_gap'] = absolute_gap
        self.features['relative_gap'] = relative_gap
        self.features['log'] = show_log
        self.features['write_model_file'] = save_model
        self.features['save_solver_log'] = save_log
        self.features['email_address'] = email
        self.features['max_iterations'] = max_iterations

        if type(objective_id) != str and directions != None:
            if self.features['directions'][objective_id] == None:
                self.features['directions'][objective_id] = directions[objective_id]
            for i in range(len(self.features['objectives'])):
                if i != objective_id:
                    del self.features['directions'][i]
                    del directions[i]
                    del self.features['objectives'][i]
            objective_id = 0
            self.features['objective_counter'] = [1, 1]

        match self.features['solution_method']:

            case 'exact':

                self.features['model_object_before_solve'] = self.model

                from .generators import solution_generator
                self.solution = solution_generator.generate_solution(
                    self.features)

                try:
                    self.obj_val = self.get_objective()
                    self.status = self.get_status()
                    self.cpt = self.get_time()*10**6

                except:
                    "None"

            case 'heuristic':

                if self.features['agent_status'] == 'idle':

                    "Do nothing"

                else:

                    if self.features['vectorized']:

                        self.penalty = np.zeros(np.shape(self.agent)[0])

                        if self.features['penalty_coefficient'] != 0 and len(self.features['constraints']) == 1:

                            self.features['constraints'][0] = np.reshape(
                                self.features['constraints'][0], [np.shape(self.agent)[0], 1])
                            self.features['constraints'].append(
                                np.zeros(shape=(np.shape(self.agent)[0], 1)))
                            self.penalty = np.amax(np.concatenate(
                                self.features['constraints'], axis=1), axis=1)

                            self.agent[np.where(self.penalty == 0), -2] = 1
                            self.agent[np.where(self.penalty > 0), -2] = -1

                        if self.features['penalty_coefficient'] != 0 and len(self.features['constraints']) > 1:

                            self.features['constraints'].append(
                                np.zeros(shape=(np.shape(self.agent)[0], 1)))
                            self.penalty = np.amax(np.concatenate(
                                self.features['constraints'], axis=1), axis=1)
                            self.agent[np.where(self.penalty == 0), -2] = 1
                            self.agent[np.where(self.penalty > 0), -2] = -1

                        else:

                            self.agent[:, -2] = 2

                        if type(objective_id) != str:

                            if directions[objective_id] == 'max':
                                self.agent[:, -1] = np.reshape(self.features['objectives'][objective_id], [self.agent.shape[0],]) - np.reshape(
                                    self.features['penalty_coefficient'] * (self.penalty)**2, [self.agent.shape[0],])

                            if directions[objective_id] == 'min':
                                self.agent[:, -1] = np.reshape(self.features['objectives'][objective_id], [self.agent.shape[0],]) + np.reshape(
                                    self.features['penalty_coefficient'] * (self.penalty)**2, [self.agent.shape[0],])

                    else:

                        self.penalty = 0

                        if len(self.features['constraints']) >= 1:
                            self.penalty = np.amax(
                                np.array([0]+self.features['constraints'], dtype=object))

                        if directions[objective_id] == 'max':
                            self.response = self.features['objectives'][objective_id] - \
                                self.features['penalty_coefficient'] * \
                                (self.penalty-0)**2

                        if directions[objective_id] == 'min':
                            self.response = self.features['objectives'][objective_id] + \
                                self.features['penalty_coefficient'] * \
                                (self.penalty-0)**2

    def get_variable(self, variable_with_index):
        from .generators import result_generator
        return result_generator.get(self.features, self.model, self.solution, 'variable', variable_with_index)

    def get_objective(self):
        from .generators import result_generator
        return result_generator.get(self.features, self.model, self.solution, 'objective', None)

    def get_status(self):
        from .generators import result_generator
        return result_generator.get(self.features, self.model, self.solution, 'status', None)

    def get_time(self):
        from .generators import result_generator
        return result_generator.get(self.features, self.model, self.solution, 'time', None)

    def dis_variable(self, *variables_with_index):
        for i in variables_with_index:
            print(str(i)+'*:', self.get_variable(i))

    def dis_status(self):
        print('status: ', self.get_status())

    def dis_obj(self):
        print('objective: ', self.get_objective())

    def dis_model(self):

        print('~~~~~~~~~~')
        print('MODEL INFO')
        print('~~~~~~~~~~')
        print('name:', self.features['model_name'])
        obdirs = 0
        for objective in self.features['objectives']:
            print(
                f"objective: {self.features['directions'][obdirs]}", objective)
            obdirs += 1
        print('subject to:')
        if self.features['constraint_labels'][0] != None:
            for constraint in sorted(zip(self.features['constraint_labels'], self.features['constraints']), key=lambda x: x[0]):
                print(f"constraint {constraint[0]}:", constraint[1])
        else:
            counter = 0
            for constraint in self.features['constraints']:
                print(f"constraint {counter}:", constraint)
                counter += 1
        print('~~~~~~~~~~')
        print()

    def dis_time(self):

        hour = round((self.get_time()), 3) % (24 * 3600) // 3600
        min = round((self.get_time()), 3) % (24 * 3600) % 3600 // 60
        sec = round((self.get_time()), 3) % (24 * 3600) % 3600 % 60

        print(f"cpu time [{self.features['interface_name']}]: ", self.get_time(
        )*10**6, '(microseconds)', "%02d:%02d:%02d" % (hour, min, sec), '(h, m, s)')

    def inf(self):

        data = {"info": ["model", "interface", "solver", "direction", "method"], "detail": [self.features['model_name'], self.features['interface_name'], self.features['solver_name'], self.features['directions'], self.features['solution_method']], "variable": ["positive", "binary", "integer", "free", "tot"], "count [cat,tot]": [str(self.features['positive_variable_counter']), str(
            self.features['binary_variable_counter']), str(self.features['integer_variable_counter']), str(self.features['free_variable_counter']), str(self.features['total_variable_counter'])], "other": ["objective", "constraint"], "count [cat,tot] ": [self.features['objective_counter'], self.features['constraint_counter']]}

        A = tb(data, headers="keys", tablefmt="github")

        print("~~~~~~~~~~~~\nPROBLEM INFO\n~~~~~~~~~~~~")
        print(A)
        print("~~~~~~~~~~~~\n")

        return A

    def report(self):

        print("\n~~~~~~~~~~~~~~\nFELOOPY v0.2.4\n~~~~~~~~~~~~~~")

        import datetime

        e = datetime.datetime.now()

        print("\n~~~~~~~~~~~\nDATE & TIME\n~~~~~~~~~~~")
        print(e.strftime("%Y-%m-%d %H:%M:%S"))
        print(e.strftime("%a, %b %d, %Y"))

        try:
            print()
            self.inf()

            print("~~~~~~~~~~\nSOLVE INFO\n~~~~~~~~~~")

            self.dis_status()
            self.dis_obj()
            self.dis_time()
            print("~~~~~~~~~~~\n")

            self.dis_model()
        except:
            self.inf()
            self.dis_status()
            self.dis_obj()
            self.dis_time()

    def abs(self, input):

        if self.features['interface_name'] in ['cplex_cp', 'gekko']:

            return self.model.abs(input)

        else:

            return abs(input)

    def acos(self, input):
        """

        Inverse cosine

        """

        if self.features['interface_name'] == 'gekko':

            return self.model.acos(input)

    def acosh(self, input):
        """

        Inverse hyperbolic cosine

        """

        if self.features['interface_name'] == 'gekko':

            return self.model.acosh(input)

    def asin(self, input):
        """

        Inverse sine

        """

        if self.features['interface_name'] == 'gekko':

            return self.model.acos(input)

    def asinh(self, input):
        """

        Inverse hyperbolic sine

        """

        if self.features['interface_name'] == 'gekko':

            return self.model.acos(input)

    def atan(self, input):
        """

        Inverse tangent

        """

        if self.features['interface_name'] == 'gekko':

            return self.model.acos(input)

    def atanh(self, input):
        """

        Inverse hyperbolic tangent

        """

        if self.features['interface_name'] == 'gekko':

            return self.model.atanh(input)

    def cos(self, input):
        """

        Cosine

        """

        if self.features['interface_name'] == 'gekko':

            return self.model.cos(input)

    def erf(self, input):
        """

        Error function

        """

        if self.features['interface_name'] == 'gekko':

            return self.model.erf(input)

    def erfc(self, input):
        """

        complementary error function

        """
        if self.features['interface_name'] == 'gekko':

            return self.model.erfc(input)

    def plus(self, input1, input2):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.plus(input1, input2)

        else:

            return input1+input2

    def minus(self, input1, input2):
        """

        Creates an expression that represents the product of two expressions.

        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.minus(input1, input2)

        else:

            return input1-input2

    def times(self, input1, input2):
        """

        Creates an expression that represents the product of two expressions.

        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.times(input1, input2)

        else:

            return input1*input2

    def true(self):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.true()

        else:

            return True

    def false(self):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.false()

        else:

            return False

    def trunc(self, input):
        '''
        Builds the truncated integer parts of a float expression
        '''

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.trunc(input)

        else:

            return "None"

    def int_div(self, input1, input2):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.int_div(input)

        else:

            return input1//input2

    def float_div(self, input1, input2):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.int_div(input)

        else:

            return input1/input2

    def mod(self, input1, input2):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.mod(input1, input2)

        else:

            return input1 % input2

    def square(self, input):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.square(input)

        else:

            return input * input

    def power(self, input1, input2):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.power(input1, input2)

        else:

            return input1 ** input2

    def log(self, input):
        """

        Natural Logarithm

        """

        if self.features['interface_name'] in ['cplex_cp']:

            return self.model.log(input)

        elif self.features['interface_name'] in ['gekko']:

            return self.model.log(input)

        else:

            return np.log(input)

    def log10(self, input):
        """

        Logarithm Base 10

        """

        if self.features['interface_name'] in ['gekko']:

            return self.model.log10(input)

    def sin(self, input):
        """

        Sine

        """

        if self.features['interface_name'] in ['gekko']:

            return self.model.sin(input)

    def sinh(self, input):
        """

        Hyperbolic sine

        """

        if self.features['interface_name'] in ['gekko']:

            return self.model.sinh(input)

    def sqrt(self, input):
        """

        Square root

        """

        if self.features['interface_name'] in ['gekko']:

            return self.model.sqrt(input)

    def tan(self, input):
        """

        Tangent

        """

        if self.features['interface_name'] in ['gekko']:

            return self.model.tan(input)

    def tanh(self, input):
        """

        Hyperbolic tangent

        """

        if self.features['interface_name'] in ['gekko']:

            return self.model.tanh(input)

    def sigmoid(self, input):
        """

        Sigmoid function

        """

        if self.features['interface_name'] in ['gekko']:

            return self.model.sigmoid(input)

    def exponent(self, input):

        if self.features['interface_name'] in ['cplex_cp', 'gekko']:

            return self.model.exp(input)

        else:

            return np.exp(input)

    def count(self, input, value):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.count(input, value)

        else:

            return input.count(value)

    def scal_prod(self, input1, input2):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.scal_prod(input1, input2)

        else:

            return np.dot(input1, input2)

    def range(self, x, lb=None, ub=None):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.range(x, lb, ub)

        else:

            return [x >= lb] + [x <= ub]

    def floor(self, x):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.floor(x)

        else:

            return np.floor(x)

    def ceil(self, x):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.ceil(x)

        else:

            return np.ceil(x)

    def round(self, x):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.round(x)

        else:

            return np.round(x)

    def all_dist_above(self, exprs, value):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.all_min_distance(exprs, value)

        else:

            return abs(exprs) >= value

    def if_then(self, input1, input2):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.if_then(input1, input2)

        else:

            if input1:

                return input2

# Alternatives for defining this class:

model = add_model = create_environment = env = feloopy = representor_model = leaner_model = target_model = op = Model

warnings.simplefilter(action='ignore', category=FutureWarning)

class Implement:

    def __init__(self, ModelFunction):
        '''
        * ModelFunction (Function): The function that contains the model, its corresponding solve command, and returns its objective, fitness or hypothesis value.
        '''

        self.ModelInfo = ModelFunction(['idle'])

        self.ModelFunction = ModelFunction

        self.InterfaceName = self.ModelInfo.features['interface_name']

        self.SolutionMethod = self.ModelInfo.features['solution_method']
        self.ModelName = self.ModelInfo.features['model_name']
        self.SolverName = self.ModelInfo.features['solver_name']
        self.ModelConstraints = self.ModelInfo.features['constraints']
        self.ModelObjectives = self.ModelInfo.features['objectives']
        self.ObjectivesDirections = self.ModelInfo.features['directions']
        self.PositiveVariableCounter = self.ModelInfo.features['positive_variable_counter']
        self.BinaryVariableCounter = self.ModelInfo.features['binary_variable_counter']
        self.IntegerVariableCounter = self.ModelInfo.features['integer_variable_counter']
        self.FreeVariableCounter = self.ModelInfo.features['free_variable_counter']
        self.ToTalVariableCounter = self.ModelInfo.features['total_variable_counter']
        self.ConstraintsCounter = self.ModelInfo.features['constraint_counter']
        self.ObjectivesCounter = self.ModelInfo.features['objective_counter']
        self.AlgOptions = self.ModelInfo.features['solver_options']
        self.VariablesSpread = self.ModelInfo.features['variable_spread']
        self.VariablesType = self.ModelInfo.features['variable_type']
        self.ObjectiveBeingOptimized = self.ModelInfo.features['objective_being_optimized']
        self.VariablesBound = self.ModelInfo.features['variable_bound']
        self.VariablesDim = self.ModelInfo.features['variable_dim']

        self.status = 'Not solved'
        self.response = None

        self.AgentProperties = [None, None, None, None]

        self.get_objective = self.get_obj
        self.get_var = self.get_variable = self.get
        self.search = self.solve = self.optimize = self.run = self.sol

        match self.InterfaceName:

            case 'mealpy':

                from .generators.model import mealpy_model_generator
                self.ModelObject = mealpy_model_generator.generate_model(
                    self.SolverName, self.AlgOptions)

            case 'feloopy':

                from .generators.model import feloopy_model_generator
                self.ModelObject = feloopy_model_generator.generate_model(
                    self.ToTalVariableCounter[1], self.ObjectivesDirections, self.SolverName, self.AlgOptions)

    def sol(self, penalty_coefficient=0, number_of_times=1, show_plots=False, save_plots=False):

        self.penalty_coefficient = penalty_coefficient

        match self.InterfaceName:

            case 'mealpy':

                from .generators.solution import mealpy_solution_generator
                self.BestAgent, self.BestReward, self.start, self.end = mealpy_solution_generator.generate_solution(
                    self.ModelObject, self.Fitness, self.ToTalVariableCounter, self.ObjectivesDirections, self.ObjectiveBeingOptimized, number_of_times, show_plots, save_plots)

            case 'feloopy':

                from .generators.solution import feloopy_solution_generator
                self.BestAgent, self.BestReward, self.start, self.end, self.status = feloopy_solution_generator.generate_solution(
                    self.ModelObject, self.Fitness, self.ToTalVariableCounter, self.ObjectivesDirections, self.ObjectiveBeingOptimized, number_of_times, show_plots)

    def dis_status(self):
        print('status:', self.get_status())

    def get_status(self):

        if self.status[0] == 1:
            return 'feasible (constrained)'
        elif self.status[0] == 2:
            return 'feasible (unconstrained)'
        elif self.status[0] == -1:
            return 'infeasible'

    def Fitness(self, X):

        self.AgentProperties[0] = 'active'
        self.AgentProperties[1] = X
        self.AgentProperties[2] = self.VariablesSpread
        self.AgentProperties[3] = self.penalty_coefficient

        return self.ModelFunction(self.AgentProperties)

    def get(self, *args):
        if self.ObjectivesCounter[0] == 1:
            match self.InterfaceName:
                case 'mealpy':
                    for i in args:
                        if len(i) >= 2:
                            match self.VariablesType[i[0]]:
                                case 'pvar':
                                    if self.VariablesDim[i[0]] == 0:
                                        return (self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))[0]
                                    else:
                                        def var(*args):
                                            self.NewAgentProperties = (self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (
                                                self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                            return self.NewAgentProperties[sum(args[k]*mt.prod(len(self.VariablesDim[i[0]][j]) for j in range(k+1, len(self.VariablesDim[i[0]]))) for k in range(len(self.VariablesDim[i[0]])))]
                                        return var(*i[1])
                                case 'fvar':
                                    if self.VariablesDim[i[0]] == 0:
                                        return (self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))[0]
                                    else:
                                        def var(*args):
                                            self.NewAgentProperties = (self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (
                                                self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                            return self.NewAgentProperties[sum(args[k]*mt.prod(len(self.VariablesDim[i[0]][j]) for j in range(k+1, len(self.VariablesDim[i[0]]))) for k in range(len(self.VariablesDim[i[0]])))]
                                        return var(*i[1])
                                case 'bvar':
                                    if self.VariablesDim[i[0]] == 0:
                                        return np.round(self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))[0]
                                    else:
                                        def var(*args):
                                            self.NewAgentProperties = np.round(self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (
                                                self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                            return self.NewAgentProperties[sum(args[k]*mt.prod(len(self.VariablesDim[i[0]][j]) for j in range(k+1, len(self.VariablesDim[i[0]]))) for k in range(len(self.VariablesDim[i[0]])))]
                                        return var(*i[1])
                                case 'ivar':
                                    if self.VariablesDim[i[0]] == 0:
                                        return np.floor(self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))[0]
                                    else:
                                        def var(*args):
                                            self.NewAgentProperties = np.floor(self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (
                                                self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                            return self.NewAgentProperties[sum(args[k]*mt.prod(len(self.VariablesDim[i[0]][j]) for j in range(k+1, len(self.VariablesDim[i[0]]))) for k in range(len(self.VariablesDim[i[0]])))]
                                        return var(*i[1])
                                case 'svar':
                                    return np.argsort(self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]])[i[1]]

                        else:
                            match self.VariablesType[i[0]]:
                                case 'pvar':
                                    return (self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))[0]
                                case 'fvar':
                                    return (self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))[0]
                                case 'bvar':
                                    return np.round(self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))[0]
                                case 'ivar':
                                    return np.floor(self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))[0]
                                case 'svar':
                                    return np.argsort(self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]])
                case 'feloopy':
                    for i in args:
                        if len(i) >= 2:
                            match self.VariablesType[i[0]]:
                                case 'pvar':
                                    if self.VariablesDim[i[0]] == 0:
                                        return (self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                    else:
                                        def var(*args):
                                            self.NewAgentProperties = (self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (
                                                self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                            return self.NewAgentProperties[sum(args[k]*mt.prod(len(self.VariablesDim[i[0]][j]) for j in range(k+1, len(self.VariablesDim[i[0]]))) for k in range(len(self.VariablesDim[i[0]])))]
                                        return var(*i[1])
                                case 'fvar':

                                    if self.VariablesDim[i[0]] == 0:
                                        return (self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))

                                    else:
                                        def var(*args):
                                            self.NewAgentProperties = (self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (
                                                self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                            return self.NewAgentProperties[sum(args[k]*mt.prod(len(self.VariablesDim[i[0]][j]) for j in range(k+1, len(self.VariablesDim[i[0]]))) for k in range(len(self.VariablesDim[i[0]])))]

                                        return var(*i[1])

                                case 'bvar':
                                    if self.VariablesDim[i[0]] == 0:
                                        return np.floor(self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))

                                    else:
                                        def var(*args):
                                            self.NewAgentProperties = np.round(self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (
                                                self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                            return self.NewAgentProperties[sum(args[k]*mt.prod(len(self.VariablesDim[i[0]][j]) for j in range(k+1, len(self.VariablesDim[i[0]]))) for k in range(len(self.VariablesDim[i[0]])))]

                                        return var(*i[1])
                                case 'ivar':
                                    if self.VariablesDim[i[0]] == 0:
                                        return np.floor(self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))

                                    else:
                                        def var(*args):
                                            self.NewAgentProperties = np.floor(self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (
                                                self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                            return self.NewAgentProperties[sum(args[k]*mt.prod(len(self.VariablesDim[i[0]][j]) for j in range(k+1, len(self.VariablesDim[i[0]]))) for k in range(len(self.VariablesDim[i[0]])))]
                                        return var(*i[1])

                                case 'svar':
                                    return np.argsort(self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]])[i[1]]

                        else:
                            match self.VariablesType[i[0]]:

                                case 'pvar':
                                    return (self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                case 'fvar':
                                    return (self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                case 'bvar':
                                    return np.round(self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                case 'ivar':
                                    return np.floor(self.VariablesBound[i[0]][0] + self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                case 'svar':
                                    return np.argsort(self.BestAgent[self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]])
        else:

            for i in args:
                if len(i) >= 2:

                    match self.VariablesType[i[0]]:

                        case 'pvar':

                            if self.VariablesDim[i[0]] == 0:
                                return (self.VariablesBound[i[0]][0] + self.BestAgent[:, self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))

                            else:
                                def var(*args):
                                    self.NewAgentProperties = (self.VariablesBound[i[0]][0] + self.BestAgent[:, self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (
                                        self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                    return self.NewAgentProperties[sum(args[k]*mt.prod(len(self.VariablesDim[i[0]][j]) for j in range(k+1, len(self.VariablesDim[i[0]]))) for k in range(len(self.VariablesDim[i[0]])))]

                                return var(*i[1])

                        case 'fvar':
                            if self.VariablesDim[i[0]] == 0:
                                return (self.VariablesBound[i[0]][0] + self.BestAgent[:, self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))

                            else:
                                def var(*args):
                                    self.NewAgentProperties = (self.VariablesBound[i[0]][0] + self.BestAgent[:, self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (
                                        self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                    return self.NewAgentProperties[sum(args[k]*mt.prod(len(self.VariablesDim[i[0]][j]) for j in range(k+1, len(self.VariablesDim[i[0]]))) for k in range(len(self.VariablesDim[i[0]])))]

                                return var(*i[1])

                        case 'bvar':
                            if self.VariablesDim[i[0]] == 0:
                                return np.floor(self.VariablesBound[i[0]][0] + self.BestAgent[:, self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))

                            else:
                                def var(*args):
                                    self.NewAgentProperties = np.round(self.VariablesBound[i[0]][0] + self.BestAgent[:, self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (
                                        self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                    return self.NewAgentProperties[sum(args[k]*mt.prod(len(self.VariablesDim[i[0]][j]) for j in range(k+1, len(self.VariablesDim[i[0]]))) for k in range(len(self.VariablesDim[i[0]])))]

                                return var(*i[1])
                        case 'ivar':
                            if self.VariablesDim[i[0]] == 0:
                                return np.floor(self.VariablesBound[i[0]][0] + self.BestAgent[:, self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                            else:
                                def var(*args):
                                    self.NewAgentProperties = np.floor(self.VariablesBound[i[0]][0] + self.BestAgent[:, self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (
                                        self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                    return self.NewAgentProperties[sum(args[k]*mt.prod(len(self.VariablesDim[i[0]][j]) for j in range(k+1, len(self.VariablesDim[i[0]]))) for k in range(len(self.VariablesDim[i[0]])))]
                                return var(*i[1])

                        case 'svar':

                            return np.argsort(self.BestAgent[:, self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]])[i[1]]

                else:

                    match self.VariablesType[i[0]]:
                        case 'pvar':
                            return (self.VariablesBound[i[0]][0] + self.BestAgent[:, self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                        case 'fvar':
                            return (self.VariablesBound[i[0]][0] + self.BestAgent[:, self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                        case 'bvar':
                            return np.round(self.VariablesBound[i[0]][0] + self.BestAgent[:, self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                        case 'ivar':
                            return np.floor(self.VariablesBound[i[0]][0] + self.BestAgent[:, self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                        case 'svar':
                            return np.argsort(self.BestAgent[:, self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]])

    def dis_time(self):

        hour = round(((self.end-self.start)), 3) % (24 * 3600) // 3600
        min = round(((self.end-self.start)), 3) % (24 * 3600) % 3600 // 60
        sec = round(((self.end-self.start)), 3) % (24 * 3600) % 3600 % 60

        print(f"cpu time [{self.InterfaceName}]: ", (self.end-self.start)*10 **
              6, '(microseconds)', "%02d:%02d:%02d" % (hour, min, sec), '(h, m, s)')

    def get_time(self):
        """

        Used to get solution time in seconds.


        """

        return self.end-self.start

    def get_obj(self):
        return self.BestReward

    def dis(self, input):

        if len(input) >= 2:

            print(input[0]+str(input[1])+': ', self.get(input))

        else:

            print(str(input[0])+': ', self.get(input))

    def dis_obj(self):

        print('objective: ', self.BestReward)

    def inf(self):

        print()
        print("~~~~~~~~~~~~\nPROBLEM INFO\n~~~~~~~~~~~~")

        A = tb(
            {
                "info": ["model", "interface", "solver", "direction", "method"],
                "detail": [self.ModelName, self.InterfaceName, self.SolverName, self.ObjectivesDirections, self.SolutionMethod],
                "variable": ["positive", "binary", "integer", "free", "tot"],
                "count [cat,tot]": [str(self.PositiveVariableCounter), str(self.BinaryVariableCounter), str(self.IntegerVariableCounter), str(self.FreeVariableCounter), str(self.ToTalVariableCounter)],
                "other": ["objective", "constraint"],
                "count [cat,tot] ": [str(self.ObjectivesCounter), str(self.ConstraintsCounter)]
            },
            headers="keys", tablefmt="github"
        )
        print(A)
        print("~~~~~~~~~~~~\n")

        return A

    def report(self):

        print("\n~~~~~~~~~~~~~~\nFELOOPY v0.2.4\n~~~~~~~~~~~~~~")

        import datetime

        e = datetime.datetime.now()

        print("\n~~~~~~~~~~~\nDATE & TIME\n~~~~~~~~~~~")
        print(e.strftime("%Y-%m-%d %H:%M:%S"))
        print(e.strftime("%a, %b %d, %Y"))

        print()
        self.inf()

        print("~~~~~~~~~~\nSOLVE INFO\n~~~~~~~~~~")
        self.dis_obj()
        self.dis_time()
        print("~~~~~~~~~\n")

# Alternatives for defining this class:

construct = make_model = implementor = implement = Implement
