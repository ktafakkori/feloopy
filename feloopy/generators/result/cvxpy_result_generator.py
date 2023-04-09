def Get(model_object, result, input1, input2=None):

   input1 = input1[0]

   match input1:

    case 'variable':
        
        return input2.value[0]
    
    case 'status':

        return result[0][0].status

    case 'objective':

        return result[0][1]

    case 'time':

        return (result[1][1]-result[1][0])