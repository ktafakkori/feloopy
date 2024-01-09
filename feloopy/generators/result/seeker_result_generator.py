# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


from ...helpers.formatter import *

def Get(model_object, result, input1, input2=None):

    input1 = input1[0]

    match input1:

        case 'variable':

            return input2.get_value()

        case 'status':
        
            return model_object.get_status()

        case 'objective':

            return result[0].get_value()

        case 'time':

            return (result[1][1]-result[1][0])
