import pulp as pulp_interface

def Get(modelobject, result, input1, input2=None):

   match input1:

    case 'variable':

        return input2.varValue
    
    case 'status':

        return pulp_interface.LpStatus[result[0]]
         
    case 'objective':

        return pulp_interface.value(modelobject.objective)

    case 'time':

        return (result[1][1]-result[1][0])