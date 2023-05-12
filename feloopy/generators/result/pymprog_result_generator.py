'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
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
