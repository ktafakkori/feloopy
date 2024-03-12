# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


import sys

import highspy as highs_interface
from ...helpers.formatter import *

highs_status_dict = {
    highs_interface.kSolutionStatusFeasible: 'feasible',
    highs_interface.kSolutionStatusInfeasible: 'infeasible',
    highs_interface.kSolutionStatusNone: 'none',
}

def Get(model_object, result, input1, input2=None):
    input1 = input1[0]

    match input1:
        case 'variable':
            
            return model_object.val(input2)
        
        case 'status':
            return model_object.getModelStatus()

        case 'objective':
            return model_object.getObjectiveValue()

        case 'time':
            return (result[1][1] - result[1][0])