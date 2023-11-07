'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.8)                               |
|  Modified: Wednesday, 27th September 2023 11:30:37 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''


import mip as mip_interface


def Get(model_object, result, input1, input2=None):

    input1 = input1[0]

    match input1:

        case 'variable':

            return input2.x

        case 'status':

            return result[0]

        case 'objective':

            return model_object.objective_value

        case 'time':

            return (result[1][1]-result[1][0])
