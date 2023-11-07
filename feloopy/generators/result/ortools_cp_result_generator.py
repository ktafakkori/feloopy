'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.8)                               |
|  Modified: Wednesday, 27th September 2023 11:30:42 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''


from ortools.sat.python import cp_model

ortools_status_dict = {
    cp_model.OPTIMAL: "optimal",
    cp_model.FEASIBLE: "feasible",
    cp_model.INFEASIBLE: "infeasible",
    cp_model.MODEL_INVALID: "model_invalid",
    cp_model.UNKNOWN: "unknown"
}


def Get(model_object, result, input1, input2=None):

    input1 = input1[0]

    match input1:

        case 'variable':

            return result[0][1].Value(input2)

        case 'status':

            return ortools_status_dict.get(result[0][0], "Not Optimal")

        case 'objective':

            return result[0][1].ObjectiveValue()

        case 'time':

            return (result[1][1]-result[1][0])
