# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


from gamspy import ModelStatus
import math as mt

def Get(model_object, result, input1, input2=None):

    input1 = input1[0]

    match input1:

        case 'variable':

            return input2.toValue()

        case 'status':

            return result[0][2].status

        case 'objective':

            return result[0][1].toValue()

        case 'time':

            return (result[1][1]-result[1][0])
        
        case 'dual':
        
            return result[0][0][input2].records['marginal'].item()

        case 'slack':
            
            upper = result[0][0][input2].records['upper'].item()
            lower = result[0][0][input2].records['lower'].item()
            level = result[0][0][input2].records['level'].item()
            
            if upper!=mt.inf:
                return upper - level
            
            if lower!=mt.inf:
                return level - lower
            
            