import xpress as xpress_interface

def Get(model_object, result, input1, input2=None):

   input1 = input1[0]

   match input1:

    case 'variable':
        return model_object.getSolution(input2)
    
    case 'status':
        return result[0]

    case 'objective':
        return model_object.getSolution(result[0])

    case 'time':
        return (result[1][1]-result[1][0])
