import gekko as gekko_interface
gekko_status_dict = {0: "not_optimal", 1: "optimal"}

def Get(modelobject, result, input1, input2=None):
   
   dir = +1 if input1[1][input1[2]]=='min' else -1
   input1 = input1[0]

   match input1:
      
    case 'variable':
        return input2.value[0]
    
    case 'status':
        return gekko_status_dict.get(modelobject.options.SOLVESTATUS)
         
    case 'objective':
        return  dir*modelobject.options.objfcnval

    case 'time':
        return (result[1][1]-result[1][0])