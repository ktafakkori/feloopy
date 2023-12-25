# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


import gekko as gekko_interface

gekko_status_dict = {0: "unknown", 1: "optimal"}

def Get(model_object, result, input1, input2=None):

    directions = +1 if input1[1][input1[2]] == 'min' else -1

    input1 = input1[0]

    match input1:

        case 'variable':

            try:
                return input2.value[0]
            except: 
                return input2

        case 'status':

            return gekko_status_dict.get(model_object.options.SOLVESTATUS)

        case 'objective':

            return directions*model_object.options.objfcnval

        case 'time':

            return (result[1][1]-result[1][0])
