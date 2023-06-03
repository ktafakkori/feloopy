'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

import cplex
from docplex.mp.model import Model as CPLEXMODEL


def Get(model_object, result, input1, input2=None):

    input1 = input1[0]

    match input1:

        case 'variable':

            return input2.solution_value

        case 'status':

            return model_object.solve_details.status

        case 'objective':

            return model_object.objective_value

        case 'time':

            return (result[1][1]-result[1][0])

        case 'dual':

            return  model_object.get_duals(model_object.get_constraints_by_name(input2))[0]
        
        case 'slack':

            return model_object.get_slacks(model_object.get_constraints_by_name(input2))[0]
        

            
        