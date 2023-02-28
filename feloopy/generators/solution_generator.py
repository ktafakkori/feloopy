
def generate_solution(features, model_object, email, debug, time_limit, thread_count, absolute_gap, relative_gap):
    
    interface_name = features['interface_name']
    model_objectives = features['objectives']
    model_constraints = features['constraints']
    constraint_labels = features['constraint_labels']
    directions = features['directions']
    solver_name = features['solver_name']
    solver_options = features['solver_options']
    objective_id = features['objective_being_optimized']
    log = features['log']    

    match interface_name:

        case 'pulp':

            from .solution import pulp_solution_generator
            ModelSolution = pulp_solution_generator.generate_solution(log, model_object, model_objectives, model_constraints, directions, constraint_labels, debug, solver_name, objective_id)

        case 'pyomo':

            from .solution import pyomo_solution_generator
            ModelSolution = pyomo_solution_generator.generate_solution(
                model_object, model_objectives, model_constraints, directions, constraint_labels, debug, solver_name, objective_id, solver_options, email)

        case 'ortools':

            from .solution import ortools_solution_generator
            ModelSolution = ortools_solution_generator.generate_solution(
                model_object, model_objectives, model_constraints, directions, constraint_labels, debug, solver_name, objective_id)

        case 'gekko':

            from .solution import gekko_solution_generator
            ModelSolution = gekko_solution_generator.generate_solution(
                model_object, model_objectives, model_constraints, directions, constraint_labels, debug, solver_name, objective_id)

        case 'picos':

            from .solution import picos_solution_generator
            ModelSolution = picos_solution_generator.generate_solution(
                model_object, model_objectives, model_constraints, directions, constraint_labels, debug, solver_name, objective_id)

        case 'cvxpy':

            from .solution import cvxpy_solution_generator
            ModelSolution = cvxpy_solution_generator.generate_solution(
                model_object, model_objectives, model_constraints, directions, constraint_labels, debug, solver_name, objective_id)

        case 'cylp':

            from .solution import cylp_solution_generator
            ModelSolution = cylp_solution_generator.generate_solution(
                model_object, model_objectives, model_constraints, directions, constraint_labels, debug, solver_name, objective_id)

        case 'pymprog':

            from .solution import pymprog_solution_generator
            ModelSolution = pymprog_solution_generator.generate_solution(
                model_object, model_objectives, model_constraints, directions, constraint_labels, debug, solver_name, objective_id)

        case 'cplex':

            from .solution import cplex_solution_generator
            ModelSolution = cplex_solution_generator.generate_solution(
                model_object, model_objectives, model_constraints, directions, constraint_labels, debug, time_limit, absolute_gap, relative_gap, thread_count, solver_name, objective_id)

        case 'gurobi':

            from .solution import gurobi_solution_generator
            ModelSolution = gurobi_solution_generator.generate_solution(
                model_object, model_objectives, model_constraints, directions, constraint_labels, debug, solver_name, objective_id)

        case 'xpress':

            from .solution import xpress_solution_generator
            ModelSolution = xpress_solution_generator.generate_solution(
                model_object, model_objectives, model_constraints, directions, constraint_labels, debug, solver_name, objective_id)

        case 'mip':

            from .solution import mip_solution_generator
            ModelSolution = mip_solution_generator.generate_solution(
                model_object, model_objectives, model_constraints, directions, constraint_labels, debug, solver_name, objective_id)

        case 'linopy':

            from .solution import linopy_solution_generator
            ModelSolution = linopy_solution_generator.generate_solution(
                model_object, model_objectives, model_constraints, directions, constraint_labels, debug, solver_name, objective_id)

    return ModelSolution
