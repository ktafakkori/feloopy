# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

from ...helpers.formatter import *
from juliacall import Main as jl

def Get(model_object, result, input1, input2=None):

    input1 = input1[0]

    match input1:

        case 'variable':

            return result[0]["solutions"][input2]
            
        case 'status':

            return result[0]["status"]

        case 'objective':

            return result[0]["objective_value"]

        case 'time':

            return (result[1][1]-result[1][0])

        case 'dual':
            
            return result[0]["dual"][input2]