import pip
import timeit 
import os
import sys
import pandas as pd
import numpy as np
import itertools as it

sets = it.product

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

def end_timer():
    '''
    Timer Ends Here!
    ~~~~~~~~~~~~~~~~
    '''
    global EndTime
    EndTime = timeit.default_timer()
    sec = round((EndTime - StartTime), 3)% (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    print("Elapsed time (microseconds):", (EndTime-StartTime)*10**6)
    print("Elapsed time (hour:min:sec):", "%02d:%02d:%02d" % (hour, min, sec))
    return EndTime

def LoadfromExcel(DataFile: str, Dimension: list, RowDim: int, ColDim: int, IndexNames: str, SheetName: str, path=None):
        '''
        Multi-Dimensional Excel Parameter Reader! 
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        *DataFile: Name of the dataset file (e.g., data.xlsx)
        *Dimension: Dimension of the dataset
        *RowDim: Number of indices that exist in each row from left (e.g., 0, 1, 2, 3...)
        *ColDim: Number of indices that exist in each column from top (e.g., 0, 1, 2, 3...)
        *IndexNames: The string which accompanies index counter (e.g., if row0, row1, ... and col0,col1, then index is ['row','col'])
        *SheetName: Name of the excel sheet in which the corresponding parameter exists.
        *Path: specify directory of the dataset file (if not provided, the dataset file should exist in the same directory as the code.)
        '''
        if path == None:
            data_file = os.path.join(sys.path[0], DataFile)
        else:
            data_file = path

        parameter = pd.read_excel(data_file, header=[i for i in range(ColDim)], index_col=[
            i for i in range(RowDim)], sheet_name=SheetName)

        if (RowDim == 1 and ColDim == 1) or (RowDim == 1 and ColDim == 0) or (RowDim == 0 and ColDim == 0) or (RowDim == 0 and ColDim == 1):

            return parameter.to_numpy()

        else:

            created_par = np.zeros(shape=([len(i) for i in Dimension]))

            for keys in it.product(*Dimension):

                try:

                    created_par[keys] = parameter.loc[tuple([IndexNames[i]+str(keys[i]) for i in range(
                        RowDim)]), tuple([IndexNames[i]+str(keys[i]) for i in range(RowDim, len(IndexNames))])]

                except:

                    created_par[keys] = None

            return created_par

def version(INPUT):
    print(INPUT.__version__)
    return(INPUT)

