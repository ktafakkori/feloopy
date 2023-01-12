import picos as picos_interface

def Get(modelobject, result, input1, input2=None):

   match input1:

    case 'variable':

        return input2.value
    
    case 'status':

        return result[0].claimedStatus
         
    case 'objective':

        return modelobject.obj_value()

    case 'time':

        return (result[1][1]-result[1][0])


