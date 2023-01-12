from ortools.linear_solver import pywraplp as ortools_interface

def GenerateModel():
    return ortools_interface.Solver.CreateSolver('SCIP')
