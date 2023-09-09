'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''


def generate_solution(features):

    match features['interface_name']:

        case 'pulp':

            from .solution import pulp_solution_generator
            ModelSolution = pulp_solution_generator.generate_solution(features)

        case 'pyomo':

            from .solution import pyomo_solution_generator
            ModelSolution = pyomo_solution_generator.generate_solution(
                features)

        case 'ortools':

            from .solution import ortools_solution_generator
            ModelSolution = ortools_solution_generator.generate_solution(
                features)

        case 'ortools_cp':

            from .solution import ortools_cp_solution_generator
            ModelSolution = ortools_cp_solution_generator.generate_solution(
                features)

        case 'gekko':

            from .solution import gekko_solution_generator
            ModelSolution = gekko_solution_generator.generate_solution(
                features)

        case 'picos':

            from .solution import picos_solution_generator
            ModelSolution = picos_solution_generator.generate_solution(
                features)

        case 'cvxpy':

            from .solution import cvxpy_solution_generator
            ModelSolution = cvxpy_solution_generator.generate_solution(
                features)

        case 'cylp':

            from .solution import cylp_solution_generator
            ModelSolution = cylp_solution_generator.generate_solution(features)

        case 'pymprog':

            from .solution import pymprog_solution_generator
            ModelSolution = pymprog_solution_generator.generate_solution(
                features)

        case 'cplex':

            from .solution import cplex_solution_generator
            ModelSolution = cplex_solution_generator.generate_solution(features)
            
        case 'localsolver':

            from .solution import localsolver_solution_generator
            ModelSolution = localsolver_solution_generator.generate_solution(features)

        case 'cplex_cp':

            from .solution import cplex_cp_solution_generator
            ModelSolution = cplex_cp_solution_generator.generate_solution(
                features)

        case 'gurobi':

            from .solution import gurobi_solution_generator
            ModelSolution = gurobi_solution_generator.generate_solution(
                features)

        case 'copt':

            from .solution import copt_solution_generator
            ModelSolution = copt_solution_generator.generate_solution(
                features)

        case 'xpress':

            from .solution import xpress_solution_generator
            ModelSolution = xpress_solution_generator.generate_solution(
                features)

        case 'mip':

            from .solution import mip_solution_generator
            ModelSolution = mip_solution_generator.generate_solution(features)

        case 'linopy':

            from .solution import linopy_solution_generator
            ModelSolution = linopy_solution_generator.generate_solution(
                features)

        case 'rsome_ro':

            from .solution import rsome_ro_solution_generator
            ModelSolution = rsome_ro_solution_generator.generate_solution(
                features)

        case 'rsome_dro':

            from .solution import rsome_dro_solution_generator
            ModelSolution = rsome_dro_solution_generator.generate_solution(
                features)
                     
    return ModelSolution
