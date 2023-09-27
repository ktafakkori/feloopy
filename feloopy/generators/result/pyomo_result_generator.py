'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.7)                               |
|  Modified: Wednesday, 27th September 2023 11:31:07 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''

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
    