# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


import picos as picos_interface


def Get(model_object, result, input1, input2=None):

    input1 = input1[0]

    match input1:

        case 'variable':

            return input2.value

        case 'status':

            return result[0][0].claimedStatus

        case 'objective':

            return model_object.obj_value()

        case 'time':

            return (result[1][1]-result[1][0])

        case 'dual':
            dual_values = {}

            for constraint_name in result[0][1].keys():
                dual_value = model_object.constraints[result[0][1][constraint_name]].dual_value
                dual_values[constraint_name] = dual_value
            
            for constraint_name, dual_value in dual_values.items():
                if constraint_name == input2:
                    return dual_value

