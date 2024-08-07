# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.



import timeit
from juliacall import Main as jl

import os

os.environ['PYTHON_JULIACALL_AUTOLOAD_IPYTHON_EXTENSION'] = 'yes'

import numpy as np

jump_solver_selector = {
    'cbc': 'Cbc',
    'glpk': 'GLPK',
    'clp': 'Clp',
    'cplex': 'CPLEX',
    'gurobi': 'Gurobi',
    'highs': 'HiGHS',
    'ipopt': 'Ipopt',
    'knitro': 'Knitro',
    'mosek': 'Mosek',
    'scip': 'SCIP',
    'xpress': 'Xpress',
    'osicbc': 'OSICbc',
    'osiglpk': 'OSIGLPK',
    'cosmo': 'COSMO',
    'path': 'PATH',
    'profound': 'Proximal',
    'alpine': 'Alpine.jl',
    'artelys_knitro': 'Artelys Knitro',
    'baron': 'BARON',
    'bonmin': 'Bonmin',
    'cdc': 'CDCS',
    'cdd': 'CDD',
    'clarabel': 'Clarabel.jl',
    'copt': 'COPT',
    'couenne': 'Couenne',
    'csdp': 'CSDP',
    'daqp': 'DAQP',
    'dsdp': 'DSDP',
    'eago': 'EAGO.jl',
    'ecos': 'ECOS',
    'fico_xpress': 'FICO Xpress',
    'hypatia': 'Hypatia.jl',
    'juniper': 'Juniper.jl',
    'loraine': 'Loraine.jl',
    'madnlp': 'MadNLP.jl',
    'maingo': 'MAiNGO',
    'manopt': 'Manopt.jl',
    'minotaur': 'Minotaur',
    'minizinc': 'MiniZinc',
    'nlopt': 'NLopt',
    'octeract': 'Octeract',
    'optim': 'Optim.jl',
    'osqp': 'OSQP',
    'pajarito': 'Pajarito.jl',
    'pavito': 'Pavito.jl',
    'penbmi': 'Penbmi',
    'percival': 'Percival.jl',
    'polyjump_kkt': 'PolyJuMP.KKT',
    'polyjump_qcqp': 'PolyJuMP.QCQP',
    'raposa': 'RAPOSa',
    'scs': 'SCS',
    'sdpa': 'SDPA',
    'sdplr': 'SDPLR',
    'sdpnal': 'SDPNAL',
    'sdpt3': 'SDPT3',
    'sedumi': 'SeDuMi',
    'status_switching_qp': 'StatusSwitchingQP.jl',
    'tulip': 'Tulip.jl'
}

def generate_solution(features):

    solver_name = features['solver_name']
    model_object=""
    model_object+="\nusing "+jump_solver_selector[solver_name]
    model_object+=features.get("jlcode_preamble","")
    model_object+=features.get("jlcode_data","")
    model_object+= features['model_object_before_solve']
    model_objectives = features['objectives']
    model_constraints = features['constraints']
    directions = features['directions']
    constraint_labels = features['constraint_labels']
    debug = features['debug_mode']
    time_limit = features['time_limit']
    absolute_gap = features['absolute_gap']
    relative_gap = features['relative_gap']
    thread_count = features['thread_count']
    
    objective_id = features['objective_being_optimized']
    log = features['log']
    save = features['save_solver_log']
    save_model = features['write_model_file']
    email = features['email_address']
    max_iterations = features['max_iterations']
    solver_options = features['solver_options']
    
    model_object+=features.get("jlcode_before_variables","")
    for value in features['variables'].values():
        model_object += value

    if solver_name not in jump_solver_selector.keys():
        raise RuntimeError(
            "Using solver '%s' is not supported by 'jump'! \nPossible fixes: \n1) Check the solver name. \n2) Use another interface. \n" % (solver_name))

    if time_limit != None:
        model_object+=f"\nset_optimizer_attribute(jlmodel, \"time_limit\", {time_limit})"

    if thread_count != None:
        model_object+=f"\nset_optimizer_attribute(jlmodel, \"threads\", {thread_count})"

    if relative_gap != None:
        model_object+=f"\nset_optimizer_attribute(jlmodel, \"mip_gap\", {relative_gap})"

    if absolute_gap != None:
        model_object+=f"\nset_optimizer_attribute(jlmodel, \"mip_gap_abs\", {absolute_gap})"

    if log:
        model_object+=f"\nset_optimizer_attribute(jlmodel, \"output_flag\", true)"
    else:
        model_object+=f"\nset_optimizer_attribute(jlmodel, \"output_flag\", false)"

    match debug:

        case False:
            
            model_object+=features.get("jlcode_before_objectives","")
            match directions[objective_id]:

                case 'min': model_object+=f"\n@objective(jlmodel, Min, {model_objectives[objective_id]})"

                case 'max': model_object+=f"\n@objective(jlmodel, Max, {model_objectives[objective_id]})"
            
            model_object+=features.get("jlcode_before_constraints","")
            counter=0
            for constraint in model_constraints:
                if constraint_labels[counter]==None:
                    model_object+=f"\n@constraint(jlmodel, c{counter+1} , {constraint})"
                else:
                    model_object+=f"\n@constraint(jlmodel, {constraint_labels[counter]},{constraint})"
                counter+=1

            model_object+=f"\nset_optimizer(jlmodel, {jump_solver_selector[solver_name]}.Optimizer)"
            model_object+=f"\nelapsed_time = @elapsed begin"
            model_object+=f"\n  optimize!(jlmodel)"
            model_object+=f"\nend"
            for key in features['variables']:
                model_object+=f"\n{key[1]}=value.({key[1]})"
            model_object+=features.get("jlcode_before_solve","")
            jl.seval(model_object)
            jl.seval(features.get("jlcode_after_solve",""))
 
            result = {}
            status = jl.termination_status(jl.jlmodel)
            result["status"] = status
            if "optimal" or "feaisble" in status.lower():
                objective_value = jl.objective_value(jl.jlmodel)
                solutions = {key[1]: np.array(getattr(jl,key[1])) for key in features['variables']}
                
                result["objective_value"] = objective_value
                result["solutions"] = solutions
                try:
                    dual = {label: jl.shadow_price(getattr(jl,label)) for label in constraint_labels if label!=None}
                    dual.update({f"c{label+1}": jl.shadow_price(getattr(jl,f"c{label+1}")) for label in range(len(constraint_labels)) if constraint_labels[label]==None})
                    result["dual"] = dual
                except:
                    pass

            generated_solution = [result, [0, jl.elapsed_time]]

    file_path = './__pycache__/data.json'
    # Check if the file exists
    if os.path.exists(file_path):
        # Remove the file
        os.remove(file_path)
        
        # Get the directory from the file path
        dir_path = os.path.dirname(file_path)
        
        # Check if the directory is empty
        if not os.listdir(dir_path):
            # Remove the directory
            os.rmdir(dir_path)


    return generated_solution
