'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

from coptpy import *

copt_status_dict = {
    COPT.OPTIMAL: 'optimal',
    COPT.INFEASIBLE: 'infeasible',
    COPT.UNBOUNDED: 'unbounded',
    COPT.NODELIMIT: 'node limit',
    COPT.INTERRUPTED: 'interrupted',
}


def Get(model_object, result, input1, input2=None):

    input1 = input1[0]

    match input1:

        case 'variable':

            return input2.X

        case 'status':

            return copt_status_dict[model_object.status]

        case 'objective':

            return model_object.objval

        case 'time':

            return (result[1][1]-result[1][0])
