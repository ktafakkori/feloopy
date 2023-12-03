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
import pandas as pd
import os
import sys
import json
import csv
import itertools as it
import sqlite3

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

    def load_from_excel(self, data_file: str, data_dimension: list, shape: list, indices_list: None, sheet_name: str, path=None):

        """
        Load data from an Excel file with multiple dimensions.

        Parameters:
        - data_file (str): Name of the dataset file (e.g., data.xlsx).
        - data_dimension (list): Dimensions of the dataset.
        - shape (list): Number of indices that exist in each row and column.
        - indices_list (None or list): The string which accompanies index counter (e.g., if row0, row1, and col0, col1, then index is ['row', 'col']).
        - sheet_name (str): Name of the excel sheet containing the parameter.
        - path (None or str): Specify the directory of the dataset file (if not provided, the dataset file should exist in the same directory as the code).

        Returns:
        - NumPy array containing the loaded data.
        """

        if path == None:
            data_file = os.path.join(sys.path[0], data_file)
        else:
            data_file = path
        if len(shape) == 2:
            if (shape[0] == 1 and shape[1] == 1) or (shape[0] == 1 and shape[1] == 0) or (shape[0] == 0 and shape[1] == 0) or (shape[0] == 0 and shape[1] == 1):
                return pd.read_excel(data_file, index_col=0, sheet_name=sheet_name).to_numpy()
            else:
                parameter = pd.read_excel(data_file, header=[i for i in range(shape[1])], index_col=[i for i in range(shape[0])], sheet_name=sheet_name)
                created_par = np.zeros(shape=([len(i) for i in data_dimension]))
                for keys in it.product(*data_dimension):
                    try:
                        created_par[keys] = parameter.loc[tuple([indices_list[i]+str(keys[i]) for i in range(shape[0])]), tuple([indices_list[i]+str(keys[i]) for i in range(shape[0], len(indices_list))])]
                    except:
                        created_par[keys] = None
                return created_par
        else:
            par = pd.read_excel(data_file, index_col=0,sheet_name=sheet_name).to_numpy()
            return par.reshape(par.shape[0],)
        
    def load_from_csv(self, data_file: str, csv_delimiter=',', path=None):
        """
        Load data from a CSV file with multiple dimensions.

        Parameters:
        - data_file (str): Name of the CSV dataset file (e.g., data.csv).
        - data_dimension (list): Dimensions of the dataset.
        - indices_list (None or list): The string which accompanies index counter (e.g., if row0, row1, and col0, col1, then index is ['row', 'col']).
        - delimiter (str): The delimiter used in the CSV file (default is ',').
        - path (None or str): Specify the directory of the CSV dataset file (if not provided, the CSV file should exist in the same directory as the code).

        Returns:
        - NumPy array containing the loaded data.
        """
        if path is None:
            data_file = os.path.join(os.getcwd(), data_file)
        else:
            data_file = os.path.join(path, data_file)

        data = np.genfromtxt(data_file, delimiter=csv_delimiter, dtype=float, skip_header=1)
        
        return data[:,1:]
    
    def load_from_json(self, data_file: str, json_key=None, path=None):
        """
        Load data from a JSON file.

        Parameters:
        - data_file (str): Name of the JSON dataset file (e.g., data.json).
        - path (None or str): Specify the directory of the JSON dataset file (if not provided, the JSON file should exist in the same directory as the code).

        Returns:
        - Python dictionary containing the loaded data.
        """
        if path is None:
            data_file = os.path.join(os.getcwd(), data_file)
        else:
            data_file = os.path.join(path, data_file)

        with open(data_file, 'r') as file:
            data = json.load(file)
        
        if json_key != None:
            return data[json_key]
        else:
            return data
        
    def load_from_sqlite(self, db_file: str, table_name: str):
        """
        Load data from an SQLite database table.

        Parameters:
        - db_file (str): Name of the SQLite database file.
        - table_name (str): Name of the table to retrieve data from.

        Returns:
        - List of tuples containing the loaded data rows.
        """
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()

        connection.close()

        return data
    
    def load(self, file_name: str, excel_dim=None, excel_struct=None, excel_indices=None, excel_sheet=None, csv_delimiter=',', json_key=None, sql_table=None, path=None):

        file_extension = os.path.splitext(file_name)[1].lower()
        
        if file_extension == '.xlsx':
            if excel_dim is not None and excel_struct is not None:
                if excel_indices is not None and excel_sheet is not None:
                    return self.load_from_excel(file_name, excel_dim, excel_struct, excel_indices, excel_sheet, path)
                else:
                    return self.load_from_excel(file_name, excel_dim, excel_struct, path=path)
            else:
                return self.load_from_excel(file_name, excel_dim, shape=[0, 0], indices_list=[], sheet_name=excel_sheet, path=path)
        
        elif file_extension == '.csv':
            return self.load_from_csv(file_name, csv_delimiter, path=path)

        elif file_extension == '.json':
            return self.load_from_json(file_name, json_key, path=path)

        elif file_extension in ['.sqlite', '.db']:
            if sql_table is not None:
                return self.load_from_sqlite(file_name, sql_table)
            else:
                raise ValueError("For SQLite files, you must specify the table name (sql_table).")
        
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")
        
data_toolkit = data_utils = data_manager = data_frame = DataToolkit