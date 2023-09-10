'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

import pip
import timeit
import os
import sys
import pandas as pd
import numpy as np
import itertools as it
import matplotlib.style as style
import matplotlib.pyplot as plt
from openpyxl import load_workbook
import math as mt
from ..helpers.formatter import *

from tabulate import tabulate as tb

def if_then_else(*conditions_and_values):
    conditions = conditions_and_values[::2]
    values = conditions_and_values[1::2]
    if len(conditions) != len(values) + 1:
        raise ValueError("Number of conditions must be one more than the number of values")
    return np.select(conditions[:-1], values, default=conditions[-1])

def if_then(*conditions_and_values):
    conditions = conditions_and_values[::2]
    values = conditions_and_values[1::2]
    if len(conditions) != len(values):
        raise ValueError("Number of conditions and values must be the same")
    return np.select(conditions, values)

import numpy as np

def dims(a):
    return np.ndindex(a.shape[1:])

import numpy as np
import pandas as pd


def keys(a):
    if isinstance(a, np.ndarray):
        return range(len(a))
    elif isinstance(a, dict):
        return list(a.keys())
    elif isinstance(a, pd.Series):
        return a.index.tolist()
    elif isinstance(a, list):
        return range(len(a))
    else:
        return None
ids = keys


import numpy as np
import pandas as pd

def kvs(a):
    if isinstance(a, np.ndarray):
        return enumerate(a)
    elif isinstance(a, dict):
        return a.items()
    elif isinstance(a, pd.Series):
        return zip(a.index, a.values)
    elif isinstance(a, list):
        return enumerate(a)
    else:
        return None

sets = it.product


def random_number_generator(key):

    return np.random.default_rng(key)


def make_set(input):

    if type(input) == int:

        return range(input)

    else:

        return set(input)


def make_uniform_param(rng, lb, ub, variable_dim=0):

    if variable_dim == 0:

        return rng.uniform(low=lb, high=ub)

    else:

        return rng.uniform(low=lb, high=ub, size=([len(i) for i in variable_dim]))


def exponent(input):
    return np.exp(input)


def floor(input):
    return np.floor(input)


def ceil(input):
    return np.ceil(input)


def round(input):
    return np.round(input)


def log_of_base(input, base):
    return mt.log(input, base)


def log(input):
    return np.log(input)

def log10(input):
    return np.log10(input)

def sqrt(input):
    return np.sqrt(input)


def sin(input):
    return np.sin(input)


def cos(input):
    return np.cos(input)


def power(input1, input2):
    return input1**input2


def install(package):
    '''
    Package Installer!
    ~~~~~~~~~~~~~~~~~~

    *package: enter a string representing the name of the package (e.g., 'numpy' or 'feloopy')

    '''

    if hasattr(pip, 'main'):
        pip.main(['install', package])
        pip.main(['install', '--upgrade', package])
    else:
        pip._internal.main(['install', package])
        pip._internal.main(['install', '--upgrade', package])


def uninstall(package):
    '''
    Package Uninstaller!
    ~~~~~~~~~~~~~~~~~~~~

    *package: enter a string representing the name of the package (e.g., 'numpy' or 'feloopy')

    '''

    if hasattr(pip, 'main'):
        pip.main(['uninstall', package])
    else:
        pip._internal.main(['unistall', package])


def begin_timer():
    '''
    Timer Starts Here!
    ~~~~~~~~~~~~~~~~~~
    '''
    global StartTime
    StartTime = timeit.default_timer()
    return StartTime


def end_timer(show=False):
    '''
    Timer Ends Here!
    ~~~~~~~~~~~~~~~~
    '''
    global EndTime
    EndTime = timeit.default_timer()
    sec = round(EndTime - StartTime) % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    if show:
        print("Elapsed time (microseconds):", (EndTime-StartTime)*10**6)
        print("Elapsed time (hour:min:sec):",
              "%02d:%02d:%02d" % (hour, min, sec))
    return EndTime

def load_from_excel(data_file: str, data_dimension: list, shape: list, indices_list: None, sheet_name: str, path=None):
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

            parameter = pd.read_excel(data_file, header=[i for i in range(shape[1])], index_col=[
                                      i for i in range(shape[0])], sheet_name=sheet_name)

            created_par = np.zeros(shape=([len(i) for i in data_dimension]))

            for keys in it.product(*data_dimension):

                try:

                    created_par[keys] = parameter.loc[tuple([indices_list[i]+str(keys[i]) for i in range(
                        shape[0])]), tuple([indices_list[i]+str(keys[i]) for i in range(shape[0], len(indices_list))])]

                except:

                    created_par[keys] = None

            return created_par
    else:
        par = pd.read_excel(data_file, index_col=0,
                            sheet_name=sheet_name).to_numpy()

        return par.reshape(par.shape[0],)

def save_to_excel(data_array, data_file: str, sheet_name: str, indices: list = None, path=None):
    
    """
    Save NumPy array data to an Excel file.

    Parameters:
    - data_array: NumPy array to be saved (3D or 4D).
    - data_file (str): Name of the dataset file (e.g., data.xlsx).
    - sheet_name (str): Base name for Excel sheets. For 3D data, sheets will be named as "{sheet_name}_slice_x", where x is the slice index.
    - indices (None or list): The list of strings for row and column indices (e.g., ['Row', 'Column']).
    - path (None or str): Specify the directory of the dataset file (if not provided, the dataset file will be created in the same directory as the code).

    Raises:
    - ValueError: If the input data_array's dimensions are not 2D, 3D, or 4D.

    Notes:
    - If the specified Excel file does not exist, it will be created.
    - If the specified Excel file already exists, data will be appended to it.

    """
    
    if path is None:
        data_file = os.path.join(os.getcwd(), data_file)
    else:
        data_file = os.path.join(path, data_file)

    if indices is None:
        indices = ['Index']

    if data_array.ndim not in [2, 3, 4]:
        raise ValueError("Only 2D, 3D, and 4D arrays are supported.")

    num_sheets = 1
    if data_array.ndim > 2:
        num_sheets = data_array.shape[0]

    if not os.path.exists(data_file):
       
        with pd.ExcelWriter(data_file, engine='xlsxwriter') as writer:
            for sheet_idx in range(num_sheets):
                sheet_name_with_idx = f"{sheet_name}{sheet_idx}" if num_sheets > 1 else sheet_name
                data_slice = data_array[sheet_idx] if num_sheets > 1 else data_array

                num_rows, num_columns = data_slice.shape 

                data_df = pd.DataFrame(data_slice, columns=[f'{indices[1]}{i}' for i in range(num_columns)])
                data_df.insert(0, '', [f'{indices[0]}{i}' for i in range(num_rows)])

                
                data_df.to_excel(writer, sheet_name=sheet_name_with_idx, index=False, header=True)

                
                workbook = writer.book
                worksheet = writer.sheets[sheet_name_with_idx]

                
                cell_format = workbook.add_format({'bold': False, 'border': 0})
                for col_num, col in enumerate(data_df.columns, start=1):
                    worksheet.set_column(col_num, col_num, None, cell_format)
    else:
       
        with pd.ExcelWriter(data_file, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            writer.book.sheets = {ws.title: ws for ws in writer.book.worksheets}
            for sheet_idx in range(num_sheets):
                sheet_name_with_idx = f"{sheet_name}{sheet_idx}" if num_sheets > 1 else sheet_name
                data_slice = data_array[sheet_idx] if num_sheets > 1 else data_array

                num_rows, num_columns = data_slice.shape  

                data_df = pd.DataFrame(data_slice, columns=[f'{indices[1]}{i}' for i in range(num_columns)])
                data_df.insert(0, '', [f'{indices[0]}{i}' for i in range(num_rows)])

                
                data_df.to_excel(writer, sheet_name=sheet_name_with_idx, index=False, header=True, startrow=0)
                

import os
import csv
import numpy as np


def load_from_csv(data_file: str, data_dimension: list, indices_list=None, delimiter=',', path=None):
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

    if indices_list is None:
        indices_list = ['']  
        
    data = np.genfromtxt(data_file, delimiter=delimiter, dtype=float, skip_header=1)
    
    return data[:,1:]


def save_to_csv(data_array, data_file: str, indices: list = None, delimiter=',', path=None):
    """
    Save NumPy array data to a CSV file.

    Parameters:
    - data_array: NumPy array to be saved (2D).
    - data_file (str): Name of the CSV dataset file (e.g., data.csv).
    - indices (None or list): The list of strings for row and column indices (e.g., ['Row', 'Column']).
    - delimiter (str): The delimiter to be used in the CSV file (default is ',').
    - path (None or str): Specify the directory of the CSV dataset file (if not provided, the CSV file will be created in the same directory as the code).

    Raises:
    - ValueError: If the input data_array's dimensions are not 2D.

    Notes:
    - If the specified CSV file does not exist, it will be created.
    - If the specified CSV file already exists, data will be overwritten.

    """
    if path is None:
        data_file = os.path.join(os.getcwd(), data_file)
    else:
        data_file = os.path.join(path, data_file)

    if indices is None:
        indices = ['Index']

    if data_array.ndim != 2:
        raise ValueError("Only 2D arrays are supported for saving to CSV files.")

    mode = 'w' 
    
    with open(data_file, mode, newline='') as file:
        writer = csv.writer(file, delimiter=delimiter)

        if mode == 'w':
            writer.writerow([''] + [f"{indices[1]}{i}" for i in range(data_array.shape[1])])

        for row_idx in range(data_array.shape[0]):
            writer.writerow([f"{indices[0]}{row_idx}"] + data_array[row_idx].tolist())


import json
import os

def load_from_json(data_file: str, path=None):
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
    
    return data

def save_to_json(data_dict, data_file: str, path=None):
    """
    Save data as a JSON file.

    Parameters:
    - data_dict (dict): Python dictionary to be saved.
    - data_file (str): Name of the JSON dataset file (e.g., data.json).
    - path (None or str): Specify the directory of the JSON dataset file (if not provided, the JSON file will be created in the same directory as the code).

    Raises:
    - ValueError: If the input data_dict is not a dictionary.

    Notes:
    - If the specified JSON file does not exist, it will be created.
    - If the specified JSON file already exists, data will be overwritten.
    """
    if not isinstance(data_dict, dict):
        raise ValueError("Input data_dict must be a dictionary.")

    if path is None:
        data_file = os.path.join(os.getcwd(), data_file)
    else:
        data_file = os.path.join(path, data_file)

    with open(data_file, 'w') as file:
        json.dump(data_dict, file)

import sqlite3

def save_to_sqlite(data_list, db_file: str, table_name: str, columns: dict, primary_key=None):
    """
    Save data to an SQLite database table. If the table doesn't exist, it will be created.

    Parameters:
    - data_list (list of tuples): List of data rows to be inserted into the table.
    - db_file (str): Name of the SQLite database file.
    - table_name (str): Name of the table to insert data into.
    - columns (dict): Dictionary mapping column names to their data types.
    - primary_key (str or None): Name of the primary key column. If None, no primary key is used.

    Notes:
    - The data_list should be a list of tuples, where each tuple represents a row of data.
    - If a primary key is specified, the data for rows with existing primary keys will be updated.
    """
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    if primary_key:
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join([f'{col} {data_type}' for col, data_type in columns.items()])}, PRIMARY KEY ({primary_key}))")
    else:
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join([f'{col} {data_type}' for col, data_type in columns.items()])})")

    cursor.executemany(f"INSERT OR REPLACE INTO {table_name} ({', '.join(columns.keys())}) VALUES ({', '.join(['?'] * len(columns))})", data_list)

    connection.commit()
    connection.close()


def load_from_sqlite(db_file: str, table_name: str):
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


def version(INPUT):

    print(INPUT.__version__)

    return (INPUT)

def sensitivity(model_function, params_list, range_of_change_list, step_of_change_list, show_table=True, show_plot=False, save_plot=False, file_name='sensfig.png', plot_style='ggplot', legends_list=None, axis_names=['% Change', 'Objective Value'], size_of_fig=[8, 6], dpi=80):
    """
    Generate a sensitivity analysis plot for parameters within their range of change.

    Parameters:
        model_function (callable): The model function to evaluate.
        params_list (list): List of initial parameter values.
        range_of_change_list (list): List of tuples representing the range of change for each parameter.
        step_of_change_list (list): List of step values for sensitivity analysis.
        show_table (bool, optional): Display a table of sensitivity analysis results. Default is True.
        show_plot (bool, optional): Display the sensitivity analysis plot. Default is False.
        save_plot (bool, optional): Save the plot as an image file. Default is False.
        file_name (str, optional): File name for the saved plot. Default is 'sensfig.png'.
        plot_style (str, optional): Style of the plot, e.g., 'ggplot'. Default is 'ggplot'.
        legends_list (list, optional): List of legend labels for parameters. Default is None.
        axis_names (list, optional): Names for the x and y axes. Default is ['% Change', 'Objective Value'].
        size_of_fig (list, optional): Size of the figure in inches. Default is [8, 6].
        dpi (int, optional): Dots per inch for the saved plot. Default is 80.

    """
    if show_plot:
        fig, ax = plt.subplots(figsize=(size_of_fig[0], size_of_fig[1]), dpi=dpi)

    for i in range(len(params_list)):
        OriginalParameterValue = np.asarray(params_list[i])

        SensitivityPoints = []
        Percent = []

        range_of_change = range_of_change_list[i].copy()
        diff = np.copy(range_of_change[1] - range_of_change[0])
        step_of_change = step_of_change_list[i]

        for j in range(0, diff // step_of_change + 1):
            Percent.append(range_of_change[0])

            if isinstance(params_list[i], int) and step_of_change in [-1, 1]:
                SensitivityPoints.append(OriginalParameterValue + step_of_change)
            else:
                SensitivityPoints.append(OriginalParameterValue * (1 + range_of_change[0] / 100))

            range_of_change[0] += step_of_change

        x = Percent
        y = []

        for SensitivityPointofaParam in SensitivityPoints:
            NewParamValues = params_list.copy()
            NewParamValues[i] = SensitivityPointofaParam
            m = model_function(*tuple(NewParamValues))
            y.append(m.get_obj())

        if show_table:
            if legends_list:
                tline_text(f"Sensitivity to {legends_list[i]}")
            else:
                tline_text(f"Sensitivity to {i}")

            two_column("% Change", "Objective value")
            for xi, yi in zip(x, y):
                two_column(format_string(xi), format_string(yi))
            bline()

        if show_plot:
            style.use(plot_style)
            ax.set_xlabel(axis_names[0], fontsize=12)
            ax.set_ylabel(axis_names[1], fontsize=12)

            if legends_list:
                ax.plot(x, y, label=legends_list[i], linewidth=3.5)
            else:
                ax.plot(x, y, label=f"Parameter {i}", linewidth=3.5)

            ax.scatter(x, y)

    if show_plot:
        ax.legend()

    if show_plot and save_plot:
        plt.savefig(file_name, dpi=500)

    if show_plot:
        plt.show()


    if show_plot and save_plot:
        plt.savefig(file_name, dpi=500)

    if show_plot:
        plt.show()


def compare(results, show_fig=True, save_fig=False, file_name=None, dpi=800, fig_size=(15, 3), alpha=0.8, line_width=5):

    # [obj, time, accuracy, prob_per_epoch]

    fig, axs = plt.subplots(1, 4, figsize=fig_size)

    names = list(results.keys())

    obj_dict = dict()

    time_dict = dict()

    min_acc = np.inf
    max_acc = -np.inf

    min_prob = np.inf
    max_prob = -np.inf
    for keys in results.keys():

        x = np.arange(len(results[keys][3]))
        axs[3].plot(x, results[keys][3], alpha=alpha, lw=line_width)

        if np.min(results[keys][3]) <= min_prob:
            min_prob = np.min(results[keys][3])
        if np.max(results[keys][3]) >= max_prob:
            max_prob = np.max(results[keys][3])

        # axs[3].set_ylim(min_prob-0.5,max_prob+0.5)
        axs[3].set_xlim(0-0.5, len(results[keys][3])-1+0.5)
        axs[3].legend(names, loc=(1.04, 0))

        x = np.arange(len(results[keys][2]))
        axs[2].plot(x, results[keys][2], alpha=alpha, lw=line_width)

        if np.min(results[keys][2]) <= min_acc:
            min_acc = np.min(results[keys][2])
        if np.max(results[keys][2]) >= min_acc:
            max_acc = np.max(results[keys][2])

        # axs[2].set_ylim(min_acc-0.5,max_acc+0.5)
        axs[2].set_xlim(0-0.5, len(results[keys][2])-1+0.5)

        obj_dict[keys] = results[keys][0]
        time_dict[keys] = results[keys][1]

    axs[0].boxplot(obj_dict.values(), showfliers=False)
    axs[1].boxplot(time_dict.values(), showfliers=False)
    axs[0].set_xticklabels(obj_dict.keys())
    axs[1].set_xticklabels(time_dict.keys())

    axs[0].set_ylabel('Reward')
    axs[1].set_ylabel('Time (second)')
    axs[2].set_ylabel('Accuracy (%)')
    axs[2].set_xlabel('Epoch')
    axs[3].set_ylabel('Probability')
    axs[3].set_xlabel('Epoch')

    plt.subplots_adjust(left=0.071, bottom=0.217, right=0.943,
                        top=0.886, wspace=0.34, hspace=0.207)

    if save_fig:
        if file_name == None:
            plt.savefig('comparision_results.png', dpi=dpi)
        else:
            plt.savefig(file_name, dpi=dpi)

    if show_fig:
        plt.show()




