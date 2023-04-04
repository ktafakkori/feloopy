from ortools.sat.python import cp_model as ortools_interface

def generate_model():
    return ortools_interface.CpModel()