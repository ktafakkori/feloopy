'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

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
