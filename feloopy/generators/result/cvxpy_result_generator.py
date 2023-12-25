# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


def Get(model_object, result, input1, input2=None):

    input1 = input1[0]

    match input1:

        case 'variable':

            if len(input2.value) == 1:

                return input2.value[0]

            else:
                return input2.value

        case 'status':

            return result[0][0][0].status

        case 'objective':

            return result[0][0][0].value

        case 'time':

            return (result[1][1]-result[1][0])
        
        case 'dual':

            if len(result[0][1][input2].dual_value)==1:

                return result[0][1][input2].dual_value[0]
            else:

                return result[0][1][input2].dual_value

        case 'slack':
            
            print('Warning: Slacks are not supported. Expr value is returned.')

            #Needs to be corrected

            if len(result[0][1][input2].dual_value)==1:

                return result[0][1][input2].expr.value[0]
            else:
                
                return result[0][1][input2].expr.value
        