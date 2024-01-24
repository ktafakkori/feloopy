# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import pyomo.environ as pyomo_interface


def Get(model_object, result, input1, input2=None):

    input1 = input1[0]

    match input1:

        case 'variable':

            return pyomo_interface.value(input2)

        case 'status':

            return result[0].solver.termination_condition

        case 'objective':

            return pyomo_interface.value(model_object.OBJ)

        case 'time':

            return (result[1][1]-result[1][0])
        
        case 'dual':

            return model_object.dual[model_object.c[input2]]

        case 'slack':

            upper_slack = model_object.c[input2].uslack()
            lower_slack = model_object.c[input2].lslack()

            return min(upper_slack, lower_slack)
        
        case 'rc':
            ""
    