import warnings
import itertools as it
import math as mt
import numpy as np
from tabulate import tabulate as tb
import sys

warnings.filterwarnings("ignore")

def sol_multi(
    instance, 
    directions=None, 
    solver_name=None, 
    solver_options=dict(), 
    objective_id=0,
    email=None, 
    debug=False, 
    time_limit=None, 
    cpu_threads=None, 
    absolute_gap=None, 
    relative_gap=None, 
    show_log=False, 
    save_log=False, 
    save_model=False, 
    max_iterations=None, 
    approach_options=dict(),
    weights = [],
    save_vars = False):
    
    from ...generators import solution_generator

    if type(objective_id) != str:
        
        m = instance()
        m.features['objective_being_optimized'] = objective_id
        m.features['solver_name'] = solver_name
        m.features['solver_options'] = solver_options
        if m.features['directions'][objective_id] == None:
            m.features['directions'][objective_id] = directions[objective_id]
            for i in range(len(m.features['objectives'])):
                if i != objective_id:
                    del m.features['directions'][i]
                    del directions[i]
                    del m.features['objectives'][i]
            objective_id = 0
            m.features['objective_counter'] = [1, 1]
        else:
            for i in range(len(m.features['directions'])):
                m.features['directions'][i] = directions[i]
        m.features['log'] = show_log
        m.features['model_object_before_solve'] = m
        m.features['debug_mode'] = False
        m.solution = solution_generator.generate_solution(m.features)

    M = np.copy(len(directions))
    dir_map = {'max': -1, 'min': 1}

    if approach_options.get('payoff_method', 'separated') == 'separated':
        
        payoff = np.zeros([M, M])
        for m in range(M):
            model_object = instance()
            model_object.features['directions'] = directions
            model_object.features['objective_being_optimized'] = m
            model_object.features['solver_name'] = solver_name
            model_object.features['solver_options'] = solver_options
            model_object.features['debug_mode'] = debug
            model_object.features['time_limit'] = time_limit
            model_object.features['thread_count'] = cpu_threads
            model_object.features['absolute_gap'] = absolute_gap
            model_object.features['relative_gap'] = relative_gap
            model_object.features['log'] = show_log
            model_object.features['write_model_file'] = save_model
            model_object.features['save_solver_log'] = save_log
            model_object.features['email_address'] = email
            model_object.features['max_iterations'] = max_iterations
            z = model_object.fvar('_z', dim=[range(M)])
            for k in range(M):
                model_object.con(z[k] == model_object.features['objectives'][k])
            model_object.features['model_object_before_solve'] = model_object.model
            model_object.solution = solution_generator.generate_solution(model_object.features)
            for k in range(M):
                payoff[m, k] = model_object.get_variable(z[k])
                
    if objective_id == 'ecm':

        def eps_constraint_model(g, intervals, important):
            model_object = instance()
            model_object.features['directions'] = directions
            model_object.features['objective_being_optimized'] = M
            model_object.features['directions'].append(directions[approach_options.get('important_objective', important)])
            model_object.features['solver_name'] = solver_name
            model_object.features['solver_options'] = solver_options
            model_object.features['log'] = show_log
            model_object.features['solver_name'] = solver_name
            model_object.features['solver_options'] = solver_options
            model_object.features['debug_mode'] = debug
            model_object.features['time_limit'] = time_limit
            model_object.features['thread_count'] = cpu_threads
            model_object.features['absolute_gap'] = absolute_gap
            model_object.features['relative_gap'] = relative_gap
            model_object.features['log'] = show_log
            model_object.features['write_model_file'] = save_model
            model_object.features['save_solver_log'] = save_log
            model_object.features['email_address'] = email
            model_object.features['max_iterations'] = max_iterations
            z = model_object.fvar('_z', [range(M)])
            model_object.obj(z[approach_options.get('important_objective', important)])
            for k in range(M):
                model_object.con(z[k] == model_object.features['objectives'][k])
            for k in range(M):
                if k != approach_options.get('important_objective', important):
                    if directions[k] == 'max':
                        model_object.con(z[k] >= maxobj[k] - ((1/intervals)*(g))*(maxobj[k] - minobj[k]))
                    if directions[k] == 'min':
                        model_object.con(z[k] <= minobj[k] + ((1/intervals)*(g))*(maxobj[k] - minobj[k]))
            model_object.features['model_object_before_solve'] = model_object.model
            model_object.features['debug_mode'] = False
            model_object.features['time_limit'] = time_limit
            model_object.features['solver_name'] = solver_name
            model_object.features['solver_options'] = solver_options
            model_object.features['debug_mode'] = debug
            model_object.features['time_limit'] = time_limit
            model_object.features['thread_count'] = cpu_threads
            model_object.features['absolute_gap'] = absolute_gap
            model_object.features['relative_gap'] = relative_gap
            model_object.features['log'] = show_log
            model_object.features['write_model_file'] = save_model
            model_object.features['save_solver_log'] = save_log
            model_object.features['email_address'] = email
            model_object.features['max_iterations'] = max_iterations
            model_object.solution = solution_generator.generate_solution(model_object.features)
            return model_object, [model_object.get(z[k]) for k in range(M)]

        maxobj = np.amax(payoff, axis=0)
        minobj = np.amin(payoff, axis=0)
        
        if np.any(maxobj-minobj) == 0:
            raise ValueError('Please check the conflict among objectives!')

        intervals = approach_options.get('intervals', 10)
        pareto = []
        variables = []
        if approach_options.get('important_objective', None) == None:
            for k in range(M):
                for g in range(0, intervals+1):
                    models, result = eps_constraint_model(g, intervals, k)
                    if models.healthy():
                        pareto.append(result)
                        if save_vars:
                            variables.append({})
                            for typ,var in models.features['variables'].keys():
                                variables[-1][var] = models.get_numpy_var(var)
                    else:
                        print('early exit (jump)')
                        break
        else:
            for g in range(0, intervals+1):
                models, result = eps_constraint_model(g, intervals, k)
                if models.healthy():
                    pareto.append(result)
                    if save_vars:
                        variables.append({})
                        for typ,var in models.features['variables'].keys():
                            variables[-1][var] = models.get_numpy_var(var)
                else:
                    print('early exit (jump)')
                    break

        pareto = np.array(pareto)

    if objective_id == 'nwsm':

        def nwsm_model(weights):
            model_object = instance()
            model_object.features['directions'] = directions
            model_object.features['objective_being_optimized'] = M
            model_object.features['directions'].append('min')
            model_object.features['solver_name'] = solver_name
            model_object.features['solver_options'] = solver_options
            model_object.features['log'] = show_log
            model_object.features['debug_mode'] = debug
            model_object.features['time_limit'] = time_limit
            model_object.features['thread_count'] = cpu_threads
            model_object.features['absolute_gap'] = absolute_gap
            model_object.features['relative_gap'] = relative_gap
            model_object.features['write_model_file'] = save_model
            model_object.features['save_solver_log'] = save_log
            model_object.features['email_address'] = email
            model_object.features['max_iterations'] = max_iterations
            z = model_object.fvar('_z', [range(M)])
            model_object.obj(sum((1/2)*weights[k]*((1+dir_map[directions[k]])*(z[k]-minobj[k]) + (1-dir_map[directions[k]])*(maxobj[k]-z[k]))/(maxobj[k] - minobj[k]) for k in range(M)))
            for k in range(M):
                model_object.con(z[k] == model_object.features['objectives'][k])
            model_object.features['model_object_before_solve'] = model_object.model
            model_object.features['debug_mode'] = False
            model_object.features['time_limit'] = time_limit
            model_object.features['solver_name'] = solver_name
            model_object.features['solver_options'] = solver_options
            model_object.features['debug_mode'] = debug
            model_object.features['thread_count'] = cpu_threads
            model_object.features['absolute_gap'] = absolute_gap
            model_object.features['relative_gap'] = relative_gap
            model_object.features['log'] = show_log
            model_object.features['write_model_file'] = save_model
            model_object.features['save_solver_log'] = save_log
            model_object.features['email_address'] = email
            model_object.features['max_iterations'] = max_iterations
            model_object.solution = solution_generator.generate_solution(model_object.features)
            return model_object, [model_object.get(z[k]) for k in range(M)]

        maxobj = np.amax(payoff, axis=0)
        minobj = np.amin(payoff, axis=0)
        if np.any(maxobj-minobj) == 0:
            raise ValueError('Please check if the objectives have conflicts!!')

        intervals = approach_options.get('intervals', 10)
        pareto = np.empty([intervals+1, M])
        variables = []

        if len(weights)==0:
            for g in range(0, intervals+1):
                if approach_options.get('wm', 'dirichlet'):
                    weights = np.random.dirichlet(np.ones(M), size=1)[0]
                if approach_options.get('wm', 'random'):
                    nums = np.random.rand(M)
                    weights = nums/sum(nums)
                models, result = nwsm_model(weights)
                if models.healthy():
                    for k in range(M):
                        pareto[g, k] = result[k]
                        variables.append({})
                        if save_vars:
                            for typ,var in models.features['variables'].keys():
                                variables[g][var] = models.get_numpy_var(var)
                                variables[g]['_weights'] = weights
                else:
                    print('early exit (jump)')
                    break

        else:
            models, result = nwsm_model(weights)
            if models.healthy():
                for k in range(M):
                    pareto[g, k] = result[k]
                    variables.append({})
                    if save_vars:
                        for typ,var in models.features['variables'].keys():
                            variables[g][var] = models.get_numpy_var(var)

    conflict = np.corrcoef(*tuple(pareto[:,i] for i in range(M)))

    return pareto, payoff, conflict, variables
