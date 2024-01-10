# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


from gamspy import Equation

import timeit

solvers = [
  'alphaecp',
  'antigone',
  'baron',
  'cbc',
  'conopt',
  'convert',
  'copt',
  'cplex',
  'de',
  'decis',
  'dicopt',
  'emp',
  'empsp',
  'examiner',
  'gamschk',
  'gurobi',
  'guss',
  'highs',
  'ipopt',
  'jams',
  'kestrel',
  'knitro',
  'lindo',
  'lindoglobal',
  'miles',
  'minos',
  'mosek',
  'mps2gms',
  'mpsge',
  'msnlp',
  'nlpec',
  'octeract',
  'odh',
  'path',
  'pathnlp',
  'quad',
  'sbb',
  'scip',
  'shot',
  'snopt',
  'soplex',
  'xpress'
]

from gamspy import Options

gams_solver_selector = {key.lower(): key.upper() for key in solvers}

def generate_solution(features):

    model_object = features['model_object_before_solve']
    model_objectives = features['objectives']
    model_constraints = features['constraints']
    directions = features['directions']
    constraint_labels = features['constraint_labels']
    debug = features['debug_mode']
    time_limit = features['time_limit']
    absolute_gap = features['absolute_gap']
    relative_gap = features['relative_gap']
    thread_count = features['thread_count']
    solver_name = features['solver_name']
    objective_id = features['objective_being_optimized']
    log = features['log']
    save = features['save_solver_log']
    save_model = features['write_model_file']
    email = features['email_address']
    max_iterations = features['max_iterations']
    solver_options = features['solver_options']
    
    if solver_name not in gams_solver_selector.keys():
        raise RuntimeError("Using solver '%s' is not supported by 'gams'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))
    
    # Initialize an empty list for solver options
    gams_options = {}

    # Append options if they are not None
    if time_limit is not None:
        gams_options['time_limit'] = time_limit

    if thread_count is not None:
        gams_options['threads'] = thread_count

    if relative_gap is not None:
        gams_options['relative_optimality_gap'] = relative_gap
        
    if absolute_gap is not None:
        gams_options['absolute_optimality_gap'] = absolute_gap

    if log:
        import sys
        output = sys.stdout
    else:
        output = None
        
    match debug:

        case False:
                    
            obj_equation = Equation(model_object, name=f'obj{objective_id}', type="regular")
            obj_equation[...] = model_objectives[objective_id]
            
            counter=0
            equation_dict = {}
            for constraint in model_constraints:
                equation_dict[constraint_labels[counter]] = Equation(model_object, name=constraint_labels[counter], type="regular")
                equation_dict[constraint_labels[counter]][...] = constraint
                counter+=1
            
            from gamspy import Model 
            
            MIP1 = Model(
                model_object,
                name='yourmodel',
                equations=model_object.getEquations(),
                problem=solver_options.get('model_type', 'mip'),
                sense=directions[objective_id],
                objective=features['objective_variable'],
            )
            
            gams_options = {'iteration_limit': 2, }
            
            result = equation_dict
            time_solve_begin = timeit.default_timer()
            MIP1.solve(solver=gams_solver_selector.get(solver_name, None), options=Options(**gams_options), solver_options=solver_options, output=output)
            time_solve_end = timeit.default_timer()
            generated_solution = [[result,features['objective_variable'],MIP1], [time_solve_begin, time_solve_end]]

    return generated_solution
