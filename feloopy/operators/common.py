# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

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

def dims(a):
    return np.ndindex(a.shape[1:])

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

def kvs_advanced(a, sort_order='increasing', sort_by='key', b=None, output='both'):
    if isinstance(a, np.ndarray):
        return enumerate(a)
    elif isinstance(a, dict):
        if sort_by == 'keys':
            sorted_items = sorted(a.items(), key=lambda x: x[0], reverse=(sort_order == 'decreasing'))
        elif sort_by == 'values':
            sorted_items = sorted(a.items(), key=lambda x: x[1], reverse=(sort_order == 'decreasing'))
        elif sort_by == 'b' and b is not None:
            sorted_items = sorted(a.items(), key=lambda x: b[x[0]], reverse=(sort_order == 'decreasing'))
        else:
            return None
        if output == 'keys':
            return [item[0] for item in sorted_items]
        elif output == 'values':
            return [item[1] for item in sorted_items]
        else:  # output == 'both'
            return sorted_items
    elif isinstance(a, pd.Series):
        if sort_by == 'keys':
            sorted_items = a.sort_index(ascending=(sort_order == 'increasing'))
        elif sort_by == 'values':
            sorted_items = a.sort_values(ascending=(sort_order == 'increasing'))
        elif sort_by == 'b' and b is not None:
            sorted_items = a.sort_values(by=b, ascending=(sort_order == 'increasing'))
        else:
            return None
        if output == 'keys':
            return sorted_items.index.tolist()
        elif output == 'values':
            return sorted_items.values.tolist()
        else:  # output == 'both'
            return zip(sorted_items.index, sorted_items.values)
    elif isinstance(a, list):
        if sort_by == 'keys':
            sorted_items = sorted(enumerate(a), key=lambda x: x[0], reverse=(sort_order == 'decreasing'))
        elif sort_by == 'values':
            sorted_items = sorted(enumerate(a), key=lambda x: x[1], reverse=(sort_order == 'decreasing'))
        elif sort_by == 'b' and b is not None:
            sorted_items = sorted(enumerate(a), key=lambda x: b[x[0]], reverse=(sort_order == 'decreasing'))
        else:
            return None
        if output == 'keys':
            return [item[0] for item in sorted_items]
        elif output == 'values':
            return [item[1] for item in sorted_items]
        else:  # output == 'both'
            return sorted_items
    else:
        return None

sets = it.product

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

def version(INPUT):
    print(INPUT.__version__)
    return (INPUT)

import pandas as pd
import os
import sys



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




