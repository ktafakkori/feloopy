import warnings
import itertools as it
import math as mt
import numpy as np
from tabulate import tabulate as tb
import sys

product = mt.prod


class EMPTY:

    '''
    A class to manage variables in the heuristic optimization process.
    '''

    def __init__(self, val):

        self.val = val

    def __call__(self, *args):

        return 5

    def __getitem__(self, *args):

        return 5

    def __setitem__(self, *args):
        'none'

    def __hash__(self):

        return 5

    def __str__(self):

        return 5

    def __repr__(self):

        return 5

    def __neg__(self):

        return 5

    def __pos__(self):

        return 5

    def __pow__(self, other):

        return 5

    def __bool__(self):

        return 5

    def __add__(self, other):

        return 5

    def __radd__(self, other):

        return 5

    def __sub__(self, other):

        return 5

    def __rsub__(self, other):

        return 5

    def __mul__(self, other):

        return 5

    def __rmul__(self, other):

        return 5

    def __div__(self, other):

        return 5

    def __rdiv__(self, other):

        raise 5

    def __le__(self, other):

        return 5

    def __ge__(self, other):

        return 5

    def __eq__(self, other):

        return 5

    def __ne__(self, other):

        return 5

def sets(*args):    

    """ 
    Used to mimic 'for all' in mathamatical modeling, for multiple sets.

    Arguments:

        * Multiple sets separated by commas.
        * Required

    Example: `for i,j in sets(I,J):`
    
    """

    return it.product(*args)


def count_variable(variable_dim, total_count, special_count):
    """ For calculating total number of variables of each category.
    """
    total_count[0] += 1
    special_count[0] += 1
    special_count[1] += 1 if variable_dim == 0 else product(
        len(dims) for dims in variable_dim)
    total_count[1] += 1 if variable_dim == 0 else product(
        len(dims) for dims in variable_dim)
    return total_count, special_count


def create_random_number_generator(key):
    """ For creating a random number generator with a fixed special seed.
    """
    return np.random.default_rng(key)


def update_variable_features(name, variable_dim, variable_bound, variable_counter_type, features):
    """ For hierarchical updating the features of the problem.
    """
    match features['solution_method']:

        case 'exact':

            features['total_variable_counter'], features['variable_counter_type'] = count_variable(
                variable_dim, features['total_variable_counter'], features[variable_counter_type])

        case 'heuristic':

            if features['agent_status'] == 'idle':

                features['variable_spread'][name] = [
                    features['total_variable_counter'][1], 0]
                features['total_variable_counter'], features[variable_counter_type] = count_variable(
                    variable_dim, features['total_variable_counter'], features[variable_counter_type])
                features['variable_spread'][name][1] = features['total_variable_counter'][1]
                if variable_counter_type == 'free_variable_counter':
                    features['variable_type'][name] = 'fvar'
                if variable_counter_type == 'binary_variable_counter':
                    features['variable_type'][name] = 'bvar'
                if variable_counter_type == 'integer_variable_counter':
                    features['variable_type'][name] = 'ivar'
                if variable_counter_type == 'positive_variable_counter':
                    features['variable_type'][name] = 'pvar'
                features['variable_bound'][name] = variable_bound
                features['variable_dim'][name] = variable_dim

    return features


def generate_heuristic_variable(features, type, name, variable_dim, variable_bound, agent):

    if features['agent_status'] == 'idle':
        if features['vectorized']:
            if variable_dim == 0:
                return EMPTY(0)
            else:
                return np.random.rand(*tuple([100]+[len(dims) for dims in variable_dim]))
        else:
            if variable_dim == 0:
                return EMPTY(0)
            else:
                return np.random.rand(*tuple([len(dims) for dims in variable_dim]))
    else:
        spread = features['variable_spread'][name]

        if features['vectorized']:
            if variable_dim == 0:
                if type == 'bvar' or type == 'ivar':
                    return np.round(variable_bound[0] + agent[:, spread[0]:spread[1]] * (variable_bound[1] - variable_bound[0]))
                elif type == 'pvar' or type == 'fvar':
                    return variable_bound[0] + agent[:, spread[0]:spread[1]] * (variable_bound[1] - variable_bound[0])
                else:
                    return np.argsort(agent[:, spread[name][0]:spread[name][1]])
            else:
                if type == 'bvar' or type == 'ivar':
                    var = np.round(
                        variable_bound[0] + agent[:, spread[0]:spread[1]] * (variable_bound[1] - variable_bound[0]))
                    return np.reshape(var, [var.shape[0]]+[len(dims) for dims in variable_dim])
                elif type == 'pvar' or type == 'fvar':
                    var = variable_bound[0] + agent[:, spread[0]:spread[1]
                                                    ] * (variable_bound[1] - variable_bound[0])
                    return np.reshape(var, [var.shape[0]]+[len(dims) for dims in variable_dim])
                else:
                    return np.argsort(agent[:, spread[name][0]:spread[name][1]])
        else:
            if variable_dim == 1:
                if type == 'bvar' or type == 'ivar':
                    return np.round(variable_bound[0] + agent[spread[0]:spread[1]] * (variable_bound[1] - variable_bound[0]))
                elif type == 'pvar' or type == 'fvar':
                    return variable_bound[0] + agent[spread[0]:spread[1]] * (variable_bound[1] - variable_bound[0])
                else:
                    return np.argsort(agent[spread[name][0]:spread[name][1]])
            else:
                if type == 'bvar' or type == 'ivar':
                    return np.reshape(np.round(variable_bound[0] + agent[spread[0]:spread[1]] * (variable_bound[1] - variable_bound[0])), [len(dims) for dims in variable_dim])
                elif type == 'pvar' or type == 'fvar':
                    return np.reshape(variable_bound[0] + agent[spread[0]:spread[1]] * (variable_bound[1] - variable_bound[0]), [len(dims) for dims in variable_dim])
                else:
                    return np.argsort(agent[spread[name][0]:spread[name][1]])


class Model:

    def __init__(self, solution_method, model_name, interface_name, agent=None, key=None):
        """ 
        Environment Definition
        ~~~~~~~~~~~~~~~~~~~~~~
        To define the modeling environment.

        Args:
            solution_method (str): what is your desired solution (optimization) method?
            model_name (str): what is your Model name?
            interface_name (str): what is the interface name?
            agent (X, optional): if you are using a heuristic optimization method, provide the input of the function here. Defaults to None.
            key (number, optional): what is your desired key for random number generator?. Defaults to None.

        Examples:
            * m = Model('exact', 'tsp', 'ortools', None, None)
            * m = Model('exact', 'tsp', 'ortools', key=0)
            * def instance(X): m = Model('heuristic', 'tsp', 'feloopy', X)
            * def instance(X): m = Model('heuristic', 'tsp', 'feloopy', X, 0)
        """

        self.binary_variable = self.add_binary_variable = self.bvar
        self.positive_variable = self.add_positive_variable = self.pvar
        self.integer_variable = self.add_integer_variable = self.ivar
        self.free_variable = self.add_free_variable = self.fvar
        self.sequential_variable = self.add_sequential_variable = self.svar
        self.dependent_variable = self.add_dependent_variable = self.dvar
        self.objective = self.add_objective = self.obj
        self.constraint = self.equation = self.add_constraint = self.add_equation = self.con
        self.solve = self.implement = self.run = self.optimize = self.sol
        self.get_obj = self.get_objective
        self.get_stat = self.get_status
        self.get_var = self.value = self.get = self.get_variable
        self.dis = self.dis_var = self.display = self.show = self.print = self.display_variable = self.dis_variable
        self.status = self.show_status = self.dis_status
        self.objective_value = self.show_objective = self.display_objective = self.dis_obj

        self.RNG = create_random_number_generator(key)

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
                self.model = model_generator.generate_model(
                    self.features['interface_name'])

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
        """To return required Model data.

        Args:
            agent (X): if you are using a heuristic optimization method, provide the input of the function here.

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

    def bvar(self, name, variable_dim=0, variable_bound=[0, 1]):
        """
        Binary Variable Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~
        To define a binary variable.

        Args:
            name (str): what is the name of this variable?
            variable_dim (list, optional): what are dimensions of this variable?. Defaults to 0.
            variable_bound (list, optional): what are bounds on this variable?. Defaults to [0, 1].

        Examples:
            * x = bvar('x')
            * x = bvar('x',[I,J])
            * x = bvar('x', [I,J], [0, 1])
        """

        self.features = update_variable_features(
            name, variable_dim, variable_bound, 'binary_variable_counter', self.features)

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
            variable_bound (list, optional): what are bounds on this variable?. Defaults to [0, 1].

        Examples:
            * x = pvar('x')
            * x = pvar('x',[I,J])
            * x = pvar('x', [I,J], [0, 100])
        """

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
            variable_bound (list, optional): what are bounds on this variable?. Defaults to [0, 1].

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
            variable_bound (list, optional): what are bounds on this variable?. Defaults to [0, 1].

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

    def invar(self,name, variable_dim=0, variable_bound=[None, None, None]):
        
        """        
        Interval Variable Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Used to define an interval variable for constraint programming.

        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.interval_var(start=variable_bound[0], size=variable_bound[1], end=variable_bound[2], name=name)


    def sqvar(self,name, variable_dim=0, variable_bound=[None, None, None]):
        """        
        Sequence Variable Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Used to define an interval variable for constraint programming.

        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.interval_var(start=variable_bound[0], size=variable_bound[1], end=variable_bound[2], name=name)

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
            return self.RNG.uniform(low=lb, high=ub)
        else:
            return self.RNG.uniform(low=lb, high=ub, size=([len(i) for i in variable_dim]))

    def uniformint(self, lb, ub, variable_dim=0):
        """
        Uniform Integer Parameter Definition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        To generate an integer parameter using uniform distribution inside a range.
        """

        if variable_dim == 0:
            return self.RNG.integers(low=lb, high=ub)
        else:
            return self.RNG.integers(low=lb, high=ub+1, size=([len(i) for i in variable_dim]))

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

    def sol(self, directions=None, solver_name=None, solver_options=dict(), objective_id=0, email=None, debug=False, time_limit=28800, cpu_threads=None, absolute_gap=None, relative_gap=None, log=False, save_log=False, max_iterations=None):
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
        self.features['log'] = log
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
                    self.cpt = self.get_time()

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

        hour = round((self.get_time()/10**6), 3) % (24 * 3600) // 3600
        min = round((self.get_time()/10**6), 3) % (24 * 3600) % 3600 // 60
        sec = round((self.get_time()/10**6), 3) % (24 * 3600) % 3600 % 60

        print(f"cpu time [{self.features['interface_name']}]: ", self.get_time(
        ), '(microseconds)', "%02d:%02d:%02d" % (hour, min, sec), '(h, m, s)')

    def inf(self):

        data = {"info": ["model", "interface", "solver", "direction", "method"], "detail": [self.features['model_name'], self.features['interface_name'], self.features['solver_name'], self.features['directions'], self.features['solution_method']], "variable": ["positive", "binary", "integer", "free", "tot"], "count [cat,tot]": [str(self.features['positive_variable_counter']), str(
            self.features['binary_variable_counter']), str(self.features['integer_variable_counter']), str(self.features['free_variable_counter']), str(self.features['total_variable_counter'])], "other": ["objective", "constraint"], "count [cat,tot] ": [self.features['objective_counter'], self.features['constraint_counter']]}

        A = tb(data, headers="keys", tablefmt="github")

        print("~~~~~~~~~~~~\nPROBLEM INFO\n~~~~~~~~~~~~")
        print(A)
        print("~~~~~~~~~~~~\n")

        return A

    def report(self):

        print("\n~~~~~~~~~~~~~~\nFELOOPY v0.2.3\n~~~~~~~~~~~~~~")

        import datetime

        e = datetime.datetime.now()

        print("\n~~~~~~~~~~~\nDATE & TIME\n~~~~~~~~~~~")
        print(e.strftime("%Y-%m-%d %H:%M:%S"))
        print(e.strftime("%a, %variable_bound %d, %Y"))

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

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.abs(input)
    
        else:

            return abs(input)
        
    def plus(self, input1, input2):
    
        if self.features['interface_name'] == 'cplex_cp':

            return self.model.plus(input1,input2)

        else:

            return input1+input2
        
    def minus(self, input1, input2):
        """
        
        Creates an expression that represents the product of two expressions.

        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.minus(input1,input2)

        else:

            return input1-input2     
        
    def times(self, input1, input2):

        """
        
        Creates an expression that represents the product of two expressions.

        """

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.times(input1,input2)

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

            return self.model.mod(input1,input2)

        else:

            return input1 % input2

    def square(self, input):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.square(input)

        else:

            return input * input

    def power(self, input1, input2):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.power(input1,input2)

        else:

            return input1 ** input2

    def log(self, input):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.log(input)

        else:

            return np.log(input)

    def exponent(self, input):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.exp(input)

        else:

            return np.exp(input)
    
    def count(self, input, value):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.count(input,value)

        else:

            return input.count(value)
        
    def scal_prod(self, input1, input2):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.scal_prod(input1,input2)

        else:

            return np.dot(input1, input2)
        
    def range(self,x, lb=None, ub=None):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.range(x, lb, ub)

        else:

            return [x>=lb] + [x<=ub]
        
    def floor(self, x):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.floor(x)

        else:

            return np.floor(x)
    
    def ceil(self,x):

        if self.features['interface_name'] == 'cplex_cp':

            return self.model.ceil(x)

        else:

            return np.ceil(x)
        
    def round(self,x):
        
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
        
        



        

        
def count_occurrences(arr, value):
    return 


model = add_model = create_environment = env = feloopy = Model

warnings.simplefilter(action='ignore', category=FutureWarning)


class implement:

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

        hour = round(((self.end-self.start)/10**6), 3) % (24 * 3600) // 3600
        min = round(((self.end-self.start)/10**6),
                    3) % (24 * 3600) % 3600 // 60
        sec = round(((self.end-self.start)/10**6), 3) % (24 * 3600) % 3600 % 60
        print(f"cpu time [{self.InterfaceName}]: ", (self.end-self.start),
              '(microseconds)', "%02d:%02d:%02d" % (hour, min, sec), '(h, m, s)')

    def get_time(self):
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

        print("\n~~~~~~~~~~~~~~\nFELOOPY v0.2.3\n~~~~~~~~~~~~~~")

        import datetime

        e = datetime.datetime.now()

        print("\n~~~~~~~~~~~\nDATE & TIME\n~~~~~~~~~~~")
        print(e.strftime("%Y-%m-%d %H:%M:%S"))
        print(e.strftime("%a, %variable_bound %d, %Y"))

        print()
        self.inf()

        print("~~~~~~~~~~\nSOLVE INFO\n~~~~~~~~~~")
        self.dis_obj()
        self.dis_time()
        print("~~~~~~~~~\n")


construct = implement
