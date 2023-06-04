'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-25
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

from .helpers.empty import *
from .helpers.error import *
from .helpers.formatter import *
from .operators.set_operators import *
from .operators.math_operators import *
from .operators.count_operators import *
from .operators.update_operators import *
from .operators.random_operators import *
from .operators.heuristic_operators import *
from .operators.fix_operators import *
from .operators.epsilon import *
from .operators.metric_operators import *
from collections import defaultdict
        

import warnings
import itertools as it
import math as mt
import numpy as np
from tabulate import tabulate as tb
from typing import List, Tuple, Optional
import sys

warnings.filterwarnings("ignore")

avar = defaultdict()

class Model:

    # Method for the modeling envrionment.

    def __init__(self, solution_method, model_name, interface_name, agent=None, scens=1, key=None):
        """
        Creates and returns the modeling environment.

        Args:
            solution_method (str): Desired solution (optimization) method.
            model_name (str): Name of this model.
            interface_name (str): Desired interface name.
            agent (X, optional): Input of the representor model. Default: None. 
            scens (int, optional): Number of uncertainty scenarios, which can also be an array containing scenario indices. Default: 1.
            key (number, optional): Key for the random number generator. Default: None.
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
        self.random_variable = self.add_random_variable = self.rvar
        self.random_tensor_variable = self.add_random_tensor_variable = self.rtvar
        self.dependent_variable = self.add_dependent_variable = self.dvar
        self.objective = self.reward = self.hypothesis = self.fitness = self.goal = self.add_objective = self.obj
        self.constraint = self.equation = self.add_constraint = self.add_equation = self.st = self.subject_to = self.cb = self.computed_by = self.con
        self.solve = self.implement = self.run = self.optimize = self.sol
        self.get_obj = self.get_objective
        self.get_stat = self.get_status
        self.get_var = self.value = self.get = self.get_variable
        self.dis = self.dis_var = self.display = self.show = self.print = self.display_variable = self.dis_variable
        self.status = self.show_status = self.dis_status
        self.objective_value = self.show_objective = self.display_objective = self.dis_obj
        self.random = create_random_number_generator(key)
        self.avar= self.coll()

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
                    'scens': scens,
                }
                self.mainvars = self.coll()
                self.maindims = self.coll()
                from .generators import model_generator
                self.model = model_generator.generate_model(self.features)
                self.sm = self.model
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
                elif self.agent[0] == 'feasibility_check':
                    self.features = {
                        'agent_status': 'feasibility_check',
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
                    case 'pymultiobjective': self.features['vectorized'] = False
                    case 'feloopy': self.features['vectorized'] = True

    def __getitem__(self, agent):
        """
        Returns the required features of the model object.

        Args:
            agent (X): Input of the representor model/instance.
        """

        if self.features['agent_status'] == 'idle':
            return self
        elif self.features['agent_status'] == 'feasibility_check':
            if self.features['penalty_coefficient'] == 0:
                return 'feasible (unconstrained)'
            else:
                if self.penalty > 0:
                    return 'infeasible (constrained)'
                else:
                    return 'feasible (constrained)'
        else:
            if self.features['vectorized']:
                return self.agent
            else:
                return self.response

    # Methods for variables definitions.

    def coll(dim):
        """
        Creates and returns an empty collection (dictionary) of variables.
        """
        from collections import defaultdict
        return defaultdict()

    def btvar(self, name, dim=0, bound=[0, 1]):
        """
        Creates and returns a tensor-like binary variable.

        Args:
            name (str): Name of this variable.
            dim (list, optional): Dimensions of this variable. Default: 0.
            bound (list, optional): Bounds of this variable. Default: [0, 1].
        """
        
        dim = fix_dims(dim)
        self.features = update_variable_features(
            name, dim, bound, 'binary_variable_counter', self.features)

        match self.features['solution_method']:

            case 'exact':

                from .generators import variable_generator
                self.mainvars[("btvar",name)] = variable_generator.generate_variable(self.features['interface_name'], self.model, 'btvar', name, bound, dim)
                self.maindims[name] = dim
                return self.mainvars[("btvar",name)]

    def ptvar(self, name, dim=0, bound=[0, None]):
        """
        Creates and returns a tensor-like positive variable.

        Args:
            name (str): Name of this variable.
            dim (list, optional): Dimensions of this variable. Default: 0.
            bound (list, optional): Bounds of this variable. Default: [0, None].
        """

        dim = fix_dims(dim)
        self.features = update_variable_features(
            name, dim, bound, 'positive_variable_counter', self.features)

        match self.features['solution_method']:

            case 'exact':

                from .generators import variable_generator
                self.mainvars[("ptvar",name)] = variable_generator.generate_variable(self.features['interface_name'], self.model, 'ptvar', name, bound, dim)
                self.maindims[name] = dim
                if self.features['interface_name'] in ['rsome_ro', 'rsome_dro']:
                    self.con(self.mainvars[("ptvar",name)]>=0)
                return self.mainvars[("ptvar",name)]

    def itvar(self, name, dim=0, bound=[0, None]):
        """
        Creates and returns a tensor-like integer variable.

        Args:
            name (str): Name of this variable.
            dim (list, optional): Dimensions of this variable. Default: 0.
            bound (list, optional): Bounds of this variable. Default: [0, None].
        """

        dim = fix_dims(dim)
        self.features = update_variable_features(
            name, dim, bound, 'integer_variable_counter', self.features)

        match self.features['solution_method']:

            case 'exact':

                from .generators import variable_generator
                self.mainvars[("ptvar",name)] = variable_generator.generate_variable(self.features['interface_name'], self.model, 'itvar', name, bound, dim)
                self.maindims[name] = dim
                return self.mainvars[("ptvar",name)]

        return self.vars[name]

    def ftvar(self, name, dim=0, bound=[None, None]):
        """
        Creates and returns a tensor-like free variable.

        Args:
            name (str): Name of this variable.
            dim (list, optional): Dimensions of this variable. Default: 0.
            bound (list, optional): Bounds of this variable. Default: [None, None].
        """

        dim = fix_dims(dim)
        self.features = update_variable_features(
            name, dim, bound, 'free_variable_counter', self.features)

        match self.features['solution_method']:

            case 'exact':

                from .generators import variable_generator
                self.mainvars[("ftvar",name)] = variable_generator.generate_variable(self.features['interface_name'], self.model, 'ftvar', name, bound, dim)
                self.maindims[name] = dim
                return self.mainvars[("ftvar",name)]

    def bvar(self, name, dim=0, bound=[0, 1]):
        """
        Creates and returns a binary variable.

        Args:
            name (str): Name of this variable.
            dim (list, optional): Dimensions of this variable. Default: 0.
            bound (list, optional): Bounds of this variable. Default: [0, 1].
        """

        dim = fix_dims(dim)
        self.features = update_variable_features(
            name, dim, bound, 'binary_variable_counter', self.features)

        match self.features['solution_method']:

            case 'exact':

                from .generators import variable_generator
                self.mainvars[("bvar",name)] = variable_generator.generate_variable(self.features['interface_name'], self.model, 'bvar', name, bound, dim)
                self.maindims[name] = dim

                if self.features['interface_name'] in ['cvxpy']:
                    if dim==0:
                        self.con(self.mainvars[("bvar",name)]>=0)
                        self.con(self.mainvars[("bvar",name)]<=1)
                    elif len(dim)==1:
                        for i in dim[0]:
                            self.con(self.mainvars[("bvar",name)][i]>=0)
                            self.con(self.mainvars[("bvar",name)][i]<=1)
                    else:
                        for i in it.product(*tuple(dim)):
                            self.con(self.mainvars[("bvar",name)][i]>=0)
                            self.con(self.mainvars[("bvar",name)][i]<=1)
                return self.mainvars[("bvar",name)]

            case 'heuristic':

                return generate_heuristic_variable(self.features, 'bvar', name, dim, bound, self.agent)

    def pvar(self, name, dim=0, bound=[0, None]):
        """
        Creates and returns a positive variable.

        Args:
            name (str): Name of this variable.
            dim (list, optional): Dimensions of this variable. Default: 0.
            bound (list, optional): Bounds of this variable. Default: [0, None].
        """

        dim = fix_dims(dim)
        self.features = update_variable_features(
            name, dim, bound, 'positive_variable_counter', self.features)

        match self.features['solution_method']:

            case 'exact':

                from .generators import variable_generator
                self.mainvars[("pvar",name)] = variable_generator.generate_variable(self.features['interface_name'], self.model, 'pvar', name, bound, dim)
                self.maindims[name] = dim

                if self.features['interface_name'] in ['rsome_ro', 'rsome_dro']:

                    if dim==0:
                        self.con(self.mainvars[("pvar",name)]>=0)
                        self.con(self.mainvars[("pvar",name)]<=1)

                    elif len(dim)==1:

                        for i in dim[0]:
                            self.con(self.mainvars[("pvar",name)][i]>=0)
                            self.con(self.mainvars[("pvar",name)][i]<=1)
                    else:

                        for i in it.product(*tuple(dim)):
                            self.con(self.mainvars[("pvar",name)][i]>=0)
                            self.con(self.mainvars[("pvar",name)][i]<=1)

                return self.mainvars[("pvar",name)]

            case 'heuristic':

                return generate_heuristic_variable(self.features, 'pvar', name, dim, bound, self.agent)

    def ivar(self, name, dim=0, bound=[0, None]):
        """
        Creates and returns an integer variable.

        Args:
            name (str): Name of this variable.
            dim (list, optional): Dimensions of this variable. Default: 0.
            bound (list, optional): Bounds of this variable. Default: [0, None].
        """

        dim = fix_dims(dim)
        self.features = update_variable_features(name, dim, bound, 'integer_variable_counter', self.features)

        match self.features['solution_method']:

            case 'exact':

                from .generators import variable_generator
                self.mainvars[("ivar",name)] = variable_generator.generate_variable(self.features['interface_name'], self.model, 'ivar', name, bound, dim)
                self.maindims[name] = dim
                return self.mainvars[("ivar",name)]

            case 'heuristic':

                return generate_heuristic_variable(self.features, 'ivar', name, dim, bound, self.agent)

    def fvar(self, name, dim=0, bound=[None, None]):
        """
        Creates and returns a free variable.

        Args:
            name (str): Name of this variable.
            dim (list, optional): Dimensions of this variable. Default: 0.
            bound (list, optional): Bounds of this variable. Default: [None, None].
        """

        dim = fix_dims(dim)
        self.features = update_variable_features(
            name, dim, bound, 'free_variable_counter', self.features)

        match self.features['solution_method']:

            case 'exact':

                from .generators import variable_generator
                self.mainvars[("fvar",name)] = variable_generator.generate_variable(self.features['interface_name'], self.model, 'fvar', name, bound, dim)
                self.maindims[name] = dim
                return self.mainvars[("fvar",name)]

            case 'heuristic':

                return generate_heuristic_variable(self.features, 'fvar', name, dim, bound, self.agent)

    def dvar(self, name, dim=0):
        """
        Creates and returns a dependent variable.

        Args:
            name (str): Name of this variable.
            dim (list, optional): Dimensions of this variable. Default: 0.
        """

        dim = fix_dims(dim)

        match self.features['solution_method']:

            case 'exact':

                return np.zeros([len(dims) for dims in dim])
            
            case 'heuristic':

                if self.features['agent_status'] == 'idle':
                    if self.features['vectorized']:
                        if dim == 0:
                            return 0
                        else:
                            return np.random.rand(*tuple([50]+[len(dims) for dims in dim]))
                    else:
                        if dim == 0:
                            return 0
                        else:
                            return np.zeros([len(dims) for dims in dim])
                else:
                    if self.features['vectorized']:
                        if dim == 0:
                            return np.zeros(self.features['pop_size'])
                        else:
                            return np.zeros([self.features['pop_size']]+[len(dims) for dims in dim])
                    else:
                        if dim == 0:
                            return 0
                        else:
                            return np.zeros([len(dims) for dims in dim])

    def rvar(self, name, dim=0):
        """
        Creates and returns a random variable.

        Args:
            name (str): Name of this variable.
            dim (list, optional): Dimensions of this variable. Default: 0.
        """
        dim = fix_dims(dim)
        from .generators import variable_generator
        return variable_generator.generate_variable(self.features['interface_name'], self.model, 'rvar', name, [None, None], dim)
    
    def rtvar(self, name, dim=0):
        """
        Creates and returns a tensor-like random variable.

        Args:
            name (str): Name of this variable.
            dim (list, optional): Dimensions of this variable. Default: 0.
        """
        dim = fix_dims(dim)
        from .generators import variable_generator
        return variable_generator.generate_variable(self.features['interface_name'], self.model, 'rtvar', name, [None, None], dim)
    
    def svar(self, name, dim=0):
        """
        Creates and returns a sequential variable.

        Args:
            name (str): Name of this variable.
            dim (list, optional): Dimensions of this variable. Default: 0.
        """

        self.features = update_variable_features(
            name, dim, [0, 1], 'integer_variable_counter', self.features)
        self.features['variable_type'][name] = 'svar'

        return generate_heuristic_variable(self.features, 'svar', name, dim, [0, 1], self.agent)

    def evar(self, name, interval=[None, None, None], dim=0, is_present=False):
        """        
        Creates and returns an event (interval) variable.

        Args:
            name: Name of this variable.
            interval: [size, start, end]. 
            dim (list, optional): Dimensions of this variable. Default: 0.
        """

        if len(interval) == 1:
            interval = [interval[0], None, None]

        if dim == 0:

            if self.features['interface_name'] == 'cplex_cp':
                return self.model.interval_var(start=interval[1], size=interval[0], end=interval[2], name=name, optional=is_present)
            if self.features['interface_name'] == 'ortools_cp':
                return self.model.NewOptionalIntervalVar(start=interval[1], size=interval[0], end=interval[2], name=name, is_present=is_present)
        else:
            if self.features['interface_name'] == 'cplex_cp':
                if len(dim) == 1:
                    return {key: self.model.interval_var(start=interval[1], size=interval[0], end=interval[2], name=f"{name}{key}", optional=is_present) for key in dim[0]}
                else:
                    return {key: self.model.interval_var(start=interval[1], size=interval[0], end=interval[2], name=f"{name}{key}", optional=is_present) for key in sets(*dim)}

            if self.features['interface_name'] == 'ortools_cp':

                if len(dim) == 1:
                    return {key: self.model.NewOptionalIntervalVar(start=interval[1], size=interval[0], end=interval[2], name=f"{name}{key}", is_present=is_present) for key in dim[0]}
                else:
                    return {key: self.model.NewOptionalIntervalVar(start=interval[1], size=interval[0], end=interval[2], name=f"{name}{key}", is_present=is_present) for key in sets(*dim)}

    # Methods for handling special automation operations
    def scon_exactly_one_one(self, list_of_binary_variables):
        self.con(sum(list_of_binary_variables[i] for i in range(len(list_of_binary_variables)))==1)

    def scon_max_one_one(self, list_of_binary_variables):
        self.con(sum(list_of_binary_variables[i] for i in range(len(list_of_binary_variables)))<=1)

    def scon_min_one_one(self, list_of_binary_variables):
        self.con(sum(list_of_binary_variables[i] for i in range(len(list_of_binary_variables)))>=1)

    def scon_exactly_m_one(self, list_of_binary_variables, m):
        self.con(sum(list_of_binary_variables[i] for i in range(len(list_of_binary_variables)))==m)

    def scon_max_m_one(self, list_of_binary_variables, m):
        self.con(sum(list_of_binary_variables[i] for i in range(len(list_of_binary_variables)))<=m)

    def scon_min_m_one(self, list_of_binary_variables, m):
        self.con(sum(list_of_binary_variables[i] for i in range(len(list_of_binary_variables)))>=m)

    def scon_only_one_of_the_values(self, variable, list_of_values):
        try:
            for i in range(len(list_of_values)):
                self.features['indicators'].append(self.features['indicators'][-1]+1)
        except:
            self.features['indicators'] = []
            for i in range(len(list_of_values)):
                self.features['indicators'].append(i)
        z = self.bvar(f"indicator{self.features['indicators'][-1]}",[range(len(list_of_values))])
        self.con(variable==sum(list_of_values[i]*z[i] for i in range(len(list_of_values))))
        self.con(sum(z[i] for i in range(len(list_of_values)))==1)

    def scon_only_one_of_the_values_or_zero(self, variable, list_of_values):
        try:
            for i in range(len(list_of_values)):
                self.features['indicators'].append(self.features['indicators'][-1]+1)
        except:
            self.features['indicators'] = []
            for i in range(len(list_of_values)):
                self.features['indicators'].append(i)
        z = self.bvar(f"indicator{self.features['indicators'][-1]}",[range(len(list_of_values))])
        self.con(variable==sum(list_of_values[i]*z[i] for i in range(len(list_of_values))))
        self.con(sum(z[i] for i in range(len(list_of_values)))<=1)

    def scon_this_depends_on_that(self, this, that):
        self.con(this<=that)

    def scon_this_indeed_that(self, this, that):
        self.con(this<=that)

    def scon_strict_indicator_leq(self,indicator, expr, rhs, big_m=10e9, epsilon=10e-9):
        """
        Either expr<=rhs or expr>rhs should be true (1), using the user-provided indicator (0,1).
        """
        self.con(expr<=rhs+(1-indicator)*big_m)
        self.con(expr>=rhs-indicator*big_m+epsilon)

    def scon_strict_indicator_geq(self,indicator, expr, rhs, big_m=10e9, epsilon=10e-9):
        """
        Either expr>=rhs or expr<rhs should be true (1), using the user-provided indicator (0,1).
        """
        self.con(expr>=rhs-(1-indicator)*big_m)
        self.con(expr<=rhs+indicator*big_m-epsilon)

    def scon_soft_indicator_leq(self,indicator, expr, rhs, big_m=10e9):
        """
        expr<=rhs might be true (1) or not (0).
        """
        self.con(expr<=rhs+(1-indicator)*big_m)

    def scon_soft_indicator_geq(self,indicator, expr, rhs, big_m=10e9):
        """
        expr>=rhs might be true (1) or not (0).
        """
        self.con(expr>=rhs-(1-indicator)*big_m)

    def scon_this_or_that(self,this,rhs_this,that,rhs_that,big_m=10e9):
        """
        Adds two constraints and one indicator variable, to find if this<=rhs_this or that<=rhs_that.
        """
        try:
            self.features['indicators'].append(
                self.features['indicators'][-1]+1)
        except:

            self.features['indicators'] = [0]

        z = self.bvar(f"indicator{self.features['indicators'][-1]}")
        self.con(this<=rhs_this+z*big_m)
        self.con(that<=rhs_that+(1-z)*big_m)

    def scon_if_then(self, this, rhs_this, that, rhs_that, big_m=10e9, epsilon=10e-9):
        """
        Adds two constraints and one indicator variable, to find if this<=rhs_this then that<=rhs_that.
        """

        try:
            self.features['indicators'].append(
                self.features['indicators'][-1]+1)
        except:

            self.features['indicators'] = [0]

        z = self.bvar(f"indicator{self.features['indicators'][-1]}")

        self.con(this >= rhs_this + epsilon - z*big_m)
        self.con(that <= rhs_that + (1-z)*big_m)

    def scon_viol_leq(self,expr,rhs=0):
        """
        
        Returns the amount of violation for soft constraints of type less than or equal (<=).
        
        """
        try:
            self.features['indicators'].append(
                self.features['indicators'][-1]+1)
        except:

            self.features['indicators'] = [0]
        
        z = self.pvar(f"indicator{self.features['indicators'][-1]}")
        self.con(expr<=rhs+z)
        return z
    
    def scon_viol_geq(self,expr,rhs=0):
        """
        Returns the amount of violation for soft constraints of type greater than or equal (>=).
        
        """
        try:
            self.features['indicators'].append(
                self.features['indicators'][-1]+1)
        except:

            self.features['indicators'] = [0]
        
        z = self.pvar(f"indicator{self.features['indicators'][-1]}")
        self.con(expr>=rhs-z)
        return z 
    
    def scon_slack_leq(self,expr,rhs=0):
        try:
            self.features['indicators'].append(
                self.features['indicators'][-1]+1)
        except:

            self.features['indicators'] = [0]
        
        z = self.pvar(f"indicator{self.features['indicators'][-1]}")
        self.con(expr+z==rhs)
        return z 

    def scon_surplus_leq(self,expr,rhs=0):
        try:
            self.features['indicators'].append(
                self.features['indicators'][-1]+1)
        except:

            self.features['indicators'] = [0]
        
        z = self.pvar(f"indicator{self.features['indicators'][-1]}")
        self.con(expr-z==rhs)
        return z

    def lin_piecewise(self, slopes, intercepts, breakpoints):

        try:
            for i in range(len(breakpoints)):
                self.features['indicators'].append(self.features['indicators'][-1]+1)
        except:
            self.features['indicators'] = []
            for i in range(len(breakpoints)):
                self.features['indicators'].append(0)

        x = self.pvar(f"indicatorr{self.features['indicators'][-1]}",[range(len(breakpoints))])
        y = self.bvar(f"indicatorr{self.features['indicators'][-1]}",[range(len(breakpoints))])
        for i in range(len(breakpoints)):
            if i!=len(breakpoints)-1:
                self.scon_in_bound(x[i], lb= (breakpoints[i+1]-breakpoints[i])*y[i], ub=(breakpoints[i+1]-breakpoints[i])*y[i])

        return sum(slopes[i]*x[i]+intercepts[i] for i in range(len(breakpoints)-1))

    def scon_in_bound(self, expr, lb=None, ub=None, label=None):
        """
        Creates upper and/or lower bounds on the given variable in the optimization model.
        """
        if lb is not None:
            self.con(expr >= lb, label=label)
        if ub is not None:
            self.con(expr <= ub, label=label)

    def scon_abs_leq(self, expr, rhs):
        """
        Linearizes a constraint like |a| <= b.
        """

        self.con(expr >= -1*rhs)
        self.con(expr <= rhs)

    def scon_lin_abs_geq(self, expr, rhs, big_m=10e9):
        """
        Linearizes a constraint like |a| >= b.
        """

        try:
            self.features['abs_geq_linearizers'].append(
                self.features['abs_geq_linearizers'][-1]+1)
        except:
            self.features['abs_geq_linearizers'] = [0]

        z = self.bvar(
            f"abs_geq_linearizer{self.features['abs_geq_linearizers'][-1]}")
        
        self.scon_this_or_that()

        self.con(expr >= rhs-z*big_m)
        self.con(expr <= -1*rhs+(1-z)*big_m)

    def lin_abs_in_obj(self, expr, method=0, dir_obj=None):
        """
        Linearizes an |a| expression inside the objective function.

        * method 0: +2 pvars and +1 constraint (for min and max)
        * method 1: +1 pvar and + 2 constraints (+1 bvar for max) (for min or max, requires user input)
        * method 2: +1 pvar and +1 constraint (only for min, does not require user input)
        """

        if method == 0:
            try:
                self.features['abs_obj_linearizers'].append(
                    self.features['abs_obj_linearizers'][-1]+1)
                self.features['abs_obj_linearizers'].append(
                    self.features['abs_obj_linearizers'][-1]+1)
            except:
                self.features['abs_obj_linearizers'] = [0, 1]
            z1 = self.pvar(
                f"abs_obj_linearizer{self.features['abs_obj_linearizers'][-1]}")
            z2 = self.pvar(
                f"abs_obj_linearizer{self.features['abs_obj_linearizers'][-2]}")
            self.con(expr == z1-z2)
            return z1+z2

        if method == 1:
            if dir_obj == 'min':
                try:
                    self.features['abs_obj_linearizers'].append(
                        self.features['abs_obj_linearizers'][-1]+1)
                except:
                    self.features['abs_obj_linearizers'] = [0]
                z = self.pvar(
                    f"abs_obj_linearizer{self.features['abs_obj_linearizers'][-1]}")
                self.scon_abs_leq(expr, z)
                return z
            if dir_obj == 'max':
                try:
                    self.features['abs_obj_linearizers'].append(
                        self.features['abs_obj_linearizers'][-1]+1)
                except:
                    self.features['abs_obj_linearizers'] = [0]
                z = self.pvar(
                    f"abs_obj_linearizer{self.features['abs_obj_linearizers'][-1]}")
                self.scon_abs_geq(expr, z)
                return z

        if method == 2:
            try:
                self.features['abs_obj_linearizers'].append(
                    self.features['abs_obj_linearizers'][-1]+1)
            except:
                self.features['abs_obj_linearizers'] = [0]
            z = self.pvar(
                f"abs_obj_linearizer{self.features['abs_obj_linearizers'][-1]}")
            self.con(expr+z >= 0)
            return expr + 2*z

    def lin_max(self, input_list, type_max, ub_max):
        """
        Linearizes the max function.
        """
        if self.features['solution_method'] == 'exact':

            try:
                self.features['max_linearizers'].append(
                    self.features['max_linearizers'][-1]+1)
            except:
                self.features['max_linearizers'] = [0]

            if type_max == 'bvar':
                z = self.bvar(
                    f"max_linearizer{self.features['max_linearizers'][-1]}")
            if type_max == 'ivar':
                z = self.ivar(
                    f"max_linearizer{self.features['max_linearizers'][-1]}")
            if type_max == 'pvar':
                z = self.pvar(
                    f"max_linearizer{self.features['max_linearizers'][-1]}")
            if type_max == 'fvar':
                z = self.fvar(
                    f"max_linearizer{self.features['max_linearizers'][-1]}")

            for item in input_list:
                self.con(z >= item)
            if ub_max != None:
                self.con(z <= ub_max)
            return z

    def lin_min(self, input_list, type_min, lb_min=None):
        """
        Linearizes the min function.
        """
        try:
            self.features['min_linearizers'].append(
                self.features['min_linearizers'][-1]+1)
        except:
            self.features['min_linearizers'] = [0]

        if type_min == 'bvar':
            z = self.bvar(
                f"min_linearizer{self.features['min_linearizers'][-1]}")
        elif type_min == 'ivar':
            z = self.ivar(
                f"min_linearizer{self.features['min_linearizers'][-1]}")
        elif type_min == 'pvar':
            z = self.pvar(
                f"min_linearizer{self.features['min_linearizers'][-1]}")
        elif type_min == 'fvar':
            z = self.fvar(
                f"min_linearizer{self.features['min_linearizers'][-1]}")

        for item in input_list:
            self.con(z <= item)
        if lb_min != None:
            self.con(z >= lb_min)
        return z

    def lin_prod_bb(self, binary1, binary2):
        """
        Linearizes a Binary * Binary product.

        constraints: +3
        positive variables: +1
        """

        try:
            self.features['bb_linearizers'].append(
                self.features['bb_linearizers'][-1]+1)
        except:

            self.features['bb_linearizers'] = [0]

        z = self.pvar(f"bb_linearizer{self.features['bb_linearizers'][-1]}")
        self.con(z <= binary1)
        self.con(z <= binary2)
        self.con(z >= binary1 + binary2 - 1)
        return z

    def lin_prod_bp(self, binary, positive, ub_positive=10e9):
        """
        Linearizes a Binary * Positive product.

        constraints: +3
        positive variables: +1
        """
        try:
            self.features['bp_linearizers'].append(
                self.features['bp_linearizers'][-1]+1)
        except:
            self.features['bp_linearizers'] = [0]

        z = self.pvar(f"bp_linearizer{self.features['bp_linearizers'][-1]}")
        self.con(z <= positive)
        self.con(z <= binary*ub_positive)
        self.con(z >= positive - ub_positive*(1-binary))
        return z

    def lin_prod_bi(self, binary, integer, ub_integer=10e9):
        """
        Linearizes a Binary * Integer product.

        constraints: +3
        positive variables: +1
        """
        try:
            self.features['bi_linearizers'].append(
                self.features['bi_linearizers'][-1]+1)
        except:
            self.features['bi_linearizers'] = [0]

        z = self.pvar(f"bi_linearizer{self.features['bi_linearizers'][-1]}")
        self.con(z <= integer)
        self.con(z <= binary*ub_integer)
        self.con(z >= integer - ub_integer*(1-binary))
        return z

    def lin_prod_ip(self, integer, positive, ub_integer, ub_positive):
        """
        Linearizes a Integer * Positive product.

        constraints: +1+3*(mt.ceil(mt.log2(ub_integer + 1)))
        positive variables: +(mt.ceil(mt.log2(ub_integer + 1)))
        binary variables: +(mt.ceil(mt.log2(ub_integer + 1)))
        """

        try:
            self.features['ip_linearizers'].append(
                self.features['ip_linearizers'][-1]+1)
        except:
            self.features['ip_linearizers'] = [0]

        z = self.pvar(f"ip_linearizer{self.features['ip_linearizers'][-1]}", [
                      range(mt.ceil(mt.log2(ub_integer + 1)))])
        x = self.bvar(f"ip_binary_convert{self.features['ip_linearizers'][-1]}", [
                      range(mt.ceil(mt.log2(ub_integer + 1)))])

        self.con(integer == sum(
            2**i * x[i] for i in range(mt.ceil(mt.log2(ub_integer + 1)))))

        for i in range(mt.ceil(mt.log2(ub_integer + 1))):

            self.con(z[i] <= positive)
            self.con(z[i] <= x[i]*ub_positive)
            self.con(z[i] >= positive - ub_positive*(1-x[i]))

        return sum(2**i * z[i] for i in range(mt.ceil(mt.log2(ub_integer + 1))))

    def lin_prod_ii(self, integer1, integer2, ub_integer1, ub_integer2):
        """
        Linearizes a Integer * Integer product.

        constraints: +1+3*(mt.ceil(mt.log2(ub_integer + 1)))
        positive variables: +(mt.ceil(mt.log2(ub_integer + 1)))
        binary variables: +(mt.ceil(mt.log2(ub_integer + 1)))
        """
        try:
            self.features['ii_linearizers'].append(
                self.features['ii_linearizers'][-1]+1)
        except:
            self.features['ii_linearizers'] = [0]

        z = self.pvar(f"ii_linearizer{self.features['ii_linearizers'][-1]}", [
                      range(mt.ceil(mt.log2(ub_integer1 + 1)))])
        x = self.bvar(f"ii_binary_convert{self.features['ii_linearizers'][-1]}", [
                      range(mt.ceil(mt.log2(ub_integer1 + 1)))])

        self.con(integer1 == sum(
            2**i * x[i] for i in range(mt.ceil(mt.log2(ub_integer1 + 1)))))

        for i in range(mt.ceil(mt.log2(ub_integer1 + 1))):

            self.con(z[i] <= integer2)
            self.con(z[i] <= x[i]*ub_integer2)
            self.con(z[i] >= integer2 - ub_integer2*(1-x[i]))

        return sum(2**i * z[i] for i in range(mt.ceil(mt.log2(ub_integer1 + 1))))

    # Methods for constraint programming

    def start_of(self, interval_variable, absent_value=None):
        """

        Returns the start of an interval_variable. 
        If it was absent, the absent_value is returned, which is by default equal to 0.

        """

        if self.features['interface_name'] == 'cplex_cp':
            return self.model.start_of(interval_variable, absent_value)
        if self.features['interface_name'] == 'ortools_cp':
            return interval_variable.StartExpr()

    def end_of(self, interval_variable, absent_value=None):
        """
        Returns the end of an interval_variable. 
        If it was absent, the absent_value is returned, which is by default equal to 0.
        """

        if self.features['interface_name'] == 'cplex_cp':
            return self.model.end_of(interval_variable, absent_value)
        if self.features['interface_name'] == 'ortools_cp':
            return interval_variable.EndExpr()

    def length_of(self, interval_variable, absent_value=None):
        """

        Returns the length of an interval_variable. 
        If it was absent, the absent_value is returned, which is by default equal to 0.

        """

        if self.features['interface_name'] == 'cplex_cp':
            return self.model.length_of(interval_variable, absent_value)
        if self.features['interface_name'] == 'ortools_cp':
            return interval_variable.EndExpr() - interval_variable.StartExpr()

    def size_of(self, interval_variable, absent_value=None):
        """

        Returns the size of an interval_variable. 
        If it was absent, the absent_value is returned, which is by default equal to 0.

        """

        if self.features['interface_name'] == 'cplex_cp':
            return self.model.size_of(interval_variable, absent_value)
        if self.features['interface_name'] == 'ortools_cp':
            return interval_variable.SizeExpr()

    def presence_of(self, interval_variable):
        """

        Returns the presence (1) or absence (0) of an interval_variable. 
        Can be used for assignments.

        """
        if self.features['interface_name'] == 'cplex_cp':

            return self.model.presence_of(interval_variable)

        if self.features['interface_name'] == 'ortools_cp':

            return 1

    def prec_start_at_start(self, one, two, delay=None):
        """
        start(one) + delay == start(two)
        """

        if self.features['interface_name'] == 'cplex_cp':
            return self.model.start_at_start(one, two, delay)
        if self.features['interface_name'] == 'ortools_cp':
            return one.StartExpr() + delay == two.StartExpr()

    def prec_start_at_end(self, one, two, delay=None):
        """
        start(one) + delay == end(two)
        """

        if self.features['interface_name'] == 'cplex_cp':
            return self.model.start_at_end(one, two, delay)
        if self.features['interface_name'] == 'ortools_cp':
            return one.StartExpr() + delay == two.EndExpr()

    def prec_start_before_start(self, one, two, delay=None):
        """
        start(one) + delay <= start(two)
        """

        if self.features['interface_name'] == 'cplex_cp':
            return self.model.start_before_start(one, two, delay)
        if self.features['interface_name'] == 'ortools_cp':
            return one.StartExpr() + delay <= two.StartExpr()

    def prec_start_before_end(self, one, two, delay=None):
        """
        start(one) + delay <= end(two)
        """

        if self.features['interface_name'] == 'cplex_cp':
            return self.model.start_before_end(one, two, delay)
        if self.features['interface_name'] == 'ortools_cp':
            return one.StartExpr() + delay <= two.EndExpr()

    def prec_end_at_start(self, one, two, delay=None):
        """
        end(one) + delay == start(two)
        """

        if self.features['interface_name'] == 'cplex_cp':
            return self.model.end_at_start(one, two, delay)
        if self.features['interface_name'] == 'ortools_cp':
            return one.EndExpr() + delay == two.StartExpr()

    def prec_end_at_end(self, one, two, delay=None):
        """
        end(one) + delay == end(two)
        """

        if self.features['interface_name'] == 'cplex_cp':
            return self.model.end_at_end(one, two, delay)
        if self.features['interface_name'] == 'ortools_cp':
            return one.EndExpr() + delay == two.EndExpr()

    def prec_end_before_start(self, one, two, delay=None):
        """
        end(one) + delay <= start(two)
        """

        if self.features['interface_name'] == 'cplex_cp':
            return self.model.end_before_start(one, two, delay)
        if self.features['interface_name'] == 'ortools_cp':
            return one.EndExpr() + delay <= two.StartExpr()

    def prec_end_before_end(self, one, two, delay=None):
        """
        end(one) + delay <= end(two)
        """

        if self.features['interface_name'] == 'cplex_cp':
            return self.model.end_before_end(one, two, delay)
        if self.features['interface_name'] == 'ortools_cp':
            return one.EndExpr() + delay <= two.EndExpr()

    def forbid_start(self, interval, function):
        """

        Forbids an interval variable to start during specified regions.

        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.forbid_start(interval, function)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def forbid_end(self, interval, function):
        """

        Forbids an interval variable to end during specified regions.

        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.forbid_end(interval, function)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def forbid_overlap(self, interval_variables, transition_matrix=None):
        """

        Forbids overlapping of interval variables.

        """

        if self.features['interface_name'] == 'cplex_cp':

            if transition_matrix == None:

                return self.model.no_overlap(interval_variables)

            else:

                return self.model.no_overlap(interval_variables, transition_matrix)

        if self.features['interface_name'] == 'ortools_cp':

            return self.model.AddNoOverlap(interval_variables)

    def forbid_extent(self, interval, function):
        """

        Forbid an interval variable to overlap with specified regions.

        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.forbid_extent(interval, function)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def overlap_length(self, interval_variable1, interval_variable2, absent_value=None):
        """
        To get the length of the overlap of two interval variables.
        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.overlap_length(interval_variable1, interval_variable2, absent_value)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def start_eval(self, interval, function, absent_value=None):
        """
        To evaluate a segmented function at the start of an interval variable
        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.start_eval(interval, function, absent_value)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def end_eval(self, interval, function, absent_value=None):
        """
        To evaluate a segmented function at the end of an interval variable
        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.end_eval(interval, function, absent_value)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def size_eval(self, interval, function, absent_value=None):
        """
        To evaluate a segmented function on the size of an interval variable
        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.size_eval(interval, function, absent_value)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def length_eval(self, interval, function, absent_value=None):
        """
        To evaluate a segmented function on the length of an interval variable
        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.length_eval(interval, function, absent_value)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def span(self, interval, function, absent_value=None):
        """
        Forces that one interval variable must exactly cover a set of interval variables.
        """

        if self.features['interface_name'] == 'cplex_cp':
            return self.model.span(interval, function, absent_value)
        if self.features['interface_name'] == 'ortools_cp':

            ""

    def always_equal(self, state_fucntion, input1, input2):
        """

        Creates an equality constraint between two expressions.

        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.always_equal(state_fucntion, input1, input2)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def alternative(self, interval, array, cardinality=None):
        """
        Create an alternative constraint between interval variables.
        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.alternative(interval, array, cardinality)

        if self.features['interface_name'] == 'ortools_cp':

            ""

    def all_dist_above(self, exprs, value):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.all_min_distance(exprs, value)

        else:

            return abs(exprs) >= value

    def sum(self, input):

        return self.model.sum(input)

    def if_then(self, input1, input2):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.if_then(input1, input2)

        else:

            if input1:

                return input2

    def control_resource(self, *args, function='pulse'):
        """
        Creates and returns a dynamic resource usage control function.

        A cumulative function expression can be modified with the atomic demand functions:

        function = 'step', change resource level by a given amount at a given time.
        function = 'pulse', change resource level by a given amount based on the length of a given interval variable or fixed interval.
        function = 'start', change resource level by a given amount based on the start of a given interval variable.
        function = 'end', change resource level by by a given amount at the end of a given interval variable.
        """

        if function == 'pulse':
            return self.model.pulse(*args)
        if function == 'step':
            return self.model.step(*args)
        if function == 'start':
            return self.model.step_at_start(*args)
        if function == 'end':
            return self.model.step_at_end(*args)

    # Methods for modeling and solving.

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

    def sol(self, directions=None, solver_name=None, solver_options=dict(), objective_id=0, email=None, debug=False, time_limit=None, cpu_threads=None, absolute_gap=None, relative_gap=None, show_log=False, save_log=False, save_model=False, max_iterations=None, obj_operators=[]):
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

        if len(directions)<len(self.features['objectives']):
            raise MultiObjectivityError("The number of directions and the provided objectives do not match.")

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
        self.features['obj_operators'] = obj_operators

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

        else:

            for i in range(len(self.features['directions'])):

                self.features['directions'][i] = directions[i]

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

                            self.agent[:, -1] = 0

                            total_obj = self.features['objective_counter'][0]

                            self.features['objectives'] = np.array(
                                self.features['objectives']).T[0]

                            for i in range(self.features['objective_counter'][0]):

                                if directions[i] == 'max':
                                    self.agent[:, -2-total_obj+i] = self.features['objectives'][:,
                                                                                                i] - self.features['penalty_coefficient'] * (self.penalty)**2

                                if directions[i] == 'min':
                                    self.agent[:, -2-total_obj+i] = self.features['objectives'][:,
                                                                                                i] + self.features['penalty_coefficient'] * (self.penalty)**2

                    else:

                        self.penalty = 0

                        if len(self.features['constraints']) >= 1:

                            self.penalty = np.amax(
                                np.array([0]+self.features['constraints'], dtype=object))

                        if type(objective_id) != str:

                            if directions[objective_id] == 'max':
                                self.response = self.features['objectives'][objective_id] - \
                                    self.features['penalty_coefficient'] * \
                                    (self.penalty-0)**2

                            if directions[objective_id] == 'min':
                                self.response = self.features['objectives'][objective_id] + \
                                    self.features['penalty_coefficient'] * \
                                    (self.penalty-0)**2

                        else:

                            total_obj = self.features['objective_counter'][0]

                            self.response = [None for i in range(total_obj)]

                            for i in range(total_obj):

                                if directions[i] == 'max':

                                    self.response[i] = self.features['objectives'][i] - \
                                        self.features['penalty_coefficient'] * \
                                        (self.penalty)**2

                                if directions[i] == 'min':

                                    self.response[i] = self.features['objectives'][i] + \
                                        self.features['penalty_coefficient'] * \
                                        (self.penalty)**2

    def get_variable(self, variable_with_index):
        from .generators import result_generator
        return result_generator.get(self.features, self.model, self.solution, 'variable', variable_with_index)

    def get_dual(self, constraint_label_with_index):
        from .generators import result_generator
        return result_generator.get(self.features, self.model, self.solution, 'dual', constraint_label_with_index)

    def get_slack(self, constraint_label_with_index):
        from .generators import result_generator
        return result_generator.get(self.features, self.model, self.solution, 'slack', constraint_label_with_index)
    
    def get_objective(self):
        from .generators import result_generator
        return result_generator.get(self.features, self.model, self.solution, 'objective', None)

    def get_status(self):
        from .generators import result_generator
        return result_generator.get(self.features, self.model, self.solution, 'status', None)

    def get_time(self):
        from .generators import result_generator
        return result_generator.get(self.features, self.model, self.solution, 'time', None)

    def get_start(self, invterval_variable):

        if self.features['interface_name'] == 'cplex_cp':
            return self.solution[0].get_var_solution(invterval_variable).get_start()
        if self.features['interface_name'] == 'ortools_cp':
            ""

    def get_interval(self, invterval_variable):

        if self.features['interface_name'] == 'cplex_cp':
            return self.solution[0].get_var_solution(invterval_variable)
        if self.features['interface_name'] == 'ortools_cp':
            ""

    def get_end(self, invterval_variable):

        if self.features['interface_name'] == 'cplex_cp':
            return self.solution[0].get_var_solution(invterval_variable).get_end()
        if self.features['interface_name'] == 'ortools_cp':
            ""

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

    def scen_probs(self):
        """
        Returns an array of scenario probabilities
        """
        if self.features['interface_name'] in ['rsome_ro', 'rsome_dro']:
            return self.model.p

    def exval(self,expr):

        """
        Expected Value
        --------------
        1) Returns the expected value of random variables if the uncertainty set of expectations is being determined.
        2) Returns the worst case expected values of an expression that has random variables inside.

        """
        if self.features['interface_name'] in ['rsome_ro', 'rsome_dro']:
            from rsome import E
            return E(expr)

    def norm(self,expr_or_1D_array_of_variables, degree):
        """
        Returns the first, second, or infinity norm of a 1-D array.
        """

        if self.features['interface_name'] in ['rsome_ro', 'rsome_dro']:
            from rsome import norm
            return norm(expr_or_1D_array_of_variables, degree)
    
    def sumsqr(self,expr_or_1D_array_of_variables):


        if self.features['interface_name'] in ['rsome_ro', 'rsome_dro']:
        
            from rsome import sumsqr
            return sumsqr(expr_or_1D_array_of_variables)
    

    def state_function(self):
        """

        Creates and returns a state function.

        """

        return self.model.state_function()

    def report(self, show_all_metrics=False):
        print()

        self.InterfaceName = self.features['interface_name']
        self.SolutionMethod = self.features['solution_method']
        self.ModelName = self.features['model_name']
        self.SolverName = self.features['solver_name']
        self.ModelConstraints = self.features['constraints']
        self.ModelObjectives = self.features['objectives']
        self.ObjectivesDirections = self.features['directions']
        self.PositiveVariableCounter = self.features['positive_variable_counter']
        self.BinaryVariableCounter = self.features['binary_variable_counter']
        self.IntegerVariableCounter = self.features['integer_variable_counter']
        self.FreeVariableCounter = self.features['free_variable_counter']
        self.ToTalVariableCounter = self.features['total_variable_counter']
        self.ConstraintsCounter = self.features['constraint_counter']
        self.ObjectivesCounter = self.features['objective_counter']

        import datetime
        now = datetime.datetime.now()
        date_str = now.strftime("Date: %Y-%m-%d")
        time_str = now.strftime("Time: %H:%M:%S")

        box_width = 80
        padding = box_width - len(date_str) - len(time_str) - 2

        print("+" + "-"*box_width + "+")
        print("|" + " " + "FelooPy v0.2.5".center(box_width-2) + " " + "|")
        print("+" + "-"*box_width + "+")
        print("| " + date_str + " "*padding + time_str + " |")
        padding = box_width - len("Solver: "+ self.SolverName) - len("Interface: "+ self.InterfaceName) - 2
        print("| " + "Interface: " + self.InterfaceName + " "*padding + "Solver: "+ self.SolverName + " |")
        print("+" + "-"*box_width + "+")
        print("|" + " " + "Model Information".center(box_width-2) + " " + "|")
        print("+" + "-"*box_width + "+")

        self.ModelName, self.InterfaceName, self.SolverName, self.ObjectivesDirections, self.SolutionMethod
        # determine the maximum length of variables
        ModelName = "The '" + self.ModelName + "' model has:"
        print("|" + " " + ModelName.center(box_width-2) + " " + "|")
        if self.PositiveVariableCounter[0]>0:
            P_report = str(self.PositiveVariableCounter[1]) + " positive variable(s) in " + str(self.PositiveVariableCounter[0]) + " class(es)."
            print("|" + " " + P_report.center(box_width-2) + " " + "|")
        if self.BinaryVariableCounter[0]>0:
            P_report = str(self.BinaryVariableCounter[1]) + " binary variable(s) in " + str(self.BinaryVariableCounter[0]) + " class(es)."
            print("|" + " " + P_report.center(box_width-2) + " " + "|")
        if self.IntegerVariableCounter[0]>0:
            P_report = str(self.IntegerVariableCounter[1]) + " integer variable(s) in " + str(self.IntegerVariableCounter[0]) + " class(es)."
            print("|" + " " + P_report.center(box_width-2) + " " + "|")
        if self.FreeVariableCounter[0]>0:
            P_report = str(self.FreeVariableCounter[1]) + " free variable(s) in " + str(self.FreeVariableCounter[0]) + " class(es)."
            print("|" + " " + P_report.center(box_width-2) + " " + "|")
        if self.ObjectivesCounter[0]>0:
            P_report = str(self.ObjectivesCounter[1]) + " objective(s)."
            print("|" + " " + P_report.center(box_width-2) + " " + "|")
        if self.ConstraintsCounter[0]>0:
            P_report = str(self.ConstraintsCounter[1]) + " constraint(s) in " + str(self.ConstraintsCounter[0]) + " class(es)."
            print("|" + " " + P_report.center(box_width-2) + " " + "|")
        P_report =  "Total number of variables is " + str(self.ToTalVariableCounter[1]) + f" in {self.ToTalVariableCounter[0]} class(es)."
        print("|" + " " + P_report.center(box_width-2) + " " + "|")


        print("+" + "-"*box_width + "+")
        print("|" + " " + "Solve Information".center(box_width-2) + " " + "|")
        print("+" + "-"*box_width + "+")
        padding = box_width - len("Method: "+ self.SolutionMethod) - len("Objective Value(s)") - 2
        print("| " + "Method: "+ self.SolutionMethod + " "*padding + "Objective Value(s)" + " |")
        status= self.get_status()
        if len(self.ObjectivesDirections)!=1:
            row = "| " + "Status: " + " "*(len(status[0]) - len("Status: ")) + " " * (box_width-9*len(self.ObjectivesDirections) +1 - len(str(status[0])) - 3)
            for j in range(len(self.ObjectivesDirections)):
                obj_row = self.ObjectivesDirections[j]
                row += " " * (8 - len(obj_row)) + obj_row
            print(row + " |")
            for i in range(len(status)): 
                row = "| " + str(status[i]) + " " * (box_width-9*len(self.ObjectivesDirections) +1 - len(str(status[i])) - 3)
                obj_row = self.get_obj()[i]
                for j in range(len(obj_row)):
                    num_str = format_string(obj_row[j])
                    row += " " * (9 - len(num_str)) + num_str
                print(row + " |")
        else:
            row = "| " + "Status: " + " "*(len(status) - len("Status: ")) + " " * (box_width-9*len(self.ObjectivesDirections) +1 - len(str(status)) - 3)
            for j in range(len(self.ObjectivesDirections)):
                obj_row = self.ObjectivesDirections[j]
                row += " " * (8 - len(obj_row)) + obj_row
            print(row + " |")
            row = "| " + str(status) + " " * (box_width-9*len(self.ObjectivesDirections) +1 - len(str(status)) - 3)
            obj_row = self.get_obj()
            num_str = format_string(obj_row)
            row += " " * (9 - len(num_str)) + num_str
            print(row + " |")
        print("+" + "-"*box_width + "+")
        print("|" + " " + "Metric Information".center(box_width-2) + " " + "|")
        print("+" + "-"*box_width + "+")
        hour = round((self.get_time()), 3) % (24 * 3600) // 3600
        min = round((self.get_time()), 3) % (24 * 3600) % 3600 // 60
        sec = round((self.get_time()), 3) % (24 * 3600) % 3600 % 60

    
        if len(self.ObjectivesDirections)!=1:
            if show_all_metrics:
                try:
                    try:
                        self.get_indicators()
                        print("| CPT   (microseconds): ", format_string(self.get_time()*10**6) + " "*(box_width-len("| CPT   (microseconds): " + format_string(self.get_time()*10**6))) + "|")
                        print("| CPT   (hour:min:sec): ", "%02d:%02d:%02d" % (hour, min, sec)+ " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| GD    (min):          ", format_string(self.calculated_indicators['gd'])+ " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| GDP   (min):          ", format_string(self.calculated_indicators['gdp'])+ " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| IGD   (min):          ", format_string(self.calculated_indicators['igd'])+ " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| IGDP  (min):          ", format_string(self.calculated_indicators['igdp'])+ " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| MS    (max):          ", format_string(self.calculated_indicators['ms']) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| SP    (max):          ", format_string(self.calculated_indicators['sp']) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| HV    (max):          ", format_string(self.calculated_indicators['hv']) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                    except:
                        print("| CPT   (microseconds): ", format_string(self.get_time()*10**6) + " "*(box_width-len("| CPT   (microseconds): " + format_string(self.get_time()*10**6))) + "|")
                        print("| GD    (min):          ", format_string(self.calculated_indicators['gd']) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| GDP   (min):          ", format_string(self.calculated_indicators['gdp']) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| IGD   (min):          ", format_string(self.calculated_indicators['igd']) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| IGDP  (min):          ", format_string(self.calculated_indicators['igdp']) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| MS    (max):          ", format_string(self.calculated_indicators['ms']) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| SP    (max):          ", format_string(self.calculated_indicators['sp']) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                except:
                    print("| CPT   (microseconds): ", format_string(self.get_time()*10**6) + " "*(box_width-len("| CPT   (microseconds): " + format_string(self.get_time()*10**6))) + "|")
                    print("| CPT   (hour:min:sec): ", "%02d:%02d:%02d" % (hour, min, sec) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
            else:
                print("| CPT   (microseconds): ", format_string(self.get_time()*10**6) + " "*(box_width-len("| CPT   (microseconds): " + format_string(self.get_time()*10**6))) + "|")
                print("| CPT   (hour:min:sec): ", "%02d:%02d:%02d" % (hour, min, sec) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")     
        else:
            print("| CPT   (microseconds): ", format_string((self.get_time())*10 **6) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
            print("| CPT   (hour:min:sec): ", "%02d:%02d:%02d" % (hour, min, sec) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")     
        print("+" + "-"*box_width + "+")
        print("|" + " " + "Decision Information".center(box_width-2) + " " + "|")
        print("+" + "-"*box_width + "+")
        for i,j in self.mainvars.keys():
            if self.maindims[j] == 0:
                if self.get(self.mainvars[(i,j)]) not in [0, None]:
                    print(f"| {j} =", self.get(self.mainvars[(i,j)]), " "* (box_width-(len(f"| {j} =") + len(str(self.get(self.mainvars[(i,j)]))))-1) + "|")
            elif len(self.maindims[j])==1:
                try:
                    for k in fix_dims(self.maindims[j])[0]:
                        if self.get(self.mainvars[(i,j)][k]) not in [0, None]:
                            print(f"| {j}[{k}] =", self.get(self.mainvars[(i,j)][k]), " "* (box_width-(len(f"| {j}[{k}] =") + len(str(self.get(self.mainvars[(i,j)][k])))) - 1) + "|")
                except:
                    for k in fix_dims(self.maindims[j])[0]:
                        if self.get(self.mainvars[(i,j)])[k] not in [0, None]:
                            print(f"| {j}[{k}] =", self.get(self.mainvars[(i,j)])[k], " "* (box_width-(len(f"| {j}[{k}] =") + len(str(self.get(self.mainvars[(i,j)])[k]))) - 1) + "|")
            else:
                try:
                    for k in it.product(*tuple(fix_dims(self.maindims[j]))):
                        if self.get(self.mainvars[(i,j)][k]) not in [0, None]:
                            print(f"| {j}[{k}] =".replace("(", "").replace(")", ""), self.get(self.mainvars[(i,j)][k]), " "* (box_width-(len(f"| {j}[{k}] =".replace("(", "").replace(")", "")) + len(str(self.get(self.mainvars[(i,j)][k])))) - 1) + "|")
                except:
                    for k in it.product(*tuple(fix_dims(self.maindims[j]))):
                        if self.get(self.mainvars[(i,j)])[k] not in [0, None]:
                            print(f"| {j}[{k}] =".replace("(", "").replace(")", ""), self.get(self.mainvars[(i,j)])[k], " "* (box_width-(len(f"| {j}[{k}] =".replace("(", "").replace(")", "")) + len(str(self.get(self.mainvars[(i,j)])[k]))) - 1) + "|")

        print("+" + "-"*box_width + "+")

    # Methods to work with input and output data.

    def max(self, *args):

        if self.features['interface_name'] == 'cplex_cp':
            return self.model.max(*args)

    def set(self, *size):
        """
        Set Definition
        ~~~~~~~~~~~~~~
        To define a set.
        """

        return range(*size)

    def ambiguity_set(self,*args,**kwds):
        """
        Ambiguity set defintion
        """
        return self.model.ambiguity(*args,**kwds)

    def card(self, set):
        """
        Card Definition
        ~~~~~~~~~~~~~~~~
        To measure size of the set, etc.
        """

        return len(set)

    def uniform(self, lb, ub, parameter_dim=0):
        """
        Uniform Parameter Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        To generate a real-valued parameter using uniform distribution inside a range.
        """

        dim = fix_dims(parameter_dim)

        if dim == 0:
            return self.random.uniform(low=lb, high=ub)
        else:
            return self.random.uniform(low=lb, high=ub, size=([len(i) for i in dim]))

    def uniformint(self, lb, ub, parameter_dim=0):
        """
        Uniform Integer Parameter Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        To generate an integer parameter using uniform distribution inside a range.
        """

        dim = fix_dims(parameter_dim)

        if dim == 0:
            return self.random.integers(low=lb, high=ub)
        else:
            return self.random.integers(low=lb, high=ub+1, size=([len(i) for i in dim]))

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
        
        elif self.features['interface_name'] in ['rsome_ro', 'rsome_dro']:
            from rsome import square
            return square(input)
        
        else:
            return input * input

    def quad(self,expr_or_1D_array_of_variables, positive_or_negative_semidefinite_matrix):

        if self.features['interface_name'] in ['rsome_ro', 'rsome_dro']:
            from rsome import quad
            return quad(expr_or_1D_array_of_variables,positive_or_negative_semidefinite_matrix)

    def expcone(self,rhs,a,b):
        """
        Returns an exponential cone constraint in the form: b*exp(a/b) <= rhs.

        Args
        rhs : array of variables or affine expression
        a : Scalar.
        b : Scalar.
        """

        if self.features['interface_name'] in ['rsome_ro', 'rsome_dro']:
            from rsome import expcone
            return expcone(rhs,a,b)

    def power(self, input1, input2):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.power(input1, input2)

        else:

            return input1 ** input2


    def kldive(self, input, emprical_rpob, ambiguity_constant):

        """
        Returns KL divergence
        
        input: an 1D array of variables, an affine expression, or probabilities. 
        emprical_rpob: an 1D array of emprical probabilities.
        ambiguity_constant: Ambiguity constant.
        """

        if self.features['interface_name'] in ['rsome_ro', 'rsome_dro']:
            from rsome import kldiv
            return kldiv(input, emprical_rpob, ambiguity_constant)

    def entropy(self, input):

        """
        Returns an entropy expression like sum(input*log(input))
        """

        if self.features['interface_name'] in ['rsome_ro', 'rsome_dro']:

            from rsome import entropy
            return entropy(input)
    


    def log(self, input):
        """

        Natural Logarithm

        """

        if self.features['interface_name'] in ['cplex_cp']:

            return self.model.log(input)

        elif self.features['interface_name'] in ['gekko']:

            return self.model.log(input)
        
        elif self.features['interface_name'] in ['rsome_ro', 'rsome_dro']:

            from rsome import log
            return log(input)

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
        
        elif self.features['interface_name'] in ['rsome_ro', 'rsome_dro']:

            from rsome import exp
            return exp(input)
    
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

    # Methods to visualize data.

    def show_gantt(interval_variables, names, colors='lightblue'):

        import docplex.cp.utils_visu as visu
        import matplotlib.pyplot as plt

        counter = 0
        for i in interval_variables:
            visu.interval(i, colors[counter], names[counter])
            counter += 1
        visu.show()

# Alternatives for defining this class:


model = mdl = add_model = create_environment = env = feloopy = representor_model = learner_model = target_model = optimizer = Model

warnings.simplefilter(action='ignore', category=FutureWarning)


class Implement:

    def __init__(self, ModelFunction):
        '''
        Creates and returns an implementor for the representor model.
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

            case 'pymultiobjective':

                self.ModelObject = None

            case 'feloopy':

                from .generators.model import feloopy_model_generator
                self.ModelObject = feloopy_model_generator.generate_model(
                    self.ToTalVariableCounter[1], self.ObjectivesDirections, self.SolverName, self.AlgOptions)

    def remove_infeasible_solutions(self):

        self.BestAgent = np.delete(self.BestAgent, self.remove, axis=0)
        self.BestReward = np.delete(self.BestReward, self.remove, axis=0)

    def sol(self, penalty_coefficient=0, number_of_times=1, show_plots=False, save_plots=False):

        self.penalty_coefficient = penalty_coefficient

        match self.InterfaceName:

            case 'mealpy':

                from .generators.solution import mealpy_solution_generator
                self.BestAgent, self.BestReward, self.start, self.end = mealpy_solution_generator.generate_solution(
                    self.ModelObject, self.Fitness, self.ToTalVariableCounter, self.ObjectivesDirections, self.ObjectiveBeingOptimized, number_of_times, show_plots, save_plots)

            case 'pymultiobjective':

                from .generators.solution import pymultiobjective_solution_generator
                self.BestAgent, self.BestReward, self.start, self.end = pymultiobjective_solution_generator.generate_solution(
                    self.SolverName, self.AlgOptions, self.Fitness, self.ToTalVariableCounter, self.ObjectivesDirections, self.ObjectiveBeingOptimized, number_of_times, show_plots, save_plots)
                self.remove = []
                for i in range(np.shape(self.BestReward)[0]):

                    if 'infeasible' in self.Check_Fitness(self.BestAgent[i]):

                        self.remove.append(i)

                if len(self.remove) != 0:
                    self.remove_infeasible_solutions()

            case 'feloopy':

                from .generators.solution import feloopy_solution_generator
                self.BestAgent, self.BestReward, self.start, self.end, self.status = feloopy_solution_generator.generate_solution(
                    self.ModelObject, self.Fitness, self.ToTalVariableCounter, self.ObjectivesDirections, self.ObjectiveBeingOptimized, number_of_times, show_plots)

    def dis_plots(self, ideal_pareto: Optional[np.ndarray] = [], step: Optional[tuple] = (0.1,)):

        """
        Calculates selected Pareto front metrics and displays the results in a tabulated format.

        :param ideal_pareto: An array of shape (n_samples, n_objectives) containing the ideal Pareto front. Default is None.
        """

        obtained_pareto = self.BestReward

        from pyMultiobjective.util import graphs
        ObjectivesDirections = [-1 if direction =='max' else 1 for direction in self.ObjectivesDirections]
        def f1(X): return ObjectivesDirections[0]*self.Fitness(np.array(X))[0]
        def f2(X): return ObjectivesDirections[1]*self.Fitness(np.array(X))[1]
        def f3(X): return ObjectivesDirections[2]*self.Fitness(np.array(X))[2]
        def f4(X): return ObjectivesDirections[3]*self.Fitness(np.array(X))[3]
        def f5(X): return ObjectivesDirections[4]*self.Fitness(np.array(X))[4]
        def f6(X): return ObjectivesDirections[5]*self.Fitness(np.array(X))[5]
        my_list_of_functions = [f1, f2, f3, f4, f5, f6]
        parameters = dict()
        list_of_functions = []
        for i in range(len(ObjectivesDirections)): list_of_functions.append(my_list_of_functions[i])
        
        solution = np.concatenate((self.BestAgent, self.BestReward*ObjectivesDirections), axis=1)
    
        parameters = {
        'min_values': (0,)*self.ToTalVariableCounter[1],
        'max_values': (1,)*self.ToTalVariableCounter[1],
        'step': step*self.ToTalVariableCounter[1],
        'solution': solution, 
        'show_pf': True,
        'show_pts': True,
        'show_sol': True,
        'pf_min': True, 
        'custom_pf': ideal_pareto*ObjectivesDirections if type(ideal_pareto) == np.ndarray else [],
        'view': 'browser'
        }
        graphs.plot_mooa_function(list_of_functions = list_of_functions, **parameters)

        parameters = {
            'min_values': (0,)*self.ToTalVariableCounter[1],
            'max_values': (1,)*self.ToTalVariableCounter[1],
            'step': step*self.ToTalVariableCounter[1],
            'solution': solution, 
            'show_pf': True,
            'pf_min': True,  
            'custom_pf': ideal_pareto*ObjectivesDirections if type(ideal_pareto) == np.ndarray else [],
            'view': 'browser'
        }
        graphs.parallel_plot(list_of_functions = list_of_functions, **parameters)

    def dis_status(self):
        print('status:', self.get_status())

    def get_status(self):

        if self.InterfaceName in ['mealpy', 'pymultiobjective']:

            if self.InterfaceName == 'mealpy':

                return self.Check_Fitness(self.BestAgent)

            else:
                status = []
                for i in range(np.shape(self.BestReward)[0]):
                    status.append(self.Check_Fitness(self.BestAgent[i]))

                return status

        else:
            if self.status[0] == 1:
                return 'feasible (constrained)'
            elif self.status[0] == 2:
                return 'feasible (unconstrained)'
            elif self.status[0] == -1:
                return 'infeasible'

    def Check_Fitness(self, X):

        self.AgentProperties[0] = 'feasibility_check'
        self.AgentProperties[1] = X
        self.AgentProperties[2] = self.VariablesSpread
        self.AgentProperties[3] = self.penalty_coefficient

        return self.ModelFunction(self.AgentProperties)

    def Fitness(self, X):

        self.AgentProperties[0] = 'active'
        self.AgentProperties[1] = X
        self.AgentProperties[2] = self.VariablesSpread
        self.AgentProperties[3] = self.penalty_coefficient

        return self.ModelFunction(self.AgentProperties)

    def evaluate(self, show_fig=True, save_fig=False, file_name=None, dpi=800, fig_size=(18, 4), opt=None, opt_features=None, pareto=None, abs_tol=0.001, rel_tol=0.001):

        import matplotlib.pyplot as plt

        fig = plt.figure(figsize=fig_size)

        m = self.ModelObject.epsiode

        no_epochs = self.AlgOptions['epoch']
        no_episodes = self.AlgOptions['episode']

        max_epoch_time = []
        for epoch in range(0, no_epochs):
            episode_time = []
            for episode in range(0, no_episodes):
                episode_time.append(m[episode]['epoch_time'][epoch])
            max_epoch_time.append(np.max(episode_time))
        max_epoch_time = np.array(max_epoch_time)

        min_epoch_time = []
        for epoch in range(0, no_epochs):
            episode_time = []
            for episode in range(0, no_episodes):
                episode_time.append(m[episode]['epoch_time'][epoch])
            min_epoch_time.append(np.min(episode_time))
        min_epoch_time = np.array(min_epoch_time)

        ave_epoch_time = []
        for epoch in range(0, no_epochs):
            episode_time = []
            for episode in range(0, no_episodes):
                episode_time.append(m[episode]['epoch_time'][epoch])
            ave_epoch_time.append(np.average(episode_time))
        ave_epoch_time = np.array(ave_epoch_time)

        std_epoch_time = []
        for epoch in range(0, no_epochs):
            episode_time = []
            for episode in range(0, no_episodes):
                episode_time.append(m[episode]['epoch_time'][epoch])
            std_epoch_time.append(np.std(episode_time))
        std_epoch_time = np.array(std_epoch_time)

        axs = fig.add_subplot(1, 5, 5)
        x = np.arange(no_epochs)
        axs.plot(x, max_epoch_time, 'blue', alpha=0.4)
        axs.plot(x, ave_epoch_time, 'blue', alpha=0.8)
        axs.plot(x, min_epoch_time, 'blue', alpha=0.4)
        axs.fill_between(x, ave_epoch_time - std_epoch_time,
                         ave_epoch_time + std_epoch_time, color='blue', alpha=0.3)
        axs.set_xlabel('Epoch')
        axs.set_ylabel('Time (second)')
        axs.set_xlim(-0.5, no_epochs-1+0.5)

        max_epoch_obj = []
        for epoch in range(0, no_epochs):
            max_episode_obj = []
            for episode in range(0, no_episodes):
                max_episode_obj.append(
                    np.max(m[episode]['epoch_solutions'][epoch][:, -1]))
            max_epoch_obj.append(np.max(max_episode_obj))
        max_epoch_obj = np.array(max_epoch_obj)

        min_epoch_obj = []
        for epoch in range(0, no_epochs):
            max_episode_obj = []
            for episode in range(0, no_episodes):
                max_episode_obj.append(
                    np.max(m[episode]['epoch_solutions'][epoch][:, -1]))
            min_epoch_obj.append(np.min(max_episode_obj))
        min_epoch_obj = np.array(min_epoch_obj)

        ave_epoch_obj = []
        for epoch in range(0, no_epochs):
            max_episode_obj = []
            for episode in range(0, no_episodes):
                max_episode_obj.append(
                    np.max(m[episode]['epoch_solutions'][epoch][:, -1]))
            ave_epoch_obj.append(np.average(max_episode_obj))
        ave_epoch_obj = np.array(ave_epoch_obj)

        std_epoch_obj = []
        for epoch in range(0, no_epochs):
            max_episode_obj = []
            for episode in range(0, no_episodes):
                max_episode_obj.append(
                    np.max(m[episode]['epoch_solutions'][epoch][:, -1]))
            std_epoch_obj.append(np.std(max_episode_obj))
        std_epoch_obj = np.array(std_epoch_obj)

        axs = fig.add_subplot(1, 5, 4)
        x = np.arange(no_epochs)
        if self.ObjectivesDirections[self.ObjectiveBeingOptimized] == 'max':
            axs.plot(x, max_epoch_obj, 'green', alpha=0.4)
            axs.plot(x, ave_epoch_obj, 'green', alpha=0.8)
            axs.plot(x, min_epoch_obj, 'green', alpha=0.4)
            axs.fill_between(x, ave_epoch_obj - std_epoch_obj,
                             ave_epoch_obj + std_epoch_obj, color='green', alpha=0.3)
        else:
            axs.plot(x, max_epoch_obj, 'red', alpha=0.4)
            axs.plot(x, ave_epoch_obj, 'red', alpha=0.8)
            axs.plot(x, min_epoch_obj, 'red', alpha=0.4)

            axs.fill_between(x, ave_epoch_obj - std_epoch_obj,
                             ave_epoch_obj + std_epoch_obj, color='red', alpha=0.3)
        axs.set_xlabel('Epoch')
        if self.ObjectivesDirections[self.ObjectiveBeingOptimized] == 'max':
            axs.set_ylabel('Maximum reward')
        else:
            axs.set_ylabel('Maximum loss')
        axs.set_xlim(-0.5, no_epochs-1+0.5)

        max_epoch_obj = []
        for epoch in range(0, no_epochs):
            max_episode_obj = []
            for episode in range(0, no_episodes):
                max_episode_obj.append(np.average(
                    m[episode]['epoch_solutions'][epoch][:, -1]))
            max_epoch_obj.append(np.max(max_episode_obj))
        max_epoch_obj = np.array(max_epoch_obj)

        min_epoch_obj = []
        for epoch in range(0, no_epochs):
            max_episode_obj = []
            for episode in range(0, no_episodes):
                max_episode_obj.append(np.average(
                    m[episode]['epoch_solutions'][epoch][:, -1]))
            min_epoch_obj.append(np.min(max_episode_obj))
        min_epoch_obj = np.array(min_epoch_obj)

        ave_epoch_obj = []
        for epoch in range(0, no_epochs):
            max_episode_obj = []
            for episode in range(0, no_episodes):
                max_episode_obj.append(np.average(
                    m[episode]['epoch_solutions'][epoch][:, -1]))
            ave_epoch_obj.append(np.average(max_episode_obj))
        ave_epoch_obj = np.array(ave_epoch_obj)

        std_epoch_obj = []
        for epoch in range(0, no_epochs):
            max_episode_obj = []
            for episode in range(0, no_episodes):
                max_episode_obj.append(np.average(
                    m[episode]['epoch_solutions'][epoch][:, -1]))
            std_epoch_obj.append(np.std(max_episode_obj))
        std_epoch_obj = np.array(std_epoch_obj)

        axs = fig.add_subplot(1, 5, 3)
        x = np.arange(no_epochs)
        axs.plot(x, max_epoch_obj, 'orange', alpha=0.4)
        axs.plot(x, ave_epoch_obj, 'orange', alpha=0.8)
        axs.plot(x, min_epoch_obj, 'orange', alpha=0.4)
        axs.fill_between(x, ave_epoch_obj - std_epoch_obj,
                         ave_epoch_obj + std_epoch_obj, color='orange', alpha=0.3)
        axs.set_xlabel('Epoch')
        if self.ObjectivesDirections[self.ObjectiveBeingOptimized] == 'max':
            axs.set_ylabel('Average reward')
        else:
            axs.set_ylabel('Average loss')
        axs.set_xlim(-0.5, no_epochs-1+0.5)

        max_epoch_obj = []
        for epoch in range(0, no_epochs):
            max_episode_obj = []
            for episode in range(0, no_episodes):
                max_episode_obj.append(
                    np.min(m[episode]['epoch_solutions'][epoch][:, -1]))
            max_epoch_obj.append(np.max(max_episode_obj))
        max_epoch_obj = np.array(max_epoch_obj)

        min_epoch_obj = []
        for epoch in range(0, no_epochs):
            max_episode_obj = []
            for episode in range(0, no_episodes):
                max_episode_obj.append(
                    np.min(m[episode]['epoch_solutions'][epoch][:, -1]))
            min_epoch_obj.append(np.min(max_episode_obj))
        min_epoch_obj = np.array(min_epoch_obj)

        ave_epoch_obj = []
        for epoch in range(0, no_epochs):
            max_episode_obj = []
            for episode in range(0, no_episodes):
                max_episode_obj.append(
                    np.min(m[episode]['epoch_solutions'][epoch][:, -1]))
            ave_epoch_obj.append(np.average(max_episode_obj))
        ave_epoch_obj = np.array(ave_epoch_obj)

        std_epoch_obj = []
        for epoch in range(0, no_epochs):
            max_episode_obj = []
            for episode in range(0, no_episodes):
                max_episode_obj.append(
                    np.min(m[episode]['epoch_solutions'][epoch][:, -1]))
            std_epoch_obj.append(np.std(max_episode_obj))
        std_epoch_obj = np.array(std_epoch_obj)

        axs = fig.add_subplot(1, 5, 2)
        x = np.arange(no_epochs)
        if self.ObjectivesDirections[self.ObjectiveBeingOptimized] == 'max':
            axs.plot(x, max_epoch_obj, 'red', alpha=0.4)
            axs.plot(x, ave_epoch_obj, 'red', alpha=0.8)
            axs.plot(x, min_epoch_obj, 'red', alpha=0.4)
            axs.fill_between(x, ave_epoch_obj - std_epoch_obj,
                             ave_epoch_obj + std_epoch_obj, color='red', alpha=0.3)
        else:
            axs.plot(x, max_epoch_obj, 'green', alpha=0.4)
            axs.plot(x, ave_epoch_obj, 'green', alpha=0.8)
            axs.plot(x, min_epoch_obj, 'green', alpha=0.4)
            axs.fill_between(x, ave_epoch_obj - std_epoch_obj,
                             ave_epoch_obj + std_epoch_obj, color='green', alpha=0.3)
        axs.set_xlabel('Epoch')
        axs.set_xlim(-0.5, no_epochs-1+0.5)
        if self.ObjectivesDirections[self.ObjectiveBeingOptimized] == 'max':
            axs.set_ylabel('Minimum reward')
        else:
            axs.set_ylabel('Minimum loss')

        if self.ObjectivesDirections[self.ObjectiveBeingOptimized] == 'min':
            best_min_min = np.inf
            best_min_min_t = []
            best_sol_t = []
            best_per_episode = []
            no_features = self.ToTalVariableCounter[1]
            for epoch in range(0, no_epochs):
                best_min = []
                best_sol = []
                for episode in range(0, no_episodes):
                    best_min.append(
                        np.min(m[episode]['epoch_solutions'][epoch][:, -1]))
                    best_sol.append(m[episode]['epoch_solutions'][epoch][np.argmin(
                        m[episode]['epoch_solutions'][epoch][:, -1]), :])
                    best_track = np.min(best_min)
                    for x in best_sol:
                        if x[-1] == best_track:
                            best_sol_found = x[:no_features]
                if best_track <= best_min_min:
                    best_min_min = best_track
                    best_min_min_t.append(best_track)
                    if no_features == 1:
                        best_sol_t.append(best_sol_found[0])
                    if no_features == 2:
                        best_sol_t.append(
                            [best_sol_found[0], best_sol_found[1]])
                    else:
                        best_sol_t.append(
                            [best_sol_found[0], best_sol_found[1], best_sol_found[2]])
                else:
                    best_min_min_t.append(best_min_min)
                    best_sol_t.append(best_sol_t[-1])

                    if epoch == no_epochs-1:
                        best_per_episode.append(best_track)

            best_min_min_t = np.array(best_min_min_t)
        else:
            best_min_min = -np.inf
            best_min_min_t = []
            best_sol_t = []
            best_per_episode = []
            no_features = self.ToTalVariableCounter[1]
            for epoch in range(0, no_epochs):
                best_min = []
                best_sol = []
                for episode in range(0, no_episodes):
                    best_min.append(
                        np.max(m[episode]['epoch_solutions'][epoch][:, -1]))
                    best_sol.append(m[episode]['epoch_solutions'][epoch][np.argmax(
                        m[episode]['epoch_solutions'][epoch][:, -1]), :])
                    best_track = np.max(best_min)
                    for x in best_sol:
                        if x[-1] == best_track:
                            best_sol_found = x[:no_features]
                if best_track >= best_min_min:
                    best_min_min = best_track
                    best_min_min_t.append(best_track)
                    if no_features == 1:
                        best_sol_t.append(best_sol_found[0])
                    if no_features == 2:
                        best_sol_t.append(
                            [best_sol_found[0], best_sol_found[1]])
                    else:
                        best_sol_t.append(
                            [best_sol_found[0], best_sol_found[1], best_sol_found[2]])
                else:
                    best_min_min_t.append(best_min_min)
                    best_sol_t.append(best_sol_t[-1])

                    if epoch == no_epochs-1:
                        best_per_episode.append(best_track)

            best_min_min_t = np.array(best_min_min_t)

        if no_features == 1:
            axs = fig.add_subplot(1, 5, 1)
            axs.plot(np.arange(no_epochs), best_sol_t, c='black', lw=1)
            if opt_features != None:
                axs.scatter(np.arange(no_epochs),
                            opt_features[0], c='black', marker='*', lw=1)

            axs.set_ylim(-0.5, 1.5)
            axs.set_xlim(-0.5, no_epochs-1+0.5)
            axs.set_xlabel('Epoch')
            axs.set_ylabel('Feature')

        if no_features == 2:
            axs = fig.add_subplot(1, 5, 1)
            from matplotlib.patches import Rectangle
            for i in range(0, no_epochs):
                hg = 0.1+i/(no_epochs)
                axs.scatter(best_sol_t[i][0], best_sol_t[i]
                            [1], c='black', lw=1, alpha=hg)
            if opt_features != None:
                axs.scatter(opt_features[0], opt_features[1],
                            c='black', marker='*', lw=1)

            axs.add_patch(Rectangle((0, 0), 1, 1, fill=None, alpha=1))

            axs.set_ylim(-0.5, 1.5)
            axs.set_xlim(-0.5, 1.5)
            axs.set_xlabel('Feature 1')
            axs.set_ylabel('Feature 2')

        if no_features == 3:
            axs = fig.add_subplot(1, 5, 1, projection='3d')
            for i in range(0, no_epochs):
                hg = 0.1+i/(no_epochs)
                axs.scatter(best_sol_t[i][0], best_sol_t[i][1],
                            best_sol_t[i][2], lw=1, alpha=hg, color='black')
            if opt_features != None:
                axs.scatter(opt_features[0], opt_features[1],
                            opt_features[2], c='red', marker='*', lw=1)
            axs.set_xlabel('Feature 1')
            axs.set_ylabel('Feature 2')
            axs.set_zlabel('Feature 3')
            axs.set_ylim(-0.5, 1.5)
            axs.set_xlim(-0.5, 1.5)
            axs.set_zlim(-0.5, 1.5)

            axs.view_init(azim=30)

        if no_features <= 2:
            plt.subplots_adjust(left=0.071, bottom=0.217,
                                right=0.943, top=0.886, wspace=0.35, hspace=0.207)
        else:
            plt.subplots_adjust(left=0.03, bottom=0.252,
                                right=0.945, top=0.886, wspace=0.421, hspace=0.22)

        if save_fig:
            if file_name == None:
                plt.savefig('evaluation_results.png', dpi=dpi)
            else:
                plt.savefig(file_name, dpi=dpi)

        if show_fig:
            plt.show()

        obj = []
        time = []
        for episode in range(0, no_episodes):
            obj.append(m[episode]['best_single'][0][-1])
            time.append(m[episode]['episode_time'][0])

        opt = np.array([opt])
        if opt != 0:
            accuracy = (1-np.abs(opt-best_min_min_t)/opt)*100
        else:
            opt = opt + 1
            best_min_min_t = best_min_min_t+1
            accuracy = (1-np.abs(opt-best_min_min_t)/opt)*100
            accuracy[np.where(accuracy < 0)] = 0

        from math import isclose

        opt = np.array([opt])
        prob_per_epoch = []

        findbest = np.zeros(shape=(no_episodes, no_epochs))

        if self.ObjectivesDirections[self.ObjectiveBeingOptimized] == 'min':
            for episode in range(0, no_episodes):
                episode_tracker = []
                best = np.inf
                for epoch in range(0, no_epochs):
                    if np.min(m[episode]['epoch_solutions'][epoch][:, -1]) <= best:
                        best = np.min(
                            m[episode]['epoch_solutions'][epoch][:, -1])
                        episode_tracker.append(
                            np.min(m[episode]['epoch_solutions'][epoch][:, -1]))
                    else:
                        episode_tracker.append(best)
                for epoch in range(0, no_epochs):
                    if opt == 0:
                        if isclose(episode_tracker[epoch], opt, abs_tol=abs_tol):
                            findbest[episode, epoch] = 1
                    else:
                        if isclose(episode_tracker[epoch], opt, rel_tol=rel_tol):
                            findbest[episode, epoch] = 1
        else:
            for episode in range(0, no_episodes):
                episode_tracker = []
                best = -np.inf
                for epoch in range(0, no_epochs):
                    if np.max(m[episode]['epoch_solutions'][epoch][:, -1]) >= best:
                        best = np.max(
                            m[episode]['epoch_solutions'][epoch][:, -1])
                        episode_tracker.append(
                            np.max(m[episode]['epoch_solutions'][epoch][:, -1]))
                    else:
                        episode_tracker.append(best)
                for epoch in range(0, no_epochs):
                    if opt == 0:
                        if isclose(episode_tracker[epoch], opt, abs_tol=abs_tol, rel_tol=rel_tol):
                            findbest[episode, epoch] = 1
                    else:
                        if isclose(episode_tracker[epoch], opt, abs_tol=abs_tol, rel_tol=rel_tol):
                            findbest[episode, epoch] = 1

        # abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

        prob_per_epoch = [sum(findbest[episode, epoch] for episode in range(
            0, no_episodes))/no_episodes for epoch in range(0, no_epochs)]

        return [obj, time, accuracy, prob_per_epoch]

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
                                return np.round(self.VariablesBound[i[0]][0] + self.BestAgent[:, self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))

                            else:
                                def var(*args):
                                    self.NewAgentProperties = np.round(self.VariablesBound[i[0]][0] + self.BestAgent[:, self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (
                                        self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                                    return self.NewAgentProperties[sum(args[k]*mt.prod(len(self.VariablesDim[i[0]][j]) for j in range(k+1, len(self.VariablesDim[i[0]]))) for k in range(len(self.VariablesDim[i[0]])))]

                                return var(*i[1])
                        case 'ivar':
                            if self.VariablesDim[i[0]] == 0:
                                return np.round(self.VariablesBound[i[0]][0] + self.BestAgent[:, self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                            else:
                                def var(*args):
                                    self.NewAgentProperties = np.round(self.VariablesBound[i[0]][0] + self.BestAgent[:, self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (
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
                            return np.round(self.VariablesBound[i[0]][0] + self.BestAgent[:, self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]] * (self.VariablesBound[i[0]][1] - self.VariablesBound[i[0]][0]))
                        case 'svar':
                            return np.argsort(self.BestAgent[:, self.VariablesSpread[i[0]][0]:self.VariablesSpread[i[0]][1]])


    def dis_indicators(self, ideal_pareto: Optional[np.ndarray] = [], ideal_point: Optional[np.array] = [], step: Optional[tuple] = (0.1,), epsilon: float = 0.01, p: float = 2.0, n_clusters: int = 5, save_path: Optional[str] = None, show_log: Optional[bool] = False):

        """
        Calculates selected Pareto front metrics and displays the results in a tabulated format.

        :param ideal_pareto: An array of shape (n_samples, n_objectives) containing the ideal Pareto front. Default is None.
        :param epsilon: A float value for the epsilon value used in the epsilon metric. Default is 0.01.
        :param p: A float value for the power parameter used in the weighted generational distance and weighted inverted generational distance metrics. Default is 2.0.
        :param n_clusters: An integer value for the number of clusters used in the knee point distance metric. Default is 5.
        :param save_path: A string value for the path where the results should be saved. Default is None.
        """


        self.get_indicators(ideal_pareto, ideal_point, step, epsilon, p, n_clusters, save_path, show_log = True)

    def get_indicators(self, ideal_pareto: Optional[np.ndarray] = [], ideal_point: Optional[np.array] = [], step: Optional[tuple] = (0.1,), epsilon: float = 0.01, p: float = 2.0, n_clusters: int = 5, save_path: Optional[str] = None, show_log: Optional[bool] = False):

        """
        Calculates selected Pareto front metrics and displays the results in a tabulated format.

        :param ideal_pareto: An array of shape (n_samples, n_objectives) containing the ideal Pareto front. Default is None.
        :param epsilon: A float value for the epsilon value used in the epsilon metric. Default is 0.01.
        :param p: A float value for the power parameter used in the weighted generational distance and weighted inverted generational distance metrics. Default is 2.0.
        :param n_clusters: An integer value for the number of clusters used in the knee point distance metric. Default is 5.
        :param save_path: A string value for the path where the results should be saved. Default is None.
        """

        obtained_pareto = self.BestReward

        from pyMultiobjective.util import indicators
        ObjectivesDirections = [-1 if direction =='max' else 1 for direction in self.ObjectivesDirections]
        def f1(X): return ObjectivesDirections[0]*self.Fitness(np.array(X))[0]
        def f2(X): return ObjectivesDirections[1]*self.Fitness(np.array(X))[1]
        def f3(X): return ObjectivesDirections[2]*self.Fitness(np.array(X))[2]
        def f4(X): return ObjectivesDirections[3]*self.Fitness(np.array(X))[3]
        def f5(X): return ObjectivesDirections[4]*self.Fitness(np.array(X))[4]
        def f6(X): return ObjectivesDirections[5]*self.Fitness(np.array(X))[5]
        my_list_of_functions = [f1, f2, f3, f4, f5, f6]
        parameters = dict()
        list_of_functions = []
        for i in range(len(ObjectivesDirections)): list_of_functions.append(my_list_of_functions[i])
        
        solution = np.concatenate((self.BestAgent, self.BestReward*ObjectivesDirections), axis=1)
    
        parameters = {
            'min_values': (0,)*self.ToTalVariableCounter[1],
            'max_values': (1,)*self.ToTalVariableCounter[1],
            'step': step*self.ToTalVariableCounter[1],
            'solution': solution,
            'pf_min': True,
            'custom_pf': ideal_pareto*ObjectivesDirections if type(ideal_pareto) == np.ndarray else []
        }

        self.calculated_indicators = dict()
        gd = indicators.gd_indicator(list_of_functions=list_of_functions, **parameters)
        gdp = indicators.gd_plus_indicator(list_of_functions=list_of_functions, **parameters)
        igd = indicators.igd_indicator(list_of_functions=list_of_functions, **parameters)
        igdp = indicators.igd_plus_indicator(list_of_functions=list_of_functions, **parameters)
        ms = indicators.ms_indicator(list_of_functions=list_of_functions, **parameters)
        sp = indicators.sp_indicator(list_of_functions=list_of_functions, **parameters)

        self.calculated_indicators['gd'] = gd
        self.calculated_indicators['gdp'] = gdp
        self.calculated_indicators['igd'] = igd
        self.calculated_indicators['igdp'] = igdp
        self.calculated_indicators['ms'] = ms
        self.calculated_indicators['sp'] = sp

        parameters = {
            'solution': solution,
            'n_objs': len(ObjectivesDirections),
            'ref_point': ideal_point,
        }
        
        hypervolume = indicators.hv_indicator(**parameters)
        self.calculated_indicators['hv'] = hypervolume
        metrics = []

        if type(ideal_pareto) == np.ndarray:
            metrics = [
                ('Additive Epsilon Indicator Metric (min) [0, +inf)',metric_pareto_aem(ideal_pareto, obtained_pareto)),
                ('Convergence Metric (min) [0,+inf)', metric_pareto_cvm(obtained_pareto, ideal_pareto)),
                ('Coverage Ratio Metric (max) [0,1]', metric_pareto_crm(ideal_pareto, obtained_pareto)),
                ('Epsilon Metric (max) [0 or 1]', metric_pareto_epm(obtained_pareto, ideal_pareto, epsilon)),
                ('F-Ratio Metric (max) [0,1]', metric_pareto_frm(obtained_pareto, ideal_pareto)),
                ('Generational Distance Metric (min) [0,+inf)', self.calculated_indicators['gd']),
                ('Hyper Volume Metric (max) [0, +inf)', self.calculated_indicators['hv']),
                ('Inverted Generational Distance (min) [0, +inf)', self.calculated_indicators['igd']),
                ('Knee Point Distance Metric (min) [0, +inf)', metric_pareto_kdm(obtained_pareto, ideal_pareto, n_clusters)),
                ('Maximum Pareto Front Error Metric (min) [0, +inf)',metric_pareto_mem(ideal_pareto, obtained_pareto)),
                ('Maximum Spread Metric (max) [0, +inf)', self.calculated_indicators['ms']),
                ('Quantity Metric (max) [0,1]', metric_pareto_qvm(obtained_pareto, ideal_pareto)),
                ('R2 Metric (max) [0,1]', metric_pareto_r2m(obtained_pareto, ideal_pareto)),
                ('Spacing Metric (max) [0,+inf)', self.calculated_indicators['sp']),
                ('Spread Metric (max) [0, +inf)', metric_pareto_rsm(obtained_pareto, ideal_pareto)),
                ('Generational Distance Metric Plus (min) [0, +inf)', self.calculated_indicators['gdp']),
                ('Weighted Inverted Generational Distance Plus (min) [0, +inf)', self.calculated_indicators['igdp'])]
        else:

            metrics = [
                ('Generational Distance Metric (min) [0,+inf)', self.calculated_indicators['gd']),
                ('Hyper Volume Metric (max) [0, +inf)', self.calculated_indicators['hv']),
                ('Inverted Generational Distance (min) [0, +inf)', self.calculated_indicators['igd']),
                ('Maximum Spread Metric (max) [0, +inf)', self.calculated_indicators['ms']),
                ('Spacing Metric (max) [0,+inf)', self.calculated_indicators['sp']),
                ('Generational Distance Metric Plus (min) [0, +inf)', self.calculated_indicators['gdp']),
                ('Inverted Generational Distance Plus (min) [0, +inf)', self.calculated_indicators['igdp'])]

        headers = ['Metric', 'Value']
        results = [[metric[0], metric[1]] for metric in metrics]
        table = tb(results, headers=headers)

        if show_log:
            print(table)

            mean_values = np.mean(self.BestReward, axis=0)
            std_values = np.std(self.BestReward, axis=0)
            min_values = np.min(self.BestReward, axis=0)
            max_values = np.max(self.BestReward, axis=0)

            table_data = [['Objective']+['Mean', 'Standard Deviation', 'Min', 'Max']]
            for i in range(len(ObjectivesDirections)):
                table_data.append([f'Objective {i+1}', mean_values[i], std_values[i], min_values[i], max_values[i]])
            print()
            print(tabulate(table_data, headers='firstrow'))

        if save_path is not None:
            with open(save_path, 'w') as f:
                f.write(table)

        return metrics

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

    def get_payoff(self):

        payoff=[]
        for i in range(len(self.ObjectivesDirections)):
            if self.ObjectivesDirections[i]=='max':
                ind =np.argmax(self.get_obj()[:, i])
                val = self.get_obj()[ind, :]
            elif self.ObjectivesDirections[i] =='min':
                ind = np.argmin(self.get_obj()[:, i])
                val = self.get_obj()[ind, :]
            payoff.append(val)
        return np.array(payoff)

    def report(self, show_all_metrics=False):

        print()

        import datetime
        now = datetime.datetime.now()
        date_str = now.strftime("Date: %Y-%m-%d")
        time_str = now.strftime("Time: %H:%M:%S")

        box_width = 80
        padding = box_width - len(date_str) - len(time_str) - 2

        print("+" + "-"*box_width + "+")
        print("|" + " " + "FelooPy v0.2.5".center(box_width-2) + " " + "|")
        print("+" + "-"*box_width + "+")
        print("| " + date_str + " "*padding + time_str + " |")
        padding = box_width - len("Solver: "+ self.SolverName) - len("Interface: "+ self.InterfaceName) - 2
        print("| " + "Interface: " + self.InterfaceName + " "*padding + "Solver: "+ self.SolverName + " |")
        print("+" + "-"*box_width + "+")
        print("|" + " " + "Model Information".center(box_width-2) + " " + "|")
        print("+" + "-"*box_width + "+")

        self.ModelName, self.InterfaceName, self.SolverName, self.ObjectivesDirections, self.SolutionMethod
        # determine the maximum length of variables
        ModelName = "The '" + self.ModelName + "' model has:"
        print("|" + " " + ModelName.center(box_width-2) + " " + "|")
        if self.PositiveVariableCounter[0]>0:
            P_report = str(self.PositiveVariableCounter[1]) + " positive variable(s) in " + str(self.PositiveVariableCounter[0]) + " class(es)."
            print("|" + " " + P_report.center(box_width-2) + " " + "|")
        if self.BinaryVariableCounter[0]>0:
            P_report = str(self.BinaryVariableCounter[1]) + " binary variable(s) in " + str(self.BinaryVariableCounter[0]) + " class(es)."
            print("|" + " " + P_report.center(box_width-2) + " " + "|")
        if self.IntegerVariableCounter[0]>0:
            P_report = str(self.IntegerVariableCounter[1]) + " integer variable(s) in " + str(self.IntegerVariableCounter[0]) + " class(es)."
            print("|" + " " + P_report.center(box_width-2) + " " + "|")
        if self.FreeVariableCounter[0]>0:
            P_report = str(self.FreeVariableCounter[1]) + " free variable(s) in " + str(self.FreeVariableCounter[0]) + " class(es)."
            print("|" + " " + P_report.center(box_width-2) + " " + "|")
        if self.ObjectivesCounter[0]>0:
            P_report = str(self.ObjectivesCounter[1]) + " objective(s)."
            print("|" + " " + P_report.center(box_width-2) + " " + "|")
        if self.ConstraintsCounter[0]>0:
            P_report = str(self.ConstraintsCounter[1]) + " constraint(s) in " + str(self.ConstraintsCounter[0]) + " class(es)."
            print("|" + " " + P_report.center(box_width-2) + " " + "|")
        P_report =  "Total number of variables is " + str(self.ToTalVariableCounter[1]) + f" in {self.ToTalVariableCounter[0]} class(es)."
        print("|" + " " + P_report.center(box_width-2) + " " + "|")

        print("+" + "-"*box_width + "+")
        print("|" + " " + "Solve Information".center(box_width-2) + " " + "|")
        print("+" + "-"*box_width + "+")
        padding = box_width - len("Method: "+ self.SolutionMethod) - len("Objective Value(s)") - 2
        print("| " + "Method: "+ self.SolutionMethod + " "*padding + "Objective Value(s)" + " |")
        status= self.get_status()
        if len(status)==0: 
            status = ['infeasible (constrained)']
        if len(self.ObjectivesDirections)!=1:
            row = "| " + "Status: " + " "*(len(status[0]) - len("Status: ")) + " " * (box_width-10*len(self.ObjectivesDirections)+1  - len(str(status[0])) - 3)
            for j in range(len(self.ObjectivesDirections)):
                obj_row = self.ObjectivesDirections[j]
                row += " " * (10 - len(obj_row)) + obj_row
            print(row + " |")
            if status[0] != "infeasible (constrained)":
                for i in range(len(status)): 
                    row = "| " + str(status[i]) + " " * (box_width-10*len(self.ObjectivesDirections) +1 - len(str(status[i])) - 3)
                    obj_row = self.get_obj()[i]
                    for j in range(len(obj_row)):
                        num_str = format_string(obj_row[j])
                        row += " " * (10 - len(num_str)) + num_str
                    print(row + " |")
                for j in range(len(self.ObjectivesDirections)):
                    row = "| " + str(f"payoff {j}") + " " * (box_width-10*len(self.ObjectivesDirections) +1 - len(str(f"payoff {j}")) - 3)
                    for k in range(len(self.ObjectivesDirections)):
                        num_str = format_string(self.get_payoff()[j,k])
                        row += " " * (10 - len(num_str)) + num_str
                    print(row + " |")
        else:
            row = "| " + "Status: " + " "*(len(status) - len("Status: ")) + " " * (box_width-9*len(self.ObjectivesDirections) +1 - len(str(status)) - 3)
            for j in range(len(self.ObjectivesDirections)):
                obj_row = self.ObjectivesDirections[j]
                row += " " * (9 - len(obj_row)) + obj_row
            print(row + " |")
            row = "| " + str(status) + " " * (box_width-9*len(self.ObjectivesDirections) +1 - len(str(status)) - 3)
            obj_row = self.get_obj()
            num_str = format_string(obj_row)
            row += " " * (9 - len(num_str)) + num_str
            print(row + " |")
        print("+" + "-"*box_width + "+")
        print("|" + " " + "Metric Information".center(box_width-2) + " " + "|")
        print("+" + "-"*box_width + "+")
        hour = round(((self.end-self.start)), 3) % (24 * 3600) // 3600
        min = round(((self.end-self.start)), 3) % (24 * 3600) % 3600 // 60
        sec = round(((self.end-self.start)), 3) % (24 * 3600) % 3600 % 60
        if len(self.ObjectivesDirections)!=1:
            if show_all_metrics:
                try:
                    try:
                        self.get_indicators()
                        print("| CPT   (microseconds): ", format_string((self.end-self.start)*10 **6) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| CPT   (hour:min:sec): ", "%02d:%02d:%02d" % (hour, min, sec)+ " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| NP    (max):          ", format_string(len((self.get_obj())))+ " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| GD    (min):          ", format_string(self.calculated_indicators['gd'])+ " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| GDP   (min):          ", format_string(self.calculated_indicators['gdp'])+ " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| IGD   (min):          ", format_string(self.calculated_indicators['igd'])+ " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| IGDP  (min):          ", format_string(self.calculated_indicators['igdp'])+ " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        if np.isnan(self.calculated_indicators['ms']):
                            print("| MS    (max):               ", format_string(self.calculated_indicators['ms']) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        else:
                            print("| MS    (max):          ", format_string(self.calculated_indicators['ms']) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| SP    (max):          ", format_string(self.calculated_indicators['sp']) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| HV    (max):          ", format_string(self.calculated_indicators['hv']) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                    except:
                        print("| CPT   (microseconds): ", format_string((self.end-self.start)*10 **6) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| CPT   (hour:min:sec): ", "%02d:%02d:%02d" % (hour, min, sec)+ " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| NP    (max):          ", format_string(len((self.get_obj())))+ " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| GD    (min):          ", format_string(self.calculated_indicators['gd']) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| GDP   (min):          ", format_string(self.calculated_indicators['gdp']) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| IGD   (min):          ", format_string(self.calculated_indicators['igd']) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| IGDP  (min):          ", format_string(self.calculated_indicators['igdp']) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        if np.isnan(self.calculated_indicators['ms']):
                            print("| MS    (max):               ", format_string(self.calculated_indicators['ms']) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        else:
                            print("| MS    (max):          ", format_string(self.calculated_indicators['ms']) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                        print("| SP    (max):          ", format_string(self.calculated_indicators['sp']) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                except:
                    print("| CPT   (microseconds): ", format_string((self.end-self.start)*10 **6) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                    print("| CPT   (hour:min:sec): ", "%02d:%02d:%02d" % (hour, min, sec) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
            else:
                print("| CPT   (microseconds): ", format_string((self.end-self.start)*10 **6) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
                print("| CPT   (hour:min:sec): ", "%02d:%02d:%02d" % (hour, min, sec) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")     
        else:
            print("| CPT   (microseconds): ", format_string((self.end-self.start)*10 **6) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")
            print("| CPT   (hour:min:sec): ", "%02d:%02d:%02d" % (hour, min, sec) + " "*(box_width-len("| CPT   (micro-sec):    ")-8) + "|")     
        print("+" + "-"*box_width + "+")
        if type(status) == str:
            print("|" + " " + "Decision Information".center(box_width-2) + " " + "|")
            print("+" + "-"*box_width + "+")
            for i in self.VariablesDim.keys():
                if self.VariablesDim[i] == 0:
                    if self.get([i,(0,)])!=0:
                        print(f"| {i} =", self.get([i,(0,)]), " "* (box_width-(len(f"| {i} =") + len(str(self.get([i,(0,)])))) -1) + "|")
                elif len(self.VariablesDim[i])==1:
                    for k in fix_dims(self.VariablesDim[i])[0]:
                        if self.get([i,(k,)])!=0:
                            print(f"| {i}[{k}] =", self.get([i,(k,)]), " "* (box_width-(len(f"| {i}[{k}] =") + len(str(self.get([i,(k,)])))) - 1) + "|")
                else:
                    for k in it.product(*tuple(fix_dims(self.VariablesDim[i]))):
                        if self.get([i,(*k,)])!=0:
                            print(f"| {i}[{k}] =".replace("(", "").replace(")", ""), self.get([i,(*k,)]), " "* (box_width-(len(f"| {i}[{k}] =".replace("(", "").replace(")", "")) + len(str(self.get([i,(*k,)])))) - 1) + "|")
            print("+" + "-"*box_width + "+")

        
# Alternatives for defining this class:
            
construct = make_model = implementor = implement = Implement



