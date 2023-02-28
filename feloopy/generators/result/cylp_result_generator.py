import cylp as cylp_interface
from cylp.cy import CyClpSimplex

def Get(modelobject, result, input1, input2=None):

    input1 = input1[0]
    match input1:

        case 'variable':
            return modelobject.primalVariableSolution[input2]
        
        case 'status':
            return result[0].status
            
        case 'objective':
            return   -modelobject.objectiveValue

        case 'time':
            return (result[1][1]-result[1][0])