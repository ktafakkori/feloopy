import pulp as pulp_interface

def Get(modelobject, result, input1, input2=None):

   dir = +1 if input1[1][input1[2]]=='min' else -1
   input1 = input1[0]

   match input1:

    case 'variable':
        return input2.varValue
    
    case 'status':
        return pulp_interface.LpStatus[result[0]]
         
    case 'objective':
        return dir*pulp_interface.value(modelobject.objective)

    case 'time':
        return (result[1][1]-result[1][0])