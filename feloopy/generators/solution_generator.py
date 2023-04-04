
def generate_solution(features):

    inputs = {'model_object': features['model_object_before_solve'],
              'model_objectives': features['objectives'],
              'model_constraints': features['constraints'],
              'directions': features['directions'],
              'constraint_labels': features['constraint_labels'],
              'debug': features['debug_mode'],
              'time_limit': features['time_limit'],
              'absolute_gap': features['absolute_gap'],
              'relative_gap': features['relative_gap'],
              'thread_count': features['thread_count'],
              'solver_name': features['solver_name'],
              'objective_id': features['objective_being_optimized'],
              'log': features['log'],
              'save': features['save_solver_log'],
              'email': features['email_address'],
              'max_iterations': features['max_iterations'],
              'solver_options': features['solver_options']
              }

    match features['interface_name']:

        case 'pulp':

            from .solution import pulp_solution_generator 
            ModelSolution = pulp_solution_generator.generate_solution(**inputs)

        case 'pyomo':

            from .solution import pyomo_solution_generator
            ModelSolution = pyomo_solution_generator.generate_solution(**inputs)

        case 'ortools':

            from .solution import ortools_solution_generator
            ModelSolution = ortools_solution_generator.generate_solution(**inputs)

        case 'ortools_cp':

            from .solution import ortools_cp_solution_generator
            ModelSolution = ortools_cp_solution_generator.generate_solution(**inputs)

        case 'gekko':

            from .solution import gekko_solution_generator
            ModelSolution = gekko_solution_generator.generate_solution(**inputs)

        case 'picos':

            from .solution import picos_solution_generator
            ModelSolution = picos_solution_generator.generate_solution(**inputs)

        case 'cvxpy':

            from .solution import cvxpy_solution_generator
            ModelSolution = cvxpy_solution_generator.generate_solution(**inputs)

        case 'cylp':

            from .solution import cylp_solution_generator
            ModelSolution = cylp_solution_generator.generate_solution(**inputs)

        case 'pymprog':

            from .solution import pymprog_solution_generator
            ModelSolution = pymprog_solution_generator.generate_solution(**inputs)

        case 'cplex':

            from .solution import cplex_solution_generator
            ModelSolution = cplex_solution_generator.generate_solution(**inputs)

        case 'cplex_cp':

            from .solution import cplex_cp_solution_generator
            ModelSolution = cplex_cp_solution_generator.generate_solution(**inputs)

        case 'gurobi':

            from .solution import gurobi_solution_generator
            ModelSolution = gurobi_solution_generator.generate_solution(**inputs)

        case 'xpress':

            from .solution import xpress_solution_generator
            ModelSolution = xpress_solution_generator.generate_solution(**inputs)

        case 'mip':

            from .solution import mip_solution_generator
            ModelSolution = mip_solution_generator.generate_solution(**inputs)

        case 'linopy':

            from .solution import linopy_solution_generator
            ModelSolution = linopy_solution_generator.generate_solution(**inputs)

    return ModelSolution
