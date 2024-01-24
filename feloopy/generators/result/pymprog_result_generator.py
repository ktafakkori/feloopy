# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

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
