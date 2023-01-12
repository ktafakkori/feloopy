import gurobipy as gurobi_interface


gurobi_status_dict = {
    gurobi_interface.GRB.LOADED: 'loaded',
    gurobi_interface.GRB.OPTIMAL: 'optimal',
    gurobi_interface.GRB.INFEASIBLE: 'infeasible',
    gurobi_interface.GRB.INF_OR_UNBD: 'infeasible or unbounded',
    gurobi_interface.GRB.UNBOUNDED: 'unbounded',
    gurobi_interface.GRB.CUTOFF: 'cutoff',
    gurobi_interface.GRB.ITERATION_LIMIT: 'iteration limit',
    gurobi_interface.GRB.NODE_LIMIT: 'node limit',
    gurobi_interface.GRB.TIME_LIMIT: 'time limit',
    gurobi_interface.GRB.SOLUTION_LIMIT: 'solution limit',
    gurobi_interface.GRB.INTERRUPTED: 'interrupted',
    gurobi_interface.GRB.NUMERIC: 'numerical',
    gurobi_interface.GRB.SUBOPTIMAL: 'suboptimal',
    gurobi_interface.GRB.INPROGRESS: 'inprogress'
}


def Get(modelobject, result, input1, input2=None):

   match input1:

    case 'variable':

        return input2.X
    
    case 'status':

        return  gurobi_status_dict[modelobject.status]
         
    case 'objective':

        return  modelobject.ObjVal

    case 'time':

        return (result[1][1]-result[1][0])


