import xpress as xpress_interface

def Get(modelobject, result, input1, input2=None):

   match input1:

    case 'variable':

        print(input2)

        return modelobject.getSolution(input2)
    
    case 'status':

        return result[0]

    case 'objective':

        return modelobject.getSolution(result[0])

    case 'time':

        return (result[1][1]-result[1][0])



