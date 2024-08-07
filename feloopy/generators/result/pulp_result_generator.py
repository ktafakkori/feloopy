# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


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

           if input2 in model_object.constraints:
               sense = model_object.constraints[input2].sense

               if sense == pulp_interface.LpConstraintEQ:
                  return model_object.constraints[input2].pi

               elif sense == pulp_interface.LpConstraintLE and directions==1:
                  return -1*abs(model_object.constraints[input2].pi)
               
               elif sense == pulp_interface.LpConstraintLE and directions==-1:
                  return 1*abs(model_object.constraints[input2].pi)
               
               elif sense == pulp_interface.LpConstraintGE and directions==1:
                  return abs(model_object.constraints[input2].pi)
               
               elif sense == pulp_interface.LpConstraintGE and directions==-1:
                  return -1*abs(model_object.constraints[input2].pi)
               
               else:
                  print("Unknown constraint sense")

       case 'slack':

           if input2 in model_object.constraints:
               return abs(model_object.constraints[input2].slack)

       case 'rc':
            return directions*input2.dj
