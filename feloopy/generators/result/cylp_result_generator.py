# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


import cylp as cylp_interface
from cylp.cy import CyClpSimplex


def Get(model_object, result, input1, input2=None):

    input1 = input1[0]

    match input1:

        case 'variable':

            return model_object.primalVariableSolution[input2]

        case 'status':

            return result[0].status

        case 'objective':

            return -model_object.objectiveValue

        case 'time':

            return (result[1][1]-result[1][0])
