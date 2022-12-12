
def Get(modelobject, result, input1, input2=None):

   match input1:

    case 'variable':

        return input2.value[0]
    
    case 'status':

        return modelobject.status

    case 'objective':

        return modelobject.value

    case 'time':

        return (result[1][1]-result[1][0])
