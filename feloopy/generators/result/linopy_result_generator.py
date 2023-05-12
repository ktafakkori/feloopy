'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

from linopy import Model as LINOPYMODEL


def Get(model_object, result, input1, input2=None):

    directions = +1 if input1[1][input1[2]] == 'min' else -1

    input1 = input1[0]

    match input1:

        case 'variable':

            return input2.solution

        case 'status':

            return result[0][1]

        case 'objective':

            return "None"

        case 'time':

            return (result[1][1]-result[1][0])
