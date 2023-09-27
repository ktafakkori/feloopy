'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.7)                               |
|  Modified: Wednesday, 27th September 2023 11:30:57 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''


import pulp as pulp_interface



def Get(model_object, result, input1, input2=None):

    directions = +1 if input1[1][input1[2]] == 'min' else -1
    input1 = input1[0]

    match input1:

        case 'variable':

            return input2.varValue

        case 'status':

            return pulp_interface.LpStatus[result[0]]

        case 'objective':

            return directions*pulp_interface.value(model_object.objective)

        case 'time':

            return (result[1][1]-result[1][0])

        case 'dual':

            sense = dict(model_object.constraints).get(input2, None).sense

            if sense == pulp_interface.LpConstraintEQ:
                return dict(model_object.constraints).get(input2, None).pi

            elif sense == pulp_interface.LpConstraintLE and directions==1:
                return -1*abs(dict(model_object.constraints).get(input2).pi)
            
            elif sense == pulp_interface.LpConstraintLE and directions==-1:
                return 1*abs(dict(model_object.constraints).get(input2).pi)
        
            elif sense == pulp_interface.LpConstraintGE and directions==1:
                return abs(dict(model_object.constraints).get(input2).pi)
            
            elif sense == pulp_interface.LpConstraintGE and directions==-1:
                return -1*abs(dict(model_object.constraints).get(input2).pi)
            
            else:
                print("Unknown constraint sense")

        case 'slack':

            return  abs(dict(model_object.constraints).get(input2).slack)
        
        case 'rc':
             return directions*input2.dj

