import pyomo.environ as pyomo_interface

def Get(model_object, result, input1, input2=None):
   
   input1 = input1[0] 

   match input1:
      
    case 'variable':
        
        return pyomo_interface.value(input2)
      
    case 'status':

        return result[0].solver.termination_condition
      
    case 'objective':

        return pyomo_interface.value(model_object.OBJ)

    case 'time':

        return (result[1][1]-result[1][0])