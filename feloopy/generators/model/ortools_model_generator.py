# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

from ortools.linear_solver import pywraplp as ortools_interface


def generate_model(features):
    return ortools_interface.Solver.CreateSolver('SCIP')
