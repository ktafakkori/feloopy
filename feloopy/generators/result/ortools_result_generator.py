'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.8)                               |
|  Modified: Wednesday, 27th September 2023 11:30:47 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''

from ortools.linear_solver import pywraplp as ortools_interface

ortools_status_dict = {0: "optimal", 1: "feasible", 2: "infeasible",
                       3: "unbounded", 4: "abnormal", 5: "model_invalid", 6: "not_solved"}

def Get(model_object, result, input1, input2=None):

    input1 = input1[0]

    match input1:

        case 'variable':

            return input2.solution_value()

        case 'status':

            return ortools_status_dict.get(result[0], "Not Optimal")

        case 'objective':

            return model_object.Objective().Value()

        case 'time':

            return (result[1][1]-result[1][0])
        
        case 'dual':

            return model_object.LookupConstraint(input2).dual_value()
        
        case 'slack':

            print('Not supported in ortools.')
