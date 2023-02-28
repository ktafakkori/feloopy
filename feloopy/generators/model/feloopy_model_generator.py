

def generate_model(total_variables, directions, solver_name, solver_options):

    match solver_name:

        case 'GWO':
            from ...algorithms.heuristic.GWO import GWO
            model_object = GWO(f=total_variables, d=directions, s=solver_options.get('epoch', 100), t=solver_options.get('pop_size', 50))
        
        case 'GA':
            from ...algorithms.heuristic.GA import GA
            model_object = GA(f=total_variables, d=directions, s=solver_options.get('epoch', 100), t=solver_options.get('pop_size', 50), mu=solver_options.get('mutation_rate', 0.02), cr=solver_options.get('crossover_rate', 0.7), sfl=  solver_options.get('survival_lb', 0.4), sfu=  solver_options.get('survival_ub', 0.6))

        case 'DE':
            from ...algorithms.heuristic.DE import DE
            model_object = DE(f=total_variables, d=directions, s=solver_options.get('epoch', 100), t=solver_options.get('pop_size', 50), mu=solver_options.get('mutation_rate', 0.02), cr=solver_options.get('crossover_rate', 0.7))

        case 'SA':
            from ...algorithms.heuristic.SA import SA
            model_object = SA(f=total_variables, d=directions, s=solver_options.get('epoch', 100), t=1, cc=solver_options.get('cooling_cycles', 10), mt=solver_options.get('maximum_temperature', 1000))

        case 'TS':
            from ...algorithms.heuristic.TS import TS
            model_object = TS(f=total_variables, d=directions, s=solver_options.get('epoch', 100), t=1, c=solver_options.get('tabu_list_size', 10))

    return model_object