from ortools.linear_solver import pywraplp as ortools_interface

def generate_model():
    return ortools_interface.Solver.CreateSolver('SCIP')