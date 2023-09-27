'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.7)                               |
|  Modified: Wednesday, 27th September 2023 11:31:01 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''


import pymprog as pymprog_interface

pymprog_status_dict = {5: "optimal"}


def Get(model_object, result, input1, input2=None):

    input1 = input1[0]

    match input1:

        case 'variable':

            return input2.primal

        case 'status':

            return pymprog_status_dict.get(pymprog_interface.status(), 'Not Optimal')

        case 'objective':

            return pymprog_interface.vobj()

        case 'time':

            return (result[1][1]-result[1][0])
