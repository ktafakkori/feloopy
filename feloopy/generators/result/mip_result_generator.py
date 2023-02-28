import mip as mip_interface

def Get(modelobject, result, input1, input2=None):

   input1 = input1[0]
   
   match input1:

    case 'variable':
        return input2.x
    
    case 'status':
        return result[0]
         
    case 'objective':
        return  modelobject.objective_value

    case 'time':
        return (result[1][1]-result[1][0])