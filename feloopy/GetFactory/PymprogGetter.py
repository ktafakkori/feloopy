import pymprog as pymprog_interface


pymprog_status_dict = {5: "optimal"}

def Get(modelobject, result, input1, input2=None):

   match input1:

    case 'variable':

        return input2.primal
    
    case 'status':

        return pymprog_status_dict.get(pymprog_interface.status(), 'Not Optimal')
         
    case 'objective':

        return pymprog_interface.vobj()

    case 'time':

        return (result[1][1]-result[1][0])

