# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

def Get(model_object, result, input1, input2=None):

    directions = +1 if input1[1][input1[2]] == 'min' else -1
    input1 = input1[0]

    match input1:

        case 'variable':

            return input2.get()
            
        case 'status':

            try:
                model_object.get()
                return 'optimal*'
            except:
                return 'not optimal or nothing found'

        case 'objective':

            return model_object.get()

        case 'time':

            return (result[1][1]-result[1][0])
