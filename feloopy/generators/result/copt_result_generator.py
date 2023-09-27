'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

from coptpy import *

copt_status_dict = {
    COPT.OPTIMAL: 'optimal',
    COPT.INFEASIBLE: 'infeasible',
    COPT.UNBOUNDED: 'unbounded',
    COPT.NODELIMIT: 'node limit',
    COPT.INTERRUPTED: 'interrupted',
}

def Get(model_object, result, input1, input2=None):

    input1 = input1[0]

    match input1:

        case 'variable':

            return input2.X

        case 'status':

            return copt_status_dict[model_object.status]

        case 'objective':

            return model_object.objval

        case 'time':

            return (result[1][1]-result[1][0])

        case 'dual':
            return model_object.getConstrByName(input2).Pi

        case 'slack':
            return model_object.getConstrByName(input2).Slack
        
        case 'iis':
            model_object.computeIIS()
            for c in model_object.getConstrs():
                if c.getUpperIIS()>0 or c.getLowerIIS():
                    print("│" + " " + str(f"con: {c.constrName}").ljust(80-2) + " " + "│")
            for v in model_object.getVars():
                if v.getLowerIIS > 0 or v.getUpperIIS > 0:
                    print("│" + " " + str(f"var: {v.varName}").ljust(80-2) + " " + "│")

