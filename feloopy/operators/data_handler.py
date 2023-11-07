'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.8)                               |
|  Modified: Wednesday, 8th November 2023 12:40:23 am   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''

import numpy as np

class DataToolkit:

    def __init__(self, data_structure='numpy', key=None):
        """
        Initialize the Data object.

        Parameters:
        - data_structure (str, optional): Data structure type (default is 'numpy').
        - key: Random number generator key.

        Attributes:
        - data_structure (str): The data structure type.
        - data (dict): A dictionary to store data.
        - history (dict): A dictionary to store historical data.
        - random: Random number generator.
        - criteria_directions (dict): A dictionary to store criteria directions.

        """
        self.data_structure = data_structure
        self.data = dict()
        self.history = dict()
        self.random = np.random.default_rng(key)
        self.criteria_directions = dict()

    def fix_dims(self, dim):
        """
        Fix the dimension format.

        Parameters:
        - dim: Dimension information.

        Returns:
        - Fixed dimension.

        """
        if dim == 0:
            return dim

        if not isinstance(dim, set):
            if len(dim) >= 1:
                if not isinstance(dim[0], set):
                    dim = [range(d) if not isinstance(d, range) else d for d in dim]

        return dim

    def alias(self, name, input):
        """
        Create an alias for a data parameter.

        Parameters:
        - name: The name of the alias.
        - input: The name of the original data parameter or a value.

        Returns:
        - The alias.

        """
        if type(input) == str:
            self.data[name] = self.data[input]
        else:
            self.data[name] = input
        return input 

    def start_recording(self, name, direction):
        """
        Record the direction for a criterion and initialize it.

        Parameters:
        - name: The name of the criterion.
        - direction: The direction of the criterion ('max' or 'min').

        """
        self.criteria_directions[name] = direction
        if direction == 'max':
            self.data[name] = [-np.inf]
        if direction == 'min':
            self.data[name] = [np.inf]

    def set(self, index='', bound=None, step=1, to_list=False):
        """
        Define a set using label index or a range of values.

        Parameters:
        - index (str, optional): Label index to create the set.
        - bound (list of int, optional): Start and end values of the range.
        - step (int, optional, default 1): Step size of the range.
        - to_list (bool, optional): Convert the set to a list.

        Returns:
        - The created set.

        Raises:
        - ValueError: If neither bound nor index is provided.

        """
        if index == '':
            if not to_list:
                created_set = set(range(bound[0], bound[1] + 1, step))
            else:
                created_set = list(range(bound[0], bound[1] + 1, step))

        if bound is not None:
            if not to_list:
                created_set = set(f'{index}{i}' for i in range(bound[0], bound[1] + 1, step))
            else:
                created_set = list([f'{index}{i}' for i in range(bound[0], bound[1] + 1, step)])

        elif index:
            if not to_list:
                created_set = set(f'{index}{i}' for i in range(0, len(index), step))
            else:
                created_set = list([f'{index}{i}' for i in range(0, len(index), step)])
        else:
            raise ValueError('Either bound or index must be provided.')

        if index != '':
            self.data[index] = created_set

        return created_set

    def zeros(self, name, dim=0):
        """
        Create a parameter filled with zeros.

        Parameters:
        - name: The name of the parameter.
        - dim: Dimension of the parameter.

        Returns:
        - The created parameter.

        """
        dim = self.fix_dims(dim)
        if dim == 0:
            self.data[name] = np.zeros(1)
            return self.data[name]
        else:
            self.data[name] = np.zeros(tuple(len(i) for i in dim))
            return self.data[name]

    def ones(self, name, dim=0):
        """
        Create a parameter filled with ones.

        Parameters:
        - name: The name of the parameter.
        - dim: Dimension of the parameter.

        Returns:
        - The created parameter.

        """
        dim = self.fix_dims(dim)
        if dim == 0:
            self.data[name] = np.ones(1)
            return self.data[name]
        else:
            self.data[name] = np.ones(tuple(len(i) for i in dim))
            return self.data[name]

    def uniform(self, name, dim=0, bound=[0, 1]):

        """
        Create a real-valued parameter using uniform distribution inside a range.

        Parameters:
        - name: The name of the parameter.
        - dim: Dimension of the parameter.
        - bound (list of int, optional): The range for the uniform distribution.

        Returns:
        - The created parameter.

        """

        dim = self.fix_dims(dim)
        if dim == 0:
            self.data[name] = self.random.uniform(low=bound[0], high=bound[1])
            return self.data[name]
        else:
            self.data[name] = self.random.uniform(low=bound[0], high=bound[1], size=[len(i) for i in dim])
            return self.data[name]

    def uniformint(self, name, dim=0, bound=[0, 10]):
        """
        Create an integer-valued parameter using uniform distribution inside a range.

        Parameters:
        - name: The name of the parameter.
        - dim: Dimension of the parameter.
        - bound (list of int, optional): The range for the uniform distribution.

        Returns:
        - The created parameter.

        """
        dim = self.fix_dims(dim)
        if dim == 0:
            self.data[name] = self.random.integers(low=bound[0], high=bound[1] + 1)
            return self.data[name]
        else:
            self.data[name] = self.random.integers(low=bound[0], high=bound[1] + 1, size=[len(i) for i in dim])
            return self.data[name]

    def uniformlist(self, name, dim, candidate_set, size_bound=[0, 1], with_replacement=False, sorted=True):
        """
        Generate a list of uniformly distributed random samples from a candidate set within a specified sample size range.

        Parameters:
        - name: The name of the parameter.
        - dim: Dimension of the parameter.
        - candidate_set (list): The candidate set from which to draw random samples.
        - size_bound (list of int): The lower and upper bounds of the sample size range.
        - with_replacement (bool, optional): Whether to allow sampling with replacement.
        - sorted (bool, optional): Whether to sort the generated samples.

        Returns:
        - The created parameter.

        """
        dim = self.fix_dims(dim)
        if dim == 0:
            if sorted:
                self.data[name] = np.sort(self.random.choice(candidate_set, self.random.integers(size_bound[0], size_bound[1] + 1), replace=with_replacement))
                return self.data[name]
            else:
                self.data[name] = self.random.choice(candidate_set, self.random.integers(size_bound[0], size_bound[1] + 1), replace=with_replacement)
                return self.data[name]
        else:
            if sorted:
                self.data[name] = [np.sort(self.random.choice(candidate_set, self.random.integers(size_bound[0], size_bound[1] + 1), replace=with_replacement)) for i in dim[0]]
                return self.data[name]
            else:
                self.data[name] = [self.random.choice(candidate_set, self.random.integers(size_bound[0], size_bound[1] + 1), replace=with_replacement) for i in dim[0]]
                return self.data[name]

    def update_recording(self, names_of_parameters, names_of_criteria, values_of_parameters, values_of_criteria):
        """
        Updates values for specified parameters based on given criteria.

        Parameters:
        - names_of_parameters (list): Names of the parameters to be updated.
        - names_of_criteria (list): Names of the criteria for evaluation.
        - values_of_parameters (list): Values of the parameters to be compared.
        - values_of_criteria (list): Values of the criteria for evaluation.

        """
        xcounter = 0
        for i in names_of_parameters:
            counter = 0
            for j in names_of_criteria:
                if self.criteria_directions[j] == 'max':
                    if values_of_criteria[counter] >= self.data[j][-1]:
                        self.data[i] = values_of_parameters[xcounter]
                        self.data[j].append(values_of_criteria[counter])
                if self.criteria_directions[j] == 'min':
                    if values_of_criteria[counter] <= self.data[j][-1]:
                        self.data[i] = values_of_parameters[xcounter]
                        self.data[j].append(values_of_criteria[counter])
                counter += 1
            xcounter += 1