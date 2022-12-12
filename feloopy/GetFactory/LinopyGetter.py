from linopy import Model as LINOPYMODEL

def Get(modelobject, result, input1, input2=None):

   match input1:

    case 'variable':

        return input2.solution
    
    case 'status':

        return result[0][1]
         
    case 'objective':

        return  "None"

    case 'time':

        return (result[1][1]-result[1][0])




