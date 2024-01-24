# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


import cplex
from docplex.mp.model import Model as CPLEXMODEL
from ...helpers.formatter import *

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

            all_duals = model_object.cplex.solution.get_dual_values()
            for lc, lcd in zip(model_object.iter_linear_constraints(), all_duals):
                lcx = lc.index
                if lcd:
                    if lc.name == input2:
                        return  lcd
                        break
        
        case 'slack':

            return model_object.get_slacks(model_object.get_constraints_by_name(input2))[0]

        case 'rc':

            return  input2.reduced_cost
        
