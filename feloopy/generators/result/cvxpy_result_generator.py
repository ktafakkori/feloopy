'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''


def Get(model_object, result, input1, input2=None):

    input1 = input1[0]

    match input1:

        case 'variable':

            if len(input2.value) == 1:

                return input2.value[0]

            else:
                return input2.value

        case 'status':

            return result[0][0].status

        case 'objective':

            return result[0][0].value

        case 'time':

            return (result[1][1]-result[1][0])
