from ortools.linear_solver import pywraplp as ortools_interface

ortools_status_dict = {0: "optimal", 1: "feasible", 2: "infeasible",
                            3: "unbounded", 4: "abnormal", 5: "model_invalid", 6: "not_solved"}


def Get(modelobject, result, input1, input2=None):

   match input1:

    case 'variable':

        return input2.solution_value()
    
    case 'status':

        return ortools_status_dict.get(result[0], "Not Optimal")
         
    case 'objective':

        return  modelobject.Objective().Value()

    case 'time':

        return (result[1][1]-result[1][0])



