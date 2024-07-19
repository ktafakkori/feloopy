# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

from ortools.math_opt.python import mathopt

mathopt_status_dict = {
    mathopt.TerminationReason.OPTIMAL: "optimal",
    mathopt.TerminationReason.INFEASIBLE: "infeasible",
    mathopt.TerminationReason.UNBOUNDED: "unbounded",
    mathopt.TerminationReason.INFEASIBLE_OR_UNBOUNDED: "infeasible or unbounded",
    mathopt.TerminationReason.IMPRECISE: "imprecise",
    mathopt.TerminationReason.FEASIBLE: "feasible",
    mathopt.TerminationReason.NO_SOLUTION_FOUND: "no solution found",
    mathopt.TerminationReason.NUMERICAL_ERROR: "numerical error",
    mathopt.TerminationReason.OTHER_ERROR: "other error"
}

def Get(model_object, result, input1, input2=None):

    input1 = input1[0]

    match input1:

        case 'variable':

            return result[0].variable_values()[input2]

        case 'status':

            return mathopt_status_dict.get(result[0].termination.reason, None)

        case 'objective':

            return result[0].objective_value()

        case 'time':

            return (result[1][1]-result[1][0])
        
        case 'dual':

            return result[2].get(input2)
        
