from docplex.mp.model import Model as CPLEXMODEL

def Get(modelobject, result, input1, input2=None):
   
   input1 = input1[0]

   match input1:

    case 'variable':
        return input2.solution_value
    
    case 'status':
        return modelobject.solve_details.status

    case 'objective':
        return modelobject.objective_value

    case 'time':
        return (result[1][1]-result[1][0])*10**6